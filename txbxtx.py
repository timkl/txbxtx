import click
from helpers import createSpeak, createTick
from pydub import AudioSegment
import json


@click.command()
@click.argument('i', type=click.File('r'), default='txbxtx.json')
def cli(i):
    '''This script transform your body!'''
    input = json.load(i)

    def jsonInput(json_object):
        tabatas = []

        for i in range(0, len(input["tabatas"])):
            current = input["tabatas"][i]
            tabataID = current["id"]
            exercises = current["exercises"]
            numExercises = len(current["exercises"])
            durExercise = current["durExercise"]
            durRest = current["durRest"]
            numCycles = current["numCycles"]
            tabata = Tabata(tabataID, numExercises, durExercise,
                            durRest, exercises, numCycles)
            tabatas.append(tabata)

        return tabatas

    class Tabata(object):
        '''
        Use the Tabata instance properties to create the mp3.
        '''
        def __init__(self, tabataID, numExercises, durExercise,
                     durRest, exercises, numCycles):
            self.tabataID = tabataID
            self.numExercises = numExercises
            self.durExercise = durExercise
            self.durRest = durRest
            self.exercises = exercises
            self.numCycles = numCycles

        def createTabataMp3(self):
            exerciseSnippets = []
            exerciseTickPath = createTick('tickExercise', self.durExercise)
            exerciseTick = AudioSegment.from_mp3(exerciseTickPath)
            restSpeakPath = createSpeak("Rest")
            restSpeak = AudioSegment.from_mp3(restSpeakPath)
            restTickPath = createTick('tickRest', self.durRest)
            restTick = AudioSegment.from_mp3(restTickPath)
            for e in self.exercises:
                exerciseSpeakPath = createSpeak(e, self.exercises.index(e))
                exerciseSpeak = AudioSegment.from_mp3(exerciseSpeakPath)
                exercise = exerciseSpeak + exerciseTick + restSpeak + restTick
                exerciseSnippets.append(exercise)
            tabata = (sum(exerciseSnippets) * self.numCycles)
            tabataFile = "temp/tabata-" + str(self.tabataID) + ".mp3"
            tabata.export(tabataFile, format="mp3")

    init = jsonInput(input)

    foo = []

    for i, t in enumerate(init):
        foo.append([i, t])

    with click.progressbar(foo, label='Creating Tabata...') as bar:
        for f in bar:
            f[1].createTabataMp3()

    click.echo("Wrapping up...")

    allTabatas = []

    for i, t in enumerate(init):
        allTabatas.append(AudioSegment.from_mp3("temp/tabata-" +
                                                str(i) + ".mp3"))

    tabataFoo = sum(allTabatas)

    go = AudioSegment.from_mp3("audio/go.mp3")
    fanfare = AudioSegment.from_mp3("audio/fanfare.mp3")

    finalTabata = go + tabataFoo + fanfare
    finalTabata.export("finalTabata.mp3", format="mp3")
    click.launch('finalTabata.mp3', locate=True)

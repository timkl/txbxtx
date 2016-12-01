from pydub import AudioSegment
from helpers import createSpeak, createTick


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

    def createTabataSegmentMp3(self):
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

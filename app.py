import click
from Tabata import Tabata
from createFinalTabata import createFinalTabata
import json


@click.command()
@click.argument('i', type=click.File('r'), default='txbxtx.json')
def cli(i):
    '''This script transform your body!'''
    input = json.load(i)

    def init(json_object):
        '''This function parses JSON and creates the final Tabata mp3.'''
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

        createFinalTabata(tabatas)

    init(input)

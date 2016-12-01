import click
from pydub import AudioSegment


def createFinalTabata(tabatas):
    '''This function creates the final Tabata mp3.'''
    foo = []
    for i, t in enumerate(tabatas):
        foo.append([i, t])
    with click.progressbar(foo, label='Creating Tabata...') as bar:
        for f in bar:
            f[1].createTabataSegmentMp3()
    click.echo("Wrapping up...")
    allTabatas = []
    for i, t in enumerate(tabatas):
        allTabatas.append(AudioSegment.from_mp3("temp/tabata-" +
                                                str(i) + ".mp3"))
    tabataFoo = sum(allTabatas)
    go = AudioSegment.from_mp3("audio/go.mp3")
    fanfare = AudioSegment.from_mp3("audio/fanfare.mp3")
    finalTabata = go + tabataFoo + fanfare
    finalTabata.export("finalTabata.mp3", format="mp3")
    click.launch('finalTabata.mp3', locate=True)

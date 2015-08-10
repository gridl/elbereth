from flask import Flask
import json
import random


app = Flask(__name__)


poem = '''A Elbereth Gilthoniel
silivren penna miriel
o menel aglar elenath!
Na-chaered palan-diriel
o galadhremmin ennorath,
Fanuilos, le linnathon
nef aear, si nef aearon!

A Elbereth Gilthoniel
o menel palan-diriel,
le nallon si di'nguruthos!
A tiro nin, Fanuilos!
'''


@app.route('/')
def gibberish():
    response = json.dumps({
        'version': 0.1,
        'elvish': random.choice(poem.split('\n'))
    })
    return (response, 200, {'content-type': 'application/json'})


if __name__ == '__main__':
    app.run()

from django.http import HttpResponse
import json
import random


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


def gibberish(*args, **kwargs):
    response = json.dumps({
        'version': 0.1,
        'elvish': random.choice(poem.split('\n'))
    })
    return HttpResponse(response, content_type='application/json')

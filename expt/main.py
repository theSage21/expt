import os
import json
from datetime import datetime
from .config import BENCH, ARX, InvalidCall, working_command


now = datetime.now
# -----------tools


def clean(string):
    whitelist = 'abcdefghijklmnopqrstuvwxyz1234567890_-'
    return ''.join(i for i in string.lower() if i in whitelist)


def resolve_blob_part(part):
    bench = list(os.listdir(BENCH))
    relevant = [i for i in bench if part in i]
    if len(relevant) != 1:
        raise InvalidCall('Blob resolution failed')
    else:
        return relevant[0]


# ----------- actual functions
def new_hyp(title, blob=None):
    bench = list(os.listdir(BENCH))
    blob = clean(title) if blob is None else blob
    print('Using blob: {}'.format(blob))
    data = {'id': len(bench) + 1,
            'title': title,
            'started': str(now()),
            'blob': blob
            }
    print('Making hypothesis folder ...', end='')
    # Hypothesis path
    path = os.path.join(BENCH, data['blob'])
    os.mkdir(path)
    # Meta info
    meta_path = os.path.join(path, 'meta.json')
    with open(meta_path, 'w') as file:
        json.dump(data, file, indent=4)
    # Notes
    meta_path = os.path.join(path, 'notes.json')
    with open(meta_path, 'w') as file:
        json.dump({}, file, indent=2)
    print('Complete')


def list_hyp():
    message = 'Hypothesis Experiments\n'
    message += '='*20 + '\n'*3
    message += '-'*20 + '\n'
    message += 'Current Bench' + '\n'
    message += '-'*20 + '\n'
    bench = list(os.listdir(BENCH))
    archive = list(os.listdir(ARX))
    for name in bench:
        path = os.path.join(BENCH, name)
        with open(os.path.join(path, 'meta.json'), 'r') as fl:
            id_ = json.load(fl)['id']
        message += '{:5}. {}\n'.format(id_, name)
    message += '-'*20 + '\n'
    message += 'Archived\n'
    message += '-'*20 + '\n'
    for name in archive:
        path = os.path.join(BENCH, name)
        with open(os.path.join(path, 'meta.json'), 'r') as fl:
            id_ = json.load(fl)['id']
        message += '{:5}. {}'.format(id_, name)
    print(message)


def work(blob):
    path = os.path.join(BENCH, blob)
    # TODO: Make compatible with non-NIX
    os.system(working_command.format(path=path))


def note(blob, msg=None):
    path = os.path.join(BENCH, blob, 'notes.json')
    with open(path, 'r') as file:
        notes = json.load(file)
    if msg is None:
        msg = input('Message:> ')
    notes[str(now())] = msg
    with open(path, 'w') as file:
        json.dump(notes, file, indent=2)


def stop(blob):
    # TODO: Clean way to run jupyter and stop
    pass

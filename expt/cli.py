import sys
import os
from .main import resolve_blob_part, new_hyp
from .main import list_hyp, work, note, stop
from .config import BENCH, ARX


help_ = '''
EXPT
----
All <hypothesis blob>s can be partial and will be resolved to the closest
maximal match.

expt
    Display this help and exit
expt init
    Initiate a folder with the structures needed for expt to work
expt list
    List the hypothesis in the workbench
expt new <hypothesis title>
    Create a new hypothesis with given title
expt work <hypothesis blob>
    Work on a hypothesis
expt note <hypothesis blob> <message>
    Add a note to a hypothesis. Think of these as important points
    you might want ot know later on
expt stop <hypothesis blob>
    Stop working on a hypothesis
expt archive <hypothesis blob>
    Archive a hypothesis permanently
expt summary [all]
    Create summaries of all experiments in the workbench.
    If all is specified, use archives too
expt report [all]
    Create reports of all experiments in the workbench.
    If all is specified, use archives too
'''


def check_initiated():
    if not(os.path.exists(BENCH) and os.path.exists(ARX)):
        print('This does not look initiated')
        print('Perhaps you should run the command')
        print('$expt init')
        sys.exit(1)


def main():
    argv = list(sys.argv[1:])
    print_help_and_exit = False
    if len(argv) == 0:
        print_help_and_exit = True
    elif len(argv) == 1:
        cmd = argv[0]
        if cmd == 'summary':
            check_initiated()
            pass  # TODO
        elif cmd == 'report':
            check_initiated()
            pass  # TODO
        elif cmd == 'init':
            if not os.path.exists(BENCH):
                print('Creating ', BENCH)
                os.mkdir(BENCH)
            if not os.path.exists(ARX):
                print('Creating ', ARX)
                os.mkdir(ARX)
            print('Initiated this directory for expt use.')
        elif cmd == 'list':
            check_initiated()
            list_hyp()
        else:
            print_help_and_exit = True
    elif len(argv) >= 2:
        cmd = argv[0]
        if cmd == 'new':
            check_initiated()
            title = argv[1]
            new_hyp(title)
        elif cmd == 'work':
            check_initiated()
            blob = resolve_blob_part(argv[1])
            work(blob)
        elif cmd == 'note':
            check_initiated()
            if len(argv) == 3:
                msg = argv[2]
            blob = resolve_blob_part(argv[1])
            note(blob, msg)
        elif cmd == 'stop':
            check_initiated()
            blob = resolve_blob_part(argv[1])
            stop(blob)
        else:
            print_help_and_exit = True
    if print_help_and_exit:
        print(help_)

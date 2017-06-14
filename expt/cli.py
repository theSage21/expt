import sys
from .main import resolve_blob_part


help_ = '''
EXPT
----
All <hypothesis blob>s can be partial and will be resolved to the closest
maximal match.

expt
    Display this help and exit
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


def main():
    argv = list(sys.argv[1:])
    print_help_and_exit = False
    if len(argv) == 0:
        print_help_and_exit = True
    elif len(argv) == 1:
        cmd = argv[0]
        if cmd == 'summary':
            pass
        elif cmd == 'report':
            pass
        else:
            print_help_and_exit = True
    elif len(argv) >= 2:
        blob_part = argv[1]
        blob = resolve_blob_part(blob_part)
        if cmd == 'new':
            pass
        elif cmd == 'work':
            pass
        elif cmd == 'note':
            if len(argv) == 3:
                msg = argv[2]
        elif cmd == 'stop':
            pass
        else:
            print_help_and_exit = True
    if print_help_and_exit:
        print(help_)

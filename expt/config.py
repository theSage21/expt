class InvalidCall(Exception):
    pass


BENCH, ARX = 'bench', 'archive'
working_command = 'cd {path} && jupyter notebook & &>/dev/null && echo $!>pid'

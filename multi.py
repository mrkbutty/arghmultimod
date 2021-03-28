import os
import glob
import importlib
import argh
# import ptools.dirlist
# import ptools.mygrep

PTOOLS = 'ptools'

def cli():

    parser = argh.ArghParser()
    
    cwd = os.path.dirname(os.path.realpath(__file__))
    for ptool in os.listdir(os.path.join(cwd, PTOOLS)):
        if ptool.endswith('.py'):
            modbase = os.path.splitext(os.path.basename(ptool))[0]
            modname = PTOOLS + '.' + modbase
            impmod = importlib.import_module(modname)
            parser.add_commands([impmod.__dict__[modbase]])

    parser.dispatch()

if __name__ == '__main__':
    cli()
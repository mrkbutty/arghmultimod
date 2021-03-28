import os
import glob
import importlib
import argh
# import ptools.dirlist
# import ptools.mygrep

PTOOLS = 'tools'

def argh_dir(subdirname):
    """
    Set argh parsers to python programs in the 
    """

    parser = argh.ArghParser()
    
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    for ptool in os.listdir(os.path.join(scriptdir, subdirname)):
        if ptool.endswith('.py'):
            modbase = os.path.splitext(os.path.basename(ptool))[0]
            modname = subdirname + '.' + modbase
            impmod = importlib.import_module(modname)
            parser.add_commands([impmod.__dict__[modbase]])

    parser.dispatch()

if __name__ == '__main__':
    argh_dir(PTOOLS)
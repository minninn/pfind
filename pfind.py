#!python_path

# --------------------------------
# Version: 1.1.4
# OS:Rocky Linux 8.7 
# Last Modify: 2023.04.13.
# Made by: minninn, guaca123
# https://github.com/minninn/pfind
# --------------------------------


import os
import sys
import subprocess
from tqdm import tqdm

exclude_path = [ 'sys', 'proc', 'dev', 'run' ]

help = """
pfind help

Find all files in working directory.

usage: pfind [options] [content]

options
    -v, --version: show version
    -h, --help: show this message
    -c, --content: find files that include this content
                   pfind -c "content"
"""


def run_command( command ):
    proc = subprocess.Popen( command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )

    try:
        stdout, stderr = proc.communicate()

    except KeyboardInterrupt:
        print( "\n\nStop Search by KeyboardInterrupt" )
        sys.exit()

    try:
        return stdout.decode()

    except:
        return stdout.decode( 'ISO-8859-1' )

def options():
    if "-h" in sys.argv or "--help" in sys.argv:
        print( help )
        sys.exit()

    elif "-v" in sys.argv or "--version" in sys.argv:
        print( "Version: 1.1.4" )
        sys.exit()
    

    elif "-c" in sys.argv:
        string = sys.argv[ sys.argv.index( "-c" ) + 1 ]
        content_option( string, select_files() )
        sys.exit()
    
    elif "--content" in sys.argv:
        string = sys.argv[ sys.argv.index( "--content" ) + 1 ]
        content_option( string, select_files() )
        sys.exit()

    else:
        print( "Not Defined This Options: Check Help Messages use -h or --help" )
        sys.exit()


def content_option( string, childFiles ):
    cnt         = 0
    match_files = ''

    print( "Search Files..." )

    for childFile in tqdm( childFiles ):
        childFile = childFile.replace( "(", r"\(" ).replace( ")", r"\)" )
                
        if run_command( "cat {0} 2>/dev/null | grep -i '{1}' 2>/dev/null".format( childFile, string ) ) != '':
            cnt += 1
            match_files += "\nmatch: {0}".format( childFile )
                
    print( match_files )
    print( "\nFiles: {0}/{1}".format( cnt, len( childFiles ) ) )




def select_files():
    childFiles = []
    path       = os.popen( 'pwd' ).read().rstrip( '\n' )

    for child_path, dirs, files in os.walk( path ):
        if any( exclude in child_path.split( '/' ) for exclude in exclude_path ):
            continue
        else:
            for file in files:
                childFiles.append( child_path + '/' + file )
    
    return childFiles


def run_process():
    if len( sys.argv ) == 1:
        childFiles = select_files()

        for childFile in childFiles:
            print( childFile )

        print( "\nFiles: {0}".format( len( childFiles ) ) )

    else:
        options()


if __name__ == '__main__':
    run_process()

#!python_path

# --------------------------------
# Version: 1.1.3
# OS:Rocky Linux 8.7 
# Last Modify: 2023.04.10.
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

    return stdout


def options( option ):
    if option == "-h" or option == "--help":
        print( help )
        sys.exit()

    if option == "-v" or option == "--version":
        print( "Version: 1.1.3" )
        sys.exit()
    
    if option == "-c" or option == "--content":
        string      = sys.argv[2]
        cnt         = 0
        match_files = ''

        print( "Search Files..." )

        for childFile in tqdm( childFiles ):
            childFile = childFile.replace( "(", r"\(" ).replace( ")", r"\)" )
                
            if run_command( "cat {0} 2>/dev/null | grep -i '{1}' 2>/dev/null".format( childFile, string ) ).decode() != '':
                cnt += 1
                match_files += "\nmatch: {0}".format( childFile )
                
        print( match_files )
        print( "\nFiles: {0}/{1}".format( cnt, len( childFiles ) ) )
        sys.exit()


    print( "Not Defined This Options: Check Help Messages use -h or --help" )


path       = os.popen( 'pwd' ).read().rstrip( '\n' )
childFiles = []

for child_path, dirs, files in os.walk( path ):
    if any( exclude in child_path.split( '/' ) for exclude in exclude_path ):
        continue
    else:
        for file in files:
            childFiles.append( child_path + '/' + file )


if len( sys.argv ) == 1:
    for childFile in childFiles:
        print( childFile )

    print( "\nFiles: {0}".format( len( childFiles ) ) )

else:
    options( sys.argv[1] )

#!python_path

# --------------------------------
# Version: 1.3.1
# OS:Rocky Linux 8.7 
# Last Modify: 2023.08.02.
# Made by: minninn, guaca123
# https://github.com/minninn/pfind
# --------------------------------


import os
import sys
import subprocess
from tqdm import tqdm

exclude_path = [ 'sys', 'proc', 'dev', 'run' ]
runMode = True

help = """
pfind help

Find all files in working directory.

usage: pfind [options] [content]

options
    -v, --version: show version
    -h, --help: show this message
    -x, --exclude: Exclude Directories in search
                   pfind -x "directory"
    -c, --content: find files that include this content
                   pfind -c "content"
    -t, --target: Enter the path to search
                   pfind -t "directory"
    -q, --quiet: Quiet Mode
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
        print( "Version: 1.3.1" )
        sys.exit()    


    elif "-c" in sys.argv:
        string = sys.argv[ sys.argv.index( "-c" ) + 1 ]
        content_option( string, select_files( target_path ) )
        sys.exit()
    
    elif "--content" in sys.argv:
        string = sys.argv[ sys.argv.index( "--content" ) + 1 ]
        content_option( string, select_files( target_path ) )
        sys.exit()

    else:
        print( "Not Defined This Options: Check Help Messages use -h or --help" )
        sys.exit()


def content_option( string, childFiles ):
    cnt         = 0
    match_files = ''

    if runMode:
        print( "Search Files..." )
        for childFile in tqdm( childFiles ):
            childFile = childFile.replace( "(", r"\(" ).replace( ")", r"\)" )
                
            if run_command( "cat {0} 2>/dev/null | grep -i '{1}' 2>/dev/null".format( childFile, string ) ) != '':
                cnt += 1
                match_files += "\n{0}".format( childFile )
                
        print( match_files )
        print( "\nMatch Files: {0}/{1}".format( cnt, len( childFiles ) ) )

    else:
        for childFile in childFiles:
            childFile = childFile.replace( "(", r"\(" ).replace( ")", r"\)" )

            if run_command( "cat {0} 2>/dev/null | grep -i '{1}' 2>/dev/null".format( childFile, string ) ) != '':
                cnt += 1
                match_files += "\n{0}".format( childFile )

        print( match_files )


def select_files( target_path ):
    if target_path:
        if os.path.isdir( target_path ):
            path   = target_path
        else:
            try:
                raise ValueError
            except:
                print( f"{target_path} is not Directory" )
                sys.exit()
    else:
        path   = os.popen( 'pwd' ).read().rstrip( '\n' )

    childFiles = []


    for child_path, dirs, files in os.walk( path ):
        if any( exclude in child_path.split( '/' ) for exclude in exclude_path ):
            continue
        else:
            for file in files:
                childFiles.append( child_path + '/' + file )
    
    return childFiles


def run_process( target_path ):
    if len( [ item for item in [ '-c', '--content', '-h', '--help', '-v', '--version' ] if item in sys.argv ] ) == 0:
        childFiles = select_files( target_path )

        for childFile in childFiles:
            print( childFile )

        if runMode:
            print( "\nFiles: {0}".format( len( childFiles ) ) )

    else:
        options()


if __name__ == '__main__':
    target_path = ''

    if "-x" in sys.argv:
        paths = sys.argv[ sys.argv.index( "-x" ) + 1 ].split()
        for path in paths:
            exclude_path.append( path.strip( "/" ) )

    if "--exclude" in sys.argv:
        paths = sys.argv[ sys.argv.index( "--exclude" ) + 1 ].split()
        for path in paths:
            exclude_path.append( path.strip( "/" ) )        

    if "-t" in sys.argv:
        target_path = sys.argv[ sys.argv.index( "-t" ) + 1 ]
    
    if "--target" in sys.argv:
        target_path = sys.argv[ sys.argv.index( "--target" ) + 1 ]

    if "-q" in sys.argv:
        runMode = False

    if "--quiet" in sys.argv:
        runMode = False

    run_process( target_path )

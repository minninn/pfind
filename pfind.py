#!/opt/homebrew/bin/python3

# --------------------------------
# Version: 1.0.0
# OS: macOS Ventura 13.0.1
# Last Modify: 2022.12.04.
# Made by: minninn, guaca123
# https://github.com/minninn/pfind
# --------------------------------


import os
import sys

help = """
Pfind Help

Find all files in working directory.

usage: pfind [options] [content]

options
    -v, --version: show version
    -h, --help: show this message
    -c, --content: find files that include this content
                   pfind -c "content"
"""

def options( option ):
    if option == "-h" or option == "--help":
        print( help )
        return 0

    if option == "-v" or option == "--version":
        print( "Pfind Version: 1.0.0" )
        return 0
    
    if option == "-c" or option == "--content":
        try:
            string  = sys.argv[2]
            cnt     = 0

            for childFile in childFiles:
                if os.system( "cat {0} | grep -i '{1}' 1>/dev/null".format( childFile, string ) ) == 0:
                    cnt += 1
                    print( "match: {0}".format( childFile ) )

            print( "Files: {0}/{1}".format( cnt, len( childFiles ) ) )
            return 0

        except:
            pass


    print( "Not Defined This Options: Check Help Messages use -h or --help" )


path       = os.popen( 'pwd' ).read().rstrip( '\n' )
childFiles = []

for child_path, dirs, files in os.walk( path ):
    for file in files:
        childFiles.append( child_path + '/' + file )

if len( sys.argv ) == 1:
    for childFile in childFiles:
        print( childFile )

    print( "Files: {0}".format( len( childFiles ) ) )

else:
    options( sys.argv[1] )

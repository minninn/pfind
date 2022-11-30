#!/opt/homebrew/bin/python3

import os
import sys

path       = os.popen( 'pwd' ).read().rstrip( '\n' )
childFiles = []

for child_path, dirs, files in os.walk( path ):
    for file in files:
        childFiles.append( child_path + '/' + file )

try:
    string  = sys.argv[1]
    cnt     = 0
    for childFile in childFiles:
        if os.system( "cat {0} | grep -i '{1}' 1>/dev/null".format( childFile, string ) ) == 0:
            cnt += 1
            print( "match: {0}".format( childFile ) )

    print( "Files: {0}/{1}".format( cnt, len( childFiles ) ) )

except:
    for childFile in childFiles:
        print( childFile )

    print( "Files: {0}".format( len( childFiles ) ) )

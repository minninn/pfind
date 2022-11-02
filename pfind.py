import os
import sys

path       = os.popen( 'pwd' ).read().rstrip( '\n' )
childFiles = []

for child_path, dirs, files in os.walk( path ):
    for file in files:
        childFiles.append( child_path + '/' + file )

try:
    string  = sys.argv[1]
    for childFile in childFiles:
        if os.system( "cat {0} | grep {1} 1>/dev/null".format( childFile, string ) ) == 0:
            print( "match: {0}".format( childFile ) )
    
    print( "Files: {0}".format( len( childFiles ) ) )

except:
    for childFile in childFiles:
        print( childFile )
    
    print( "Files: {0}".format( len( childFiles ) ) )    

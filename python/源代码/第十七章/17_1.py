import sys

try:
    filename = sys.argv[1]
    print (filename)
except:
    print (“Usage:”, sys.argv[0], “filename”)
    sys.exit(1)
return 0

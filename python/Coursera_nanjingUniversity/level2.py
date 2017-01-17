# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print args.echo

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a",type=float,help="display a square of a given number")
parser.add_argument("-b",type=float,default = 40,help="display a square of a given number")

args = parser.parse_args()
a = args.a
b = args.b
print a,b
print a**b
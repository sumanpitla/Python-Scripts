import argparse,datetime

parser=argparse.ArgumentParser(description="A random prgram")

parser.add_argument('file name',help='file name of the file')
parser.add_argument('-c','--copy',dest='new_dest')

parser.add_argument('-s','--something',action='store_false')
parser.add_argument('-v','--version',action='version',version='python 3.10')

arguments=parser.parse_args()
print(arguments.filenane)
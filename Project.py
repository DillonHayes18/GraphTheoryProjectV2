import argparse

parser = argparse.ArgumentParser(description='Enter Regular Expression & File Path:')
parser.add_argument('regexp', metavar='expression', type=str,
                    help='a string for the search')
parser.add_argument('filepath', metavar='path', type=str,
                    help='a filepath for the search')
args = parser.parse_args()

fd=open(args.filepath)
for i, line in enumerate(fd):
      print(line)

fd.close()
print(args.regexp)
print(args.filepath)
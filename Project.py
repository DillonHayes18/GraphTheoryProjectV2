import argparse
# Graph Theory Project 
# Dillon Hayes - G00373320
# April 2021

# Program to take a regular expression and the name or path of the file 
# as command line arguments and output the lines of the file matching the regular expression.


# User prompt for adding inputing Regular Expression & File Path
# Stores input as rexep which is type string
# Stores input as filepath which is type string

parser = argparse.ArgumentParser(description='Enter Regular Expression & File Path:')
parser.add_argument('regexp', metavar='expression', type=str,
                    help='a string for the search')
parser.add_argument('filepath', metavar='path', type=str,
                    help='a filepath for the search')
args = parser.parse_args()

# Opens the filepath and stores it as fileSearcher
# for every line that has fileSearcher
# if the regexp is in that line, print the line
# close the filepath
with open(args.filepath, 'r') as fileSearcher:
    for line in fileSearcher:
        if args.regexp in line:
            print (line)
fileSearcher.close()

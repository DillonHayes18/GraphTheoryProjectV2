# Graph Theory Project 
# Dillon Hayes - G00373320
# April 2021

# Program to take a regular expression and the name or path of the file 
# as command line arguments and output the lines of the file matching the regular expression.

# Pre-requisits: 
# Visual Studio Code
# Windows Terminal 
# w2l subsystem 

# How to run the project:
# 1) launch a windows terminal
# 2) cd into the repo location
# 3) cd into the project: GraphTheoryProjectV2
# 4) enter code . to open visual studio code
# 5) run python3 project.py "Enter expression" "Enter filepath"
# 6) returns all lines in file containing expression

# What to expect
# Run the python project file and enter the regular expression and the file path
# The program will read through the file for the expression and display the line matching the expression

# Pseudocode 
import argparse

create a parser
add an arguement for a str
add an arguement for a path
parse the arguements

with open the filepath and read it as a variable
for line in the variable search through 
if file path is in the line
print line

# Questions
# Q: What is a regular expression?
# A: Referenced from Lecture Notes & https://en.wikipedia.org/wiki/Regular_expression
#    Regular expressions are strings that represent text patterns, the strings can contain specialized characters
#    and brackets which can group characters together. Regular expressions match strings to strings and are
#    used to search other strings for patterns. Regular expressions follow a precedence:
#       - Always apply the '*' operator first, and stands for zero
#       - Then comes '.' it means concatenate.
#       - The | is applied last which represents or.
#       - Any characters contained within brackets are treated individually 
#    The concept of a regular expresion came about in the 50's after being formalized by mathematician 
#    Stephen Cole Kleene. Regular expression are seen everywhere in todays age, they are present in most 
#    text editors, word processors, search engine and an extension of most software languages.
#    

# Q: How do regular expressions differ across implementations?
# A: Referenced from https://www.w3schools.com/java/java_regex.asp & https://docs.python.org/3/library/re.html
#    As stated regular expressions are an extension of most languages however, there implemantation can vary
#    language to language. 
#
#    In Java regular expressions are not a library but are present in the regex package. It contains 3 classes;
#       - Pattern Class - For designating the search pattern 
#       - Matcher Class - Used to search for the pattern
#       - PatternSyntaxException Class - Used for cases of syntax errors
#   The user can use a compile method to query their search and then the matcher method for searching for the
#   string and sending back the information about the search.
#
#   In Python however regular expressions work slightly different, 
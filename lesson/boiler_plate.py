#!/usr/bin/env python
#
# @date 25 Sept 2015
# @author james Boocock
#

import argparse

def print_file(input_file):
    """ 
        Function opens a file and prints the
        results to stdout.

        @param input_file
    """

    with open(input_file) as f:
        for line in f:
            print line

def main():
    """
      First function to be run in a command-line program
    """
    # Create a basic command-line program the reads a file and prints it out.
    parser = argparse.ArgumentParser(description="Essentially cat, but for only one file")
    # Adds a input file argument to the parser.
    parser.add_argument("input_file")
    # parses the arguments and stores the arguments in a dictionary.
    args = parser.parse_args()
    # Call the  print_file function.
    print_file(args.input_file)

if __name__ == "__main__":
    main()

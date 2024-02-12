#!/usr/bin/env python3

def helloWorld():
	print(‘Hello World’)


helloWorld()

import sys

def print_arguments():
    script_name = sys.argv[0]
    print("Script name:", script_name)
    
    if len(sys.argv) > 1:
        arguments = ' '.join(sys.argv[1:])
        print("Arguments:", arguments)
    else:
        print("No additional arguments provided.")

print_arguments()


Compiler for our Little Language (.PIC)

import sys

# read arguments
program_filepath = sys.argv[1]

print("[CMD] Parsing")

#########################
#  Tokenize Program
#########################

# read file lines
program_lines = []
with open(program_filepath, "r") as f:
    program_lines = [
        line.strip()
            for line in program_file.readlines()]

program = []
for line in program_lines:
    if    

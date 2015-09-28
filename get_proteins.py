#!/usr/bin/python
# usage: get_proteins.py [...]/dir.des.scop.txt_[...] SCCS

import sys
import re

def main():
    output = []

    # Build query string
    query = ""
    parts = sys.argv[2].split(".")
    for i in range(0, 4):
        if i >= len(parts) or parts[i] == "*":
            query += "[0-9]+"
        else:
            query += parts[i]

        if i != 3:
            query += "\\."

    # Read scop file
    f = open(sys.argv[1], "r")
    for line in f:
        if line[0] == "#":
            continue

        parts = line.split("\t")
        if parts[1] == "px" and re.match(query, parts[2]):
            output.append(line)

    f.close()

    f = open(sys.argv[3], "w")
    for line in output:
        f.write(line)

if __name__ == "__main__":
    main()

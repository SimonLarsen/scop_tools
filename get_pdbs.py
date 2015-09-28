#!/usr/bin/python
# usage: get_pdbs.py PROTEIN_LIST

import sys
from subprocess import call

def main():
    infile = open(sys.argv[1], "r")
    for line in infile:
        line = line.strip()
        columns = line.split("\t")

        if columns[1] != "px":
            continue

        parts = columns[4].split(" ")
        id = parts[0]
        call(["wget", "http://www.rcsb.org/pdb/files/"+id+".pdb", "-O", id+".pdb"])

    infile.close()

if __name__ == "__main__":
    main()

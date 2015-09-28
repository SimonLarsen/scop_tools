#!/usr/bin/python
# usage: get_segments SEGMENT_LIST

import sys

def main():
    infile = open(sys.argv[1], "r")
    for line in infile:
        line = line.strip()
        columns = line.split("\t")

        if columns[1] != "px":
            continue

        parts = columns[4].split(" ")
        id = parts[0]
        segments = parts[1]

        parts = segments.split(":")
        chain = parts[0]

        segments = parts[1]
        if segments != "":
            sep = segments.rfind("-")
            begin = segments[0:sep]
            end = segments[sep+1:len(segments)]
        else:
            begin = "_"
            end = "_"

        segfile = open(id+".seg", "w")
        segfile.write("0,"+chain+","+begin+","+end+"\n")
        segfile.close()

    infile.close()

if __name__ == "__main__":
    main()

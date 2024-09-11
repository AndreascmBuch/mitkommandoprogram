#!/usr/bin/env python3

import os
import sys

def list_files(directory="."):
    try:
        files = os.listdir(directory)
        for f in files:
            print(f)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "."
    list_files(directory)


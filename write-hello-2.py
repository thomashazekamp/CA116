#!/usr/bin/env python3

import sys

file = sys.argv[1]

message = "Hello world.\n"
file_name = "some-file.txt"
with open(file, "w") as f:
   f.write(message)

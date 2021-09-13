#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  if files[i][0] != ".":
    if files[i][(len(files[i]) - 3):] == ".py":
      with open(files[i]) as f:
        read = f.read()
      if read != "":
        print (files[i])
    else:
      with open(files[i]) as f:
        read = f.read()
      if read[0:22] == "#!/usr/bin/env python3":
        print (files[i])
  i = i + 1

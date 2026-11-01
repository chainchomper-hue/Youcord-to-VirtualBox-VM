# This file will just display the contents of the CommandHistory.txt file every 3 seconds.

import os
import subprocess
import time

while True:
    if os.path.exists("CommandHistory.txt"):
        subprocess.run(["cls" if os.name == "nt" else "clear"])
        with open("CommandHistory.txt", "r") as History:
            Lines = History.readlines()
        Lines = Lines[-20:]
        with open("CommandHistory.txt", "w") as History:
            History.writelines(Lines)
        for Line in Lines:
            print(Line.strip())
        print("\nHistory will be displayed here.")
        time.sleep(3)
    else:
        History = open("CommandHistory.txt", "x")
        History.close()

import os
from glob import glob
import shutil

INP = '~/out.txt' #input("ENTER .TXT FILE PATH WITH STATUS: ")
TXTFILE = os.path.expanduser(INP)
INP = '~/ROM-IMG' #input("ENTER SEARCH PATH: ")
SLOCATION = os.path.expanduser(INP)
INP = '~/android/lineage/vendor/leeco/s2/proprietary/' #input("ENTER PASTE PATH: ")
PLOCATION = os.path.expanduser(INP)


SEARCHFILE = []

with open(TXTFILE) as f:
    for line in f.readlines():
        if line[4:7].strip() == "!!":
            SEARCHFILE.append(line[7:line.find(":")])


for f in SEARCHFILE:
    FILE = f[-f[::-1].find('/'):]
    for dir,_,_ in os.walk(SLOCATION):
        if len(glob(os.path.join(dir, FILE))) != 0:
            os.makedirs(os.path.dirname(PLOCATION + f[:-f[::-1].find('/')]), exist_ok=True)
            print("{}".format(*glob(os.path.join(dir,FILE))), "->", PLOCATION + f)
            shutil.copyfile("{}".format(*glob(os.path.join(dir,FILE))), PLOCATION + f, follow_symlinks=True)

    
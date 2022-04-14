from filesplit.split import Split
import zipfile
import os
import shutil as cp

#MSG

MSG1 = """=============================
Please enter the filename.
=============================
=> """

MSG2 = """=============================
Please enter the file 
extention too.
=============================
=> """

MSG3 = """=============================
Splitting...
=============================
"""
MSG4 = """=============================
COMPLETED...
=============================
"""

name0 = input(MSG1)
EX = input(MSG2)
name = f'{name0}.{EX}'
gG = "INPUT/"
IN = f'{gG}{name}'
OUT = "OUTPUT/"



File = Split(inputfile=IN, outputdir=OUT)
print(MSG3)
File.bysize(103809024)
man_n = f"{name0}_manifest.zip"
parh = os.getcwd()
print(parh)
manifest = f"{parh}/manifest"
cp.move("OUTPUT/manifest", "manifest")
with zipfile.ZipFile(man_n, "w") as man:
    man.write("manifest")
cp.move(man_n, "OUTPUT/")
os.remove("manifest")
print(MSG4)

import glob
import os

files = glob.glob("../captures/*.pcapng")
print(files)

for f in files:
    name = f[12:f.rfind('.')]
    cmd = "tshark -T fields -n -r {} -E separator=, -e protocol -e info  >> ../captures/csv/{}".format(f, name+'.csv')
    os.system(cmd)

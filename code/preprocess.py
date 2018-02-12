import csv
import glob
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt 

# Helper function
def find_nth(text, pat):
    return text.rfind(pat, 0, text.rfind(pat))

# Read captures
files = glob.glob("../captures/csv/*.csv")
data = []

for f in files:
    csvfile=open(f)
    reader = csv.reader(csvfile,delimiter=",")
    for line in reader:
        data.append(line)
print('Read files done')

# Get dns data
dns = []
for row in data:
    if (len(row) >= 4 and row[3] == "DNS"):
        dns.append(row)
print(len(dns))

# Produce website counts
websites = {}
for row in dns:
    pld = row[5]
    if not pld.__contains__("Standard query response"):
        web = pld[pld.rfind(' ')+1:]
        web = web[find_nth(web, '.')+1:]
        websites[web] = websites.get(web, 0) + 1
print(websites)

# Plot bar chart
keys = websites.keys()
y_pos = np.arange(len(keys))
counts = []
for key in keys:
    counts.append(websites[key])
 
plt.barh(y_pos, counts, align='center', alpha=0.5)
plt.yticks(y_pos, keys)
plt.xlabel('Number of Hits')
plt.title('Websites Ranked on Usage')
 
plt.show()

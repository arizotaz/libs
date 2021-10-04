import os
import json

path = './libraries/'

list = [];

files = os.listdir(path)

for f in files:
	print(f)
	if f != ".DS_Store" and f != "compile.py" and f != "data.txt" and f != "Thumbs.db":
                list.append(f)

with open('array.txt', 'w') as outfile:
    json.dump(list, outfile)

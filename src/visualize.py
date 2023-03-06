#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = dict(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True))
#for k,v in items:
 #   print(k,':',v)

top_ten_keys = dict(reversed(sorted(items.items(), key = lambda x: x[1], reverse=True)[:10])) 

keys = []
values = []
for key,value in top_ten_keys.items():
    keys.append(key)
    values.append(value)

print("Top 10" + str(top_ten_keys))
print(f"keys = {keys}")

plt.bar(keys,values, color = 'blue', width =0.4)

plt.show(block=True)

if args.input_path == "reduced.lang":
    plt.xlabel("Language")
    plt.ylabel("Tweets with" + args.key)
else:
    plt.xlabel("Country")
    plt.ylabel("Tweets with" + args.key)


plt.savefig(args.input_path + args.key + '.png')

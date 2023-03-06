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
first_dict = dict(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True))
#for k,v in items:
 #   print(k,':',v)
top_ten_dict = dict(reversed(sorted(first_dict.items(), key = lambda x: x[1], reverse=True)[:10]))
plt.figure(figsize = (7,4.8) )
plt.bar(range(len(top_ten_dict)), top_ten_dict.values(), align='center', color = 'lightsteelblue')
plt.xticks(range(len(top_ten_dict)), top_ten_dict.keys())

if args.input_path == "reduced.lang":
    plt.xlabel("Language")
    plt.ylabel("Number of Tweets")
    plt.title(f"Number of tweets using \"{args.key}\" by Language")
else:
    plt.xlabel("Country")
    plt.ylabel("Number of Tweets")
    plt.title(f"Number of tweets using \"{args.key}\" by Country")


plt.savefig(args.input_path + '.' + args.key + '.png', pad_inches = 0)

"""
Use this file to find the most frequent keywords from Leet code company page
"""
import re
import sys
from os.path import dirname, abspath
from collections import Counter

d = dirname(dirname(abspath(__file__)))
sys.path.insert(0, d)

from utils.page_source import source

all_tags = []
for problem in source.split('label="Title"')[1:]:
    all_anchor_tags = problem.split("</a>")
    for i in all_anchor_tags[1:-1]:
        all_tags.append(i.split(">")[-1])

all_tags = dict((Counter(all_tags)))

all_tags = {i: all_tags[i] for i in sorted(all_tags, key=lambda x: -all_tags[x])}

for key, value in all_tags.items():
    print("{}".format(value))



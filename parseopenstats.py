#! /usr/bin/env python

import json

f = open('result.json')
data = json.loads(f.read())
f.close()

status = {'1' : 0, '2' : 0, '3' : 0, '4' : 0}

for id, d in data.items():
    labels = d['issue']['labels']
    for label in labels:
        if label['name'] == '1. to develop':
            status['1'] = status['1'] + 1
        elif label['name'] == '2. developing':
            status['2'] = status['2'] + 1
        elif label['name'] == '3. to review':
            status['3'] = status['3'] + 1
        elif label['name'] == '4. to release':
            status['4'] = status['4'] + 1

print(status)

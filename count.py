#! /usr/bin/env python

import json

f = open('result.json')
data = json.loads(f.read())
f.close()

print(len(data))


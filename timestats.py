#! /usr/bin/env python

import json
import datetime
import dateutil.parser
from datetime import datetime
from dateutil import tz
import statistics


f = open('result.json')
data = json.loads(f.read())
f.close()

tz = tz.tzfile('/etc/localtime')
now = datetime.now(tz)

l = []

for id, d in data.items():
    create = dateutil.parser.parse(d['pr']['created_at'])
    diff = now - create

    l.append(diff.days)

print(min(l))
print(max(l))
print(statistics.mean(l))
print(statistics.median(l))
print(statistics.stdev(l))

#! /usr/bin/env python

import sys;
import requests
import json
import link_header

username = sys.argv[1]
password = sys.argv[2]

auth=(username, password)
headers = {'user-agent': 'rullzer-gitstats'}

prlist = dict()
requrl = 'https://api.github.com/repos/nextcloud/server/pulls'
while requrl != None:
    req = requests.get(requrl, auth=auth, headers=headers)
    prs = json.loads(req.text)

    requrl = None
    links = req.headers['Link']
    links = links.split(',')
    for link in links:
        link = link_header.parse_link_value(link)
        for url in link:
            if link[url]['rel'] == 'next':
                requrl = url
                break

        if requrl != None:
            break;

    for pr in prs:
        id = pr['number']
        prlist[id] = dict()
        prlist[id]['pr'] = pr
        pr = json.loads(requests.get(pr['issue_url'], auth=auth, headers=headers).text)
        prlist[id]['issue'] = pr


f = open('result.json', 'w')
f.write(json.dumps(prlist, indent=4))
f.close()

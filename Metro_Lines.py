#!/usr/bin/env python
# coding: utf-8

import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    'api_key': '31b16966a6c3484fab2d772ae99dceab'
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/Rail.svc/json/jLines?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
with open('rlines.json', "w") as outfile:
    json.loads(data)

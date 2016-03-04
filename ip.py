# coding: utf-8
# http://httpbin.org/ip よりグローバルipを取得する

import json
from urllib2 import urlopen

def get_ipadd():
	ip = json.load(urlopen('http://httpbin.org/ip'))['origin']
	return ip

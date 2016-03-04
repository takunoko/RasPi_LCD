# coding: utf-8
# ローカルIPを取得

import socket
import fcntl
import sys

def get_lipadd(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		result = fcntl.ioctl(s.fileno(), 0x8915, #SIOCGIFADDR,
  	                             (ifname+'\0'*32)[:32])
	except IOError:
		return None

	return socket.inet_ntoa(result[20:24])

if __name__ == '__main__':
	print get_lipadd(sys.argv[1])

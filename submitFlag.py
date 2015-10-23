#!/usr/bin/python

import socket

httpServers = ['172.16.0.47', '172.16.0.48', '172.16.0.49', '172.16.0.50', '172.16.0.51', '172.16.0.52', '172.16.0.53', '172.16.0.55', '172.16.0.56', '172.16.0.57', '172.16.0.58', '172.16.0.63', '172.16.0.66', '172.16.0.67', '172.16.0.74', '172.16.0.77', '172.16.0.86', '172.16.0.99', '172.16.0.122', '172.16.0.254']

pwnServers = ['172.16.0.17', '172.16.0.18', '172.16.0.19', '172.16.0.20', '172.16.0.21', '172.16.0.22', '172.16.0.23', '172.16.0.24', '172.16.0.25', '172.16.0.26', '172.16.0.27', '172.16.0.33', '172.16.0.36', '172.16.0.37', '172.16.0.38', '172.16.0.40', '172.16.0.42', '172.16.0.44']

def submit(i):
    print "recv: %s" % i.replace("\n","")

    payload = '''POST /index.php/wargame/submit HTTP/1.1
Host: 172.16.0.77
Content-Length: '''+str(len(i)+4)+'''
Cache-Control: max-age=0
Origin: http://172.16.0.77
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
X-FirePHP-Version: 0.0.6
DNT: 1
Referer: http://172.16.0.77/index.php/wargame/index
Accept-Encoding: deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
Cookie: PHPSESSID=tgc0fq4fsvv2jgs3rteq6eni23; xdgame_username=%2A%2A%2A%2A%2A%2A

key=''' + i

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("172.16.0.77", 80))
    s.send(payload)
    a=s.recv(1000000)
    print a
    s.close()

i=raw_input()
submit(i)

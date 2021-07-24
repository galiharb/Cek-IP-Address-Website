import socket

with open('domain.txt') as f:
    lines = [line.rstrip() for line in f]

for domain in lines:
    try:
        ip = socket.gethostbyname(domain)
        print domain+" | "+ip
    except:
        print domain+" | Tidak Ditemukan"

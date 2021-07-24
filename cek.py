import socket

with open('diskominfodomain.txt') as f:
    lines = [line.rstrip() for line in f]

for subdomain in lines:
    try:
        ip = socket.gethostbyname(subdomain)
        print subdomain+" | "+ip
    except:
        print subdomain+" | Tidak Ditemukan"
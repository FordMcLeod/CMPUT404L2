#!/usr/bin/env python3


import socket


HOST = "www.google.com"
PORT = 80
BUFFER = 1024

def main():
    addr_info=socket.getaddrinfo(HOST,PORT, proto=socket.SOL_TCP)
    for addr_tup in addr_info:
        print(addr_tup)

if __name__ == "__main__":
    main()

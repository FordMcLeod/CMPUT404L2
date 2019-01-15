#!/usr/bin/env python3


import socket


HOST = "localhost"
PORT = 8081
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def conn_socket(addr_tup):
    (family,socktype,proto,cannonname, sockaddr) = addr_tup
    print(addr_tup)
    try: 
        s = socket.socket(family,socktype,proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())

        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data+= data
    except e: 
        print(e)
    finally:
        s.close()

def main():
    addr_info=socket.getaddrinfo(HOST,PORT, proto=socket.SOL_TCP)
    for addr_tup in addr_info:
        with Pool() as p:
            p.map(conn_socket, [addr_tup for _ in range(1,50)])

        #conn_socket(addr_tup)
        break

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import socket

def main():
    host = input("Enter hostname: ")
    port = input("Enter port: ")
    try:
        port = int(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10) 
        result = s.connect_ex((host, port))
        if result == 0:
            print("Connection successful")
        else:
            print(f"Connection failed with error {result}")
    except socket.timeout:
        print("Error: Connection timed out")
    except socket.gaierror:
        print("Error: Invalid hostname or address")
    except ValueError:
        print("Error: Invalid port")
    finally:
        s.close()

if __name__ == '__main__':
    main()

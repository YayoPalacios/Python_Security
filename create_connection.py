import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'example.com'
    port = 5000
    s.settimeout(10) 
    result = s.connect_ex((host, port))
    print('The result is {}'.format(result))
    s.close()

if __name__ == '__main__':
    main()
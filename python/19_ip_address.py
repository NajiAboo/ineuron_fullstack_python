import socket

def print_ip_address():
    print(socket.gethostbyname(socket.gethostname()))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Local
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])



print_ip_address()
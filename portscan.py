import socket
import sys


_ports =  [80,443,21,22,3306,2082,2083,2096,2095]

def port_scan(target):
	for port in _ports:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.1)
		code = client.connect_ex((target, port))
		if code == 0:
			print(port, "OPEN")
		else:
			print (port, "CLOSED")


if __name__ == "__main__":
	url = sys.argv[1] 
	port_scan(url)

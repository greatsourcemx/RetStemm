import socket
import sys
palabra = sys.argv[1]

nombrepc = socket.gethostbyaddr(palabra)[0]
print(nombrepc)
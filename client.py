import socket

s = socket.socket()
s.connect(("localhost", 9998))

while True:
    mensaje = input("> ")
    s.send(mensaje.encode())
    if mensaje == "quit":
        break

print("adios")

s.close()

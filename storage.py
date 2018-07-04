import socket

s = socket.socket()
s.bind(("localhost", 9998))
s.listen(1)

sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == "quit":
        break
    print(recibido.decode())
    sc.send(recibido)

print("adios")

sc.close()
s.close()

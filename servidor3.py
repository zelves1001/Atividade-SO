import socket
from datetime import *

def server(host = 'localhost', port=8082):
    data_payload = 2048 
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5)
    i = 0
    while True:
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()
        data = client.recv(data_payload)
        
        if data:
            if data.decode() == "1":
                info = date.today()
                print("Dados: %s" %info)
                client.send(info.strftime("%m/%d/%Y").encode())
                client.close()
            elif data.decode() == "2":
                info = datetime.now().strftime("%H:%M:%S")
                print("Dados: %s" %info)
                client.send(info.encode())
                client.close()
            elif data.decode() == "3":
                info = datetime.now()
                print("Dados: %s" %info)
                client.send(info.strftime("%H/%M/%S").encode())
                client.close()
            else:
                info = "VALOR INVÁLIDO"
                print("Dados: %s" %info)
                client.send(info.encode())
                client.close()
        else:
            info = "NÃO HOUVE INPUT"
            print("Dados: %s" %info)
            client.send(info)
            client.close()
            
server()

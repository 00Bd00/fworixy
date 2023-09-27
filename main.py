import socket
import threading

def handle_client(client_socket, target_host, target_port):
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_host, target_port))
    
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        target_socket.send(data)
        
        response = target_socket.recv(4096)
        if not response:
            break
        client_socket.send(response)
        
    client_socket.close()
    target_socket.close()

def start_proxy():
    proxy_port = int(input("Enter the proxy port: "))
    target_host = input("Enter the target host: ")
    target_port = int(input("Enter the target port: "))
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', proxy_port))
    server.listen(5)
    print(f'Proxy server listening on port {proxy_port}...')
    
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, target_host, target_port))
        client_handler.start()

if __name__ == '__main__':
    start_proxy()
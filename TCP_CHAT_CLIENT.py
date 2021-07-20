#! /usr/bin/python3

import socket
import time
try:
	# Creating Sockets
	client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# Ip of host to connect 
	host=input('\n[*] Enter IP of Chat Server : ')
	
	# port on which service is running
	port=int(input('[*] Enter Port of Chat Server : '))

	# connecting to provided host and port
	name = input('\n[*] Enter your name ( Visible to Server ) : ')
	time.sleep(1)	
	client_sock.connect((host,port))
	# LOGIN INFORMATION !
	print('[NOTE] Host is requesting for Username and Password : ')
	user = input('Enter Username : ')
	passw = input('Enter Password : ')
	# Sends the data of username and password to server
	client_sock.send(user.encode())
	client_sock.send(passw.encode())
	client_sock.recv(1024).decode()	
	time.sleep(1)
	# Extracts the Hostname	
	print('\n[+] Connected to',end=' ')
	client_sock.send(bytes(socket.gethostname(),'utf-8'))
	print(client_sock.recv(1024).decode())
	time.sleep(1)
	# Banner of Host Chat Server
	print(client_sock.recv(4096).decode())
	time.sleep(1)
	print('Ready to Chat !')
	while True:
		msg = input('Type -> [ Me ] : ')
		if msg == '[exit]':
			client_sock.send(bytes('\n\t'+name+' exited the chat room !\n\tPress [Enter] to exit chat room.','utf-8'))
			client_sock.close()	
			break
		if msg == ' ':
			continue
		else:
			print('Message Sent')
			print(client_sock.recv(1024).decode())
			client_sock.send(bytes('Message from '+name+' : '+msg,'utf-8'))
			#print(client_sock.recv(1024).decode())
except BrokenPipeError:
	print('[*] Host {} is offline'.format(host))
	pass
except KeyboardInterrupt:
	print('[!] Peer pressed [ctrl+c] Exiting...!')
	pass
except OSError:
	print('[!] No Server is active on ',host)
	pass
except ConnectionRefusedError:
	print('[!] No Server is active on ',host,port)
	pass

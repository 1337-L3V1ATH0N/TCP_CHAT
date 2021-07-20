#! /usr/bin/python3

import socket
import time
username = 'iamnotahacker'
password = 'Crypt0L3V1X'
conn,addr='',''
try:
	# Creating Server with IPv4 address and TCP communication method
	serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serv_name = socket.gethostname()
	serv_sock.bind(('127.0.0.1',9999))
	serv_sock.listen(1)
	names = 'L3V1ATH0N (Akash Pandey)'
	name = input('\n[*] Enter your name ( Visible to peer ) : ')
	print('Waiting for someone to connect...')
	banner = '''\n=========================================
|\t   Chat Room by L3V1ATH0N  \t|
========================================='''
	conn,addr = serv_sock.accept()
	data_user = conn.recv(1024).decode()
	data_pass = conn.recv(1024).decode()	
	if data_user != username or data_pass != password:
		conn.send(bytes('Login failed !','utf-8'))
		print('Login failed by peer')
	elif data_user == username and data_pass == password:
		time.sleep(1)
		conn.send(bytes('Login Successful !','utf-8'))
		conn.send(names.encode())
		time.sleep(1)
		print('Connected to',conn.recv(4096).decode(),addr)
		time.sleep(1)
		conn.send(bytes(str(banner).encode()))
		print('Ready to Chat !')
		while True:
			msg = input('Type -> [ Me ] : ')
			if msg == '[exit]':
				conn.send(bytes('\n\t'+name+' exited the chat room !\n\tPress [Enter] to exit chat room.','utf-8'))
				conn.close()
				break
			elif msg == ' ':
				continue
			else:
				print('Message Sent')			
				conn.send(bytes('Message from '+name+' : '+msg,'utf-8'))
				print(conn.recv(1024).decode())
				#conn.close()
	else:
		pass
except BrokenPipeError:
	print('[!] Currently Peer {} is offline'.format(addr))
	pass
except KeyboardInterrupt:
	print('[!] Server Offline !')
	pass
except OSError as os:
	print(os)
	pass

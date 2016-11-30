#encoding:utf-8
from paramiko.client import *
import time
server = '172.18.1.39'
port = 22
username = 'py'
password = 'ctid@2016'
if __name__ == '__main__':
	try:
		cli = Transport()
		cli.set_missing_host_key_policy(client.AutoAddPolicy())
		cli.connect(server,port,username,password)
	except client.SSHException as e:
		print (str(e))
	
	stdin, stdout, stderr = cli.exec_command('su -c "cat /etc/shadow"', get_pty=True)
	time.sleep(0.5)
	stdin.write('hello@2016\n')
	
	out = stdout.readlines()
	for o in out:
		print(o)
	cli.close()	

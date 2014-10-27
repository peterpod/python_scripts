import MySQLdb
import paramiko

# paramiko module used to ssh connect into device
# for device in device list: 
#	connect to each device using ip.
# 	run commands

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('<hostname>', username='<username>', password='<password>', key_filename='<path/to/openssh-private-key-file>')

stdin, stdout, stderr = ssh.exec_command('ls')
ouput stdout.readlines()
ssh.close()
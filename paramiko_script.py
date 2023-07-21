import telnetlib
import paramiko
import time
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)

#Username = str(input('Enter username: '))
#Password = str(input('Enter password: '))

with open('device_ips') as DEVICE_IP:

	for IP in DEVICE_IP:
		IP = IP.strip()
		print('##### Connecting to ' + IP + ' #####') 


		ssh_session = paramiko.SSHClient()
		ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		ssh_session.connect(IP,port=22,
				    username='anwea',
				    password='02anwe05',
				    look_for_keys=False,
				    allow_agent=False)

		ACCESS_DEVICE = ssh_session.invoke_shell()
		ACCESS_DEVICE.send('enable\n')
		#ACCESS_DEVICE.send('02anwe05\n')
		ACCESS_DEVICE.send('terminal len 0\n')
		ACCESS_DEVICE.send('show run\n')

		time.sleep(5)
		output = ACCESS_DEVICE.recv(65000)
		print (output.decode('ascii'))
		print('\n\n')

		back_up = open('DEVICE_' + IP + '_' + str(TNOW), 'w')
		back_up.write(output.decode('ascii'))
		back_up.close

		ssh_session.close


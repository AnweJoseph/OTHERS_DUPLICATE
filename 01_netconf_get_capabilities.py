from ncclient import manager

RTR1_MGR = manager.connect(host='192.168.164.150',
				port=830,
				username='anwea',
				password='02anwe05',
				hostkey_verify=False,
				device_params={'name':'csr'})

for RTR in RTR1_MGR.server_capabilities:
	print(RTR)

RTR1_MGR.close_session()

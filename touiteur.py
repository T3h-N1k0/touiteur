#!/usr/bin/env python

import twitter
import os
import cups
import time

api = twitter.Api(consumer_key='NaO2BGx4cdfBU18kx4RcohglU',
                      consumer_secret='HiI9jo9UwUx854IkaEcdATRSSVgUJVywN8XDoeiQtDcKDXrdNZ',
                      access_token_key='1854246193-2ZMEH7jY5gsj9qMzPIrNujFE2vgqodZvWN9S8Ek',
                      access_token_secret='6eDRnawpsHEr8s9sFzkUVrW23ifc1pWNEpLtBv98k0fWr')


last_id = 0

while 1:
	statuses = api.GetSearch("#freeasinfreestyle OR #rmll2014", since_id =last_id)
	
	print str(len(statuses)) + " nouveaux messages"

	if len(statuses) != 0:
		with open('daMsg', 'w') as fileToPrint:
			for status in statuses:
				fileToPrint.write(status.text.encode("utf8") + "\n")
				if status.id > last_id: 
					last_id = status.id			
		conn = cups.Connection()
		#printers = conn.getPrinters()
		print "Debut de l'impression..."
		conn.printFile("Da_RMLL_Printer", 'daMsg', "Python_Status_print", {})
		print "Impression terminee"
	time.sleep(60)
	
#os.system('lpr /home/libres/daMsg')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from subprocess import Popen, PIPE

class penmode:
	def __init__(self,target):
		# Inizializzazione oggetto
		# Target SENZA http://
		self.t = target
		if "http://" in self.t:
    			self.t = self.t[7:]
		# IP del target da tor-resolve
		self.ip = str(Popen('tor-resolve '+self.t+' 127.0.0.1:9050', shell=True, stdout=PIPE).stdout.read()).replace("b''",'')

	def pendate(self):
		# Funzione che rileva la data per i log
		return datetime.datetime.now().strftime("-%m-%d-%Y_%H-%M")
	
	def sqlmap(self):
		return 'sudo proxychains sqlmap --wizard | tee ./' + self.t + self.pendate() + '.txt'	

	def nmap(self):
		return 'sudo proxychains nmap -sV -O -P0 -p 21,22,25,53,80,135,139,443,445 ' + self.ip + ' | tee ./' + self.t + self.pendate() + '.txt'

	def whatweb(self):
		return 'whatweb -v 127.0.0.1:8080 | tee ./nmap' + self.ip + self.pendate() + '.txt'
	
	def slowloris(self,number,timeout):
		return 'perl /opt/backbox/penmode/slowloris.pl -dns 127.0.0.1 -port 8080 -timeout '+str(timeout)+' -num '+str(number)
		
	def exploit(self):
		return 'sudo proxychains htexploit -u' + self.ip + '-o -w --verbose 3'
		
	def skipfish(self):
		return 'sudo proxychains skipfish -o /home/' + self.ip + 'http.//' + self.ip
	
	def wpscan(self):
		return 'sudo proxychains wpscan --url' + self.ip + ' | tee ./wpscan' + self.pendate() + '.txt'
		
	def joomscan(self):
		return 'joomscan -u' + self.ip + '-x 127.0.0.1:8080 | tee ./joomscan' + self.pendate() + '.txt'
		
	def nikto(self):
		return 'nikto -h 127.0.0.1:8080 | tee ./nikto' + self.pendate() + '.txt'
 
 

################## FINE CLASSE #################

#################################################
#    SOLO PER IL DEBUG - CODICE TEMPORANEO      #
#         SOLO PER ESEMPIO D'UTILIZZO           #
#################################################
#def main():
#	x = penmode("target.it")
#	print x.nmap()
#	print ''
#	print x.slowloris(1000,200)
#
#main()

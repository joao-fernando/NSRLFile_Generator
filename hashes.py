 #
 # Copyright 2020-2020, João Fernando Paiva Castro
 # GNU General Public License version 3.0
 #
 # Módulo auxiliar do script NSRLFile_Generator.py
 # Recebe o caminho de um arquivo como entrada e retorna um dicionário contendo SH1, MD5, CRC32, nome do arquivo e tamanho do arquivo

import hashlib
import binascii
import os

def calc_hashes(filename):
	BUF_SIZE = 65536 # para ler o arquivo em pedaços de 64kb

	# Cria os objetos de hash sha1 e md5
	sha1 = hashlib.sha1()
	md5 = hashlib.md5()

	# abre o arquivo no modo rb: read-only e binário
	with open(filename, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE) # lê 64kb do arquivo
			if not data:
				break
			# calcula SH1, MD5 e CRC32
			sha1.update(data) 
			md5.update(data)
			crc32 = (binascii.crc32(data))
	
	# Cria o dicionário com os dados necessários
	information = {'SHA1' : sha1.hexdigest().upper(), 
				   'MD5' : md5.hexdigest().upper(),
				   'CRC32' : "%08X" % (crc32 & 0xFFFFFFFF),
				   'FileName' : os.path.basename(filename),
				   'FileSize' : os.path.getsize(filename)
				   }
				   
	return information	
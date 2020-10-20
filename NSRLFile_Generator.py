 #
 # Copyright 2020-2020, João Fernando Paiva Castro
 # GNU General Public License version 3.0
 #
 # Script para gerar o arquivo NSRLFile.txt
 # 1) Coloque todos os arquivos que deseja incluir no NSRLFile.txt em uma pasta
 # 2) Execute o script e selecione a pasta
 # 3) O arquivo será gerado na pasta NSRL_hashes dentro da pasta selecionada no passo 2
 # 4) Para importar os hashes no IPED --> iped.exe -importkff caminho_da_pasta_criada_no_passo_3
 #
 # Observação: Não segue os códigos de produto, sistema operacional, nem nada do site NSRL.
 # 			   O objetivo é gerar uma lista de arquivos que serão ignorados do processamento do IPED e não distribuir hashes na internet.

import os
import hashes
import tkinter.filedialog
import csv

# Para montar a janela que seleciona a pasta
root = tkinter.Tk()
root.withdraw()

# Seleciona a pasta e lista todos os arquivos
folder_path = tkinter.filedialog.askdirectory()
list_directory = [f.name for f in os.scandir(folder_path) if f.is_file()]

# Cria a pasta NSRL_hashes dentro da pasta selecionada anteriormente (folder_path)
try:
	os.mkdir(folder_path + '\\NSRL_hashes')
except OSError:
	print("Erro criando a pasta de destino.")

with open(folder_path + '\\NSRL_hashes\\NSRLFile.txt', 'w', newline='') as NSRLFile:
	# Cria o cabeçalho do arquivo
	NSRLFile_field_names = ['SHA-1','MD5','CRC32','FileName','FileSize','ProductCode','OpSystemCode','SpecialCode']
	NSRLFile_writer = csv.DictWriter(NSRLFile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, fieldnames=NSRLFile_field_names, escapechar='"')
	NSRLFile_writer.writeheader()

	# Realiza os cálculos para cada arquivo encontrado em folder_path e grava os resultados no arquivo NSRLFile.txt
	for file_name in list_directory:
		information = hashes.calc_hashes(folder_path+"\\"+file_name)
		NSRLFile_writer.writerow({'SHA-1' : information['SHA1'],
								  'MD5' : information['MD5'],
								  'CRC32' : information['CRC32'],
								  'FileName' : information['FileName'],
								  'FileSize' : information['FileSize'],
								  'ProductCode' : 1,
								  'OpSystemCode' : "84",
								  'SpecialCode' : ""
								})
								
with open(folder_path + '\\NSRL_hashes\\NSRLProd.txt', 'w', newline='') as NSRLProd:
	NSRLProd_field_names = ["ProductCode","ProductName","ProductVersion","OpSystemCode","MfgCode","Language","ApplicationType"]
	NSRLProd_writer = csv.DictWriter(NSRLProd, delimiter=',', quoting=csv.QUOTE_NONNUMERIC, fieldnames=NSRLProd_field_names, escapechar='"')
	
	NSRLProd_writer.writeheader()

	# Cria o arquivo NSRLProd.txt
	NSRLProd_writer.writerow({'ProductCode' : 1,
							  'ProductName' : "Ignored Files",
							  'ProductVersion' : "1.0.0",
							  'OpSystemCode' : "646",
							  'MfgCode' : "2638",
							  'Language' : "Unknown",
							  'ApplicationType' : "Ignored Files"
							})								

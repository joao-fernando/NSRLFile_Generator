# NSRLFile_Generator
NSLRFile.txt generator for IPED
Desenvolvido em Python 3.9

Script para criar o arquivo NSRLFile.txt para importação de hashes ignoráveis pelo IPED.

Uso:
1) Copiar os arquivos que quer incluir nos hashes ignoráveis em uma pasta qualquer
2) Executar o script
3) Selecionar a pasta do passo 1 (O script criará a pasta NSLR_hashes dentro dessa pasta)
5) Importar a pasta no IPED com o comando iped.exe -importkff caminho_da_pasta_NSLR_hashes

import struct
import csv
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
print('Abrindo a planilha de janeiro')
f = open('201701_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

print('Criando o arquivo dat de janeiro')
t = open('BolsaFamiliaJanMenor.dat', 'wb')
print('Lendo a planilha')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue
	

	if i%1000000 == 0:
		print(i)

	i += 1

	info = linha[0].split('\t')
	
	if len(info[2]) < 30:
		info[2] = info[2] + ' ' * (30 - len(info[2]))

	if len(info[8]) < 50:
		info[8] = info[8] + ' ' * (50 - len(info[8]))

	if len(info[10]) < 6:
		info[10] = info[10] + ' ' * (6 - len(info[10]))

	t.write(s.pack(bytearray(info[0], encoding = 'cp1252'),
                   bytearray(info[2], encoding = 'cp1252'),
                   bytearray(info[7], encoding = 'cp1252'),
                   bytearray(info[8], encoding = 'cp1252'),
                   bytearray(info[10], encoding = 'cp1252'),
                   bytearray('\n', encoding = 'cp1252'))) 
	if i == 10000:
		break
t.close()

print('Abrindo a planilha de fevereiro')
f = open('201702_BolsaFamiliaFolhaPagamento.csv', encoding = 'cp1252')

print('Criando o arquivo dat de fevereiro')
t = open('BolsaFamiliaFevMenor.dat', 'wb')
print('Lendo a planilha')
r = csv.reader(f)

i = 1

for linha in r:
	if i == 1:
		i += 1
		continue

	if i%1000000 == 0:
		print(i)

	i += 1

	info = linha[0].split('\t')

	if len(info[2]) < 30:
		info[2] = info[2] + ' ' * (30 - len(info[2]))

	if len(info[8]) < 50:
		info[8] = info[8] + ' ' * (50 - len(info[8]))

	if len(info[10]) < 6:
		info[10] = info[10] + ' ' * (6 - len(info[10]))
	info = linha[0].split('\t')
	t.write(s.pack(bytearray(info[0], encoding = 'cp1252'),
                   bytearray(info[2], encoding = 'cp1252'),
                   bytearray(info[7], encoding = 'cp1252'),
                   bytearray(info[8], encoding = 'cp1252'),
                   bytearray(info[10], encoding = 'cp1252'),
                   bytearray('\n', encoding = 'cp1252')))
	if i == 10000:
		break

t.close()

print(time()-ti)
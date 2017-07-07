import struct
import os
from math import ceil
from time import time

tempo = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('BolsaFamiliaJanMenor.dat', 'rb')
f2 = open('BolsaFamiliaFev1.dat', 'rb')
linha1 = f1.read(s.size)
presente = 0
naoPresente = 0
total = 0

while linha1 != b'':
	inicio = 0
	fim = os.path.getsize('BolsaFamiliaFev1.dat') // s.size
	meio = int((inicio + fim) / 2)
	f2.seek(meio * s.size)
	linha2 = f2.read(s.size)
	dados1 = s.unpack(linha1)
	
	while inicio <= fim and linha2 != b'':
		dados2 = s.unpack(linha2)
		total += 1

		if int(dados1[2]) == int(dados2[2]):
			presente += 1
			break
		elif int(dados1[2]) < int(dados2[2]):
			fim = meio - 1
			meio = ceil((inicio + fim) / 2)
		else:
			inicio = meio + 1
			meio = ceil((inicio + fim) / 2)

		f2.seek(int(meio * s.size))
		linha2 = f2.read(s.size)
	
	if inicio > fim or linha2 == b'':
		naoPresente += 1

	linha1 = f1.read(s.size)

print('Quantidade de registros que existem nas duas tabelas: ' + str(presente))
print('Quantidade de registros que so existem na tabela de janeiro: ' + str(naoPresente))
print('Media de acessos: ' + str(total / 13601764))
print(time() - tempo)
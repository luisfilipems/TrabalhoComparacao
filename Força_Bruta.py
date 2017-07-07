import struct
from time import time

ti = time()
estrutura = '2s30s14s50s6s2s'
s = struct.Struct(estrutura)
f1 = open('BolsaFamiliaJanMenor.dat', 'rb')
f2 = open('BolsaFamiliaFev.dat', 'rb')
linha1 = f1.read(s.size)
presente = 0
naoPresente = 0
total = 0
i = 0

while linha1 != b'':
	i += 1

	if i%1000 == 0:
		print(str(i//1000) + "%")
	dados1 = s.unpack(linha1)
	f2.seek(0)
	linha2 = f2.read(s.size)
	
	while linha2 != b'':
		total += 1
		dados2 = s.unpack(linha2)
		
		if dados1[2] == dados2[2]:
			presente += 1
			break
		
		else:
			linha2 = f2.read(s.size)
			if linha2 == b'':
				naoPresente += 1
				break

	linha1 = f1.read(s.size)

print("Quantidade de registros que existem nas duas tabelas: " + str(presente))
print("Quantidade de registros que so existem na tabela de janeiro: " + str(naoPresente))
print("Media de acessos: " + str(total / 100000))
print(time()-ti)
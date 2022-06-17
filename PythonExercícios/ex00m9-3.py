#resposta do curso
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO')

print('='*20)

# minha resposta
cidade = str(input('Em que cidade você nasceu: '))
res = 'Paracambi'in cidade
print(res)

#treinando
cidade = str(input('Em qual cidade você nasceu? ')).strip()
estado = str(input('Em qual estado você nasceu? ')).strip()
municipio = str(input('Em qual cidade município você mora? ')).strip()
print('A sua cidade onde você nasceu foi.. {}'.format(cidade.capitalize().upper()))
print('O estado onde você nasceu foi.. {}'.format(estado.title()))


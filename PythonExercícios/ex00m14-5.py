# resposta do curso
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo),end=' > ')
    termo += razão
    cont += 1
print('FIM')

print('-='*20)

# minha resposta (com ajuda do curso)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro # Essa vai ser uma varialvel para o termo
cont = 1 # esse vai ser contador
while cont <= 10: # Enquanto (While) cont for menor ou igual (< =) 10.
    print('{}'.format(termo), end=' > ')
    termo += razao # ele vai somar o Termo (primeiro) com a Razão. Ex: 3 + 5 (razão) = 8 + 5 (razão) = 13
    cont += 1 # ele vai fazer a contagem, quando chegar no 10, ele vai parar
print('ACABOU')
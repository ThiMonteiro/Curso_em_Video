# resposta do curso
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0 # Ele vai ser o total de termos que ele vai me mostrar. Com 0 sendo o ponto de partida
mais = 10 # Ele vai simular que a pessoa que mais 10 termos.
while mais != 0: #Enquanto (While) for diferente (! =) 0 continua. Vai ser uma estrutura de laço dentro de outra
    total += mais
    while cont <= total: # Enquanto (While) cont for menor ou igual (< =) a total, faz a progressão.
        print('{}'.format(termo),end=' > ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

# minha resposta (Treinando)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' > ')
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizadam com {} termos mostrados.'.format(total))
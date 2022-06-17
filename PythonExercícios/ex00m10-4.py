#minha resposta
km = float(input('Qual é a distância da sua viagem?KM '))
menor = 0.50 * km
maior = 0.45 * km
if km <= 200:
    print('A sua viagem de {}Km, vai custar R${:.2f}'.format(km, menor))
    #menor = 0.50 * km
else:
    print('A sua viagem de {}Km, vai custar R${:.2f}'.format(km, maior))
    #maior = 0.45 * km

print('-=-'*20)

# resposta do curso (usando condição, normal.)
distancia = float(input('\033[36mQual é a distância da sua viagem?\033[m '))
print('\033[32mVocê está prestes a começar uma viagem de {}Km\033[m'.format(distancia))
if distancia <=200:
    preço =  distancia * 0.50
else:
    preço = distancia * 0.45
print('\033[35mE o preço da sua passagem será de R${:.2f}\033[m'.format(preço))
print('-=-'*20)

# resposta do curso (usando condiçõa, simples.)
distancia = float(input('Qual é distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <=200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

print('-'*20)

# treinando
km = float(input('Quantos KM sua viagem tem? '))
print('Prepare-se! Sua viagem de {}KM está prestes á começar!'.format(km))
menor = 0.50 * km
maior = 0.45 * km
if km <= 200:
    print('Analisando...')
    print('A sua viagem de {}, vai custar R${:.2f}.'.format(km, menor))
    # menor
else:
    print('Analisando...')
    print('A sua viagem de {}KM, vai custar R${:.2f}.'.format(km, maior))
    # maior
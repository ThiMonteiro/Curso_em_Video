#minha resposta
print('Limite da estrada 80km')
velocidade = float(input('Digite a velocidade de um veículo: '))
soma = (velocidade - 80) * 7
if velocidade <=80:
    print('PARABÉNS! Você está dentro do limite!')
    print('Tenha um bom dia!')
else:
    print('MULTADO!!')
    print('Você irá pagar R${:.2f}, por ter passado do limite! Dirija com cuidado!'.format(soma))

print('-=-'*20)

#resposta do curso (usando uma condição simples)
velocidade = float(input('\033[36mQual é velocidade atual do carro? \033[m'))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m')
    multa = (velocidade - 80) * 7
    print('\033[31mVocê deve pagar um multa de R${:.2f}\033[m!'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')

# treinando
print('ATENÇÃO! Limite de velocidade de 80KM/h.')
speed = float(input('Qual é velocidade atual do seu carro? '))
soma = (speed - 80) * 7
if speed <= 80:
    print('Você está dentro do limite.')
    print('Tenha um bom dia!')
else:
    print('MULTADO!')
    print('Voê está acima da velocidade!!')
    print('Você irá pagar uma multa de R${:.2f}'.format(soma))
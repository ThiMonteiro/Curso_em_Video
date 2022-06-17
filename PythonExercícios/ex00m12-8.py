# resposta do curso
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está faixa peso normal')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÔRBIDA, Cuidado!')

print('-='*20)

# minha resposta
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
soma = peso / (altura ** 2)
if soma < 18.5:
    print('IMC (Indice de Massa Corporal): {:.1f}'.format(soma))
    print('Abaixo do peso')
elif soma >= 18.5 and soma < 25:
    print('IMC (Indice de Massa Corporal): {:.1f}'.format(soma))
    print('Peso Ideal')
elif soma >= 25 and soma < 30:
    print('IMC (Indice de Massa Corporal): {:.1f}'.format(soma))
    print('Sobre-peso')
elif soma >= 30 and soma < 40:
    print('IMC (Indice de Massa Corporal): {:.1f}'.format(soma))
    print('Obesidade')
elif soma > 40:
    print('IMC (Indice de Massa Corporal): {:.1f}'.format(soma))
    print('Obesidade Mórbida')
# resposta do curso
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

print('='*20)

# minha resposta (com ajuda do curso) "forma simples"
nome = str(input('Digite o seu nome completo? ')).strip()
print('Nome(maiúsculo):', nome.upper())
print('Nome(minúscula):', nome.lower())
print('Quantidade de letras (nome completo):', len(nome) - nome.count(' '))
print('Quantidade de letras (primeiro nome):', nome.find(' '))

print('='*20)
# treinando
nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculo.. {}'.format(nome.upper()))
print('Seu nome em minúscula.. {}'.format(nome.lower()))
print('Quantidade de letras que o seu nome tem é: {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

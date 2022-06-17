# resposta do curso
nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem "Silva"? {}'.format('SILVA' in nome.upper()))

print('='*20)
# minha resposta
nome = str(input('Qual o seu nome completo? ')).strip()
res = 'Monteiro' in nome
print('Seu nome tem "Monteiro"? {}'.format(res))
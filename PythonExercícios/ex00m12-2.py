# resposta do curso
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente Novamente.')

print('-='*20)

#minha resposta (pesquisando na internet como se faz)
num = int(input('Digite um número: '))
print('-='*20)
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
conversao = str(input('Digite a opção que deseja converter: '))
if conversao == '1':
    binario = (bin(num))
    print('Seu número convertido em BINÁRIO: {}'.format(binario))
elif conversao == '2':
    octal = (oct(num))
    print('Seu número convertido em OCTAL: {}'.format(octal))
elif conversao == '3':
    exadecimal = (hex(num))
    print('Seu número convertido em HEXADECIMAL: {}'.format(exadecimal))
else:
    print('****FINALIZADO****')
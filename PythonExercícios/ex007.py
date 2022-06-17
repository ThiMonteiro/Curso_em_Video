#resposta do curso
print('-'*20)
largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede? '))
metros = largura * altura
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m2.'.format(largura, altura, metros))
tinta = metros / 2
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))
print('-'*20)

#minha "resposta"
largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
metros = largura * altura
print('A sua parede tem a dimensão de {}x{} e a sua área é de {}m2.'.format(largura, altura, metros))
tinta = metros / 2
print('Para pintar a sua parede você ira precisará de {}l de tinta.'.format(tinta))
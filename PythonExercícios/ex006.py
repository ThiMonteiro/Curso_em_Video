#"resposta" do curso
real = float(input('Quantidade em Real: '))
dolar = real / 5.20
euro = real / 6.15
libra =  real / 0.14
iene = real / 0.047
australiano = real / 3.84
print('Com R$ {:.2f}, você pode comprar: \n$ {:.2f} \n€ {:.2f} \n£ {:.2f} \n¥ {:.2f} \nA$ {:.2f}'
      .format(real, dolar, euro, libra, iene, australiano))

#minha resposta
real = float(input('Quantidade em Real: '))
dolar = real / 5.34
euro = real / 6.25
libra = real / 7.34
iene = real / 0.048
australiano = real / 3.89
print('Com R$ {:.2f}, você pode comprar: \n$ {:.2f} \n€ {:.2f} \n£ {:.2f} \n¥ {:.2f} \nA$ {:.2f}'
      .format(real, dolar, euro, libra, iene, australiano))

times = ('Cotinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'FLuminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-='*50)
print(f'lista de times do Brasileirão: {times}')
print('-='*50)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*50)
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*50)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-='*50)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

print('-=-'*50)

# minha resposta
time = ('Flamemengo', 'Santos', 'Palmeiras', 'Gremio','Athletico-PR')
print('='*50)
print(f'Lista de times do Brasileirão: {time}')
print('='*50)
print(f'Os 3 primeiros são: {time[0:3]}')
print('='*50)
print(f'Os 2 ultimos são: {time[-2:]}')
print('='*50)
print(f'Times em ordem alfabéticas: {sorted(time)}')
print('='*50)
print(f'O {time[2]} está na {time.index("Palmeiras")+1}º posição')
print('='*50)
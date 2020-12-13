hora = input('Hora: ')
h, m, s = hora.split(':')
hh = int(h)
mm = int(m)
ss = int(s)
incorrecta = False

if hh < 0 or hh > 23:
    incorrecta = True
elif mm < 0 or mm > 59:
    incorrecta = True
elif ss < 0 or ss > 59:
    incorrecta = True
else:
    ss += 1
    mm += ss // 60
    ss = ss % 60
    hh += mm // 60
    mm = mm % 60
    hh = hh % 24
    print(f'{hh}:{mm}:{ss}')

if incorrecta:
    print('La hora es incorrecta')
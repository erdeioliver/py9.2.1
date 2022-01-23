'''
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!
O O O
O O O
O O O

2.2 Feladat
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0), a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot, hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!
'''



tarolo = []
for i in range(3):
    lista = []
    tarolo.append(lista)
    for i in range(3):
        lista.append('O ')

bekeres = int(input('Egyik kordináta? '))
bekeres2 = int(input('Másik kordináta? '))
if bekeres2 == 1:
    bekeres += 3
elif bekeres2 == 2:
    bekeres += 6

szamlalo2 = 0
for i in range(3): #oszlop
    szamlalo = 0
    for i in tarolo:
        for x in i:
            if szamlalo == 3:
                for _ in range(3): #sor
                    if szamlalo2 == bekeres:
                        print('+ ', end='')
                        szamlalo2 += 1
                    else:
                        print(x, end='')
                        szamlalo2 += 1
                    
            szamlalo += 1
    print('')
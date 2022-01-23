'''
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista! Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '. A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki. A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!
O O O
O O O
O O O 
'''



tarolo = []
for i in range(3):
    lista = []
    tarolo.append(lista)
    for i in range(3):
        lista.append('O ')
        
for i in range(3):
    szamlalo = 0
    for i in tarolo:
        szamlalo += 1
        for x in i:
            if szamlalo == 3:
                print(x, end='')
    print('')

            

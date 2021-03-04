import time
import random
import json
import numpy as np
import keyboard
import copy


i = 28
j = 16

ground = '#' * (i+2)

allmatr = []



while 1:

    snecc = [8,14]
    tail = [(8,14),(8,14)]
    def mov():
        snecc[0] += 1
    move = "w"

    



    bibis_mind = open('bibis_mind.json', 'r')
    xlist_jsn = bibis_mind.read()

    bibis_mind.close()

    if not(xlist_jsn):

        xlist = []
        gen = 1
        for x in range(4):
            ylist = []
            for y in range(int(j/2)):
                zlist = []
                for z in range(int(i/2)):
                    zlist.append(2*(0.5 - random.random()))
                ylist.append(zlist)
            xlist.append(ylist)

        

    else:
        xlist_jsn = json.loads(xlist_jsn)
        xlist = xlist_jsn[1]
        for x in xlist:
            gen = xlist_jsn[2]
            print(len(x))
            for y in x:
                print(len(y))
                for z in y:
                    z += 2*(1/gen)*(0.5 - random.random())
    qlist = copy.deepcopy(xlist)

    for x in xlist:
        for y in x:
            z = y.copy()
            z.reverse()
            y.extend(z)
        k = x.copy()
        k.reverse()
        x.extend(k)
    
    matr1 = []
    
    for x in xlist:
        extendlist = []
        for y in x:
            extendlist.extend(y)
        matr1.append(extendlist)





    matr1 = np.array(matr1)
        
    
    
    while 1:
        point = [random.randint(0,j-1),random.randint(0,i-1)]
        if tuple(point) in tail or point == snecc:
            continue
        else:
            break
        
    print('\n' * 20)
    
  
    exp = 100

    repeat = 448

    while 1:
        

        
        a = [' '] * i                                #создание карты, цикл создания разных списков
        map1 = [] ; k = j
        while k:
            k = k - 1
            map1.append(a.copy())
    
        map1[point[0]][point[1]] = 'O'
        
        map1[snecc[0]][snecc[1]] = '@'               #голова змейки на карте
        for x in tail:
            map1[x[0]][x[1]] = '#'
    
        print(ground)
        for x in map1:                               #цикл вывода карты в терминал
            f = ''
            for y in x:
                f = f + y
            print('#' + f + '#')
        print(ground)
    
        
        matr2 = []
        for x in map1:
            for y in x:                             #преобразование карты для входа нейросети
                if y == ' ':
                    matr2.append(0)
                elif y == '#':
                    matr2.append(-1)
                elif y == 'O':
                    matr2.append(1)
                elif y == '@':
                    matr2.append(-2)
        matr2 = np.array(matr2)
        
        matans = matr1.dot(matr2)
    
        matans = list(matans)
    
        if point == snecc:                           #обозначение яблока на карте
            tail.append(point.copy())
            exp += 100
            repeat = 448
            while 1:
                point = [random.randint(0,j-1),random.randint(0,i-1)]
                if tuple(point) in tail or point == snecc:
                    continue
                else:
                    break
        
        score = len(tail)
        while score - 1:                             #изменение координат хвоста
            tail[score - 1] = tail[score - 2]
            score = score - 1
        tail[0] = tuple(snecc)
        
#        time.sleep(0.03)
    
    
        if matans.index(max(matans)) == 0 and move != 'w':                 
            def mov():
                snecc[0] += 1                       #изменение координаты головы змейки
            move = 's'
        elif matans.index(max(matans)) == 1 and move != 'a':
            def mov():
                snecc[1] += 1
            move = 'd'
        elif matans.index(max(matans)) == 2 and move != 's':
            def mov():
                snecc[0] = snecc[0] - 1
            move = 'w'
        elif matans.index(max(matans)) == 3 and move != 'd':
            def mov():
                snecc[1] = snecc[1] - 1
            move = 'a'
        mov()
                
        if tuple(snecc) in tail:                    #если врезаешся в хвост проигрываешь
            exp += -100
            break
        if snecc[0] < 0 or snecc[0] > j-1 or snecc[1] < 0 or snecc[1] > i-1:
            exp += -100
            break
        if keyboard.is_pressed('q'):
            exp += -100
            break
        if not(repeat):
            exp += -100
            break
        repeat += -1
            

    allmatr.append([exp,qlist])
    print(len(qlist))
    if len(allmatr) == 1000:
        gen += 1
        best = allmatr[0][0]
        bestmatr = []
        for x in allmatr:
            if x[0] >= best:
                best = x[0]
                bestmatr = x

        bestmatr.append(gen)

        bibis_mind = open('bibis_mind.json', 'w')
        bibis_mind.write(json.dumps(bestmatr))
        bibis_mind.close()

        print(len(bestmatr[1]), len(bestmatr[1][0]))
        print(bestmatr[0],bestmatr[2])
        break
#    print(exp)
#    print('\n\n##############################\n# seems like the game is over#\n##############################\n\n')

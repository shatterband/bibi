import time
import random
import json
import numpy as np
import keyboard


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

    

    '''it's for rewrite bibis mind (also that is great codeswitch system here, just remowe or add   # before """)
    matr1 = []
    for x in range(4):
        prematr = []
        for y in range(i*j):
            prematr.append(random.random())
        matr1.append(prematr)
    
    bibis_mind = json.dumps(matr1)
    
    f = open('bibis_mind.json', 'w')
    
    f.write(bibis_mind)
    
    f.close()
    '''
    
    f = open('bibis_mind.json', 'r')
    bibis_mind = f.read()
    
    matr1 = json.loads(bibis_mind)
    #and it for read bibis mind '''
    matr1 = np.array(matr1)
        
    
    
    while 1:
        point = [random.randint(0,j-1),random.randint(0,i-1)]
        if tuple(point) in tail or point == snecc:
            continue
        else:
            break
        
    print('\n' * 20)
    
    
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
            for y in x:
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
        
        time.sleep(0.17)
    
    
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
            break
        if snecc[0] < 0 or snecc[0] > j-1 or snecc[1] < 0 or snecc[1] > i-1:
            break
        if keyboard.is_pressed('q'):
            break


    
    print('\n\n##############################\n# seems like the game is over#\n##############################\n\n')

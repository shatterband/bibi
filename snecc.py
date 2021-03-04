import time
import keyboard
import random


i = 27
j = 16

ground = '#' * (i+2)

snecc = [2,6]
tail = [(2,6),(2,6)]
def mov():
    snecc[0] += 1
move = "w"


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
    
    time.sleep(0.2)

    if keyboard.is_pressed('s') and move != 'w' :                 
        def mov():
            snecc[0] += 1                       #изменение координаты головы змейки
        move = 's'                              #сохранение направления двиения
    elif keyboard.is_pressed('d') and move != 'a':
        def mov():
            snecc[1] += 1
        move = 'd'
    elif keyboard.is_pressed('w') and move != 's':
        def mov():
            snecc[0] = snecc[0] - 1
        move = 'w'
    elif keyboard.is_pressed('a') and move != 'd':
        def mov():
            snecc[1] = snecc[1] - 1
        move = 'a'

    mov()
            
    if tuple(snecc) in tail:                    #если врезаешся в хвост проигрываешь
        break
    if snecc[0] < 0 or snecc[0] > j-1 or snecc[1] < 0 or snecc[1] > i-1:
        break

input('\n\n#############################\n#seems like the game is over#\n#############################\n\n')




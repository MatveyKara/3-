class Func():

    def prosmotr(split):
        cif = '0123456789'
        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
            lines = r.readlines()
            new = [line for line in lines if len(line)!= 1] 
        with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
            w.writelines(new)
    
        with open('Машинки1.txt', 'r') as s: #, encoding="utf-8"
            S = s.readlines()
            a = len(S) # Количество автомобилей
            for x in S:
                if x[0] == '' or x[0] == ' ':
                    a -= 1
        number = [int(x) for x in range(1, a + 1)]
        
        menu = input()
        if (menu[0] == '1' or menu[0] == '2' or menu[0] == '3' or menu[0] == '4' or menu[0] == '5' or menu[0] == '6' or\
                menu[0] == '7' or menu[0] == '8' or menu[0] == '9'):
            x = int(menu)
            if x not in range(1,len(S)+1):
                print('Вы ввели неправильный номер машины.\nВведите ещё раз')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                func.prosmotr() # Вызов функции ПРОСМОТР(ИЗМЕНИТЬ)
            else:
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                stroka = []
                split = ''
                for y in S[x-1]:
                    if y == ',':
                        stroka += [split]
                        split = ''
                    else:
                        split += y
                if split:
                    stroka += [split]
                print('Характеристики автомобиля:\n')
                print('Гос. номер       ', stroka[1])
                print('Цвет             ', stroka[2])
                print('Год выпуска      ', stroka[3])
                print('Объём двигателя  ', stroka[4], end=' л.\n')
                print('Мощность         ', stroka[5], end=' л.с.\n')
                #----------------------------
                print('Состояние фар    ', stroka[6])
                print('Состояние дверей ', stroka[7])
                #----------------------------
                print('')
                print('\nЧтобы изменить характеристики введите - изменить')
                print('\nЧтобы вернуться назад введите - назад')
                f5 = 0
                while f5 == 0:
                    dobavit = str(input())
                    if dobavit == 'назад' or dobavit == 'Назад':
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                        f1 = 1
                        f5 = 1
                        func.While()# Вызов функции МЕНЮ
                    elif dobavit == 'изменить' or dobavit == 'Изменить':
                        print('1) Гос. номер     ')
                        print('2) Цвет           ')
                        print('3) Год выпуска    ')
                        print('4) Объём двигателя')
                        print('5) Мощность       ')
                        #----------------------------
                        print('6) Состояние фар   ')
                        print('7) Состояние дверей')
                        #----------------------------
                        print('Введите номер характеристики, которую хотите изменить')
                        izm = str(input())
                        while izm not in cif:
                            print('Нет такой характеристики. Введите заново: ')
                            izm = str(input())
                        while int(izm) not in range(1, 8):
                            print('Нет такой характеристики. Введите заново: ')
                            izm = str(input())
                        if int(izm) in range(1, 8):
                            print('Введите характеристику, которую вы изменили')
                            izmen = input()
                            stroka[int(izm)] = izmen
                            with open('Машинки1.txt', 'r') as r:  #encoding="utf-8"
                                stroki = r.readlines()
                                count = 1
                                with open('Машинки1.txt', 'w') as w: #encoding="utf-8"
                                    for line in stroki:
                                        if count != x:
                                            w.write(line)
                                        elif count == x:
                                            w.write(stroka[0]+','+stroka[1]+','+stroka[2]+','+stroka[3]+','+stroka[4]+','+stroka[5]+
                                                    ','+stroka[6]+','+stroka[7]+'\n')
                                        count += 1
                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nХарактеристики автомобиля успешно изменены\n')
                            f5 = 1
                            f1 = 1
                            func.While()# Вызов функции МЕНЮ
                    else:
                        print('Неверная команду. Введите заново: ')
                        f5 = 0
                        func.While()# Вызов функции МЕНЮ
        elif (menu == '+'):
            f2 = 0
            func.dobav() # Вызов функции ДОБАВИТЬ
            
        elif (menu == '-'):                
            f3 = 0
            func.delet() # Вызов функции УДАЛИТЬ
        elif (menu == 'поиск'):
            func.poisk() # Вызов функции ПОИСК
        else:
            print(' Неверное значение \n')
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            func.While()# Вызов функции МЕНЮ



    def delet(delete):
        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
            lines = r.readlines()
            new = [line for line in lines if len(line)!= 1] 
        with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
            w.writelines(new)
    
        with open('Машинки1.txt', 'r') as s: #, encoding="utf-8"
            S = s.readlines()
            a = len(S) # Количество автомобилей
            for x in S:
                if x[0] == '' or x[0] == ' ':
                    a -= 1
        number = [int(x) for x in range(1, a + 1)]
        f3 = 0
        while f3 == 0:
            print('Ведите номер автомобиля, который хотите удалить. Чтобы вернуться введите - назад')
            delete = input()
            if delete == 'назад' or delete == 'Назад':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                f3 = 1
                func.While()# Вызов функции МЕНЮ
            elif (delete[0] == '1' or delete[0] == '2' or delete[0] == '3' or delete[0] == '4' or delete[0] == '5'\
                    or delete[0] == '6' or delete[0] == '7' or delete[0] == '8' or delete[0] == '9'):
                if int(delete) in range(1, a + 1):
                    delete = int(delete)
                    delete_str = []
                    split = ''
                    for x in S[delete - 1]:
                        if x == ',':
                            delete_str += [split]
                            split = ''
                        else:
                            split += x
                    delete_str += [split]
                    marka = delete_str[0]
                    gosnomer = delete_str[1]
                    print('Вы действительно хотите удалить автомобиль', marka, gosnomer, '?  да или нет')
                    d2= str(input())
                    if d2 == 'да' or d2 == 'Да':
                        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
                                for line in stroki:
                                    if count != delete:
                                        w.write(line)
                                    count += 1
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nАвтомобиль', marka, 'удалён')
                        del number[-1]
                        f3 = 1
                        func.While()# Вызов функции МЕНЮ
                    elif d2 == 'нет' or d2 == 'Нет':
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Отмена удаления \n')
                        f3 = 1
                        func.While()# Вызов функции МЕНЮ
                else:
                    print('\n Неверный номер ')
                    f3 = 0
                    func.While()# Вызов функции МЕНЮ
            else:
                print(' Неверное значение ')
                func.While()# Вызов функции МЕНЮ




    def dobav(number):
        f2 = 0
        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
            lines = r.readlines()
            new = [line for line in lines if len(line)!= 1] 
        with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
            w.writelines(new)
    
        with open('Машинки1.txt', 'r') as s: #, encoding="utf-8"
            S = s.readlines()
            a = len(S) # Количество автомобилей
            for x in S:
                if x[0] == '' or x[0] == ' ':
                    a -= 1
        number = [int(x) for x in range(1, a + 1)]
        while f2 == 0:
            print('Ведите марку машины. Чтобы вернуться напишите - назад')
            marka = input()
            if marka == 'назад' or marka == 'Назад':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                f2 = 1
                func.While()# Вызов функции МЕНЮ
            elif marka != 'назад' or marka != 'Назад':
                cif = '0123456789'
                buk = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                proverka = False
                f4 = 0
                print('Введите гос. номер')
                number = input()
                while proverka != True:
                    if number[0] in buk:
                        if number[1] in cif:
                            if number[2] in cif:
                                if number[3] in cif:
                                    if number[4] in buk:
                                        if number[5] in buk:
                                            if len(number) == 6:
                                                proverka = True
                                            else:
                                                proverka = False
                                                print('Вы ввели неправильно номер машины')
                                                number = str(input('Введите номер машины: '))
                                        else:
                                            proverka = False
                                            print('Вы ввели неправильно номер машины')
                                            number = str(input('Введите номер машины: '))
                                    else:
                                        proverka = False
                                        print('Вы ввели неправильно номер машины')
                                        number = str(input('Введите номер машины: '))
                                else:
                                    proverka = False
                                    print('Вы ввели неправильно номер машины')
                                    number = str(input('Введите номер машины: '))
                            else:
                                proverka = False
                                print('Вы ввели неправильно номер машины')
                                number = str(input('Введите номер машины: '))
                        else:
                            proverka = False
                            print('Вы ввели неправильно номер машины')
                            number = str(input('Введите номер машины: '))
                    else:
                        proverka = False
                        print('Вы ввели неправильно номер машины')
                        number = str(input('Введите номер машины: '))
                while f4 == 0:
                    print('Ввести дополнительные характеристики автомобиля?  "да" или "нет"')
                    d = str(input())
                    if d == 'да' or d == 'Да':
                        print('Если не хотите вводить характеристику введите -')
                        print('\nЦвет            ')
                        color = input()
                        print('\nГод выпуска     ')
                        god = input()
                        print('\nОбъём двигателя ')
                        objem = input()
                        print('\nМощность        ')
                        moshn = input()
                        #----------------------------
                        print('\nСостояние фар    ')
                        fari = input()
                        print('\nСостояние дверей ')
                        dveri = input()
                        #----------------------------
                        with open('Машинки1.txt', 'r') as r: #encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('Машинки1.txt', 'w') as w: #encoding="utf-8"
                                for line in stroki:
                                    if count != a+1:
                                        w.write(line)
                                    count += 1
                                w.write('\n'+marka+','+number+','+color+','+god+','+objem+','+moshn+','+fari+','+dveri)
                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                        print('Автомобиль добавлен!')
                        f2 = 1
                        f4 = 1
                        func.While()# Вызов функции МЕНЮ
                    elif d == 'нет' or d == 'Нет':
                        with open('Машинки1.txt', 'r') as r: #encoding="utf-8"
                            stroki = r.readlines()
                            count = 1
                            with open('Машинки1.txt', 'w') as w:  #encoding="utf-8"
                                for line in stroki:
                                    if count != a+1:
                                        w.write(line)
                                        count += 1
                                w.write('\n'+marka + ',' + number + ',-,-,-,-,-,-,')
                        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
                            lines = r.readlines()
                            new = [line for line in lines if len(line)!= 1]
                            with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
                                w.writelines(new)
                        print('Автомобиль добавлен!\n')
                        f2 = 1
                        f4 = 1
                        func.While()# Вызов функции МЕНЮ
                    else:
                        f4 = 0
                        func.While()# Вызов функции МЕНЮ


    



    def poisk(cou):
        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
            lines = r.readlines()
            new = [line for line in lines if len(line)!= 1] 
        with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
            w.writelines(new)
    
        with open('Машинки1.txt', 'r') as s: #, encoding="utf-8"
            S = s.readlines()
            a = len(S) # Количество автомобилей
            for x in S:
                if x[0] == '' or x[0] == ' ':
                    a -= 1
        number = [int(x) for x in range(1, a + 1)]

    
        cou = 0
        print('Введите характеристику для поиска')
        poisk = input()
        with open('Машинки1.txt', 'r') as s1: #encoding="utf-8"
            for i in range(0, a):
                stroka = []
                split = ''
                for x in S[i]:
                    #print(x)
                    if x == ',':
                        stroka += [split]
                        split = ''
                    else:
                        split += x
                stroka += [split]
                for i in range(0, len(stroka)):
                    if stroka[i] == poisk:
                        cou = cou + 1
                        mash = stroka
                        for x in mash:
                            print(x)
                        print('\n')
                #print(number[i], stroka[0], (25-len(stroka[0]))*' ', stroka[1])
        "print('Машин с характеристикой ' + str(poisk) +': ' + str(cou))"
        cou = 0
        func.While()  # Вызов функции МЕНЮ
       


    def While(menu):
        f1 = 0
        f2 = 0
        f3 = 0
        print('\nСписок машин:\n')

        with open('Машинки1.txt', 'r') as r: #, encoding="utf-8"
            lines = r.readlines()
            new = [line for line in lines if len(line)!= 1] 
        with open('Машинки1.txt', 'w') as w: #, encoding="utf-8"
            w.writelines(new)
    
        with open('Машинки1.txt', 'r') as s: #, encoding="utf-8"
            S = s.readlines()
            a = len(S) # Количество автомобилей
            for x in S:
                if x[0] == '' or x[0] == ' ':
                    a -= 1
        number = [int(x) for x in range(1, a + 1)]
        print('  Название авто               Гос.номер')

        with open('Машинки1.txt', 'r') as s1: #encoding="utf-8"
            for i in range(0, a):
                stroka = []
                split = ''
                for x in S[i]:
                    if x == ',':
                        stroka += [split]
                        split = ''
                    else:
                        split += x
                stroka += [split]
                print(number[i], stroka[0], (25-len(stroka[0]))*' ', stroka[1])
        
        print('\nМеню:\n'
        '1)Чтобы посмотреть характеристики введите номер порядка машины\n'
        '2)Чтобы добавить машину нажмите + \n'
        '3)Чтобы удалить машину нажмите -\n'
        '4)Чтобы начать поиск введите "поиск"\n')

        while f1 == 0:
            func.prosmotr() # Вызов функции ПРОСМОТР(ИЗМЕНИТЬ)

            


func = Func() # Вызов класса
func.While()  # Вызов функции МЕНЮ


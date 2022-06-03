#1. Создать переменную count со значением 0
count = 0
#2. Создать переменную range_count со значением 10

range_count = 10

#3. Создать переменную for_count со значением 0

for_count = 0

#4. Создать переменную run со значением True

run = True

#5. Создать цикл while, который будет работать пока run
#Тело цикла: выводить в консоль "Hello Cycle!!!"

while True:
    print("Hello Cycle!!!")
#6.Создать цикл while, который будет работать пока run
#Тело цикла: выводить в консоль ('step = ', count); переменной count прибавлять 1 с присвоением

while True:
    print('step =', count)
    count += 1
#7. Создать цикл while, который будет работать пока count < range_count
#Тело цикла: выводить в консоль ('step = ', count); переменной count прибавлять 1 с присвоением

while count < range_count:
    print('step =', count)
    count += 1
#8. Создать цикл while, который будет работать пока count < range_count
#Тело цикла: выводить в консоль ('step = ', count); переменной count прибавлять 1 с присвоением; если count равен 3, то выводить в консоль
#('step = ', count, 'if body')

while count < range_count:
    count += 1
    if count == 3:
        print('step = ', count, 'if body')
    else:
        print('step = ', count)
#9. Создать цикл while, который будет работать пока count < range_count
#Тело цикла: выводить в консоль ('step = ', count); переменной count прибавлять 1 с присвоением; если count равен range_count, то
#цикл остановится, в консоль вывести ('STOP', count)

while count < range_count:
    count += 1
    if count == range_count:
        print('STOP', count)
        break
    else:
        print('step =', count)

#10. Сделать цикл for с переменной item, кторый будет работать пока счетчик range досчитает от for_count до range_count.
#Вывести в консоль ('step = ', item)

for item in range(for_count, range_count):
    print('step =', item)

#11. Сделать цикл for с переменной item, кторый будет работать пока счетчик range досчитает от 0 до 30.
#Вывести в консоль ('step = ', item). Если item == 5, то вывести в консоль ('item =', item); item == 10,
# то вывести в консоль ('item =', item), item < 4, то вывести в консоль ('item <', item), item >= 27, то
# вывести в консоль ('item >=', item)

for item in range(0, 30):
    if item == 5:
        print('item =', item)
    elif item == 10:
        print('item =', item)
    elif item < 4:
        print('item <', item)
    elif item >= 27:
        print('item >=', item)
    else:
        print('step =', item)

#12.Сделать цикл for c переменной item который будет работать пока счётчик
#range досчитает от 0 до range_count +1
#Тело цикла:
#12.1 Вывести в консоль (‘Step =’, item)
#12.2 Сделать if с условием, если item равен 7
#- В теле if создать переменную inner_count равную 0
#- В теле if вывести в консоль (‘-- inner_count =’, inner_count)
#- В теле if сделать ещё одни цикл for с переменной inner_item
#который будет работать пока счётчик range досчитает от 0 до item.
#Тело внутреннего цикла For:
#-- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
#-- Сделать if если inner_item равен 5, то в inner_count присвоить
#inner_item.
#- За пределами тела предыдущего цикла вывести в консоль (‘--
#inner_count =’, inner_count)

for item in range(0, range_count + 1):
    if item == 7:
        inner_count = 0
        print('--inner_count', inner_count)
        for inner_item in range(0, item):
            print('--------Inner_step =', inner_item)
            if inner_item == 5:
                inner_count == inner_item
        print('--inner_count =', inner_count)
    print('step =', item)

# 13.Сделать цикл for c переменной item который будет работать пока счётчик
# range досчитает от 0 до 20
# Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
# 13.2 Сделать if с условием, если item больше 7 и item меньше 12
# - В теле if вывести (‘If_item =’, item)
# - В теле if поставить continue
# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)

for item in range(0, 20):
    print('Step =', item)
    if 7 < item < 12:
        print('if_item =', item)
        continue
    print('End_iteration =', item)

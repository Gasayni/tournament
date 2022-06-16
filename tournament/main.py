# TODO

# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре “Орлеан”:
# фамилии, имена и количество баллов, набранных в первом туре.
# Во второй тур проходят участники, которые набрали более K баллов в первом туре.

# Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
# прошедших во второй тур, с нумерацией.

# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
# Затем программа должна вывести фамилии, инициалы и количество баллов всех участников,
# прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы.
# Список должен быть отсортирован по убыванию набранных баллов.

# читаем файлы
file_in = open('first_tour.txt', 'r')
# записываем все данные файла в строку
s = file_in.read()
# закрываем файл для чтения
file_in.close()

list_finish = list()
# разделим построчно
sLinesList = s.split("\n")
# вытащим проходной балл со строки
passMark = int(sLinesList[0])

# вытаскиваем балл каждого участника
for i in range(1, len(sLinesList)):
    # кадую строку разделяем на переменные (через пробел)
    list_t = sLinesList[i].split(" ")
    # вытаскиваем балл каждого участника
    mark = int(list_t[2])
    if mark > passMark:
        # редактируем вывод по условию (нумеруем, вместо имени аббревиатура)
        list_finish.append(list_t[1][:1] + ". " + list_t[0] + " " + list_t[2] + "\n")


# Сортируем в обратном порядке по кол-ву баллов
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92
def sortReverseDef():
    for i in range(0, len(list_finish) - 1):
        for j in range(i + 1, len(list_finish)):
            t1 = int(list_finish[i].split(" ")[2])
            t2 = int(list_finish[j].split(" ")[2])
            if t2 > t1:
                a = list_finish[i]
                list_finish.insert(i, list_finish.pop(j))
                list_finish.insert(j, a)
                list_finish.pop(j + 1)


sortReverseDef()
# открываем файл записи
file_out = open('second_tour.txt', 'w')
# добавляем номер следующего тура (по условию)
file_out.write("2\n")
for i in range(0, len(list_finish)):
    file_out.write(str(i + 1) + ") " + list_finish[i])
# закрываем файл записи
file_out.close()

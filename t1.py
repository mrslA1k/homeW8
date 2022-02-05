print('Записать в файл строку, потом ее считать.')
f_name_in = input("Введите имя файла: ")
f_data_in = input("Введите строку для записи в файл: ")

f_name = f_name_in+'.txt'

with open(f_name, 'w') as f:
   f.write(f_data_in)
with open(f_name,'r') as file:
   pass
   print (file.read())

print("Bye")
input("жмякни Интер для выхода")
print("Сериализовать объект простого класса, загрузить его и запустить метод, ")
print("использующий атрибут объекта, при помощи pickle.")
import pickle
class Pick:
 def f(self):
  print(5)

with open('tFile','wb') as file:
 pickle.dump(Pick.f, file)
 file.close()

with open('tFile', 'rb') as file:
 print(pickle.load(file))
 file.close()

print("Bye")
input("жмякни Интер для выхода")
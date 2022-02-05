print("Сериализовать объект при помощи json и yaml и десереализовать в/из строки/файла")
import json
import yaml

data = {'age': 45,
      'name': 'Peter',
      'children':
      [
         {
            'age': 3,
            'name': 'Alice'
         }
      ],
      'married': True,
      'city': None
      }

# Сериализация json
with open('jfile', 'w') as file_o:
   json.dump(data, file_o)
   file_o.close()

# Десериализация json
with open('jfile', 'r') as file_i:
   print(json.load(file_i))
   file_i.close()

# Сериализация yaml
with open('yfile', 'w') as Yfile_o:
   yaml.safe_dump(data, Yfile_o)
   Yfile_o.close()

# Десериализация yaml
with open('yfile', 'r') as Yfile_i:
   print(yaml.safe_load(Yfile_i))
   Yfile_i.close()

print("Bye")
input("жмякни Интер для выхода")
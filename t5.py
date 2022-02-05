print('Создать таблицу Excel и конвертировать ее в csv при помощи Python')
import pandas

data = {'age': 45,
      'name': ['Peter'],
      'married': True,
      'city': None
      }

pandas.DataFrame(data).to_excel('./data_s.xlsx', sheet_name='Sheet', index=False)
pandas.read_excel('data_s.xlsx').to_csv('data_s.csv', encoding='utf-8', index=False)

print("Bye")
input("жмякни Интер для выхода")
print("Сериализовать объект выше при помощи библиотеки pydantic")
from pydantic import BaseModel
from typing import Union

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

class Class_pydantic(BaseModel):
 age: str
 name: str
 children: list
 married: bool
 city: Union[str,None]

print(Class_pydantic(**data))

print("Bye")
input("жмякни Интер для выхода")
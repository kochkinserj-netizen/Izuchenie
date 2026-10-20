# Полный гайд по аннотациям типов (Type Hints)
from typing import List, Dict, Tuple, Union, Optional, Literal, TypeAlias, Final, TypedDict, Callable, TypeVar

name:str = 'Sergei'
print(name)

name = [1,2,3,4]
print(name)

age: int = 30
print(age)

is_married: bool = True
print(is_married)

company: None = None
print(company)

def get_full_name(first_name: str, last_name: str) -> str:
    return f'{first_name} {last_name}'


# Базовый синтаксис

def greeting(greet: str, user_name: str = 'Anon') -> str:
    return f'{greet.title()} {user_name.upper()}!'

print(greeting('Hello','Sergei'))
print(greeting('Hi'))

# Аннотации коллекций

students: List[str] = ['Victor', 'Anatholy', 'Sergei', 'Anatholy']
# совремменный вариант
languages: list[str] = ['Python', 'Java', 'TypeScript', 'PHP']

user: Dict[str,str] = {
    'id': '13',
    'name': 'Sergei',
    'surname': 'Kochkin',
    'age': '30'
}

student: dict[str,Union[str,int]] = {
    'id': 13, # id or int
    'name': 'Sergei',
    'surname': 'Kochkin',
    'age': 30,

}

teacher: dict[str, str|int|bool] = {
    'id': 13,
    'name': 'Sergei',
    'surname': 'Kochkin',
    'age': 30,
    'is_married': True

}

russia: Tuple[str,str] = ('Russia', 'Moscow')

englend: tuple[str,str] = ('English', 'French')

def find_user(user_id: int) -> Optional[str]:
    # Возвращает str или None
    if user_id == 1:
        return "Alice"
    return None

# Эквивалент через Union
def find_user_alt(user_id: int) -> Union[str, None]:
    return "Alice"

# Any — любой тип (использовать осторожно!)
from typing import Any

def tricky_function(value: Any) -> Any:
    return value

# NoReturn — функция не возвращает
from typing import NoReturn

def raise_error(message: str) -> NoReturn:
    raise ValueError(message)


# Literal — фиксированные значения
GENDER = Literal["мужской", "женский", "non-conforming"]

def set_gender(gender: GENDER) -> None:
    print(f"Gender: {gender}")

set_gender("мужской")  # ✅ OK
set_gender("другой")   # ❌ Ошибка проверки типов


# TypeAlias — псевдоним типа
UserID: TypeAlias = int
UserName: TypeAlias = str

def get_user(user_id: UserID) -> UserName:
    return "Alice"


# Final — неизменяемое значение, переменная которую нельзя измеить в подклассе

MAX_SIZE: Final = 100
PI: Final[float] = 3.14159


# TypedDict — словарь с известными ключами
class User(TypedDict):
    name: str
    age: int
    email: str

user: User = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}


# Callable — функция как параметр
def apply_operation(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply_operation(add, 5, 3)  # 8

# Generics (обобщения)
T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

age: int = first_item([1, 2, 3])      # T = int
name: str = first_item(["a", "b"])   # T = str
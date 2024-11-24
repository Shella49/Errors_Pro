from classes.users import User, UsersManager
from classes.users import UserNotFindError
# создаем менаджера
manager = UsersManager()
# создаем пользователей
user1 = User("Alex", "e123@gmail.com", 22)
user2 = User("Veronika", "ssrt54@list.ru", 30)
user3 = User("Olga","oblako22@yandex.ru", -18)
user4 = User(1234, 3434343, 12)

manager.add_user(user4)
manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)
print(manager)
manager.add_user(user2)
# Ищем существующего пользователя
try:
    found_user = manager.find_user("Alex")
except UserNotFindError as e:
    print(e)  # Пользователь с именем Alex не найден
else:
    print(f"Найден пользователь: {found_user.username}, {found_user.email}, {found_user.age}")

# Ищем несуществующего пользователя
try:
    found_user = manager.find_user("Пётр")
except UserNotFindError as e:
    print(e)  # Пользователь с именем Пётр не найден
else:
    print(f"Найден пользователь: {found_user.username}, {found_user.email}, {found_user.age}")
manager.remove_user("Alex")
manager.remove_user("Sveta")
print(manager)



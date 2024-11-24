class UserNotFindError(Exception):
    def __init__(self, message="Пользователь не найден"):
        super().__init__(message)


class UserAlreadyExistError(Exception):
    def __init__(self, name):
        super().__init__(f"Пользователь с именем {name} уже существует.")

class UserAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Введен недопустимый возраст {age}")

class User:
    def __init__(self, username:str, email:str, age:int) -> None:
        self.username = username
        self.email = email
        self.age = age
   
    def __str__(self) -> str:
        return f'Пользователь: username= {self.username} email= {self.email} возраст= {self.age} '

class UsersManager:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, user: User):
        try:
            # Проверяем, есть ли пользователь с таким именем
            if user.username in self.users:
                raise UserAlreadyExistError(user.username)
        except UserAlreadyExistError as e:
            print(e)
            return False
        # Если исключения не было, добавляем пользователя
        try:
            #Проверяем входные данные пользователя
            if 110 < user.age or user.age < 0:
                raise UserAgeError(user.age)
        except UserAgeError as e:
            print(e)
            return False
        self.users[user.username] = {
            "username": user.username,
            "email": user.email,
            "age": user.age
        }
        print(f"Регистрация нового пользователя: {user.username}")
        return True

    def find_user(self, username: str) -> User:
        try:
            # Ищем пользователя по ключу
            user_info = self.users[username]
        except KeyError:
            # Если ключа нет, выбрасываем исключение
            raise UserNotFindError(f"Пользователь с именем {username} не найден")
        else:
            # Если ключ найден, возвращаем объект User
            return User(
                username=user_info["username"],
                email=user_info["email"],
                age=user_info["age"]
            )



    def remove_user(self, username: str):
        """Удаляет пользователя по имени."""
        if username in self.users:
            removed_user = self.users.pop(username)
            print(f"Пользователь {removed_user['username']} удалён.")
            return True
        else:
            print(f"Пользователь по имени {username} не найден.")
            return False

    def __repr__(self):
        """Возвращает список всех пользователей."""
        return f"UsersManager(users={self.users})"

  
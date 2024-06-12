# Принцип единственной ответственности (SRP, Single Responsibility Principle)
# Каждый класс должен иметь только одну причину для изменения.
# Это означает, что класс должен выполнять только одну задачу или иметь только одну область ответственности.
# Это упрощает тестирование и поддержку кода.

# 1. Код без использования данного принципа
# class UserManager():
#     def __init__(self, user):
#         self.user = user
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()

# 2. Используем принцип. Каждый класс отвечает за свое действие: User хранит данные,
# UserNameChanger и SaveUser изменяют и сохраняют данные из User
class User():
    def __init__(self, user_name):
        self.user_name = user_name
        print(f"Added User: {self.user_name}")


class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user.user_name = new_name
        print(f"Changed name to {self.user.user_name}")


class SaveUser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(self.user.user_name)
        file.close()


user = User("Иван")
user_changer = UserNameChanger(user)
user_changer.change_name("Петр")
print(user.user_name)
user_saver = SaveUser(user)
user_saver.save()
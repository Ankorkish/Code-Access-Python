class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
class UserSaver:
    def save_to_file(self, user):
        with open(f'{user.name}_profile.txt', 'w') as file:
            file.write(f'Name: {user.name}\nEmail: {user.email}')

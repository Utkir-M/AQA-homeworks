class User:
    first_name = "Имя"
    last_name = "Фамилия"

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def sayFirstName(self):
        print(self.first_name)

    def sayLastName(self):
        print(self.last_name)

    def sayFullName(self):
        print(self.first_name, self.last_name)

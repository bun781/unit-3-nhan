class HumanResources:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

        self.nationality = None
        self.email = None

    def set_email(self, email:str):
        self.email = email

    def get_email(self):
        if self.email is None:
            self.set_email(email = input('Enter the email'))
        return self.email

    def set_nationality(self, name:str):
        self.nationality = name

    def greet(self)->str:
        return f'Hello {self.name} from {self.occupation}'

class Person
    def __init__(self, id, last_name, first_name, middle_name, type):
        self.id = id
        self.last_name = last_name
        self.first_name = firstname
        self.type = type
        
    def __str__(self):
      retrun f'{self.last_name}, {self.first_name}, {self.middle_name}'

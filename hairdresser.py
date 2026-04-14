class Hairdresser:

    def __init__(self, name = "Anna", surname = "Nowak"):
        self.name = name
        self.surname = surname

    def describe_hairdresser(self):
        
        full_name = f"{self.name} {self.surname}"

        return full_name

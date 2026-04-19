class Client:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def to_dictionary(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
        }

    @classmethod
    def from_dictionary(cls, data):
        return cls(data["name"], data["surname"], data["phone_number"])

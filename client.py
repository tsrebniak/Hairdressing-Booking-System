from typing import Dict

class Client:

    def __init__(self, name: str, surname: str, phone_number: str):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def to_dictionary(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
        }

    @classmethod
    def from_dictionary(cls, data: Dict[str, str]) -> "Client":
        return cls(data["name"], data["surname"], data["phone_number"])

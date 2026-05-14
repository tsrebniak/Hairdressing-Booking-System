from typing import Dict

class Hairdresser:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def describe_hairdresser(self) -> str :  

        return f"{self.name} {self.surname}"

    def to_dictionary(self) -> Dict[str, str]:
        return {"name": self.name, "surname": self.surname}

    @classmethod
    def from_dictionary(cls, data: Dict[str, str]) -> "Hairdresser":
        return cls(data["name"], data["surname"])

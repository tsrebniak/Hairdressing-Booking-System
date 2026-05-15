from typing import Dict


class Client:
    """Represents a client of the hair salon.

    Attributes:
        name: Client's first name.
        surname: Client's last name.
        phone_number: Client's phone number.
    """

    def __init__(self, name: str, surname: str, phone_number: str):
        """Initializes a client with the given data.

        Args:
            name: Client's first name.
            surname: Client's last name.
            phone_number: Client's phone number.
        """

        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def to_dictionary(self) -> Dict[str, str]:
        """Converts the client object to a dictionary.

        Returns:
            A dictionary with client data (name, surname, phone_number).
        """

        return {
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
        }

    @classmethod
    def from_dictionary(cls, data: Dict[str, str]) -> "Client":
        """Creates a Client instance from a dictionary.

        Args:
            data: A dictionary containing the keys name, surname, phone_number.

        Returns:
            A new Client instance.
        """
        
        return cls(data["name"], data["surname"], data["phone_number"])

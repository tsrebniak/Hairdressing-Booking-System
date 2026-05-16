from typing import Dict


class Hairdresser:
    """Represents a hairdresser employed at the salon.

    Attributes:
        name: Hairdresser's first name.
        surname: Hairdresser's last name.
    """

    def __init__(self, name: str, surname: str):
        """Initializes a hairdresser with the given data.

        Args:
            name: Hairdresser's first name.
            surname: Hairdresser's last name.
        """

        self.name = name
        self.surname = surname

    def describe_hairdresser(self) -> str:
        """Returns the hairdresser's full name.

        Returns:
            A string in the format 'First name Last name'.
        """

        return f"{self.name} {self.surname}"

    def to_dictionary(self) -> Dict[str, str]:
        """Converts the hairdresser object to a dictionary.

        Returns:
            A dictionary with hairdresser data (name, surname).
        """

        return {"name": self.name, "surname": self.surname}

    @classmethod
    def from_dictionary(cls, data: Dict[str, str]) -> "Hairdresser":
        """Creates a Hairdresser instance from a dictionary.

        Args:
            data: A dictionary containing the keys name, surname.

        Returns:
            A new Hairdresser instance.
        """

        return cls(data["name"], data["surname"])

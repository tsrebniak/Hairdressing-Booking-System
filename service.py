from typing import Dict

class Service:

    def __init__(self, name: str, duration_in_minutes: int, price: int) -> None:
        self.name = name
        self.duration_in_minutes = duration_in_minutes
        self.price = price

    def to_dictionary(self) -> Dict[str, str]:
        return {
            "service_name": self.name,
            "service_duration_time_in_minutes": self.duration_in_minutes,
            "service_price": self.price,
        }

    @classmethod
    def from_dictionary(cls, data: Dict[str, str]) -> "Service":
        return cls(
            data["service_name"],
            data["service_duration_time_in_minutes"],
            data["service_price"],
        )

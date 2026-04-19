class Service:

    def __init__(self, name, duration_in_minutes, price):
        self.name = name
        self.duration_in_minutes = duration_in_minutes
        self.price = price

    def to_dictionary(self):
        return {
            "service_name": self.name,
            "service_duration_time_in_minutes": self.duration_in_minutes,
            "service_price": self.price,
        }

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["service_name"],
            data["service_duration_time_in_minutes"],
            data["service_price"],
        )

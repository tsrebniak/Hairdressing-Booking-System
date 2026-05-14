from typing import Dict
from hairdresser import Hairdresser
from client import Client
from service import Service


class Reservation:

    def __init__(self, client: "Client", hairdresser: "Hairdresser", service: "Service", date_time: str, status="Umówiono"):
        self.client = client
        self.hairdresser = hairdresser
        self.service = service
        self.date_time = date_time
        self.status = status

    def describe_reservation(self) -> str:

        about_reservation = f"\n{self.client.name} {self.client.surname}\t{self.client.phone_number}\n{self.date_time}\t{self.status}\n"

        return about_reservation

    def cancel_reservation(self) -> None:
        self.status = "Anulowano"

    def complete_reservation(self) -> None:
        self.status = "Ukończono"

    def reschedule_reservation(self, new_date_time: str) -> None:
        self.date_time = new_date_time

    def to_dictionary(self) -> Dict[str, object]:
        return {
            "client": self.client.to_dictionary(),
            "hairdresser": self.hairdresser.to_dictionary(),
            "service": self.service.to_dictionary(),
            "date_of_service": self.date_time,
            "status_of_service": self.status,
        }

    @classmethod
    def from_dictionary(cls, data: Dict[str, object]) -> "Reservation":
        client = Client.from_dictionary(data["client"])
        hairdresser = Hairdresser.from_dictionary(data["hairdresser"])
        service = Service.from_dictionary(data["service"])
        return cls(
            client,
            hairdresser,
            service,
            data["date_of_service"],
            data["status_of_service"],
        )

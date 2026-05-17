from typing import Dict
from hairdresser import Hairdresser
from client import Client
from service import Service


class Reservation:
    """Represents a booking for a visit at the hair salon.

    Attributes:
        client: The client assigned to the reservation.
        hairdresser: The hairdresser handling the appointment.
        service: The service ordered by the client.
        date_time: Date and time of the appointment in 'YYYY-MM-DD HH:MM' format.
        status: Current status of the reservation (default: 'Umówiono').
    """

    def __init__(
        self,
        client: "Client",
        hairdresser: "Hairdresser",
        service: "Service",
        date_time: str,
        status="Umówiono",
    ):
        """Initializes a reservation with the given data.

        Args:
            client: The client making the reservation.
            hairdresser: The hairdresser assigned to the appointment.
            service: The service ordered by the client.
            date_time: Date and time in 'YYYY-MM-DD HH:MM' format.
            status: Reservation status. Defaults to 'Umówiono'.
        """

        self.client = client
        self.hairdresser = hairdresser
        self.service = service
        self.date_time = date_time
        self.status = status

    def describe_reservation(self) -> str:
        """Returns a text description of the reservation.

        Returns:
            A formatted string with the client's data, date, and status.
        """

        about_reservation = f"\n{self.client.name} {self.client.surname}\t{self.client.phone_number}\n{self.date_time}\t{self.status}\n"

        return about_reservation

    def cancel_reservation(self) -> None:
        """Cancels the reservation by setting the status to 'Anulowano'."""

        self.status = "Anulowano"

    def complete_reservation(self) -> None:
        """Marks the reservation as completed by setting the status to 'Ukończono'."""

        self.status = "Ukończono"

    def reschedule_reservation(self, new_date_time: str) -> None:
        """Reschedules the reservation to a new date and time.

        Args:
            new_date_time: New date and time in 'YYYY-MM-DD HH:MM' format.
        """

        self.date_time = new_date_time

    def to_dictionary(self) -> Dict[str, object]:
        """Converts the reservation object to a dictionary.

        Returns:
            A dictionary containing all reservation data (client,
            hairdresser, service, date, status).
        """

        return {
            "client": self.client.to_dictionary(),
            "hairdresser": self.hairdresser.to_dictionary(),
            "service": self.service.to_dictionary(),
            "date_of_service": self.date_time,
            "status_of_service": self.status,
        }

    @classmethod
    def from_dictionary(cls, data: Dict[str, object]) -> "Reservation":
        """Creates a Reservation instance from a dictionary.

        Args:
            data: A dictionary with the keys client, hairdresser, service,
                  date_of_service, status_of_service.

        Returns:
            A new Reservation instance.
        """

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

from hairdresser import Hairdresser
from client import Client
from service import Service
from schedule import Schedule

class Reservation: 

    def __init__(self, client, hairdresser, service, date_time, status="Umówiono"):
        self.client = client
        self.hairdresser = hairdresser
        self.service = service
        self.date_time = date_time
        self.status = status

    def describe_reservation(self):
        
        about_reservation = (f"\n{self.client.name} {self.client.surname}\t{self.client.phone_number}\n{self.date_time}\t{self.status}\n")

        return about_reservation
    
    def cancel_reservation(self):
        self.status = "Anulowano"

    def complete_reservation(self):
        self.status = "Ukończono"

    def reschedule_reservation(self, new_date_time):
        self.date_time = new_date_time

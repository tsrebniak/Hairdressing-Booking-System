class Schedule:

    def __init__(self):
        self.reservations = []

    def add_to_schedule(self, reservation):
        self.reservations.append(reservation)

    def show_schedule(self):
        for reservation in self.reservations:
            print(
                f"Fryzjerka: {reservation.hairdresser.name} {reservation.hairdresser.surname}\nKlient: {reservation.client.name} {reservation.client.surname}\nUsługa: {reservation.service.name}\nKoszt usługi: {reservation.service.price}\nCzas trwania usługi: {reservation.service.duration_in_minutes}\nData i godzina usługi: {reservation.date_time}\nStatus usługi: {reservation.status}\n"
            )

    def is_time_slot_taken(self, date_time):
        return any(reservation.date_time == date_time for reservation in self.reservations) ## tzw. generator expression 

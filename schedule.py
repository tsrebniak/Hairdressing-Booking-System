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

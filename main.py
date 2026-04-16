from pathlib import Path
from client import Client
from service import Service
from reservation import Reservation
from hairdresser import Hairdresser
from schedule import Schedule

path = Path("clients.txt")

schedule = Schedule()
default_hairdresser = Hairdresser()

toContinue = True
while toContinue == True:

    print("\nWitaj w systemie rezerwacji fryzjerskich! Wybierz opcję: ")
    print("1) Stwórz rezerwację")
    print("2) Zmień status wybranej rezerwacji")
    print("3) Wyświetl wszystkie rezerwacje")
    print("4) Usuń wybraną rezerwację")
    print("5) Wczytaj rezerwacje z pliku")

    user_choice = int(input("Twój wybór: "))

    if user_choice == 1:

        client_name = input("Podaj imię klienta: ")
        client_surname = input("Podaj nazwisko klienta: ")
        client_phone_number = input("Podaj nr telefonu klienta: ")

        new_client = Client(client_name, client_surname, client_phone_number)

        service_name = input("Podaj nazwę usługi: ")
        service_duration_in_minutes = input(
            "Podaj długość trwania powyższej usługi w minutach: "
        )
        service_price = input("Podaj cenę powyższej usługi: ")

        new_service = Service(service_name, service_duration_in_minutes, service_price)

        reservation_date_time = input(
            "Podaj datę w formacie RRRR-MM-DD HH:MM dla obecnej rezerwacji: "
        )

        new_reservation = Reservation(
            new_client, default_hairdresser, new_service, reservation_date_time
        )

        schedule.add_to_schedule(new_reservation)

        if len(schedule.reservations) == 1:
            content_to_save_in_file = new_reservation.describe_reservation()
            path.write_text(content_to_save_in_file)
        
        else:
            content_to_save_in_file += new_reservation.describe_reservation()
            path.write_text(content_to_save_in_file)

        print("\nDodano rezerwację!")

    elif user_choice == 2:

        client_surname_to_update = input(
            "Podaj nazwisko klienta, którego rezerwację chcesz zaktualizować: "
        )
        client_service_name_to_update = input(
            "Podaj nazwę usługi przypisaną do powyższego klienta, której status chcesz zaktualizować: "
        )

        for reservation in schedule.reservations:
            if (
                reservation.client.surname == client_surname_to_update
                and reservation.service.name == client_service_name_to_update
            ):

                client_status_to_update = input(
                    "Rezerwacja odnaleziona. Podaj jej nowy, zaktualizowany status (Anulowano lub Ukończono): "
                )

                if client_status_to_update.lower() == "anulowano":
                    reservation.cancel_reservation()
                    print("Rezerwację anulowano!")

                if client_status_to_update.lower() == "ukończono":
                    reservation.complete_reservation()
                    print("Rezerwację ukończono!")

    elif user_choice == 3:

        for reservation in schedule.reservations:
            print(reservation.describe_reservation())

    elif user_choice == 4:

        client_surname_to_delete = input(
            "Podaj nazwisko klienta, którego rezerwację chcesz usunąć: "
        )
        client_service_to_delete = input(
            "Podaj usługę powyższego klienta, którego rezerwację chcesz usunąć: "
        )

        for reservation in schedule.reservations:
            if (
                reservation.client.surname == client_surname_to_delete
                and reservation.service.name == client_service_to_delete
            ):
                schedule.reservations.remove(reservation)
                print("\nPomyślnie usunięte rezerwację")
            else:
                print("Nieodnaleziono takiej rezerwacji")

    elif user_choice == 5:

        content_to_read_from_file = path.read_text()
        lines = content_to_read_from_file.splitlines()

        for line in lines:
            print(line)

    else:
        toContinue = False

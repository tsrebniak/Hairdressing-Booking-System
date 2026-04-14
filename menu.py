from hairdresser import Hairdresser
from client import Client
from service import Service
from schedule import Schedule
from reservation import Reservation

print("Witaj w systemie rezerwacji fryzjerskich! Wybierz opcję: ")
print("1) Stwórz rezerwację")
print("2) Zmień status wybranej rezerwacji")
print("3) Wyświetl wszystkie rezerwacje")
print("4) Usuń wybraną rezerwację")

reservations = []

toContinue = True
while toContinue == True:
    
    user_choice = int(input("Twój wybór: "))

    if user_choice == 1:

        client_name = input("Podaj imię klienta: ")
        client_surname = input("Podaj nazwisko klienta: ")
        client_phone = input("Podaj numer telefonu klienta: ")
        date_time_of_service = input("Podaj datę wykonania usługi w formacie RRRR-MM-DD HH:MM: ")
        hairdresser_name = input("Podaj imię fryzjerki: ")
        hairdresser_surname = input("Podaj nazwisko fryzjerki: ")
        service_name = input("Podaj nazwę usługi: ")
        service_duration = input("Podaj czas trwania usługi w minutach: ")
        service_price = input("Podaj cenę usługi w złotówkach: ")

        reservation = {
            "Imię klienta": client_name,
            "Nazwisko klienta": client_surname,
            "Numer tel. klienta": client_phone,
            "Data i godzina wykonania usługi": date_time_of_service,
            "Imię fryzjerki wykonującej zabieg": hairdresser_name,
            "Nazwisko fryzjerki wykonującej zabieg": hairdresser_surname,
            "Nazwa usługi": service_name,
            "Czas trwania usługi": service_duration,
            "Koszt usługi": service_price,
            "Status usługi": "Zarezerwowano"
        }

        reservations.append(reservation)

        print("Dodano rezerwację!")

    elif user_choice == 2:

        client_surname = input("Podaj nazwisko klienta, którego status rezerwacji chcesz zmienić: ")
        service_updated_status = input("Podaj zaktualizowany status usługi: ")

        for reservation in reservations:
            if reservation["Nazwisko klienta"] == client_surname:
                reservation["Status usługi"] = service_updated_status
                print(f"Zaktualizowano status usługi pana/pani {client_surname}")
    

    elif user_choice == 3:
        
        for reservation in reservations:
            for key, value in reservation.items():
                print(f"{key}: {value}")

    elif user_choice == 4:
        client_surname = input("Podaj nazwisko klienta, którego rezerwację chcesz usunąć: ")
        service_to_delete = input("Podaj usługę przypisaną do nazwiska powyższego klienta, by usunąc daną rezerwacje: ")

        for reservation in reservations:
            if reservation["Nazwisko klienta"] == client_surname and reservation["Nazwa usługi"] == service_to_delete:
                reservations.remove(reservation)
                print("Rezerwację usunięto")
            else:
                print("Błąd podczas usuwania rezerwacji")


    else:
        exit()


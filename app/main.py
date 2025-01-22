import mysql.connector
from db import (
    add_reservation, 
    delete_multiple_reservations_by_ids, 
    update_reservation_seat, 
    add_additional_seat_to_reservation, 
    view_all_reservations,
    view_reservations_by_customer
)

def main_menu():
    while True:
        print("\n--- Meniu Principal ---")
        print("1. Adaugă o rezervare")
        print("2. Șterge o rezervare")
        print("3. Actualizează un loc rezervat")
        print("4. Adaugă un loc suplimentar pentru o rezervare")
        print("5. Vizualizează toate rezervările")
        print("6. Vizualizează rezervările unui client")
        print("7. Ieși din aplicație")

        choice = input("Alege o opțiune (1-7): ")

        if choice == '1':
            # Adaugă rezervare
            customer_name = input("Nume client: ")
            movie_name = input("Film: ")
            seats = input("Locuri (separate prin virgulă, ex: A10,A11,A12): ").split(',')
            reservation_name = input("Data rezervării (format: YYYY-MM-DD HH:MM:SS): ")
            add_reservation(customer_name, movie_name, seats, reservation_name)

        elif choice == '2':
            # Șterge rezervare
            reservation_ids = input("Introdu ID-urile rezervărilor de șters (separate prin virgulă): ").split(',')
            reservation_ids = list(map(int, reservation_ids))  # Convertim la întregi
            delete_multiple_reservations_by_ids(reservation_ids)

        elif choice == '3':
            # Actualizează locul rezervat
            reservation_id = int(input("Introdu ID-ul rezervării: "))
            new_seat = input("Introdu noul loc: ")
            update_reservation_seat(reservation_id, new_seat)

        elif choice == '4':
            # Adaugă un loc suplimentar pentru rezervare
            customer_name = input("Nume client: ")
            movie_name = input("Film: ")
            reservation_name = input("Data rezervării (format: YYYY-MM-DD HH:MM:SS): ")
            new_seat = input("Introdu locul suplimentar: ")
            add_additional_seat_to_reservation(customer_name, movie_name, reservation_name, new_seat)

        elif choice == '5':
            # Vizualizează toate rezervările
            view_all_reservations()

        elif choice == '6':
            # Vizualizează rezervările unui client
            customer_name = input("Introdu numele clientului: ")
            view_reservations_by_customer(customer_name)

        elif choice == '7':
            # Ieși din aplicație
            print("Ieșire din aplicație...")
            break  # Oprește programul

        else:
            print("Opțiune invalidă! Te rog să alegi din nou.")

if __name__ == "__main__":
    main_menu()

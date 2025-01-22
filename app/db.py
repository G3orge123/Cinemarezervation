import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ienovanumber2", 
            database="db_cinema"
        )
        if connection.is_connected():
            print("Conexiunea a reusit cu succes")
        return connection
    except mysql.connector.Error as e: 
        print(f"Error: {e}")
        return None

def add_reservation(customer_name, movie_name, seat_numbers, reservation_name):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        for seat_number in seat_numbers:
            query = """
            INSERT INTO reservations(customer_name, movie_name, seat_number, reservation_name) 
            VALUES (%s, %s, %s, %s)
            """
            values = (customer_name, movie_name, seat_number, reservation_name)
            cursor.execute(query, values)
        connection.commit()  
        print(f"Rezervare adăugată cu succes pentru {len(seat_numbers)} locuri!")
        cursor.close()
        connection.close()

def delete_multiple_reservations_by_ids(ids):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM reservations WHERE id IN (%s)"
        cursor.execute(query, (', '.join(map(str, ids)),))  
        connection.commit()
        print(f"Rezervările cu ID-urile {ids} au fost șterse cu succes!")
        cursor.close()
        connection.close()

def update_reservation_seat(reservation_id, new_seat_number):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE reservations SET seat_number = %s WHERE id = %s"
        cursor.execute(query, (new_seat_number, reservation_id))
        connection.commit()
        print(f"Locul rezervat cu ID {reservation_id} a fost actualizat la {new_seat_number} cu succes!")
        cursor.close()
        connection.close()

def add_additional_seat_to_reservation(customer_name, movie_name, reservation_name, new_seat_number):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO reservations (customer_name, movie_name, seat_number, reservation_date) VALUES (%s, %s, %s, %s)"
        values = (customer_name, movie_name, new_seat_number, reservation_name)
        cursor.execute(query, values)
        connection.commit()
        print(f"Un loc suplimentar {new_seat_number} a fost adăugat pentru rezervarea lui {customer_name}!")
        cursor.close()
        connection.close()

def view_all_reservations():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reservations")
        result = cursor.fetchall()
        if result:
            print("Toate rezervările:")
            for row in result:
                print(f"ID: {row[0]}, Nume Client: {row[1]}, Film: {row[2]}, Loc: {row[3]}, Data Rezervare: {row[4]}")
        else:
            print("Nu există rezervări.")
        cursor.close()
        connection.close()

def view_reservations_by_customer(customer_name):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM reservations WHERE customer_name = %s"
        cursor.execute(query, (customer_name,))
        result = cursor.fetchall()
        if result:
            print(f"Rezervările pentru {customer_name}:")
            for row in result:
                print(f"ID: {row[0]}, Film: {row[2]}, Loc: {row[3]}, Data Rezervare: {row[4]}")
        else:
            print(f"Nu există rezervări pentru {customer_name}.")
        cursor.close()
        connection.close()

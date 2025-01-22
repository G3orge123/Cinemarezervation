from db import connect_to_db  

# Testare conexiunea la baza de date
connection = connect_to_db()
if connection:
    connection.close()

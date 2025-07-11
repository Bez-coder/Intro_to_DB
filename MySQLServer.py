import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      # <- Replace with your MySQL username
            password=''       # <- Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database using IF NOT EXISTS
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

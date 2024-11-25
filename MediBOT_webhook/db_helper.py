# Author: Dhaval Patel. Codebasics YouTube Channel

import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="onlineconsultation"
)
# Function to get the next available order_id
def get_next_order_id():
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1

# Function to call the MySQL stored procedure and insert an order item
def Insert_Appointment(name,email,phone,Address,appointment_time,appointment_type,health_issue,duration):
    try:
        cursor = cnx.cursor()

        # Calling the stored procedure
        cursor.callproc('InsertAppointment', (name,email,phone,Address,appointment_time,appointment_type,health_issue,duration,0))

        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Appointment scheduled successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1

# Function to call the MySQL stored procedure and insert an order item
def insert_Appointment(name,email,phone,address,appointment_Datetime,appointment_type,health_issues,duration):
    try:
            cursor = cnx.cursor()

            # Calling the stored procedure
            cursor.callproc('InsertAppointment', (name,email,phone,address,appointment_Datetime,appointment_type,health_issues,duration,0))

            # Committing the changes
            cnx.commit()

            # Closing the cursor
            cursor.close()

            print("Order item inserted successfully!")

            return 1
   
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1



if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())

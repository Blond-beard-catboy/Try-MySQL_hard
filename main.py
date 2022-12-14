import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    try:
       #with connection.cursor() as cursor:
            #create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT, name varchar(32), password varchar(32), email varchar(32), PRIMARY KEY(id));"
            #cursor.execute(create_table_query)
            #print("Table created successfully")

        #insert data

        #with connection.cursor() as cursor:
            #insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
            #cursor.execute(insert_query)
            #connection.commit()

        #with connection.cursor() as cursor:
        #    insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Igor', '123456', 'iigor@gmail.com');"
        #    cursor.execute(insert_query)
        #    connection.commit()

        #with connection.cursor() as cursor:
        #    insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '223344', 'olegan@gmail.com');"
        #    cursor.execute(insert_query)
        #    connection.commit()

        #update_data

        #with connection.cursor() as cursor:
        #    update_query = "UPDATE `users` SET password = 'xxx123' WHERE id = 3;"
        #    cursor.execute(update_query)
        #    connection.commit()

        #delete data

        #with connection.cursor() as cursor:
        #    delete_query = "DELETE FROM `users` WHERE id = 2;"
        #    cursor.execute(delete_query)
        #    connection.commit()

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print('#' * 20)
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

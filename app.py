import mysql.connector

host_name = "localhost"
user_name = "username"
password = "password"
db_name = "contactbook"

my_db_con = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            database=db_name
        )

cursor = my_db_con.cursor()
query = "CREATE DATABASE contactbook"
cursor.execute(query)



# create a table
my_cursor=my_db_con.cursor()
my_cursor.execute("create table contacts(id INT AUTO_INCREMENT,name TEXT NOT NULL, surname TEXT, phone TEXT,mail TEXT, PRIMARY KEY (id))")
my_db_con .close()

#insert record
my_cursor=my_db_con.cursor()
try:
    my_cursor.execute("insert into contacts  values(1, 'name', 'surname', '064534342','some.main@gmail.com')")
    my_db_con.commit()
    print('Record inserted successfully...')
except Exception as er:
    print(str(er))
    my_db_con.rollback()
my_db_con.close()

#display all records
my_cursor=my_db_con.cursor()
try:
    my_cursor.execute("select * from contacts")
    result = my_cursor.fetchall()
    for i in result:
        id = i[0]
        name = i[1]
        surname = i[2]
        phone = i[3]
        mail = i[4]
        print(id, name, surname, phone, mail)
except:
    print('Error:Unable to fetch data.')
my_db_con.close()


#update record
my_cursor=my_db_con.cursor()
try:
    my_cursor.execute("UPDATE contacts SET mail ='some_new.main@gmail.com'")
    my_db_con.commit()
    print('Record updated successfully...')
except Exception as er:
    print(str(er))
    my_db_con.rollback()
my_db_con.close()

#delete record
my_cursor=my_db_con.cursor()
try:
    my_cursor.execute("DELETE FROM contacts WHERE name ='name'")
    my_db_con.commit()
    print('Record removed successfully...')
except Exception as er:
    print(str(er))
    my_db_con.rollback()
my_db_con.close()

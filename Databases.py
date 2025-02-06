import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="20Eve,lyne#76",
  database="mysql",
  port=3306
)
    

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
print("\t\t\tLIST OF DATABASES:")

for table in mycursor:
  print(table)

print("")
#Selection of the databases
mycursor.execute("USE login")

print("Tables in the login Database")
#Display of the tables that are in the selected database
mycursor.execute("SHOW TABLES")
for table in mycursor:
  print(table)

#Operation on tables in the database
# mycursor.execute("DESCRIBE evelyne")
# for column in mycursor:
#   print(column)

#Insertion of data into the table im many columns
sql = "INSERT INTO evelyne (Name, Age, Course) VALUES (%s, %s, %s)"
values = [("Evelyne Njambi", 19, "Software Engineering"),
("Rosenary Muthoni", 17, "Orthopeadics Medicine"),
("Peter Ng'ang'a", 50, "Employed"),
("ElizaBeth Murugi", 48, "Employeed"),
("Purity Muthoni", 23, "Cosmetology and Beauty")
]
mycursor.executemany(sql, values)
mycursor.execute("SELECT NAME FROM evelyne")
myresult = mycursor.fetchall()
for row in myresult:
  print(row)
mydb.commit()


 

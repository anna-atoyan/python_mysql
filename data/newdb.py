import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="customers"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = [("John", "Highway 21"),
      ("Sam", "North Av. 23"),
      ("Emma","North Ave 12"),
      ("William","Asol 54/1"),
      ("John", "Disney 87"),
      (" Walt", "Lily Island 44"),
      ("Micky", "Hollywood 14"),
      ("Daisy", "Hollywood 76"),
      ("Gooffy", "Hollywood 65"),
      ("Donald", "hollywood 43")
       ]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
import mysql.connector
from datetime import date
mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    passwd = "password",
    database = "cicd"
)

mycursor = mydb.cursor();

sql = "INSERT INTO USER_DETAILS (firstname, lastname,email,username,password,lastupdated) VALUES (%s,%s,%s,%s,%s,%s)"
val =[
('firstname1','lastname1','email1','admin1','admin1',date.today()),
 'firstname2','lastname2','email2','admin2','admin2',date.today()),
 'firstname3','lastname3','email3','admin3','admin3',date.today()),
 'firstname4','lastname4','email4','admin4','admin4',date.today()),
 'firstname5','lastname5','email5','admin5','admin5',date.today()),
]

mycursor.executemany(sql,val)
mydb.commit();
print (mycursor.rowcount, "record inserted");

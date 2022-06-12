import mysql.connector #import python module

#create DB using connect method
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("use rajeev")   # use database
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Rajeev", "Indra Institute 06-11")

mycursor.execute(sql, val)
mydb.commit()
#  pip install mysql-connector-python

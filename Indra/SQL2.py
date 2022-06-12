import mysql.connector

mydb = mysql.connector.connect(
   host= "localhost",
   user="root",
   password=""
)


mycursor = mydb.cursor()

mycursor.execute("use tsen")
Choice = int(input("Select your choice:"))

if Choice == 1:
	user_name = input("Enter your user name:")
	user_password = input("Enter your password:")
	sql = "INSERT INTO tsen1(name,password)  VALUES (%s,%s)"
	val = (user_name,user_password)
	mycursor.execute(sql,val)

	mydb.commit()
elif Choice == 2:
	user_name = input("What do you want to delete:")
	sql = "DELETE FROM tsen1 WHERE name = '%s' "
	val = (user_name)
	mycursor.execute(sql,val)
	mydb.commit()
elif Choice == 3:
	mycursor.execute("Drop table tsen1")
elif Choice == 4:
	sql = "CREATE TABLE tsen1(name VARCHAR(255), password VARCHAR(255))"	
	mycursor.execute(sql)
	mydb.commit()

	
import mysql.connector

inp1= int(input("Enter Number To Choose The Option:- "))

for j in a:

   if inp1==1:

      a = mysql.connector.connect(host = "localhost", user = "root",passwd = "google")  

      

      fin1 = a.cursor()  

      

      try:  

         dbs = fin1.execute("show databases")  

      except:  

         a.rollback()  

      for x in fin1:  

         print(x)

   if inp1==2:

      b = mysql.connector.connect(host = "localhost", user = "root",passwd = "google")  

      

      cur = b.cursor()  

      

      try:  

         cur.execute("create database PythonDB2")  

         dbs = cur.execute("show databases")  

            

      except:  

         b.rollback()  

      

      for x in cur:  

            print(x)

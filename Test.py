import mysql.connector
from time import sleep
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="697481",
  database = "datacamp"  
)

print(mydb)
query =" CREATE TABLE testbool(is_checked BIT); "
cursor = mydb.cursor()




for i in range(15):
    pathToFile = './Processing/{}.txt'.format(i+1)
    f = open(pathToFile, 'w')
    sleep(1)
    source = './Processing/'
    destination1 = './queue/'
    destination2 = './Processed/'
    if((i+1)%5 == 0):
      

        files = os.listdir(source)

        for f in files:
            os.rename(source + f, destination1 + f)
            
            
    queueFiles = os.listdir(destination1)
    if(len(queueFiles)!= 0 ):
        sleep(1)
        for qf in queueFiles:
            cursor.execute("INSERT INTO testbool ( is_checked) VALUES (1);")
            
            os.rename(destination1 + qf, destination2 + qf)
            

try:
    cursor.execute("SELECT * from testbool")
    result = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    print(field_names)

    for value in result:
        print(value)

    mydb.commit()
except:
    mydb.rollback()
            
# for i in range(10):
#     if((i+1)%5 == 0):
#         source = './queue/'
        

#         files = os.listdir(source)
#         cursor.execute("INSERT INTO testbool ( is_checked) VALUES (1);")
#         for f in files:
#             os.rename(source + f, destination + f)
            
        
#     else:
#         cursor.execute("INSERT INTO testbool ( is_checked) VALUES (0);")
    
#     myresult = cursor.fetchall()
# for row in myresult:
#         print(myresult[row])
#         print("\n")

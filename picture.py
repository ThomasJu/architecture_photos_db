import mysql.connector
import category_class as cc

def sql_operation():
  # Information needed to make connection to the database
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="0830ju2000", 
    database='mydatabase'
  )
  
  mycursor = mydb.cursor()
  
  mycursor.execute("SHOW DATABASES")
  create_table_commmand = '''
  CREATE TABLE 'picture' (
      id INT AUTO_INCREMENT PRIMARY KEY,
      filepath VARCHAR(255) NOT NULL, 
      category1 ENUM('func', 'theory', 'expression') NOT NULL, 
      category2 ENUM()
  )
  '''
  
if __name__ == "__main__":
  pass
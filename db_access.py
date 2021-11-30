import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Akashdeep@2000",
  database="dreamzsoftware"
)

mycursor = mydb.cursor()

#Class created for Insertion of data in table student

class Insert_data:
    def __init__(self):
        pass

#function to insert data
            
    def set_data(self):
        try:
            s_no = int(input("Enter the Student No. : "))
            s_name = input("Enter the Student Name : ")
            s_dob = input("Enter the Date Of Birth (yyyy-mm-dd) : ")
            s_dob = datetime.strptime(s_dob, "%Y-%m-%d")
            s_dob = s_dob.strftime("%Y-%m-%d")
            s_doj = input("Enter the Date Of Joining (yyyy-mm-dd) : ")
            s_doj = datetime.strptime(s_doj, "%Y-%m-%d")
            s_doj = s_doj.strftime("%Y-%m-%d")
        except:
            print("Format is wrong...")

        else:
            sql = "INSERT INTO student (STUDENT_NO, STUDENT_NAME, STUDENT_DOB, STUDENT_DOJ) VALUES (%s, %s, %s, %s)"
            val = (s_no, s_name, s_dob, s_doj)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")


#Class created for Read Data in table student

class Read_data:
    def __init__(self):
        pass

#function to read data

    def get_data(self):

        mycursor.execute("SELECT * FROM student")

        myresult = mycursor.fetchall()

        for x in myresult:
            print("Student No. : ", x[0], ", Name : ", x[1], ", DOB : ", x[2], ", DOJ : ", x[3])

#Class created for updatation of data in table student

class Update_data:
    def __init__(self):
        pass

#function to update table

    def update_table(self):
        try:
            s_no = int(input("Enter the Student No to updatation : "))
        except:
            print("Student No. is not Existing !!!")
        else:
            c = input("Enter 1 for Name Update or 2 for DOB Update or 3 for DOJ Update: ")
            if c == '1':
                try:
                    s_name = input("Enter the Student Name : ")
                    sql = "UPDATE student SET STUDENT_NAME = '%s' WHERE STUDENT_NO = '%d'" %(s_name, s_no)

                    mycursor.execute(sql)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")
                except:
                    print("Student No. is not Existing !!!")
            elif c == '2':
                try:
                    s_dob = input("Enter the Date Of Birth (yyyy-mm-dd) : ")
                    s_dob = datetime.strptime(s_dob, "%Y-%m-%d")
                    s_dob = s_dob.strftime("%Y-%m-%d")
                    sql = "UPDATE student SET STUDENT_DOB = '%s' WHERE STUDENT_NO = '%d'" %(s_dob, s_no)

                    mycursor.execute(sql)

                    mydb.commit()
                    print(mycursor.rowcount, "record(s) affected")
                except:
                    print("Date format is wrong !!!")
            elif c == '3':
                 try:
                    s_doj = input("Enter the Date Of Joining (yyyy-mm-dd) : ")
                    s_doj = datetime.strptime(s_doj, "%Y-%m-%d")
                    s_doj = s_doj.strftime("%Y-%m-%d")
                    sql = "UPDATE student SET STUDENT_DOJ = '%s' WHERE STUDENT_NO = '%d'" %(s_doj, s_no)

                    mycursor.execute(sql)

                    mydb.commit()
                    print(mycursor.rowcount, "record(s) affected")
                 except:
                    print("Date format is wrong !!!")


#Class created for deletion of data

class Delete_data:
    def __init__(self):
        pass

#function to delete data

    def drop_data(self):
        try:
            s_no = int(input("Enter the Student No to delete the record : "))
            sql = "DELETE FROM student WHERE STUDENT_NO = '%d'" %s_no
        except:
            print("Student No. is not Existing !!!")

        else:
            mycursor.execute(sql)

            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")

#Class created for choice input from user

class Main_Menu(Insert_data, Read_data, Update_data, Delete_data):
    def __init__(self):
        Insert_data.__init__(self)
        Read_data.__init__(self)
        Update_data.__init__(self)
        Delete_data.__init__(self)

    def show_menu(self):
        print(" -------------------------- ")
        print("| Enter 1 for Insertion    |")
        print("| Enter 2 for Read         |")
        print("| Enter 3 for Updatation   |")
        print("| Enter 4 for Deletion     |")
        print("| Enter 5 for Exit         |")
        print(" -------------------------- \n")
 
        c = input("Enter your Choice : ")

        if c == "1":
            self.set_data()
        elif c == "2":
            self.get_data()
        elif c == "3":
            self.update_table()
        elif c == "4":
            self.drop_data()
        elif c == "5":
            exit()
        else:
            self.show_menu()

        self.show_menu()

o = Main_Menu()
o.show_menu()
    

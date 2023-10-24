import time
from rich.progress import track
import mysql.connector as sql
import pyfiglet
from rich.console import Console
console=Console()
user=input("Enter User: ")
password=input("Enter Password: ")
user=str(user)
password=str(password)
database=sql.connect(host='localhost',user=user,passwd=password)
cursor=database.cursor()
try:
    cursor.execute('''CREATE DATABASE DoseDirect_Accounts''')
    cursor.execute("""Use DoseDirect_Accounts""")
    cursor.execute("""CREATE TABLE Accounts(Username Varchar(50),Password Varchar(50),MedicalID INT,
    Medical_Report INT Primary Key Auto_Increment)""")
    cursor.execute("""CREATE TABLE MedicalInfo(MedicalID BIGINT Primary key,Age BIGINT, MobileNo BIGINT, Email varchar(50),
    ChronicDisease varchar(50), EmiratesID BIGINT, InsuranceID BIGINT)""")
    cursor.execute("INSERT INTO accounts (Username, Password, MedicalID) VALUES(0, 0, 0)")
    cursor.execute("INSERT INTO medicalinfo VALUES(0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("""CREATE TABLE Medical_Reports(Date varchar(255),Medical_Report BIGINT,Medicines varchar(255), 
    Dosage varchar(255), Duration varchar(255), Instructions varchar(255), 
    Rand_Num INT Primary Key Auto_Increment)""")
    cursor.execute("INSERT INTO Medical_Reports VALUES(0, 0, 0, 0, 0, 0, 0)")
    database.commit()
    cursor.close()
    database.close()
    title = pyfiglet.figlet_format('DataBase Made!', font='Standard')
    console.print(f'[bold blue]{title}',justify='center')
    for i in track(range(3), description="Closing..."):
        time.sleep(1)
except:
    title = pyfiglet.figlet_format('DataBase Already Exists!', font='Standard')
    console.print(f'[bold blue]{title}',justify='center')
    for i in track(range(3), description="Closing..."):
        time.sleep(1)
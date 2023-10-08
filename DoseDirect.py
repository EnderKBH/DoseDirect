import mysql.connector as sql
import pyfiglet
import random
import numpy as np
from rich.table import Table
from drug_named_entity_recognition import find_drugs
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import time
from rich.progress import track
console = Console()
#----DataBase-----#
database=sql.connect(host='localhost',user='root',passwd='tiger',database='dosedirect_accounts')
cursor=database.cursor()
#-----Functions----#
def Username_verifier(username):
   list_DBusers=[]
   cursor.execute('select username from accounts')
   username=str(username)
   username=username.title()
   for x in cursor:
      y=list(x)
      list_DBusers.append(y)
   newlist = list(np.concatenate(list_DBusers))
   if username in newlist:
       return True
   else:
      return False
def Password_Strength(password):
   list_DBpass=[]
   cursor.execute('select Password from accounts')
   for x in cursor:
      y=list(x)
      list_DBpass.append(y)
   newlist = list(np.concatenate(list_DBpass))
   if password in newlist:
       return True
   else:
      return False
def Password_Verfier(username,password):
   list_DBpassV=[]
   query = "select Password from accounts where username=(%s)"
   cursor.execute(query, [username])
   for x in cursor:
      y=list(x)
      list_DBpassV.append(y)
   newlist = list(np.concatenate(list_DBpassV))
   password=str(password)
   if password in newlist:
       return True
   else:
      return False
def MedicalID_Grabber(username):
   username=str(username)
   list_DBMedID=[]
   query = "select MedicalID from accounts where username=(%s)"
   cursor.execute(query, [username])
   for x in cursor:
      y=list(x)
      list_DBMedID.append(y)
   newlist = list(np.concatenate(list_DBMedID))
   return newlist
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)
def medicainfo_Verfier(medicalid):
   list_DBMinfo=[]
   query = "select medicalID from medicalinfo;"
   cursor.execute(query)
   for x in cursor:
      y=list(x)
      list_DBMinfo.append(y)
   newlist = list(np.concatenate(list_DBMinfo))
   if medicalid in newlist:
       return True
   else:
      return False
def Medicalinfo_grabber(medicalID):
   list_DBMinfo=[]
   query = "select age,mobileNo,email,chronicdisease,emiratesID,insuranceID from medicalinfo where medicalID=(%s)"
   cursor.execute(query,[medicalID])
   for x in cursor:
      y=list(x)
      list_DBMinfo.append(y)
   newlist = list(np.concatenate(list_DBMinfo))
   return newlist
def main_menu():
   title = pyfiglet.figlet_format('DoseDirect', font='Standard')
   console.print(f'[bold blue]{title}',justify='center')
   table = Table(title="Main Menu")
   table.add_column("Option", style="blue")
   table.add_column("Option Number", justify="right", style="green")
   table.add_row("Create New MedicalInfo", "1")
   table.add_row("View MedicalInfo", "2")
   table.add_row("Edit MedicalInfo", "3")
   table.add_row("Create MedicalReports", "4")
   table.add_row("View MedicalReports", "5")
   table.add_row("Edit MedicalReports", "6")
   table.add_row("View All MedicalReports", "7")
   table.add_row("Exit", "8")
   console.print(table,justify="center")
def main_menu_medicalreports():
   table = Table(title="Edit MedicalReport MainMenu")
   table.add_column("Option", style="blue")
   table.add_column("Option Number", justify="right", style="green")
   table.add_row("Edit Date", "1")
   table.add_row("Edit Medicines", "2")
   table.add_row("Edit Dosage", "3")
   table.add_row("Edit Duration", "4")
   table.add_row("Edit Instructions", "5")
   table.add_row("Exit", "6")
   console.print(table,justify="center")
def main_menu_medicalinfo():
   table = Table(title="Edit MedicalInfo Main Menu")
   table.add_column("Option", style="blue")
   table.add_column("Option Number", justify="right", style="green")
   table.add_row("Edit Age", "1")
   table.add_row("Edit MobileNumber", "2")
   table.add_row("Edit EmiratesID", "3")
   table.add_row("Edit InsuranceID", "4")
   table.add_row("Edit Email", "5")
   table.add_row("Edit ChronicDisease", "6")
   table.add_row("Exit", "7")
   console.print(table,justify="center")
def MedicalReportID_Grabber(username):
   username=str(username)
   list_DBMedReportID=[]
   query = "select Medical_Report from accounts where username=(%s)"
   cursor.execute(query, [username])
   for x in cursor:
      y=list(x)
      list_DBMedReportID.append(y)
   newlist = list(np.concatenate(list_DBMedReportID))
   return newlist
def convert_string(list1):
   f1 = ""
   for i in list1:
      f1 += str(i)+ " " 
   return f1
def Date_Verifier(date,medical_reportID):
   date=str(date)
   list_DBMinfo=[]
   query = "select date from medical_reports where Medical_Report=%s;"
   cursor.execute(query,[medical_reportID])
   for x in cursor:
      y=list(x)
      list_DBMinfo.append(y)
   try:
    newlist = list(np.concatenate(list_DBMinfo))
   except:
      newlist=[]
   if date in newlist:
       return True
   else:
      return False
def Date_Verifier_ReChecker(date,new_date,medical_reportID):
   date=str(date)
   list_DBMinfo=[]
   query = "select date from medical_reports where Medical_Report=%s;"
   cursor.execute(query,[medical_reportID])
   for x in cursor:
      y=list(x)
      list_DBMinfo.append(y)
   try:
    newlist = list(np.concatenate(list_DBMinfo))
   except:
      newlist=[]
   if date in newlist:
      newlist.remove(date)
   if new_date in newlist:
       return True
   else:
      return False
def Date_Grabber(medical_reportID):
   list_DBMinfo=[]
   query = "select date from medical_reports where Medical_Report=%s;"
   cursor.execute(query,[medical_reportID])
   for x in cursor:
      y=list(x)
      list_DBMinfo.append(y)
   try:
    newlist = list(np.concatenate(list_DBMinfo))
   except:
      newlist=[]
   return newlist
def Medicine_Grabber(date,medical_reportID):
   list_DBMedReportID=[]
   query = "select medicines from medical_reports where date=%s AND Medical_Report=%s"
   cursor.execute(query, [date,medical_reportID])
   for x in cursor:
      y=list(x)
      list_DBMedReportID.append(y)
   newlist = list(np.concatenate(list_DBMedReportID))
   for medicine in newlist:
      medicines=medicine.split()
   for i in medicines:
      if i=="|":
         medicines.remove(i)
   return medicines
def MedicalReport_grabber(date,medical_reportID):
   list_DBMedReportID=[]
   query = "select Date,Medical_Report,Medicines,Dosage,Duration,Instructions from medical_reports where date=%s AND Medical_Report=%s"
   cursor.execute(query, [date,medical_reportID])
   for x in cursor:
      y=list(x)
      list_DBMedReportID.append(y)
   newlist = list(np.concatenate(list_DBMedReportID))
   return newlist
# def Medicalinfo_Option():
#    while True:
#             try:
#                Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
#                break
#             except ValueError:
#                console.print(Panel("[bold red]Error!"),justify='center')
#    return Medicalinfo_Option
#-----Functions----#

# print(Medicine_Grabber("11-8-2023",2))



Login_Print = "# Input 1 for Login"
Signin_Print = "# Input 2 for Sign In"
Login_Print = Markdown(Login_Print)
Signin_Print = Markdown(Signin_Print)
console.print(Login_Print,Signin_Print)
while True:
    try:
        login=int(console.input("[bold red]Enter Value: "))
        if login not in [1,2]:
           console.print(Panel("[bold red]Enter 1 or 2"),justify='center')
           continue
        break
    except ValueError:
        console.print(Panel("[bold red]Error!"),justify='center')
if login==1: #Login
    username_check=0
    password_check=0
    while True:
        username=console.input("[bold red]Enter Username: ")
        password=console.input("[bold red]Enter Password: ")
        username=str(username)
        if Username_verifier(username):
           username_check=1
        else:
           console.print(Panel("[bold red]Username Does not exist"),justify='center')
           continue
        if Password_Verfier(username,password):
           password_check=1
        else:
           console.print(Panel("[bold red]Password Does not match with Username!"),justify='center')
           continue
        if username_check==1 and password_check==1:
           console.print(Panel("[bold green]Logged In!"),justify='center')
           break
if login==2: #Sign In
   while True:  
    list_DBusers=[]
    username=console.input("[bold red]Enter Username: ")
    username=str(username)
    username=username.title()
    if Username_verifier(username):
       console.print(Panel("[bold red]Username Already Exists!"),justify='center')
       continue
    else:
       break
   while True:
    password=console.input("[bold red]Enter Password: ")
    if Password_Strength(password):
       console.print(Panel("[bold red]Password too weak!"),justify='center')
       continue
    break
   #Random Integer Generator for MedicalReport
   medid=random.randint(0,100000)
   query = "INSERT INTO accounts (Username, Password, MedicalID) VALUES (%s, %s, %s)"
   cursor.execute(query, (username, password, medid))
   database.commit()
   console.print(Panel("[bold green]Signed In!"),justify='center')
while True:
   main_menu()
   while True:
      try:
         Option=int(console.input("[bold red]Enter Value: "))
         break
      except ValueError:
         console.print(Panel("[bold red]Error!"),justify='center')
   #Create new MedicalInfo
   while Option==1: 
      MedicalID=convert(MedicalID_Grabber(username))
      if medicainfo_Verfier(MedicalID):
         console.print(Panel("[bold red]Medical Info already exists!"),justify='center')
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
      else:           
         while True:
            try:
               Age=int(console.input("[bold red]Enter Age: "))
               MobileNu=int(console.input("[bold red]Enter MobileNu: "))
               EmiratesID=int(console.input("[bold red]EmiratesID: "))
               InsuranceID=int(console.input("[bold red]InsuranceID: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
         Email=console.input("[bold red]Enter Email: ")
         ChronicDisease=console.input("[bold red]Enter Chronic Disease: ")
         query = "INSERT INTO medicalinfo (MedicalID, age, MobileNo, Email, ChronicDisease, EmiratesID, InsuranceID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
         cursor.execute(query, (MedicalID, Age, MobileNu, Email, ChronicDisease, EmiratesID, InsuranceID))
         database.commit()
         MedicalInfoAdd = "# MedicalInfo Added!"
         MedicalInfoAdd = Markdown(MedicalInfoAdd)
         console.print(MedicalInfoAdd)
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
   #View MedicalInfo
   while Option==2:
      MedicalID=convert(MedicalID_Grabber(username))
      if medicainfo_Verfier(MedicalID):
         List_Info=Medicalinfo_grabber(MedicalID)

         table = Table(title="Medical Info")
         table.add_column("Category", style="blue")
         table.add_column("Output", justify="right", style="green")
         table.add_row("Age", List_Info[0])
         table.add_row("Mobile Number", List_Info[1])
         table.add_row("Email", List_Info[2])
         table.add_row("ChronicDisease", List_Info[3])
         table.add_row("EmiratesID", List_Info[4])
         table.add_row("InsuranceID", List_Info[5])
         console = Console()
         console.print(table,justify="center")
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
      else:
         console.print(Panel("[bold red]There exists no Medicalinfo!"),justify='center')
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
   #EDIT medicalinfo
   while Option==3: #GUI HOLD USER COMFORT HOLD FIX IT!!!
      MedicalID=convert(MedicalID_Grabber(username))
      if medicainfo_Verfier(MedicalID):
         main_menu_medicalinfo()
         while True:
            try:
               Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==1:
           while True:
            try:
              Age=int(console.input("[bold red]Enter Age: "))
              break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
           query = "update medicalinfo set age=(%s) where MedicalID=(%s);"
           cursor.execute(query,(Age,MedicalID))
           database.commit()
           query = "update medicalinfo set age=(%s) where MedicalID=(%s);"
           MedicalInfoAge = "# Age Changed!"
           MedicalInfoAge = Markdown(MedicalInfoAge)
           console.print(MedicalInfoAge)
           main_menu_medicalinfo()
           while True:
            try:
               Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==2:
            while True:
             try:
              MobileNu=int(console.input("[bold red]Enter MobileNu: "))
              break
             except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
            query = "update medicalinfo set MobileNo=(%s) where MedicalID=(%s);"
            cursor.execute(query,(MobileNu,MedicalID))
            database.commit()
            MedicalInfoMN = "# Mobile-Number Changed!"
            MedicalInfoMN = Markdown(MedicalInfoMN)
            console.print(MedicalInfoMN)
            main_menu_medicalinfo()
            while True:
               try:
                  Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==3:
            while True:
             try:
              EmiratesID=int(console.input("[bold red]EmiratesID: "))
              break
             except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
            query = "update medicalinfo set EmiratesID=(%s) where MedicalID=(%s);"
            cursor.execute(query,(EmiratesID,MedicalID))
            database.commit()
            MedicalInfoEID = "# EmiratesID Changed!"
            MedicalInfoEID = Markdown(MedicalInfoEID)
            console.print(MedicalInfoEID)
            main_menu_medicalinfo()
            while True:
               try:
                  Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==4:
            while True:
             try:
              InsuranceID=int(console.input("[bold red]InsuranceID: "))
              break
             except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
            query = "update medicalinfo set InsuranceID=(%s) where MedicalID=(%s);"
            cursor.execute(query,(InsuranceID,MedicalID))
            database.commit()
            MedicalInfoIID = "# InsuranceID Changed!"
            MedicalInfoIID = Markdown(MedicalInfoIID)
            console.print(MedicalInfoIID)
            main_menu_medicalinfo()
            while True:
               try:
                  Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==5:
            Email=console.input("[bold red]Enter Email: ")
            query = "update medicalinfo set Email=(%s) where MedicalID=(%s);"
            cursor.execute(query,(Email,MedicalID))
            database.commit()
            MedicalInfoE = "# Email Changed!"
            MedicalInfoE = Markdown(MedicalInfoE)
            console.print(MedicalInfoE)
            main_menu_medicalinfo()
            while True:
               try:
                  Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==6:
            ChronicDisease=console.input("[bold red]Enter Chronic Disease: ")
            query = "update medicalinfo set ChronicDisease=(%s) where MedicalID=(%s);"
            cursor.execute(query,(ChronicDisease,MedicalID))
            database.commit()
            MedicalInfoCD = "# ChronicDisease Changed!"
            MedicalInfoCD = Markdown(MedicalInfoCD)
            console.print(MedicalInfoCD)
            main_menu_medicalinfo()
            while True:
               try:
                  Medicalinfo_Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         while Medicalinfo_Option==7: # I AM HERE
            main_menu()
            while True:
               try:
                  Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
                  continue
            break
      if not medicainfo_Verfier(MedicalID):
         console.print(Panel("[bold red]There exists no Medicalinfo!"),justify='center')
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
               continue
   #Create MedicalReports
   while Option==4:
         username=str(username)
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
                  try:
                     Year=int(console.input("[bold red]Enter Year: "))
                     Month=int(console.input("[bold red]Enter Month: "))
                     Day=int(console.input("[bold red]Enter Day: "))
                     break
                  except ValueError:
                     console.print(Panel("[bold red]Error!"),justify='center')
                     continue
         date=f"{Day}-{Month}-{Year}"
         if Date_Verifier(date,Medical_Report):
            console.print(Panel("[bold red]Medical Report Already Registered!"),justify='center')
            main_menu()
            while True:
               try:
                  Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
         else:
            username=str(username)
            Medical_Report=convert(MedicalReportID_Grabber(username))
            while True:
               try:
                  MedicineNu=int(console.input("[bold red]How many medicines prescribed: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
                  continue
            while True:
               Med=[]
               for i in range(MedicineNu):
                  Medicines=console.input("[bold red]Enter Generic Medicine Name (eg:Paracetamol,guaifenesin systemic): ")
                  Med.append(Medicines)
                  Med.append("|")
               while True:
                  try:
                     console.print(Panel("[bold red]Are you sure, enter 1 for yes and 2 for no"),justify='center')
                     x=int(console.input("[bold red]Enter Value: "))
                     break
                  except ValueError:
                     console.print(Panel("[bold red]Error!"),justify='center')
                     continue
               if x==1:
                  break
               else:
                  continue
            Med_Modified=[]
            for i in Med:
               if i!="|":
                  Med_Modified.append(i)
            Dosage=[]
            for i in Med_Modified:
               console.print("[bold red]Prescribed Dosage for ",i)
               Dos=console.input("[bold red]Enter: ")
               Dosage.append(Dos)
               Dosage.append("|")
            Dosage=convert_string(Dosage)
            Duration=[]
            for i in Med_Modified:
               console.print("[bold red]Prescribed Duration for ",i)
               Dur=console.input("[bold red]Enter: ")
               Duration.append(Dur)
               Duration.append("|")
            Duration=convert_string(Duration)
            Instructions=[]
            for i in Med_Modified:
               console.print("[bold red]Prescribed Instructions for ",i)
               Ins=console.input("[bold red]Enter: ")
               Instructions.append(Ins)
               Instructions.append("|")
            Instructions=convert_string(Instructions)
            Med=convert_string(Med)
            query = "INSERT INTO medical_Reports (Date, Medical_Report, Medicines, Dosage, Duration, Instructions) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (date, Medical_Report, Med, Dosage, Duration, Instructions))
            database.commit()
            console.print(Panel("[bold green]Prescription Added!"),justify='center')
            main_menu()
            while True:
               try:
                  Option=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
   #View Meddical Reports
   while Option==5:
      Medical_Report=convert(MedicalReportID_Grabber(username))
      while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
      List_Info=MedicalReport_grabber(date,Medical_Report)
      table = Table(title=f"Medical_Report on {List_Info[0]}")
      table.add_column("Category", style="blue")
      table.add_column("Output", justify="right", style="green")
      table.add_row("Date", List_Info[0])
      table.add_row("Medical_ReportID", List_Info[1])
      table.add_row("Medicine", List_Info[2])
      table.add_row("Dosage", List_Info[3])
      table.add_row("Duration", List_Info[4])
      table.add_row("Instruction", List_Info[5])
      console = Console()
      console.print(table,justify="center")
      main_menu()
      while True:
         try:
            Option=int(console.input("[bold red]Enter Value: "))
            break
         except ValueError:
            console.print(Panel("[bold red]Error!"),justify='center')
   #Edit Medical Reports
   while Option==6:
      main_menu_medicalreports()
      while True:
               try:
                  Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
      while Option_MedicalReports==1:
         username=str(username)
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
         MedicalReportD = "# Editing!"
         MedicalReportD = Markdown(MedicalReportD)
         console.print(MedicalReportD)
         while True:
                  try:
                     Year_ED=int(console.input("[bold red]Enter Year: "))
                     Month_ED=int(console.input("[bold red]Enter Month: "))
                     Day_ED=int(console.input("[bold red]Enter Day: "))
                     date_medicalreports=f"{Day_ED}-{Month_ED}-{Year_ED}"
                     if Date_Verifier_ReChecker(date,date_medicalreports,Medical_Report):
                        console.print(Panel("[bold red] Medical Report already exists with the entered Date!"),justify='center')
                        continue
                     break
                  except ValueError:
                     console.print(Panel("[bold red]Error!"),justify='center')
                     continue
         query = "update medical_reports set date=%s where date=%s AND medical_report=%s"
         cursor.execute(query, (date_medicalreports,date,Medical_Report))
         database.commit()
         MedicalReportD = "# Changed Date!"
         MedicalReportD = Markdown(MedicalReportD)
         console.print(MedicalReportD)
         main_menu_medicalreports()
         while True:
               try:
                  Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
      while Option_MedicalReports==2:
         username=str(username)
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
         MedicalReportE = "# Editing!"
         MedicalReportE = Markdown(MedicalReportE)
         console.print(MedicalReportE)
         while True:
               try:
                  MedicineNu=int(console.input("[bold red]How many medicines prescribed: "))
                  break
               except ValueError:
                  console.print(Panel("[bold red]Error!"),justify='center')
                  continue
         while True:
               Med=[]
               for i in range(MedicineNu):
                  Medicines=console.input("[bold red]Enter Generic Medicine Name (eg:Paracetamol,guaifenesin systemic): ")
                  Med.append(Medicines)
                  Med.append("|")
               while True:
                  try:
                     console.print(Panel("[bold red]Are you sure, enter 1 for yes and 2 for no"),justify='center')
                     x=int(console.input("[bold red]Enter Value: "))
                     break
                  except:
                     console.print(Panel("[bold red]Error!"),justify='center')
                     continue
               if x==1:
                  break
               else:
                  continue
         Med=convert_string(Med)
         query = "update medical_reports set Medicines=%s where Date=%s AND medical_report=%s"
         cursor.execute(query, (Med,date,Medical_Report)) 
         database.commit()
         MedicalReportM = "# Changed Medicine!"
         MedicalReportM = Markdown(MedicalReportM)
         console.print(MedicalReportM)
         main_menu_medicalreports()
         while True:
            try:
               Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
      while Option_MedicalReports==3:
         username=str(username)
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
         MedicalReportDo = "# Editing!"
         MedicalReportDo = Markdown(MedicalReportDo)
         console.print(MedicalReportDo)
         Dosage=[]
         for i in Medicine_Grabber(date,Medical_Report):
            console.print("[bold red]Prescribed Dosage for ",i)
            Dos=console.input("[bold red]Enter: ")
            Dosage.append(Dos)
            Dosage.append("|")
         Dosage=convert_string(Dosage)
         query = "update medical_reports set Dosage=%s where Date=%s AND medical_report=%s"
         cursor.execute(query, (Dosage,date,Medical_Report)) 
         database.commit()
         MedicalReportDo = "# Dosage Changed!"
         MedicalReportDo = Markdown(MedicalReportDo)
         console.print(MedicalReportDo)
         main_menu_medicalreports()
         while True:
            try:
               Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
      while Option_MedicalReports==4:
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
         MedicalReportDu = "# Editing!"
         MedicalReportDu = Markdown(MedicalReportDu)
         console.print(MedicalReportDu)
         Duration=[]
         for i in Medicine_Grabber(date,Medical_Report):
            console.print("[bold red]Prescribed Duration for ",i)
            Dur=console.input("[bold red]Enter: ")
            Duration.append(Dur)
            Duration.append("|")
         Duration=convert_string(Duration)
         query = "update medical_reports set Duration=%s where Date=%s AND medical_report=%s"
         cursor.execute(query, (Duration,date,Medical_Report)) 
         database.commit()
         MedicalReportDu = "# Duration Changed!"
         MedicalReportDu = Markdown(MedicalReportDu)
         console.print(MedicalReportDu)
         main_menu_medicalreports()
         while True:
            try:
               Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
      while Option_MedicalReports==5:
         Medical_Report=convert(MedicalReportID_Grabber(username))
         while True:
            console.print(Panel("[bold green]Enter Apporiate Date!"),justify='center')
            while True:
                     try:
                        Year=int(console.input("[bold red]Enter Year: "))
                        Month=int(console.input("[bold red]Enter Month: "))
                        Day=int(console.input("[bold red]Enter Day: "))
                        break
                     except ValueError:
                        console.print(Panel("[bold red]Error!"),justify='center')
                        continue
            date=f"{Day}-{Month}-{Year}"
            if Date_Verifier(date,Medical_Report):
               break
            else:
               console.print(Panel("[bold red] No such Medical Report exists with the entered Date!"),justify='center')
               continue
         MedicalReportI = "# Editing!"
         MedicalReportI = Markdown(MedicalReportI)
         console.print(MedicalReportI)
         Instructions=[]
         for i in Medicine_Grabber(date,Medical_Report):
            console.print("[bold red]Prescribed Instructions for ",i)
            Ins=console.input("[bold red]Enter: ")
            Instructions.append(Ins)
            Instructions.append("|")
         Instructions=convert_string(Instructions)
         query = "update medical_reports set Instructions=%s where Date=%s AND medical_report=%s"
         cursor.execute(query, (Instructions,date,Medical_Report)) 
         database.commit()
         MedicalReportI = "# Instructions Changed!"
         MedicalReportI = Markdown(MedicalReportI)
         console.print(MedicalReportI)
         main_menu_medicalreports()
         while True:
            try:
               Option_MedicalReports=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
      if Option_MedicalReports==6:
         main_menu()
         while True:
            try:
               Option=int(console.input("[bold red]Enter Value: "))
               break
            except ValueError:
               console.print(Panel("[bold red]Error!"),justify='center')
   #View ALL medical reports
   while Option==7:
      Medical_Report=convert(MedicalReportID_Grabber(username))
      for i in Date_Grabber(Medical_Report):
         List_Info=MedicalReport_grabber(i,Medical_Report)
         table = Table(title=f"Medical_Report on {List_Info[0]}")
         table.add_column("Category", style="blue")
         table.add_column("Output", justify="right", style="green")
         table.add_row("Date", List_Info[0])
         table.add_row("Medical_ReportID", List_Info[1])
         table.add_row("Medicine", List_Info[2])
         table.add_row("Dosage", List_Info[3])
         table.add_row("Duration", List_Info[4])
         table.add_row("Instruction", List_Info[5])
         console = Console()
         console.print(table,justify="center")
      main_menu()
      while True:
         try:
            Option=int(console.input("[bold red]Enter Value: "))
            break
         except ValueError:
            console.print(Panel("[bold red]Error!"),justify='center')
















      # Medical_Report=convert(MedicalReportID_Grabber(username))
      # while True:
      #    print("Enter Apporiate Date")
      #    while True:
      #             try:
      #                Year=int(input("Enter Year: "))
      #                Month=int(input("Enter Month: "))
      #                Day=int(input("Enter Day: "))
      #                break
      #             except ValueError:
      #                print("Error!")
      #                continue
      #    date=f"{Day}-{Month}-{Year}"
      #    if Date_Verifier(date,Medical_Report):
      #       break
      #    else:
      #       continue
      # for y in Medicine_Grabber(date,Medical_Report):
      #    x=find_drugs(y.split(" "))
      #    nhs_urls = [item[0]['nhs_url'] for item in x if 'nhs_url' in item[0]]
      #    wikipedia_urls = [item[0]['wikipedia_url'] for item in x if 'wikipedia_url' in item[0]]
      #    drugbankid = [item[0]['drugbank_id'] for item in x if 'drugbank_id' in item[0]]
      #    if nhs_urls!=[]:
      #       print(f"Wikipedia for {y}: {wikipedia_urls}")
      #    if wikipedia_urls!=[]:
      #       print(f"NHS for {y}: {nhs_urls}")
      #    if drugbankid!=[]:
      #       print(f"DrugBankID for {y}: {drugbankid}")
      #    else:
      #       print("Error!")
      # main_menu()
      # while True:
      #    try:
      #       Option=int(input("Enter Value: "))
      #       break
      #    except ValueError:
      #       print("Error!")
   #Exit
   if Option==8:
      title = pyfiglet.figlet_format('Thank You!', font='Standard')
      console.print(f'[bold blue]{title}',justify='center')
      for i in track(range(3), description="Closing..."):
         time.sleep(1)
      break
print("my first commit test")
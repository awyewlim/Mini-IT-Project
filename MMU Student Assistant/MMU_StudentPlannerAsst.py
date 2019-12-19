import sys
import gc
import sqlite3
import re

    
def startup(): 
    import os
    import time
    os.system ("cls")
    print ("               ==================================")
    print ("                Welcome To MMU Student Assistant")
    print ("               ==================================")

    while True:
       try:
          print ("\n")
          print ("Option:")
          print ("1. Login")
          print ("2. Register")
          option = int(input("Enter an option:"))

          if option == 1 : 

              def login():
                  
                  while True: 
                      import os
                      import time
                      os.system("cls")
                      print ("               ============")
                      print ("                Login Page")
                      print ("               ============")
                      print ("")
                      print('After key-in, press "ENTER" key to proceed next.')
                      print("")
                      global username
                      username = str(input("Username :"))
                      password = str(input("Password :"))
                      
                      
                      if username == "" or password == "":
                          os.system("cls")
                          print("  =========================================")
                          print("   Username or Password cannot be blanked!")
                          print("  =========================================")
                          time.sleep(1.5)
                          run = True

                      else:
                          with sqlite3.connect("database.db") as db:
                              c = db.cursor()
                          find_user = ("SELECT * FROM data WHERE username = ? and password = ?")
                          c.execute(find_user,[(username),(password)])
                          result = c.fetchall()
                          
                          if result:
                              print("")
                              print("Login Success!")
                              time.sleep(1.5)
                              os.system("cls") 
                              mainmenu()
                              

                          else:
                              print("")
                              print("User Not Found! Please try again.")
                              time.sleep(1.5)
                              run = True
                                                                     
              loginpage = login()

          if option == 2 :              
                               
              def register():
                  import os
                  import sqlite3
                  import time
                     
                  run = True
                  while run == True:
                      os.system("cls")
                      print ("               ===========================")
                      print ("                Account Registration Page")
                      print ("               ===========================")
                      print ("\n")               
                      
                      print('After key-in, press "ENTER" key to proceed')
                      print("")
                      n_username = str(input("New Username:"))
                      n_password = str(input("New Password:"))

                      if n_username == "" or n_password == "":
                            os.system("cls")
                            print("")
                            print("  =================================================")
                            print("   New Username or New Password cannot be blanked!")
                            print("  =================================================")
                            time.sleep(2)
                            run = True

                      else:        

                          with sqlite3.connect("database.db") as db:
                              c = db.cursor()

                          c.execute("CREATE TABLE IF NOT EXISTS data(username,password);")
                          db.commit()

                          find_user = ("SELECT * FROM data WHERE username = ?")
                          c.execute(find_user, [(n_username)])
                          result = c.fetchall()

                          if result:
                              print("")
                              print ("Username Taken!")
                              time.sleep(1.5)
                              run = True
                          else:
                              insert = "INSERT INTO data(username,password) VALUES (?,?);"
                              c.execute(insert,[(n_username),(n_password)])
                              db.commit()
                              print("\n")
                              print("Account Created!")                             
                              time.sleep(2)
                              startup()
                              os.system("cls")
                        
                                   
              register = register()

          if option!= 1 or option!= 2:
                print ("\n")
                print("Invalid option. Please enter 1 or 2.")
                time.sleep(2)
                return startup()

       except ValueError:
           print ("\n")
           print("Invalid option! Please enter 1 or 2")
           time.sleep(1.5)
           return startup()

def mainmenu():
    import os
    import time
    
    while True: 
        try:
             os.system("cls")
             print("Welcome,",username,"!")
             print("")
             print("------------ MAIN MENU ------------")
             print("\n")

             print("Option:")
             print(" 1. Academic Calculator")
             print(" 2. Budget Planner")
             print(" 3. Event Recorder")
             print(" 4. Logout")
             print(" 5. Logout and Exit")
             option = int(input("Enter an option:"))
    
             if option == 1:
                    def academic_calculator():
                        os.system("cls")
                        check ="True"
                        while check=="True":
                            print("-------------- Academic Calculator --------------")
                            print("Welcome to Academic Calculator. Please enter a number to proceed.")
                            print("Enter 1 to proceed GPA calculator.")
                            print("Enter 2 to proceed CGPA calculator.")
                            print("Enter 0 to back to the main menu.")
                            while True:
                                try:
                                    selection=int(input("Selection:"))

                                except ValueError:
                                    print("Please insert a valid number.")
                                    continue
            
                                if selection<0:
                                    print("Sorry, your input must be a positive number.")
            
                                if selection==1:
                                    gpacalculator()
                                    break

                                if selection==2:
                                    cgpacalculator()
                                    break

                                if selection==0:
                                    check="False"
                                    break
                
    

                    def getnum_subject():
                        while True:
                            try:
                                num_subject=int(input("Please enter the number of your subjects taken:"))
            
                            except ValueError:
                                print("Please insert a valid number.")
                                print("")
                                continue
        
                            if num_subject<0:
                                print("Sorry, your input must be a positive number.")
                                print("")
                            else:
                                break
 
                        return num_subject

                    def getname_subject(num_subject):
                        counter = 0
                        while True:
                            counter += 1
                            name_subject=input("Name of Subject " + str(counter) + ":")
                            user_subject.append(name_subject)
                            if counter == num_subject:
                                break
                        return name_subject

                    def getgrade_subject():
                        for i in user_subject:
                            grade_subject=input("Grade for " + i + ":")
                            user_grade.append(grade_subject)
                        return grade_subject

                    def getcredithour_subject():
                        for i in user_subject:
                            while True:
                                try:
                                    credithour_subject=int(input("Credit hour for " + i + ":"))
                                except ValueError:
                                    print("Please insert a valid number.")
                                    print("")
                                    continue

                                if credithour_subject<0:
                                    print("Sorry, your input must be a positive number.")
                                    print("")
                                else:
                                    break
                            user_credithour.append(credithour_subject)
        
                        return credithour_subject

                    def getpoint_subject():
                        global point
                        point=0
                        for i in user_grade:
                            if i=="A+" or i=="A" or i=="a" or i=="a+":
                                point=4.00
                                user_point.append(point)
            
                            if i=="A-" or i=="a-":
                                point=3.67
                                user_point.append(point)
            
                            if i=="B+" or i=="b+":
                                point=3.33
                                user_point.append(point)
            
                            if i=="B" or i=="b":
                                point=3.00
                                user_point.append(point)
            
                            if i=="B-" or i=="b-":
                                point=2.67
                                user_point.append(point)
            
                            if i=="C+" or i=="c+":
                                point=2.33
                                user_point.append(point)
            
                            if i=="C" or i=="c":
                                point=2.00
                                user_point.append(point)
            
                            if i=="C-" or i=="c-":
                                point=1.67
                                user_point.append(point)
            
                            if i=="D+" or i=="d+":
                                point=1.33
                                user_point.append(point)

                            if i=="D" or i=="d":
                                point=1.00
                                user_point.append(point)
                
                            if i=="F" or i=="f":
                                point=0.00
                                user_point.append(point)

                        return point

                    def gpacalculator():
                        num_subject = getnum_subject()
                        name_subject = getname_subject(num_subject)
                        credithour_subject = getcredithour_subject()
                        grade_subject = getgrade_subject()
                        point = getpoint_subject()
                        counter = 0
                        sum_of_mul = 0
                        while counter < len(user_subject):
                            mul_of_upuc = user_point[counter] * user_credithour[counter]
                            sum_of_mul += mul_of_upuc
                            counter += 1
        
                        gpa = sum_of_mul / sum(user_credithour)
                        print('Your GPA is ','{:.2f}'.format(gpa),'.')
                        print("")
                        print("Enter 8 to calculate again.")
                        print("Enter 9 to back to academic calculator.")
                        while True:
                                try:
                                    selection=int(input("Selection:"))

                                except ValueError:
                                    print("Please insert a valid number.")
                                    continue
            
                                if selection<0:
                                    print("Sorry, your input must be a positive number.")
            
                                if selection==8:
                                    del user_subject[:]
                                    del user_grade[:]
                                    del user_point[:]
                                    del user_credithour[:]
                                    gpacalculator()
                                    break

                                if selection==9:
                                    return academic_calculator()
                                    break

                        return gpa
    

                    def cgpacalculator():
                        while True:
                            try:
                                num_trimester = int(input('Number of trimester:'))

                            except ValueError:
                                print("Please insert a valid number.")
                                continue

                            if num_trimester<=0:
                                print("Sorry, your input must be a positive number")
                            else:
                                break


                        credit_hour = []
                        grade_point = []

                        for i in range(num_trimester):
                            print('Sem ',i+1)
                            c_h = int(input('Credit hour you earn this trimester:'))
                            g_p = int(input('Grade point you earn this trimester:'))
                            credit_hour.append(c_h)
                            grade_point.append(g_p)

                        cgpa = sum(grade_point) / sum(credit_hour)
                        print('Your CGPA is ','{:.2f}'.format(cgpa),'.')
                        print("")
                        print("Enter 8 to calculate again.")
                        print("Enter 9 to back to academic calculator.")
                        while True:
                                try:
                                    selection=int(input("Selection:"))

                                except ValueError:
                                    print("Please insert a valid number.")
                                    continue
            
                                if selection<0:
                                    print("Sorry, your input must be a positive number.")
                                    continue

                                if selection!=8 and selection!=9:
                                    print("Please enter 8 to calculate again or 9 to back to academic calculator")
                                    continue
            
                                if selection==8:
                                    del credit_hour[:]
                                    del grade_point[:]
                                    cgpacalculator()
                                    break

                                if selection==9:
                                    return academic_calculator()
                                    break
            
            
                        return cgpa
        
                    user_subject = []
                    user_grade = []
                    user_point = []
                    user_credithour = []
                    academic_calculator = academic_calculator()

             if option == 2:
                 from getBudget import currentBudget, path
                 import time
                 import os 
                 os.system("cls")

                 def main():
                     import time
                     endProgram = 'no'
                     totalBudget = currentBudget
                     while endProgram == 'no':
                         try:
                             os.system("cls")
                             import time
                             print('Welcome to the Budget Planner')
                             print('Selections: ')
                             print('1-Add Revenue: ')
                             print('2-Add an Expense: ')
                             print('3-Check Budget Balance: ')
                             print('4-Save progress')
                             print('5-Back to Main Menu')
 
                             choice = int(input('Please enter your selection: '))
                             if choice == 1:
                                 totalBudget = addRevenue(totalBudget)
                             elif choice == 2:
                                 totalBudget = addExpense(totalBudget)
                             elif choice == 3:
                                print('Your balance is RM{0}'.format(totalBudget))
                                time.sleep(2)
                                print("")
                             elif choice == 4:
                                 saveBudget(totalBudget)
                                 print('Progress saved')
                                 print("")
                                 time.sleep(2)
                             elif choice == 5:
                                 print('Thank you for using "Budget Planner"')
                                 time.sleep(2)
                                 return mainmenu()
                             else:
                                 print("")
                                 print('Invalid selection, please try again')
                                 print("")
                                 time.sleep(2)
                                 return main(  )

                         except ValueError:
                             print("")
                             print("Invalid selection, please try again!")
                             print("")
                             time.sleep(2)
                             return main()

                 def addRevenue(totalBudget):
                     revenue = float(input('Enter new monthly income: RM'))
                     totalBudget = totalBudget + revenue
                     print('your new budget is: RM{0}'.format(totalBudget))
                     print("")
                     time.sleep(2)
                     return totalBudget


                 def addExpense(totalBudget):
                     expense = float(input('Enter your expense amount: RM'))
                     timesPerMonth = int(input('How many times per month: '))
                     totalExpense = expense * timesPerMonth
                     if totalBudget - totalExpense >= 0:
                         totalBudget = totalBudget - totalExpense
                         print ('The expenses was accepted, your remaining budget is: RM{0}'.format(totalBudget))
                         print("")
                         time.sleep(2)
                         return totalBudget
                     else:
                         print ('The expenses was rejected because the budget exceeded.')
                         print("")
                         time.sleep(2)
                         return totalBudget




                 def saveBudget(totalBudget):
                     with open(path, 'w') as f:
                         f.write(str(totalBudget))
                     f.close()

                 main()

                  
             if option == 3:
                 import datetime

                 def event_recorder():
                     import os
                     import time
                     os.system("cls")
                     print("Welcome To Event Countdown")
                     print("")
                     while True:
                             print("1. View Event")
                             print("2. Add Event")
                             print("3. Back To Main Menu")
                             print("")
                             option = int(input("Enter an option:"))


                             if option == 1:
                                 viewEvent()
                                 break
                
                             elif option == 2:
                                 addEvent()
                                 break

                             elif option == 3:
                                 mainmenu()

                             elif option == '' or option != 1 or option != 2 or option != 3 :
                                 print("Invalid input. Please enter 1 or 2 or 3 to select an option")
                                 time.sleep(2)
                                 return event_recorder()                                 
            
                 def addEvent():
                     import os
                     import time
                     os.system("cls")
                     print("===========")
                     print(" Add Event")
                     print("===========")
                     print("")
    
                     global name, year, month, day, event_date
                     now = datetime.datetime.now()
          
                     name = str(input("Please enter the event name:"))
                     year = int(input("Please enter event year:"))
                     if year < now.year:
                         print("=========================================")
                         print("Please enter correct value for Event year")
                         print("=========================================")
                         time.sleep(2)
                         addEvent()
          
                     else:
                         month = int(input("Please enter event month:"))
                         if month < 1 or month > 12:
                             print("==========================================")
                             print("Please enter correct value for Event month")
                             print("==========================================")
                             time.sleep(2)
                             return addEvent()
          
                         else:
                             day = int(input("Please enter event day:"))
                             if day < 1 or day > 31:
                               print("=========================================")
                               print("Please enter correct value for Event day")
                               print("=========================================")
                               time.sleep(2)
                               return addEvent()                   
                             else:
                                 event_date = datetime.datetime(year, month, day)
                                 if event_date < now:
                                     print("==============================================")
                                     print("This module does not calculate happened event")
                                     print("==============================================")
                                     time.sleep(2)
                                     return addEvent()

                                 else:
                                     save_event()
                                     return event_recorder()
        
    
                 def save_event():
                     import sqlite3

                     with sqlite3.connect("EventCountdown.db") as db:
                         c = db.cursor()

                     c.execute("CREATE TABLE IF NOT EXISTS eventData(eventname,eventdate)")
                     db.commit()

                     insert = "INSERT INTO eventData(eventname, eventdate) VALUES (?,?)"
                     c.execute(insert,[(name),(event_date)])
                     db.commit()

    


                 def viewEvent():
                     import os
                     import pandas as pd
                     os.system("cls")
                     print("============")
                     print(" View Event")
                     print("============")
                     print("")

                     import sqlite3
                     import datetime

                     with sqlite3.connect("EventCountdown.db") as db:
                         c = db.cursor()
    
                     c.execute("CREATE VIEW IF NOT EXISTS eventData_VIEW AS SELECT eventname, eventdate FROM eventData")
                     db.commit()
                     data_pd = pd.read_sql("SELECT * FROM eventData_VIEW",db)
                     print (data_pd)

                     option = int(input("Enter 0 to Go Back:"))
                     if option == 0:
                         db.close()
                         event_recorder()
                    

                 event_recorder()

             if option == 4:
                 gc.collect()
                 return startup()

             if option == 5:
                    gc.collect()
                    sys.exit()

             if option != 1 or option != 2 or option != 3 or option != 4 or option != 5:
                 print("")
                 print("Invalid input. Please enter option with correct value (e.g. 1)")
                 time.sleep(1.5)
                 mainmenu
       
        except ValueError:
            print("")
            print("Invalid input. Please enter option in form of number (e.g. 1)")
            time.sleep(1.5)
startup = startup()
mainmenu = mainmenu()


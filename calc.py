import os, time
whereto = "0"
MainMenu = True
started = False
ProgramStarted = True
savedcalc = []
startedhistory = False
AboutStarted = False
version = 1.1
def clearscreen():
        if os.name == "nt":
             os.system("cls")
        else:
             os.system("clear")
def mainmenu():
        global ProgramStarted
        global whereto
        global MainMenu
        if ProgramStarted == True:
             clearscreen()
             ProgramStarted = False
             print("Basic Calculator {0}".format(version))
             print("1. Start Calculator")
             print("2. View History")
             print("3. Clear the Screen")
             print("4. About")
             print("5. Exit")
        whereto = input("Enter choice : ")    
        if whereto == "1":
             MainMenu = False
        elif whereto == "2":
             MainMenu = False
        elif whereto == "3":
             clearscreen()
             whereto = "0"
             print("Clearing the screen")
             time.sleep(4)
             ProgramStarted = True
        elif whereto == "4":
             MainMenu = False
        elif whereto == "5":
             exit()
        else:
             print("Invaild Entry")
             whereto = "0"
def calculator():
     global whereto
     global MainMenu
     global started
     global ProgramStarted
     if started == False:
        clearscreen()
        started = True
        print("Type m for main menu, Type c for clear the screen, Type h for history and Type e for exit")
     calc = input("Do calculation :  ")
     if calc.isalpha() or calc.isalnum():
          check = calc
          if check.lower() == 'm':
                MainMenu = True
                started = False
                ProgramStarted = True 
                clearscreen()
                whereto = "0"
          elif check.lower() == 'c':
               started = False   
          elif check.lower() == 'e':
                exit()
          elif check.lower() == 'h':
                whereto = "56"
          else:     
            print("Invaild Entry")
     else:
        try: 
            result = eval(calc)
            if isinstance(result, int) or isinstance(result, float):
                print("{0} = {1}".format(calc, result))
                entirehistory = "{0} = {1}".format(calc, result)
                savedcalc.append(entirehistory) 
            else:
                 print("Invaild entry")
        except ZeroDivisionError:
             print("Cannot divide by zero")
        except ValueError:
             print("Cannot calculate")
        except:
             print("Invaild Entry")
      
def history():
     global startedhistory
     global MainMenu
     global whereto
     global started 
     global ProgramStarted 
     if started == True : 
          started = False
     i = 0
     if startedhistory == False:
          startedhistory = True
          clearscreen()
          print("History")
          print("Type b for go back to previous page or Type c for clear the history")
          if len(savedcalc) > 0:
               for i in range(len(savedcalc)):
                    print("{0}.) {1}".format(i+1, savedcalc[i]))
          else:
               print("No history is stored")
     h = input("Command : ")
     if h.lower() == "b":
          if whereto == "2":
               startedhistory = False
               ProgramStarted = True
               MainMenu = True
               whereto = "0"
          elif whereto == "56":
               startedhistory = False   
               clearscreen()
               whereto = "1"
     elif h.lower() == "c":
          if len(savedcalc) > 0:
               print("Clearing the history")
               time.sleep(3)
               savedcalc.clear()
               print("History successfully cleared")
               time.sleep(3)
               startedhistory = False
          else:
               print("No history found so no cleaning")
     else:    
          print("Invaild entry")
def about():
     global AboutStarted 
     global MainMenu
     global started
     global whereto 
     global ProgramStarted
     if AboutStarted == False:
          clearscreen()
          AboutStarted = True
     print("Basic Calculator {0}".format(version))
     print("Written by Aniruddha Ghosh in Python")
     print("This program is open source, you are free to fork it :)")
     input("\nPress any key for go back to main menu")
     ProgramStarted = True
     AboutStarted = False
     MainMenu = True
     started = False
     clearscreen()
     whereto = "0"
while True:
    if whereto == "0" and MainMenu == True:
        mainmenu()    
    elif whereto == "1" and MainMenu == False:
        calculator()
    elif whereto == "2" and MainMenu == False:
         history()
    elif whereto == "4" and MainMenu == False:
         about()
    elif whereto == "5" and MainMenu == False:
         exit()
    elif whereto == "56" and MainMenu == False:
         history()
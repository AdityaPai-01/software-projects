from pathlib import Path
import time, os, sys

from manager.user_manager import UserManager
from manager.data_manager import JSONStorage

if getattr(sys, 'frozen', False): #Running script as .exe
    BaseDirectory = Path(sys.executable).resolve().parent
else: #Running script as a script
    BaseDirectory = Path(__file__).resolve().parent

DataDir = BaseDirectory / "data"
DataDir.mkdir(parents=True, exist_ok=True)
User_Manager = UserManager()
JSON_Storage = JSONStorage(DataDir)
User_Manager.importData(JSON_Storage.load_data())

# Clearing the terminal for cleaner UI.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "1: clear terminal executed"

def initialize():
    LoadData = JSON_Storage.load_data()
    importData = User_Manager.importData(LoadData[0])
    AuthData = User_Manager.authdata()
    if importData[1] == 1 and AuthData[1] == 1 and LoadData[1] == 1:
        return "1: Initialised user-manager class"
    else:
        return f"0: Initialisation failed.\nError-importdata: {importData[0] if importData[1] == 0 else None}\nError-authdata: {AuthData[0] if AuthData[1] == 0 else None}\nError-loaddata: {LoadData[2] if LoadData[1] == 0 else None}"
    
def login():
    Success = None
    while True:
        Username = input("Enter your username: ")
        if Username == '--q':
            Success = -1
            break
        Password = input("Enter your password: ")
        AuthData = User_Manager.authdata()
        LoginMethod = User_Manager.login(Username, Password)
        print(LoginMethod[0])
        clear()
        time.sleep(1)
        if LoginMethod[1] == 1:
            Success = 1
            break
    clear()
    if Success == 1:  
        return "1: login-method executed successfully."
    else:
        return f"-1: login-method exited by user"
   
def regiser():
    Success = None
    while True:
        Username = input("Enter username: ")
        if Username == '--q':
            Success = -1
            break
        Password = input("Enter password: ")
        User_Manager.authdata()
        RegisterMethod = User_Manager.register(Username, Password)
        print(RegisterMethod[0])
        clear()
        time.sleep(3)
        if RegisterMethod[1] == 1:
            Success = 1
            break
    if Success == 1:
        return "1: register-method executed successfully."
    else:
        return "-1: register-method exited by user."

def savedata():
    ManagerExport = User_Manager.exportData()
    if ManagerExport[1] == 1:
        StoreData = JSON_Storage.save_data(ManagerExport)
        return "1: data storage executed successfully."
    else:
        return f"0: data storage failed.\nError-managerexport: {ManagerExport[0] if ManagerExport[1] == 0 else None}\nError-storedata: {StoreData[0] if StoreData[1] == 0 else None}"
    
def Main(condition):
    Success = None
    while condition:
        Choice = input("Login or register?(L/R): ").upper()
        if Choice == "L":
            loginmethod = login()
            if loginmethod[0] == "1":
                Success = 1
                break
        elif Choice == 'R':
            registermethod = regiser()
            if registermethod[0] == "1":
                print("Please login again.")
                time.sleep(3)
                SaveData = savedata()
        elif Choice == '--Q':
            Success = -1
            break
        else:
            print("Invalid option")
            print()
    print("You exited the applications")
    print()
    if Success == 1:
        return "1: User logged in to the application"
    else:
        return "-1: User exited the application without login"
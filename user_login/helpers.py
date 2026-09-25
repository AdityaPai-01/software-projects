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
User_Manager.importData(JSON_Storage.load_data()["data"])

# Clearing the terminal for cleaner UI.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "1: clear terminal executed"

def login():
    while True:
        Username = input("Enter your username: ")
        if Username == '!Q':
            clear()
            return False
        Password = input("Enter your password: ")
        LoginMethod = User_Manager.login(Username, Password)
        print(LoginMethod["message"])
        time.sleep(1)
        clear()
        if LoginMethod["status"]:
            return True

def regiser():
    while True:
        Username = input("Enter username: ")
        if Username == '!Q':
            clear()
            return True
        Password = input("Enter password: ")
        RegisterMethod = User_Manager.register(Username, Password)
        print(RegisterMethod["message"]), time.sleep(2), print("Please login again."), time.sleep(2)
        clear()
        if RegisterMethod["status"]:
            return True

def savedata():
    ManagerExport = User_Manager.exportData()
    if ManagerExport["status"]:
        StoreData = JSON_Storage.save_data(ManagerExport)
        if StoreData["status"]:
            return "1: data storage executed successfully."
        return f"0: data storage failed.\nError-storedata: {StoreData['message']}"
    else:
        return f"0: data storage failed.\nError-managerexport: {ManagerExport['message']}"
    
def Main(condition):
    while condition:
        Choice = input("Login or register?(!L/!R): ").upper()
        if Choice == "!L":
            if login():
                break
        elif Choice == '!R':
            if regiser():
                savedata()
        elif Choice == '!Q':
            break
        else:
            print("Invalid option")
            print()
    print("You exited the applications")
    print()
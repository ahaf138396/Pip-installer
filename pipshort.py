#python3
import os
print(" Checking pip version ...  ")
os.system('python -m pip install --upgrade pip')
try:
    import time
    from datetime import datetime as dt
    import platform
except :
    print(" Your doesn\'t have software requides ! please wait while to install them")
    os.system('python -m pip install time')
    os.system('python -m pip install datetime')
    os.system('python -m pip install platform')
def main():
    print(" You are running this software in "+platform.system()+platform.release()+" version "+platform.version())
    date = dt.now()
    o = r"C:\Python Projects\pip shortcut\1.txt"
    op = open(o, "r+")
    print(op.read())
    a = input(" ...   ")
    if a != "exit" and a !="about" :
      o = r"C:\Python Projects\pip shortcut\2.txt"
      op = open(o, "r+")
      print(op.read())
      m = input(" ...   ")
      if m != "2":
         try:
             print(" Checking pip version ...  ")
             print("pip --version")
             print("     Searching Databases ...   ")
             time.sleep(2)
             os.system('python3 -m pip install ' + a)
         except :
             print(" ERR ! Installation faild !")
             print(" Exiting ... ")
             time.sleep(3)
             exit()
      elif m == "2":
          try:
              print(" Searching Database ...   ")
              time.sleep(2)
              os.system('python.exe -m pip install ' + a)
              time.sleep(1)
              print(" Good bye ! ")
              time.sleep(1)
          except :
              print(" ERR ! Installation faild !")
              print(" Exiting ... ")
              time.sleep(2)
              exit()
    elif a == "about":
        o = r"C:\Python Projects\pip shortcut\about.txt"
        op = open(o, "r+")
        print(op.read())
        time.sleep(2)
        main() 
    elif a == "exit":
        print(" Exiting ...  ")
        time.sleep(1)
        print(" Good bye ! ;) ")
        time.sleep(1)
        exit()
main()

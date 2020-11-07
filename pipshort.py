#python3
import os
import time
from datetime import datetime as dt
import platform
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
      if m == "1":
              print(" Searching Database ...   ")
              time.sleep(2)
              os.system('python3 -m pip install ' + a)
              time.sleep(1)
              print(" Exit ? (y/n) ")
              exinp1 = input(" ...  ")
              if exinp1 == "y":
                  exit()
              else :
                  main()
      elif m == "2":
              print(" Searching Database ...   ")
              time.sleep(2)
              os.system('python.exe -m pip install ' + a)
              time.sleep(1)
              print(" Exit ? (y/n) ")
              exinp1 = input(" ...  ")
              if exinp1 == "y":
                  exit()
              else :
                  main()
      elif m == "3":
          main()
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
from prettytable import os, time, random, prettytable, ALL, FRAME

# Variables

list=[]
deleted=[]

# Subroutines

def intro():
  intro="""
  ✔️ Tudu
  Your task organizer
  
  """
  print(f"{intro:^35}")

def pprint(color):
  if color=="red":
    print('\033[0;31m',sep="",end="")
  elif color=="black":
    print('\033[0;31m',sep="",end="")
  elif color=="green"
    print("\033[0;32m",sep="",end="")
  elif color=="purple":
    print("\033[0;35m",sep="",end="")

def menu():
  pprint("red")
  intro()
  pprint("black")
  print("""
  Press:
  - 'a' to add a task.
  - 'v' to view tasks.
  - 'd' to delete a task.
  - 'e' to edit a task.
  """)

def add():  
  global list
  global deleted
  print("Add task...")
  task=input("Write the task you want to add...")
  while True
    for item in list:
      x=0
      if task==item:
        print("You already have this task on the list")
        break
      else:
        itemnum=len(item)
        print(itemnum)
        list[itemnum]=task

def view():
  print("View list...")
  print(f"{list}",end='',sep='')
  time.sleep(2)
  print("Press any key to go back to main menu or exit to close the app")
  keypress=input("...")
  if keypress=="exit"
    exit()
  else:
    menu()

def edit():
  intro()
  print("Edit an item...")
  # code

def remove():
  # code

  
# Execution

while True:
  
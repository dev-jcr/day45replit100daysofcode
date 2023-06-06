from prettytable import prettytable, ALL, FRAME
import os, time, random

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
  elif color=="green":
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
  action=input().lower()
  if action=='a':
    add()
  elif action=='v':
    view()
  elif action=='d':
    delete()
  elif action=='e':
    edit()
  else:
    print("That's not an option")
    
def add():
  intro()
  global list
  global deleted
  print("Add task...")
  task=input("Write the task you want to add...\n")
  for item in list:
    x=0
    if task==item:
      print("You already have this task on the list")
      break
    else:
      itemnum=len(item)
      print(itemnum)
      list[itemnum]=task
      print("Task succesfully added!")
  time.sleep(1)
  os.system("clear")
  menu()

def view():
  intro()
  print("View list...")
  print(f"{list}",end='',sep='')
  time.sleep(2)
  print("Press any key to go back to main menu or exit to close the app")
  keypress=input("...")
  if keypress=="exit":
    exit()
  else:
    menu()

def edit():
  intro()
  print("Edit an item...")
  x=1
  for item in list:
    x+=1
    print(f"{x}{item}")
  edit=input("Input the number of the item you want to delete...\n")

def remove():
  intro()
  print("Remove an item...")
  x=1
  for item in list:
    x+=1
    print(f"{x}{item}")
  delete=input("Input the number of the item you want to delete...\n")
  deleted[delete]=list[delete]
  list[delete]=""

# Execution

while True:
  menu()
  
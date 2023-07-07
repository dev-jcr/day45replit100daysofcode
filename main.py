# To-do list
from prettytable import prettytable, ALL, FRAME
import os, time, random

# Variables

todo=[]
# list=[]
deleted=[]
itemcount=0
deletedcount=0
y=0
# Subroutines

def c(color):
  if color=="red":
    return("\033[31m")
  elif color=="white":
    return("\033[0m")
  elif color=="blue":
    return("\033[34m")
  elif color=="yellow":
    return("\033[33m")
  elif color=="green":
    return("\033[32m")
  elif color=="purple":
    return("\033[35m")

def prettyPrint():
  print("")

#1add
def add():
  global list
  global deleted
  global itemcount
  global y
  # firststart=len(list)
  os.system('clear')
  print(title)
  print("Add task...")
  print()
  name=input('Name: ')
  date=input('Due date: ')
  priority=input('Priority: ').capitalize()
  id=y+1
  row=[name, date, priority, id]
  todo.append(row)
  print('Added!')
  # task=input("Write the task you want to add...\n\n")
  # for item in list:
  #   if item==task:
  #     print("You already had this task on the list")
  #     break
  # if firststart==1:
  #   list.insert(0, task)
  # else:
  #   list.append(task)
  itemcount+=1
  # print()
  # print(f"Task:\n\n {task}\n\nwas succesfully added!")
  time.sleep(1)
  os.system("clear")

#2view
def view():
  print()
  print("View list...")
  options=input("1. All\n2. By priority\n> ")
  if options=='1':
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  print()
  # x=1
  # for item in list:
  #   print(f"{x}. {item}")
  #   x+=1
  #   print()
  # time.sleep(2)
  print("Press any key to go back to main menu or exit to close the app")
  print()
  keypress=input("...")
  if keypress=="exit":
    exit()
  else:
    os.system("clear")

#3edit
def edit():
  # global list
  print(title)
  print("Edit an item...")
  findoption=int(input('How do you want to choose the task? \n\n1. By task number\n\n2. By task name\n\n'))
  if findoption==1:
    x=0
    for row in todo:
      if item in row:
        x+=1
        print(f"{x}. {item}")
        print()
    print()
    edit=int(input("Input the number of the item you want to edit...\n"))
    print()
    print(f"The item you are going to edit is:\n\n {todo[edit-1]}.\n\n Write the new entry here:\n ")
    print()
    name = input("Name > ")
    date = input("Due Date > ")
    priority = input("Priority > ").capitalize()
    id=y+1
    row = [name, date, priority, id]
    todo.append(row)
    print("Added")
    # editTask=input()
    # list[x-1]=editTask
  else:
    find=input('Name of todo to edit > ')
    found=False
    for row in todo:
      if find in row:
        found=True
      if not found:
        print("Couldn't find that")
        return
      for row in todo:
        if find in row:
          todo.remove(row)
      name=input("Name > ")
      date=input("Due Date > ")
      priority=input("Priority > ").capitalize()
      id=y+1
      row=[name, date, priority, id]
      todo.append(row)
      print("Added")
    print()


#4remove
def remove():
  print(title)
  print("Remove an item...")
  print()
  findoption=int(input('How do you want to choose the task? \n\n1. By task number\n\n2. By task name\n\n'))
  if findoption==1:
    x=0
    for row in todo:
        print(f"{x}. {row[x]}")
        x+=1    
        print()
    print()
    find=int(input("Input the number of the item you want to delete...\n"))
    print()
    find=input('Number of the todo to edit > ')
    found=False
    for row in todo:
      if find in row:
        found=True
      if not found:
        print("Couldn't find that")
        return
      for row in todo:
        if find in row:
          print(f"The item you removed is:\n\n {row}.\n\n ")
          todo.remove(row)      
    print()
    todo.remove()
    # editTask=input()
    # list[x-1]=editTask
  else:
    find=input('Name of todo to edit > ')
    found=False
    for row in todo:
      if find in row:
        found=True
      if not found:
        print("Couldn't find that")
        return
      for row in todo:
        if find in row:
          todo.remove(row)      
    print()
  # x=0
  # for item in list:
  #   x+=1
  #   print(f"{x}. {item}")
  # print()
  # remove=int(input("Input the number of the item you want to delete...\n"))
  # remove-=1
  # print(f"The task you have selected to delete is:\n\n{list[remove]}\n\nInput 'd' to confirm you want to delete it...\n\n")
  deleted.insert(deletedcount, todo[remove])
  print(f"The task number {remove+1} has been deleted and added to removed list. Check recovery list to recover removed items.")
  # list.remove(remove)
  del todo[remove]

#5recovery
def recovery():
  print(title)
  print('The following are the tasks you have removed:')
  x=0
  for item in deleted:
    x+=1
    print(f"{x}. {item}")
  print()
  print("Press any key to go back to main menu or exit to close the app")
  print()
  keypress=input("...")
  if keypress=="exit":
    exit()
  else:
    os.system("clear")
#6execution 
while True:
  title=f"""{c('purple'):^20}  ✔️   Tudu  ✔️
  """
  print(f"{title}")
  menu=f"""{c('green'):^5}Press:
  - 'a' to add.
  - 'v' to view.
  - 'd' to delete.
  - 'e' to edit.
  - 'r' to recover deleted.
  - 'reset' to nuke the list ⚠️

  Or press 'x' to exit...\n
  """
  print(menu)
  action=input().lower()
  if action=='x':
    exit()
  if action=='a':
    add()
    continue
  elif action=='v':
    view()
    continue
  elif action=='d':
    remove()
    continue
  elif action=='e':
    edit()
    continue
  elif action=='r':
    recovery()
    continue
  else:
    print("That's not an option!")
    continue
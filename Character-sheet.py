"""Exercise:Character Sheet 2.0
Now with your attributes.
The app can record you Name, Job and Level.
Then will record your, Strenght, Dexterity, Costitution,Intelligence, Wisdom and Charisma
Finally it will show you the data, MUST USE functions and avoid to use global Variables.

Needs a loop
Terminate if in any step the user types 'exit'
    Ask the Name
        Save the name
    Ask the Job
        Save the Job
    Ask the Level
        Save the level
    Ask the Str
        Save the str
    Ask the Dex
        Save the dex
    Ask the Cons
        Save the cons
    Ask the Int
        Save the Int
    Ask the Wis
        Save the Wis
    Ask the Char
        Save the Char
"""
print("Character sheet 2.0 - Now on python")
print("Type 'exit' in any moment to close the program")


def start():
    execute = True
    while execute:
            name = input("what is the name?: ")
            if name== 'exit':
                  print('clossing the app')
                  return
            job = input("what is the job?: ")
            if job == 'exit':
                  print('clossing the app')
                  return
            lvl = input("what is the level?: ")
            if lvl == 'exit':
                  print('clossing the app')
                  return
            stre = input("what is the str?: ")
            if stre == 'exit':
                  print('clossing the app')
                  return
            dex = input("what is the dex?: ")
            if dex == 'exit':
                  print('clossing the app')
                  return
            con = input("what is the con?: ")
            if con == 'exit':
                  print('clossing the app')
                  return
            inte = input("what is the int?: ")
            if inte == 'exit':
                  print('clossing the app')
                  return
            wis = input("what is the wis?: ")
            if wis == 'exit':
                  print('clossing the app')
                  return
            char = input("what is the char?: ")
            if char == 'exit':
                  print('clossing the app')
                  return
            print(f'''CHARACTER SHEET
                    Name:{name} Class:{job} Level:{lvl}
                    =====================================       
                    Str:{stre}           
                    Dex:{dex}           
                    Con:{con}           
                    Int:{inte}           
                    Wis:{wis}           
                    Char:{char}           
                    ''')
            execute=False

start()
print("""************************************************
        Created by: Sergio.aaguilera@gmail.com
        October 2025.""")

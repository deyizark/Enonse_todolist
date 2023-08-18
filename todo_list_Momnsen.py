todo_list = []

def add_task(tp):
    todo_list.append(tp)

def display_task():
    for i in range(len(todo_list)):
        print(i + 1,"-", todo_list[i])

def mark_task_done(nb):
    try:
        todo_list.pop(nb - 1)
    except:
        print("Nonb enkorek, eseye anko : ")

def save_tasks():
    save = open("tasks.txt", "w")
    for i in todo_list:
        save.write(i + "\n")
    save.close()

def load_tasks():
    fichye = None
    try:
        non_file = input("Antre non fichye a ak tout ekstansyon l 'fichye.txt' : ")
        task = open(non_file, "r")
    except:
        print("Fichye sa pa egziste")
    for b in task:
        todo_list.append(b)
    print("\n")
    task.close()

asd = True

while asd :
    print("        Meni")
    print("1. Ajoute tach") 
    print("2. Afiche tach yo")
    print("3. Fini yon tach") 
    print("4. Anrejistre epi fèmen")
    
    choix = int(input("Ki opsyon w chwazi :"))
    while choix > 4 or choix < 1 :
        choix = int(input("Ki opsyon w chwazi :"))    
    if choix == 1:
        antre = input("Tape gran \"T\" pou w tape tach ou yo oubyen gran \"L\" pour televèse yon fichye tèks ki gen tach yo: ")
        while not (antre == "T" or antre == "L"):
            antre = input("Tape \'T\' pou w tape tach ou yo oubyen \'L\' pour televèse yon fichye tèks ki gen tach yo: ")
        if antre == "T":
            tpp = input("Ekri task la: ")
            add_task(tpp)
        else:
            load_tasks()
        #add_task()
    elif choix == 2:
        display_task()
    elif choix == 3:
        n_tach = input("Ki nimewo task ou fini an: ")
        while not n_tach.isdigit():
            n_tach = int(input("Ki nimewo task ou fini an: "))
        mark_task_done(n_tach)
        #mark_task_done()
    elif choix == 4:
        save_tasks()
        print("Bye...")
        break

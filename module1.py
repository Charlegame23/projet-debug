import csv

#DEF

def Conard():
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("------------Choisissez votre categorie-----------")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("1--Breakfast-------------------------------------")
    print("-------------------------------------------------")
    print("2--Beef & Pork-----------------------------------")
    print("-------------------------------------------------")
    print("3--Chicken & Fish--------------------------------")
    print("-------------------------------------------------")
    print("4--Salads----------------------------------------") 
    print("-------------------------------------------------")
    print("5--Snacks & Sides--------------------------------")
    print("-------------------------------------------------")
    print("6--Desserts--------------------------------------")
    print("-------------------------------------------------")
    print("7--Beverages-------------------------------------")
    print("-------------------------------------------------")
    print("8--Coffee & Tea----------------------------------")
    print("-------------------------------------------------")
    print("9--Smoothies & Shakes----------------------------")
    print("-------------------------------------------------")
    print("10-ALL-------------------------------------------")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    c = input("Choisissez votre categorie: ")
    return c

def Breakfast():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(1):
            next(csv_reader)
        
        for i, row in enumerate(csv_reader, start=2):
            if i > 43:
                break
            print(row)
def BeefPork():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(43):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=44):
            if i > 58:
                break
            print(row)
def ChickenFish():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(58):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=59):
            if i > 85:
                break
            print(row)
def Salads():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(85):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=86):
            if i > 91:
                break
            print(row)
def SnacksSides():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(91):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=92):
            if i > 104:
                break
            print(row)
def Desserts():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(104):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=105):
            if i > 111:
                break
            print(row)
def Beverages():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(111):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=112):
            if i > 261:
                break
            print(row)
def All():
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
        csv_reader = csv.reader(f)
        for r in range(1):
            next(csv_reader)
       
        for i, row in enumerate(csv_reader, start=2):
            if i > 261:
                break
            print(row)



#debug

X = 0
with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r') as f:
    r = csv.reader(f)
    for row in r:
        if X == 1:
            print(row)

#variables

c = Conard()

#main

if c == "1":
    print(Breakfast())
elif c =="2":
    print(BeefPork())
elif c == "3":
    print(ChickenFish())
elif c == "4":
    print(Salads())
elif c == "5":
    print(SnacksSides())
elif c == "6":
    print(Desserts())
elif c == "7":
    print(Beverages())
elif c == "10":
    print(All())



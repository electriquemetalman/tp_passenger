#1-cree des bus
import copy

bus = {
    "id" : 0,
    "nombreDePlace" : 0,
    "passager_bus" : []
}

passenger = {
    "id_passenger" : 0,
    "name" : "<element>",
    "poidBagage" : 0
}

exitApp = "no"
id_bus = 1
id_pass = 1
tBus = []
allBus = []
tPassenger = []
allPassenger = []
tBus = copy.deepcopy(bus)
tPassenger = copy.deepcopy(passenger)
while exitApp == "no":
    print("*******Bonjour bien venu chez TKSB Voyage********* ")
    print("1-cree un bus")
    print("2-cree un passager")
    print("3-ajouter un passager a un bus")
    create = int(input("que vouler vous faire: "))
    if create == 1:
        tBus = copy.deepcopy(bus)
        tBus["id"] = id_bus
        tBus["nombreDePlace"] = int(input("entrer le nombre de place du bus: "))
        id_bus = id_bus + 1
        allBus.append(tBus)
        print(allBus)
        create_bus = str(input("vouler vous cree un autre buss:yes/no: "))
        while create_bus == "yes":
            tBus = copy.deepcopy(bus)
            tBus["id"] = id_bus
            tBus["nombreDePlace"] = int(input("entrer le nombre de place du bus: "))
            id_bus = id_bus + 1
            allBus.append(tBus)
            print(allBus)
            create_bus = str(input("vouler vous cree un autre buss:yes/no: "))
        if  create_bus == "no":
            print("*******Bonjour bien venu chez TKSB Voyage********* ")
            print("1-cree un bus")
            print("2-cree un passager")
            print("3-ajouter un passager a un bus")
            create = int(input("que vouler vous faire: "))
    elif  create == 2:
        tPassenger = copy.deepcopy(passenger)
        tPassenger["id_passenger"] = id_pass
        tPassenger["name"] = str(input("entrer le nom du passager: "))
        tPassenger["poidBagage"] = int(input("entrer le poid des bagage passager: "))
        id_pass = id_pass + 1
        allPassenger.append(tPassenger)
        print(allPassenger)
        create_passenger = str(input("vouler vous cree un autre passager:yes/no: "))
        while create_passenger == "yes":
            tPassenger = copy.deepcopy(passenger)
            tPassenger["id_passenger"] = id_pass
            tPassenger["name"] = str(input("entrer le nom du passager: "))
            tPassenger["poidBagage"] = int(input("entrer le poid des bagage passager: "))
            id_pass = id_pass + 1
            allPassenger.append(tPassenger)
            print(allPassenger)
            create_passenger = str(input("vouler vous cree un autre passager:yes/no: "))
        if create_passenger == "no":
            print("*******Bonjour bien venu chez TKSB Voyage********* ")
            print("1-cree un bus")
            print("2-cree un passager")
            print("3-ajouter un passager a un bus")
            create = int(input("que vouler vous faire: "))
    elif  create == 3:
        print("voici la liste des bus disponible")
        print(allBus)
        print(allPassenger)   
        busChoice = int(input("choisir un bus pour un passager:(juste id du bus) ")) 
        passengerChoice = int(input("choisir le passager pour le bus que vous aver selectionner:(juste id) ")) 
        allBus[busChoice] ["passager_bus"] = passengerChoice
        print(allBus)

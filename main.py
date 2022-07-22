#1-cree des bus
import copy

bus = {
    "id" : 0,
    "nombreDePlace" : 0,
    "place_oq": 0,
    "kg" : 700,
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
    print("4-nombre de place disponible dans un buss")
    print("5-nombre de kg reserver pour un buss")
    print("6-retirer un passager d'un bus")
    print("7-savoir si un bus peut accueillir les passagers provenant d'un autre bus")
    print("8-afficher la liste des passagers d'un bus dans la console")
    print("9-afficher l'ensemble des passagers de ma flotte de bus dans la console")
    print("10-savoir si un passager est enregistré sur un bus de ma flotte")
    create = int(input("que vouler vous faire: "))
    if create == 1:
        tBus = copy.deepcopy(bus)
        tBus["id"] = id_bus
        tBus["nombreDePlace"] = int(input("entrer le nombre de place du bus: "))
        tBus["place_oq"] = int(input("entrer le nombre de place ocuper: "))
        id_bus = id_bus + 1
        allBus.append(tBus)
        print(allBus)
        create_bus = str(input("vouler vous cree un autre buss:yes/no: "))
        while create_bus == "yes":
            tBus = copy.deepcopy(bus)
            tBus["id"] = id_bus
            tBus["nombreDePlace"] = int(input("entrer le nombre de place du bus: "))
            tBus["place_oq"] = int(input("entrer le nombre de place ocuper: "))
            id_bus = id_bus + 1
            allBus.append(tBus)
            print(allBus)
            create_bus = str(input("vouler vous cree un autre buss:yes/no: "))
        if  create_bus == "no":
            print("*******Vous pouver effectuer d'autre operation********* ")
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
            print("*******Vous pouver effectuer d'autre operation*********")
    elif  create == 3:
        print("voici la liste des bus disponible")
        print(f"liste des bus {allBus}")
        print(f"liste des passager {allPassenger}")   
        busChoice = int(input("choisir un bus pour un passager:(juste id du bus) ")) 
        passengerChoice = int(input("choisir le passager pour le bus que vous aver selectionner:(juste id) ")) 
        for id in allBus:
            if id['id'] == busChoice:
                for passager in id['passager_bus']:
                    passager[0] = passengerChoice
        print(allBus)            
    elif  create == 4:
        pd = 0
        po = 0
        pr = 0
        busId = int(input("choisir le bus:(juste id du bus) "))
        for bus in allBus:
            if bus['id'] == busId:
                pd=bus['nombreDePlace']
                po=bus['place_oq']
                pr= pd - po
        print(f"nombre de place disponible {pr}") 
    elif  create == 5: 
        kg = 0          
        busId = int(input("choisir le bus:(juste id du bus) "))
        for bus in allBus:
            if bus['id'] == busId:
                kg = bus['kg']
        print(f"le nombre de kg pour un bus est de {kg}")
    elif  create == 6:
        print("bn")              

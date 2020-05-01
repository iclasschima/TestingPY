def checkDrugNameValidityAndPrice(drugName):
    drugPrice = {
        "paracetamol": 250,
        "panadol": 300,
        "armerten": 700,
        "coflin": 400,
        "postino": 1200
    }

    while not drugName.lower() in drugPrice:
        drugName = input("Incorrect drug name entered! Please enter drug name (e.g paracetamol): ")
        checkDrugNameValidityAndPrice(drugName)

    drugInfo = {
        "drugName": drugName,
        "drugPrice": drugPrice[drugName.lower()]
    }
    return drugInfo


def checkQuantityForStringValue():
    try:
        drugQuantity = int(input("Now please enter drug quantity (per packet e.g 3): "))
    except ValueError:
        while ValueError:
            try:
                drugQuantity = int(input("Please enter a number instead! Enter drug quantity (per packet e.g 3): "))
            except ValueError:
                    continue
            break
        not ValueError
    return drugQuantity


def checkQuantityForZeroValue(drugQuantity):
    while drugQuantity <= 0:
        try:
            drugQuantity = int(input("Can't take a zero value! Enter drug quantity (per packet e.g 3): "))
        except ValueError:
            drugQuantity = checkQuantityForStringValue()
            checkQuantityForZeroValue(drugQuantity)
    return drugQuantity      


def setData(drugName, drugPrice, drugQuantity):
    data = {
        "drugName": drugName,
        "drugPrice": drugPrice,
        "drugQuantity": drugQuantity
    }

    return data


def collectData(drugName):

    drugInfo = checkDrugNameValidityAndPrice(drugName)        
    drugName = drugInfo["drugName"]
    drugPrice = drugInfo["drugPrice"]

    print(f"The price for the {drugName} entered (per packet) is: {drugPrice}")

    drugQuantity = checkQuantityForStringValue()
    
    filteredDrugQuantity = checkQuantityForZeroValue(drugQuantity)
 
    totalDrugPrice = drugPrice * filteredDrugQuantity

    data = setData(drugName,totalDrugPrice,drugQuantity)

    return data

def checkForQuitCommand(drugName):
    if drugName.lower() == "quit":
        return True

def checkForShowCommand(drugName, className):
    if drugName.lower() == "show":
        message = ""
        for elm in className.getAllCart():
            message += f"""
            Drugname : {elm["drugName"]}
            Quantity: {elm["drugQuantity"]}
            Drug price: {elm["drugPrice"]}
            """ 
        print("Cart contents \n" + message)

        return True

def checkForClearCommand(drugName, className):
    if drugName.lower() == "clear":
        if className.clearCart():
            if not className.getAllCart():
                print("Cart have been cleared")
            return True
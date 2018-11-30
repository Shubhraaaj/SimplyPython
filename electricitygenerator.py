from app_electricity.Room import Room

print('Welcome to Smart Electric!\nPlease choose one of the options below:-')
selectedOption = input('1. Electricity Bill Predictor\n2. Smart Electricity Optimiser\n')
# print('Selected Option:' + selectedOption)

roomCount = {}

def checkResult():
    finalBill = 0
    for key in roomCount.keys():
        amount = roomCount[key].electricity_consumption()
        finalBill += amount
        print('Total Bill from ' + key + " = Rs." + str(amount))
    print('Final Bill: Rs.' + str(finalBill))
    pass

def billPredictor():
    rooms = int(input('Great! Welcome to Electricity Bill Predictor!'
                  '\nPlease Enter the number of Rooms in your House: '))
    for i in range(rooms):
        roomName = input('Enter room name: ')
        numOfAppliances = int(input('Enter number of appliances: '))
        applianceDetails = {}
        applianceQuantity = {}
        applianceHours = {}
        for j in range(numOfAppliances):
            nameOfAppliance = input('Enter name of Appliance: ')
            applianceDetails[nameOfAppliance] = float(input('Enter rating of Appliance kW/Hr: '))
            applianceQuantity[nameOfAppliance] = int(input('Enter quantity of this Appliance: '))
            applianceHours[nameOfAppliance] = float(input('Enter Hours of Appliance usage in a Day: '))
            roomCount[roomName] = Room(roomName, numOfAppliances, applianceDetails, applianceQuantity, applianceHours)
    checkResult()
    pass

if selectedOption is '1':
    billPredictor()
elif selectedOption is '2':
    print('Great! Welcome to Smart Electricity Optimiser!')
else:
    print('Sorry! Wrong option selected. Exiting Program...')



class Room(object):
    roomCount = 0
    roomName = "Unnamed room"
    numOfAppliances = 0
    applianceName = {}
    applianceQuantity = {}
    applianceHours = {}
    totalBill = 0.0
    RATE = 10

    def __init__(self, roomName, numOfAppliances, applianceName, applianceQuantity, applianceHours):
        self.roomName = roomName
        self.numOfAppliances = numOfAppliances
        self.applianceName = applianceName
        self.applianceQuantity = applianceQuantity
        self.applianceHours = applianceHours
        self.roomCount += 1

    def electricity_consumption(self):
        for key in self.applianceName.keys():
            self.totalBill += self.applianceName[key] * self.applianceQuantity[key] * self.applianceHours[key] * self.RATE
        return self.totalBill

def make_room(roomName, numOfAppliances):
    newRoom = Room(roomName, numOfAppliances)
    return newRoom
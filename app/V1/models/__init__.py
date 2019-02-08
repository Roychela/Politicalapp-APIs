alloffices = []
allparties = []

class PoliticalOfficeModel():
    def __init__(self, name, type, id):
        self.name = name
        self.type = type
        self.id = id
        
    @staticmethod
    def view_all_offices():
        return alloffices 

    def saveoffice(self):
        politicaloffice = {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            } 
        alloffices.append(politicaloffice)  
    
    @staticmethod
    def get_specific_office(id):
        return [office for office in alloffices if office["id"] == id]


class PoliticalPartiesModel():
    def __init__(self, name, id, hqAddress, logoUrl):
        self.name = name
        self.id = id
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    @staticmethod
    def view_all_parties():
        return allparties
      
    
    def saveparty(self):
        politicalparty = {
            "id": self.id,
            "name": self.name,
            "hqAddress": self.hqAddress,
            "logoUrl": self.logoUrl
            } 
        allparties.append(politicalparty) 

    @staticmethod
    def get_specific_party(id):
        return [party for party in allparties if party["id"] == id]    
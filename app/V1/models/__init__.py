alloffices = []

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
    
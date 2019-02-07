alloffices = []

class PoliticalOfficeModel():
    def __init__(self, name, type, id):
        self.name = name
        self.type = type
        self.id = id
        
    @staticmethod
    def view_all_offices():
        return alloffices 
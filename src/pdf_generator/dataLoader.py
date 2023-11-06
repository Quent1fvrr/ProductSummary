import json

class dataLoader:
    def __init__(self, filepath):
        self.data = self.load_data(filepath)
    
    @staticmethod
    def load_data(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)

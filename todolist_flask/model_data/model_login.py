import json

class ModelLoginData():
    def __init__(self):
        self.path = 'model_data/login_data.json'
        self.data = self.load_item()

    def load_item(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_item(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent= 2)

    def add_item(self, username, password, email):
        self.data.update({username : {'password': password, 'Email': email}})
        self.save_item()

    def get_item(self, key):
        return self.data.get(key, '')
    
    def get_all_item(self):
        return self.data
    
    def delete_item(self, key):
        if key in self.data:
            del self.data[key]
            self.save_item()
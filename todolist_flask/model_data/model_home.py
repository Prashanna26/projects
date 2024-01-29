import json
from flask import session

class ModelHomeData():
    def __init__(self):
        self.path = 'model_data/home_data.json'
        self.data = self.load_item()

    def load_item(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def greatestid(self):
        max_id = -1
        for name in self.data.values():
            for task in name:
                max_id = max(max_id, task.get('id', -1))
        return max_id+1
    
    def save_item(self):
        with open(self.path, 'w') as file:
            json.dump(self.data, file, indent=2)
            file.write('\n')

    def add_item(self, message, date_time ,priority, status, p_date):
        username = session['username']
        task_id = self.greatestid()
        message_info={'id':task_id,'message': message, 'datatime': date_time, 'priority':priority, 'status':status, 'present_date': p_date}
        if username in self.data:
            self.data[username].append(message_info)
            self.data[username].sort(key=lambda x: x['priority'], reverse=True)
        else:
            self.data[username] = [message_info]
        self.save_item()

    def get_item(self, key, task_id):
        username = session['username']
        for task in self.data.get(username, []):
            if task['id'] == task_id:
                return task.get(key, '')
        return None
    
    def get_all_item(self):
        username = session['username']
        for _ in self.data:
            if username in self.data:
                return self.data[username]
    
    def delete_item(self, key):
        username = session['username']
        user_data = self.data[username]
        i=0
        for item in user_data:
            if item.get('id') == key:
                self.data[username].remove(item)
                break 
        self.save_item()

    def update_message(self, task_id, key, new_message):
        username = session['username']
        for task in self.data.get(username, []):
            if task['id'] == task_id:
                task[key] = new_message
                return True
        return False
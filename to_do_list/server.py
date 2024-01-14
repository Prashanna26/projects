import http.server
import socketserver
import json
task = []

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/button-clicked':
            content_len = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_len).decode("utf-8")
            data = json.loads(post_data)
            text_area = data.get('message', '')
            status_msg = data.get('status', '')
            date_time = data.get('date','')
            priority = int(data.get('priority',''))
            c_unformated_date = data.get('created_date','')
            create_date = (", ").join(c_unformated_date.split('T'))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.get_html_element(text_area, status_msg, date_time, priority, create_date)

        elif self.path == '/delete-button':
            content_l = int(self.headers['Content-Length'])
            body_msg = self.rfile.read(content_l).decode("utf-8")
            body_data = json.loads(body_msg)
            button_index= int(body_data.get('message', ''))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.del_file(button_index)

        elif self.path == '/complete-button':
            cont_l = int(self.headers['Content-Length'])
            status_msg = self.rfile.read(cont_l).decode("utf-8")
            status_data = json.loads(status_msg)
            status_index = int(status_data.get('message', ''))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.com_file(status_index)

        elif self.path == '/edit-button':
            edit_cont_l = int(self.headers['Content-Length'])
            edit_msg = self.rfile.read(edit_cont_l).decode("utf-8")
            edit_data = json.loads(edit_msg)
            edit_id= int(edit_data.get('message', ''))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.edit_file(edit_id)
            

        else:
            return http.server.SimpleHTTPRequestHandler.do_POST(self)

    def do_GET(self):
        if self.path == '/button-clicked':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.send_to_html()
                          
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)                 

    def get_html_element(self, data, status, date, priority, create_date):
            task.append({'task': data , 'status': status, 'date_time':date, 'priority':priority, 'createDate':create_date})
            task.sort(key = lambda x:x['priority'] , reverse=True)

    def send_to_html(self):       
        for index, tsk in enumerate(task):
            state_sts = ""
            if tsk['status']==1:
                state_sts = "check"
            elif tsk['priority']==1:
                state_sts = "prio_yes"
            
            dttm = (", ").join(tsk['date_time'].split('T'))

            html_content = f'<div class="container {state_sts}">{tsk['task']}\
                <span class="date_cont">Task is to be completed within: {dttm}</span>\
                <span class="create_date">Created in:<br>{tsk['createDate']}</span>\
                <button class="edit_button" data-edit-id="{index}"><i class="fa fa-pencil" aria-hidden="true"></i></button>\
                <button class="com_button" data-status-id="{index}"><i class="fa fa-check" aria-hidden="true"></i></button>\
                <button class="del_button" data-delete-id="{index}"><i class="fa fa-trash" aria-hidden="true"></i></button>\
                </div><br><br>'
            self.wfile.write(html_content.encode())

    def del_file(self,index):
        removed_item = task.pop(index)
        print(f"Item at index {index} ({removed_item}) removed. Updated list:", task)

    def com_file(self,status_index):
        if task[status_index]['status'] == 0:
            task[status_index]['status'] = 1
            print(f"Status of {status_index} was changed to 1")

        elif task[status_index]['status'] == 1:
            task[status_index]['status'] = 0
            print(f"Status of {status_index} was changed to 0")

    def edit_file(self,edit_id):
        task_id = task[edit_id]
        message_value = task_id['task']
        date_value = task_id['date_time']
        priority_value = task_id['priority']
        content = f'{message_value}; {date_value};  {priority_value}'
        self.wfile.write(content.encode())
        self.del_file(edit_id)
        
# Set the port number
port = 8009

# Use the custom handler with the server
handler = MyHttpRequestHandler

# Create the server
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on http://localhost:{port}")

# Start the server
httpd.serve_forever()
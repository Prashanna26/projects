from jinja2 import Environment, FileSystemLoader
from model import Model_data
import os

def render_template(template_name, content):
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_name)
    return template.render(content).encode('utf-8')

def home():
    return render_template('index.html',{'message':'Welcome to our page'})

def aboutus():
    context = {'message':'Welcome to About us'}
    return render_template('aboutus.html',context)

def submitform():
    values = Model_data()
    name = values.get_item("name")
    dob = values.get_item("DOB")
    date = (', ').join(dob.split('T'))
    address = values.get_item("address")
    context = {'message':'Welcome to Our Page', 'name': name, 'DOB': date, 'address': address}
    return render_template('submit.html',context)
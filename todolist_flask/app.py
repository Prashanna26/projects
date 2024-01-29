from flask import Flask
from route.route import blueprint

app = Flask(__name__)

app.secret_key = 'Ok-Fine'

app.register_blueprint(blueprint, url_prefix='/')
    
if __name__=='__main__':
    app.run(debug= True)
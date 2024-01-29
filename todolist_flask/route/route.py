from flask import Blueprint
from controller.controller import login, signup, home, button_clicked, delete_button, complete_button, edit_button

blueprint = Blueprint('blueprint',__name__)

blueprint.route('/', methods=['POST','GET'])(login)
blueprint.route('/signup', methods=['POST','GET'])(signup)
blueprint.route('/home', methods=['POST','GET'])(home)
blueprint.route('/button-clicked', methods=['GET', 'POST'])(button_clicked)
blueprint.route('/delete-button/<int:task_id>', methods=['GET', 'POST'])(delete_button)
blueprint.route('/complete-button/<int:task_id>', methods=['GET', 'POST'])(complete_button)
blueprint.route('/edit-button/<int:task_id>', methods=['GET', 'POST'])(edit_button)


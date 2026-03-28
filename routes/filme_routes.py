from flask import Blueprint, request  
from controllers.filme_controllers import get_filmes, create_filme, get_filme_by_id

# Define um Blueprint para as rotas de "Filme"
filme_routes = Blueprint('filme_routes', __name__)  

# Rota para listar todos os filmes (GET)
@filme_routes.route('/Filme', methods=['GET'])
def filmes_get():
    return get_filmes()

# Rota para criar um novo filme (POST)
@filme_routes.route('/Filme', methods=['POST'])
def filmes_post():
    return create_filme(request.json)

@filme_routes.route('/Filme/<int:id>', methods=['GET'])
def filme_get_id(id):
    return get_filme_by_id(id)

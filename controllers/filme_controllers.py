from models.filme_models import Filme  
from db import db  
import json
from flask import make_response, request


def get_filmes():
    filmes = Filme.query.all()  
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes.',
            'dados': [filme.json() for filme in filmes]  
        }, ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'  
    return response


def get_filme_by_id(filme_id):
    filme = Filme.query.get(filme_id)  

    if filme:  
        response = make_response(
            json.dumps({
                'mensagem': 'Filme encontrado.',
                'dados': filme.json()  
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    else:
        
        response = make_response(
            json.dumps({'mensagem': 'Filme não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response


def create_filme(filme_data):
   
    if not all(key in filme_data for key in ['titulo', 'genero', 'duracao','ano_lancamento','diretor']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, duracao, ano_lancamento e diretor são obrigatórios.'}, ensure_ascii=False),
            400  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    
    
    novo_filme = Filme(
        
        titulo=filme_data['titulo'],
        genero=filme_data['genero'],
        duracao=filme_data['duracao'],
        ano_lancamento=filme_data['ano_lancamento'],
        diretor=filme_data['diretor'],
    )
    
    db.session.add(novo_filme)  
    db.session.commit()  

   
    response = make_response(
        json.dumps({
            'mensagem': 'Filme cadastrado com sucesso.',
            'filme': novo_filme.json()  
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  
    return response



import os
from app import app

def procurar_capa(id):
    for capa_nome in os.listdir(app.config['UPLOAD_PATH']):
        if  f'capa{id}' in capa_nome:
            return capa_nome
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = procurar_capa(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
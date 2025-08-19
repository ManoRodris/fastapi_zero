from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.get('/')
# def read_root():
#     return {'message': 'Olá Mundo'}

@app.get('/', response_class=HTMLResponse)
def ola_mundo():
    return '''
    <html>
    <head>
        <title>Olá Mundo</title>
        <h1>Olá Mundo</h1>
    </head>
    </html>'''

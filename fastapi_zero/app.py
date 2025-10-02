from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_zero.schemas import (
    UserSchema, UserPublic, UserDB
)
from http import HTTPStatus
app = FastAPI()

database = []


# @app.get('/')
# def read_root():
#     return {'message': 'Olá Mundo'}

# @app.get('/', response_class=HTMLResponse)
# def ola_mundo():
#     return '''
#     <html>
#     <head>
#         <title>Olá Mundo</title>
#         <h1>Olá Mundo</h1>
#     </head>
#     </html>'''

@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def creating_user(user : UserSchema):
    user_with_id = UserDB (
        id = len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id

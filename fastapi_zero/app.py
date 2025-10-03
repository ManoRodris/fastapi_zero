from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/', response_class=HTMLResponse)
def ola_mundo():
    return '''
    <html>
    <head>
        <title>Olá Mundo</title>
        <h1>Olá Mundo</h1>
    </head>
    </html>'''


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def creating_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/user/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/user/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(
        **user.model_dump(),
        id=user_id
    )
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/user/{user_id}', response_model=Message)
def delete_user(user_id : int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from database import(get_connection, create_table)

app = FastAPI()

create_table()

class UserCreate(BaseModel):
    username: str
    email: str

@app.get('/users')
def get_user():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    connection.close()
    return [{'id':u[0], 'username':u[1], 'email':u[2]} for u in users]

@app.get('/users/{id}')
def get_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?')
    user = cursor.fetchone()
    connection.close()
    if user:
        return {"id":user[0], 'username':user[1], 'email':user[2]}
    raise HTTPException(status_code=404, detail='User not found')

@app.post('/create_user')
def create_user(user: userCreate):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, email), VALUES (?, ?)', [user.username, user.email])
    connection.commit()
    connection.close()
    return {'message': "User created successfully"}
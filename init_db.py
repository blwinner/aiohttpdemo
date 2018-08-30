from sqlalchemy import MetaData
from aiomysql import create_pool
from db import question, choice

DSN = 'mysql+mysqlconnector://root:root@localhost:3306/aiodemo'

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])

def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'What\'s new?',
         'pub_date': '2015-12-15 17:17:49'}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    conn.close()

async def init_db(app):
    config = app['config']['mysql']
    engine = await create_pool(
        db = config['db'],
        user = config['user'],
        password = config['pwd'],
        host = config['host'],
        port = config['port'],
        minsize = 1,
        maxsize=10
    )
    app['db'] = engine

async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()
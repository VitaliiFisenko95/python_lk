import json
import os
from contextlib import contextmanager
from asyncpgsa import compile_query, connection
from sqlalchemy import create_engine

engine = create_engine(os.environ['DB_ACCESS'])


@contextmanager
def db():
    conn = None
    try:
        conn = engine.connect()
        yield conn
    except Exception as error:
        print(error)
    finally:
        if conn:
            conn.close()


dialect = connection.get_dialect(json_serializer=json._default_decoder)


def _execute(conn, query, action):
    cursor = None
    try:
        cursor = conn.connect()
        res = cursor.execute(query)
        return getattr(res, action)()
    except Exception as error:
        print(error)
    finally:
        conn.close()
        if cursor:
            cursor.close()


def insert_one(conn, query):
    return _execute(conn, query, 'fetchone')

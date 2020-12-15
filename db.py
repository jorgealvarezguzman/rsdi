import sqlite3
from sqlite3 import Error
from flask import current_app, g


def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        return g.db
    except Error:
        print(Error)


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def sql_create(query,arreglo):
    db = get_db()
    db.execute(query,arreglo)
    db.commit()
    db.close()


def sql_read(query,arreglo):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query,arreglo)
    objects = cursor.fetchall()
    return objects


def sql_update(query,arreglo):
    db = get_db()
    db.execute(query,arreglo)
    db.commit()
    db.close()


def sql_delete(query,arreglo):
    db = get_db()
    db.execute(query,arreglo)
    db.commit()
    db.close()
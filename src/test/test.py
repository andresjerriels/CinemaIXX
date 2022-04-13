from ..db import database
import sqlite3
import pathlib

connection = None

def setup_module(module):
    global connection
    connection = sqlite3.connect(str(pathlib.Path(__file__).parent.absolute()) + "/test.db")
    database.create_tables(connection)

def teardown_module(module):
    database.dropTables(connection)

def test_add_film():
    data1 = ("Film 1", "Tes sinopsis", 2021, None, 50000, 0)
    database.addFilm(connection, data1)

    fromDB = connection.execute("""
        SELECT *
        FROM film
        """).fetchall()

    assert len(fromDB) == 1
    assert fromDB[0][1] == "Film 1"

    data2 = ("Film 2", "Tes sinopsis 2", 2021, None, 45000, 0)
    database.addFilm(connection, data2)
    
    fromDB = connection.execute("""
        SELECT *
        FROM film
        """).fetchall()

    assert len(fromDB) == 2
    assert fromDB[1][0] == 2
    assert fromDB[1][2] == "Tes sinopsis 2"

def test_delete_film():
    database.deleteFilm(connection, 1)

    fromDB = connection.execute("""
        SELECT *
        FROM film
        """).fetchall()
    
    assert len(fromDB) == 1
    assert fromDB[0][1] == "Film 2"
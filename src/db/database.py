import sqlite3
import pathlib
import os

CREATE_TABLE_AKUN = "CREATE TABLE IF NOT EXISTS akun (id INTEGER PRIMARY KEY AUTOINCREMENT, phoneNumber TEXT, name TEXT, email TEXT, password TEXT, role TEXT NOT NULL DEFAULT 'CUSTOMER')"
CREATE_TABLE_FILM = "CREATE TABLE IF NOT EXISTS film (id INTEGER PRIMARY KEY AUTOINCREMENT, judul TEXT, sinopsis TEXT, tahun_rilis INTEGER, poster BLOB, harga_film INTEGER, jumlah_pembelian INTEGER)"
CREATE_TABLE_HISTORI_PEMBELIAN = "CREATE TABLE IF NOT EXISTS histori_pembelian (id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER, filmId INTEGER, FOREIGN KEY (userId) REFERENCES akun(id), FOREIGN KEY (filmId) REFERENCES film(id))"

def connect():
    path = str(pathlib.Path(__file__).parent.absolute())
    return sqlite3.connect(path + "/database.db")

def convertToBinaryData(filename):
    path = os.getcwd()

    # Convert digital data to binary format
    with open(path + '/img/' + filename, 'rb') as file:
        blobData = file.read()
    return blobData

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_AKUN)
        connection.execute(CREATE_TABLE_FILM)
        connection.execute(CREATE_TABLE_HISTORI_PEMBELIAN)

def isTablesEmpty(connection):
    with connection:
        akun = connection.execute("""
        SELECT * FROM akun""").fetchall()
        film = connection.execute("""
        SELECT * FROM film""").fetchall()
        histori = connection.execute("""
        SELECT * FROM histori_pembelian""").fetchall()
        
        if (len(akun) == 0 and len(film) == 0 and len(histori) == 0):
            return True
        else:
            return False

def create_seeder(connection):
    spidermanSynopsis = "Following the events of Avengers: Endgame (2019), Spider-Man must step up to take on new threats in a world that has changed forever."
    wonderwomanSynopsis = "Diana must contend with a work colleague and businessman, whose desire for extreme wealth sends the world down a path of destruction, after an ancient artifact that grants wishes goes missing."
    if isTablesEmpty(connection):
        with connection:
            connection.execute("""
            INSERT INTO akun(phoneNumber, name, email, password, role)
            VALUES('085212345678', 'admin', 'admin', 'admin', 'ADMIN')""")
            connection.execute("""
            INSERT INTO akun(phoneNumber, name, email, password)
            VALUES('081298765432', 'dehan', 'dehan@gmail.com', 'itb1920')""")
            connection.execute("""
            INSERT INTO film(judul, sinopsis, tahun_rilis, poster, harga_film, jumlah_pembelian)
            VALUES('Spider-Man: Far From Home', ?, 2019, ?, 100000, 0)""", (spidermanSynopsis, convertToBinaryData("spiderman.jpg"),))
            connection.execute("""
            INSERT INTO film(judul, sinopsis, tahun_rilis, poster, harga_film, jumlah_pembelian)
            VALUES('Wonder Woman 1984', ?, 2020, ?, 199000, 0)""", (wonderwomanSynopsis, convertToBinaryData("wonderwoman.jpg"),))
            connection.execute("""
            INSERT INTO histori_pembelian(userId, filmId) VALUES (1,1)""")
            connection.execute("""
            INSERT INTO histori_pembelian(userId, filmId) VALUES (1,2)""")

def dropTables(connection):
    with connection:
        connection.execute("DROP table akun")
        connection.execute("DROP table film")
        connection.execute("DROP table histori_pembelian")

def getFilmToShow(connection, user_id):
    with connection:
        return connection.execute("SELECT * FROM film WHERE film.id NOT IN (SELECT filmId FROM histori_pembelian WHERE ? = histori_pembelian.userId)", (user_id,)).fetchall()

def buyFilm(connection, id_film, id_user):
    with connection:
        connection.execute("INSERT INTO histori_pembelian(userId, filmId) VALUES (?,?)", (id_user, id_film))
        connection.execute("""
            UPDATE film
            SET jumlah_pembelian = jumlah_pembelian + 1
            WHERE id = ?
            """, (id_film,))

def addFilm(connection, data):
    with connection:
        connection.execute("""
        INSERT INTO film(judul, sinopsis, tahun_rilis, poster, harga_film, jumlah_pembelian)
        VALUES(?,?,?,?,?,?)
        """, data)

def getAllFilms(connection):
    with connection:
        return connection.execute("""
        SELECT id, judul, poster
        FROM film
        """).fetchall()

def deleteFilm(connection, id):
    connection.execute("""
    DELETE FROM film
    WHERE id=?
    """, (id,))
    connection.commit()

def getInformasiAkun(connection, id):
    return connection.execute("""
    SELECT * FROM akun
    WHERE id = (?)""", (id,)).fetchall()

def getUserFilms(connection, userId):
    films = connection.execute("""
    SELECT f.id, f.judul, f.sinopsis, f.tahun_rilis, f.poster, f.harga_film, f.jumlah_pembelian FROM akun a, histori_pembelian hp, film f
    WHERE a.id = (?) AND a.id = hp.userId AND hp.filmId = f.id""", (userId,)).fetchall()
    return films


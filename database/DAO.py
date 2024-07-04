from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.connessione import Connessione
from model.linea import Linea


class DAO():

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata "
        cursor.execute(query, ())

        for row in cursor:
            result.append(Fermata(row["id_fermata"], row["nome"], row["coordX"], row["coordY"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(v1, v2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from connessione c where c.id_stazP =%s and c.id_stazA =%s"
        cursor.execute(query, (v1.id_fermata, v2.id_fermata,))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdgesVicini(v1):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from connessione c where c.id_stazP =%s"
        cursor.execute(query, (v1.id_fermata,))

        for row in cursor:
            result.append(Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM connessione c "
        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllLinee():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM linea "
        cursor.execute(query, ())

        for row in cursor:
            result.append(Linea(**row))
        cursor.close()
        conn.close()
        return result

import pathlib

import mysql.connector


class DBConnect:

    # @classmethod  # metodo di classe, non metodo di istanza: unica classe per tutto il progetto, non devo fare un'istanza
    # def getConnection(cls):  # cls come argomento!
    #     try:
    #         cnx = mysql.connector.connect(
    #             user='root',
    #             password='root',
    #             host='127.0.0.1',
    #             database='libretto',
    #         )
    #         return cnx
    #     except mysql.connector.Error as err:
    #         print("Non riesco a collegarmi al database")
    #         print(err)
    #         return None


    # pooling
    def __init__(self):
        raise RuntimeError("Non creare una istanza di questa classe per favore!") # non necessario, ma bisogna prevedere gli usi sbagliati del codice

    _myPool = None
    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            #creo una connessione e restituisco il metodo get_connection
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(option_files = f"{pathlib.Path(__file__).resolve().parent}/connection.cfg",
                                                                          # percorso assoluto che porta al file
                                                                          pool_size=3, pool_name="myPool")
            except mysql.connector.Error as err:
                print("Something is wrong in dbconnect")
                print(err)
                return None
            return cls._myPool.get_connection()
        else:
            # se il pool già esiste, restituisco direttamente la connessione
            return cls._myPool.get_connection()


import pypyodbc as odbc

class SqlHandler:
    def __init__(self, server, database):
        self.server = server
        self.database = database

    def write(self, data):
        connection_string = f"""
        DRIVER=SQL SERVER;
        SERVER={self.server};
        DATABASE={self.database};
        TrustConnection=yes;
        """
        try:
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            sql_query = "INSERT INTO Encryption (Encrypted_text) VALUES (?);"
            cursor.execute(sql_query, (data,))
            conn.commit()

        except odbc.Error as e:
            print(f"Błąd przy zapisie do bazy danych: {e}")

        finally:
            cursor.close()
            conn.close()

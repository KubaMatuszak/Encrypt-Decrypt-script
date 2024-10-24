import pypyodbc as odbc

class Sql_handler:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        #self.username = username
        #self.password = password

    def write (self, data):
        connection_string = f"""
        DRIVER=SQL SERVER;
        SERVER={self.server};
        DATABASE={self.database};
        TrustConnection=yes;
        """
        #uid={self.username};
        #pwd={self.password};
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        sql_query = f"INSERT INTO Encryption (Encrypted_text) VALUES ({data});"

        cursor.execute(sql_query, data)
        conn.commit()
        cursor.close()
        conn.close()


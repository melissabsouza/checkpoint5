import oracledb
import json


def create_oracle_connection():
    with open("credenciais.json") as f:
        credenciais = json.load(f)

    user = credenciais["user"]
    password = credenciais["pass"]


    dsn_str = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")


    conn = oracledb.connect(user=user, password=password, dsn=dsn_str)

    cursor = conn.cursor()
    return conn, cursor


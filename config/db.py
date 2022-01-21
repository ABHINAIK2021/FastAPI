from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL

connection_url = URL.create(
    "mssql+pyodbc",
    username="",
    password="",
    host="LAPTOP-MGN75APP\SQLEXPRESS",
    database="MyDatabase",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
    },
)

engine = create_engine(connection_url)

meta = MetaData()

conn = engine.connect()
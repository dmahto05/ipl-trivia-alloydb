from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv() 

def fetch_env_variable():
    hostname = os.environ.get("PG_HOST")
    db_name = os.environ.get("PG_DB_NAME")
    password = os.environ.get("PG_PASSWORD")
    user = os.environ.get("PG_USER")
    port = os.environ.get("PG_PORT")
    return hostname, db_name, password, user, port
    
def database_connection():
    hostname, db_name, password, user, port = fetch_env_variable()
    try:
        db_url = fr"postgresql://{user}:{password}@{hostname}:{port}/{db_name}"
        engine = create_engine(db_url)
        connection = engine.connect()
        return connection
    except Exception as e:
        print(f"Issue occured while connecting in database\n{e}")

def fetch_query_output(userquery,dataframe=False):
    connection = database_connection()
    if dataframe:
        result = connection.execute(text(rf"{userquery}"))
    else:
        result = connection.execute(text(rf"""SELECT * from alloydbnl2sql('{userquery.replace("'","''")}');"""))
    if dataframe:
        data = result.fetchall()
        column = result.keys()
        df = pd.DataFrame(data, columns=column)
        return df.head(5)
    else:
        data = result.fetchone()[0]
        return data

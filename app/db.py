from sqlalchemy import create_engine
DATABSE_URL = " postgresql://postgres:postgres@localhost/chinook"
engine =create_engine("postgresql://postgres:postgres@localhost/chinook")
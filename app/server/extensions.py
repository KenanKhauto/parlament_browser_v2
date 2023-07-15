from app.database.db_connection import DBConnection
from app.data.factory import Factory

db = DBConnection()
factory = Factory(db)
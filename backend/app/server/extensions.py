from backend.app.database.db_connection import DBConnection
from backend.app.data.factory import Factory

db = DBConnection()
factory = Factory(db)
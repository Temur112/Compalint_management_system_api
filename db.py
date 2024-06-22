from decouple import config
from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASS')}@localhost:5432/complaints"

databse = Database(DATABASE_URL)

metadata = MetaData()

import datetime

import peewee as p

DB_NAME = "data.db"


def setup_db_connection():
    db = p.SqliteDatabase(
        DB_NAME,  # pragmas={"journal_mode": "wal", "foreign_keys": 1}
    )
    db.connect()
    return db


class ModelBase(p.Model):
    class Meta:
        database = setup_db_connection()


class DataModel(ModelBase):
    timestamp = p.DateTimeField(unique=True)
    some_data = p.TextField()


class DataAccess(DataModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_table()

    def get_single_record(self) -> dict:
        return self.select().get()

    def insert(self, some_data: str) -> None:
        self.timestamp = datetime.datetime.utcnow()
        self.some_data = some_data
        self.save()

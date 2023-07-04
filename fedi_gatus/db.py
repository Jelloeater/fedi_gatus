import datetime

import peewee as p

DB_NAME = "db.sqlite3"


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
    # TODO Add data fields


class Data(DataModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_table()

    def get(self, num_minutes_to_get: int) -> list:
        """
        Takes time range of past mins, and returns list of db rows w/ temp data
        """
        return self.select().where(
            self.timestamp < (datetime.datetime.utcnow() + datetime.timedelta(minutes=num_minutes_to_get))
        )

    def insert(self) -> None:
        self.timestamp = datetime.datetime.utcnow()
        self.save()

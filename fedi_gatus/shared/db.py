import datetime
import os

import peewee as p


def get_connection():
    if os.getenv("TEST_MODE"):  # Only run twice in test mode
        DB_NAME = "data.shared"
        db = p.SqliteDatabase(None, pragmas={"journal_mode": "wal", "foreign_keys": 1}
                              )
        db.init(database=DB_NAME)
        db.connect()
    else:
        db = p.PostgresqlDatabase(None)
        db.init(database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOSTNAME_MONITORING"),
                port=5432)
        db.connect()
    return db


class ModelBase(p.Model):
    class Meta:
        database = p.DatabaseProxy()


class DataModel(ModelBase):
    timestamp = p.DateTimeField(unique=True)
    some_data = p.TextField()

# class DataModel(ModelBase): # TODO Adapt data model
#     id = p.BigIntegerField()
#     domain = p.TextField()
#     open_registration = p.BooleanField()
#     description = p.TextField()
#     banner_url = p.TextField()
#     location_city = p.TextField()
#     location_country = p.TextField()
#     software_name = p.TextField()
#     software_version = p.TextField()
#     stats_status_count = p.BigIntegerField()
#     stats_user_count = p.BigIntegerField()
#     stats_monthly_active_users = p.BigIntegerField()
#     first_seen_at = p.DateTimeField()
#     last_seen_at = p.DateTimeField()

class DataAccess(DataModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.database = get_connection()
        # Updated DB Connection at runtime
        self.create_table()

    def get_single_record(self) -> dict:
        return self.select().get()

    def insert_data(self, some_data: str) -> None:
        import datetime
        self.timestamp = datetime.datetime.utcnow()
        self.some_data = some_data
        self.save()

# import datetime # TODO Maybe add Updated field?
import logging
import os

import peewee as p


def get_connection():
    DOCKER_VOLUME = "/data"
    logging.info(os.getcwd())
    if os.getenv("SQL_LITE"):  # Only run twice in test mode
        DB_NAME = "data.shared"
        if os.getenv("DOCKER"):
            logging.info("CWD=" + str(os.getcwd()))
            DB_NAME = DOCKER_VOLUME + "/" + DB_NAME
            logging.info("DB Path = " + DB_NAME)

        db = p.SqliteDatabase(None, pragmas={"journal_mode": "wal", "foreign_keys": 1})
        db.init(database=DB_NAME)
        db.connect()
        if os.getenv("DOCKER"):
            logging.info(os.listdir(DOCKER_VOLUME))
    else:
        db = p.PostgresqlDatabase(None)
        db.init(
            database=os.getenv("POSTGRES_DB_MONITORING"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOSTNAME_MONITORING"),
            port=5432,
        )
        db.connect()
    return db


class ModelBase(p.Model):
    class Meta:
        database = p.DatabaseProxy()


#
class Model(ModelBase):
    id = p.BigIntegerField()
    domain = p.TextField(unique=True)
    open_registration = p.BooleanField(null=True)
    description = p.TextField(null=True)
    banner_url = p.TextField(null=True)
    location_city = p.TextField(null=True)
    location_country = p.TextField(null=True)
    software_name = p.TextField(null=True)
    software_version = p.TextField()
    stats_status_count = p.BigIntegerField(null=True)
    stats_user_count = p.BigIntegerField()
    stats_monthly_active_users = p.BigIntegerField(null=True)
    first_seen_at = p.DateTimeField()
    last_seen_at = p.DateTimeField()


class DbAccess(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.database = get_connection()
        # Updated DB Connection at runtime
        logging.info("Got DB connection")

        ################################################################################################
        # IMPORTANT
        # Databases will NOT get created when you are using PostGREs, you need to make the DB first or
        # use default db postgres
        ################################################################################################

    def get_single_record(self) -> dict:
        return self.select().get()

    def get_top_lemmy_instances(self, count=25) -> list[Model]:
        # TODO Add env var for count

        if not os.getenv("TEST_MODE"):
            count = int(os.getenv("NUMBER_OF_SERVERS"))
        logging.info("Number of Rows:" + str(DbAccess.select().count()))
        d = (
            DbAccess.select()
            .where(DbAccess.software_name == "Lemmy")
            .order_by(DbAccess.stats_monthly_active_users)
            .limit(count)
        )
        info = []
        for i in d:
            info.append(i)
        return info

    def insert_data(self, data_in: object) -> None:
        from munch import DefaultMunch

        data_in = DefaultMunch.fromDict(data_in)
        self.id = data_in.id
        self.domain = data_in.domain
        self.open_registration = data_in.open_registration
        self.description = data_in.description
        self.banner_url = data_in.banner_url
        self.location_city = data_in.location.city
        self.location_country = data_in.location.country
        self.software_name = data_in.software.name
        self.software_version = data_in.software.version
        self.stats_status_count = data_in.stats.status_count
        self.stats_user_count = data_in.stats.user_count
        self.stats_monthly_active_users = data_in.stats.monthly_active_users
        self.first_seen_at = data_in.first_seen_at
        self.last_seen_at = data_in.last_seen_at
        self.save(force_insert=True)

    def initialize(self):
        logging.info("Create Table if missing")

        self.drop_table()
        self.create_table()

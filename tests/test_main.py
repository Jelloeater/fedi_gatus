import logging

import dotenv

import fedi_gatus.config_gen.__main__ as config_main
import fedi_gatus.shared.db as db
import fedi_gatus.updater.__main__ as updater
import fedi_gatus.updater.data as data
from fedi_gatus.config_gen import gen

dotenv.load_dotenv()

import os

os.environ["SQL_LITE"] = "1"
os.environ["TEST_MODE"] = "1"


class TestData:
    @classmethod
    def test_pull(cls):
        d = data.Worker()
        d.get_raw_data()
        assert d.raw_data is not None

    @classmethod
    def test_updater(cls):
        w = data.Worker()
        w.initialize_db()
        w.get_raw_data()
        w.insert_data()
        assert w is not None


class TestDB:
    @classmethod
    def test_db_access(cls):
        d = db.DbAccess()
        assert d is not None

    @classmethod
    def test_db_get(cls):
        d = db.DbAccess()
        r = d.get_single_record()
        assert r is not None

    @classmethod
    def test_db_get_top(cls):
        d = db.DbAccess()
        r = d.get_top_instances()
        assert r is not None

    @classmethod
    def test_db_full_load(cls):
        import time

        start = time.time()
        d = db.DbAccess()
        d.drop_table()  # Clear table
        d.create_table()
        r = d.get_top_instances()
        end = time.time()
        logging.debug(end - start)
        assert r is not None


class TestConfig:
    @classmethod
    def test_config_gen(cls):
        d = [{"name": "Lemmy World", "url": "https://lemmy.world"}, {"name": "Lemmy ML", "url": "https://lemmy.ml"}]
        out = gen.Generate_endpoints(d)
        assert out is not None
        return out

    @classmethod
    def test_ui_gen(cls):
        result = gen.generate_ui()
        logging.info(result)
        assert result is not None
        return result

    def test_generate_full_config(cls):
        x = gen.generate_full_config()
        logging.debug(x)
        assert x is not None

    def test_config_worker(self):
        config_main.main()


class TestUpdater:
    @classmethod
    def test_main_update(cls):
        updater.main()

    # @classmethod
    # def test_main_update_postgres_BG(cls):
    #     os.environ.pop("SQL_LITE")
    #     os.environ["POSTGRES_HOSTNAME_MONITORING"] = "localhost"
    #     os.environ["TEST_MODE"] = "1"
    #     updater.main()

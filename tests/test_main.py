import logging

import dotenv

import fedi_gatus.config_gen.__main__ as config_main
import fedi_gatus.shared.db as db
import fedi_gatus.updater.data
from fedi_gatus.config_gen import gen

dotenv.load_dotenv()

import os

os.environ["TEST_MODE"] = "1"


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


class TestData:
    @classmethod
    def test_pull(cls):
        d = fedi_gatus.updater.data.get_raw_data()
        assert d is not None

    @classmethod
    def test_db_insert(cls):
        d = db.DataAccess()
        d.insert_data("lol")

    @classmethod
    def test_db_get(cls):
        d = db.DataAccess()
        r = d.get_single_record()
        assert r

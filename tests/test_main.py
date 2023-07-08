import logging

import dotenv

import fedi_gatus.config_gen.__main__ as config_main
from fedi_gatus.config_gen import gen

dotenv.load_dotenv()


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

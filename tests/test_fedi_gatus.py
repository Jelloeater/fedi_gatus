import logging

import dotenv

dotenv.load_dotenv()


from fedi_gatus import __main__ as cli
from fedi_gatus import config_gen, data


class TestConfig:
    @classmethod
    def test_main(cls):
        cli.main()

    @classmethod
    def test_config_gen(cls):
        d = [{"name": "Lemmy World", "url": "https://lemmy.world"}, {"name": "Lemmy ML", "url": "https://lemmy.ml"}]
        out = config_gen.generate_endpoints(d)
        assert out is not None
        return out

    @classmethod
    def test_ui_gen(cls):
        result = config_gen.generate_ui()
        logging.info(result)
        assert result is not None
        return result

    def test_generate_full_config(cls):
        x = config_gen.generate_full_config()
        logging.debug(x)
        assert x is not None

    def test_get_data(self):
        data.generate_top_instances()

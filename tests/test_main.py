import logging

import dotenv

from fedi_gatus.config_gen import generator

dotenv.load_dotenv()


class TestConfig:
    @classmethod
    def test_config_gen(cls):
        d = [{"name": "Lemmy World", "url": "https://lemmy.world"}, {"name": "Lemmy ML", "url": "https://lemmy.ml"}]
        out = generator.Generate_endpoints(d)
        assert out is not None
        return out

    @classmethod
    def test_ui_gen(cls):
        result = generator.generate_ui()
        logging.info(result)
        assert result is not None
        return result

    def test_generate_full_config(cls):
        x = generator.generate_full_config()
        logging.debug(x)
        assert x is not None

    # @pytest.mark.skip(reason="This takes a long time to run right now")
    # def test_get_data(self):
    #     # TODO Fix Unit test
    #     config_gen.generator.generate_full_config()

from fedi_gatus import __main__ as cli
from fedi_gatus import config_gen


class TestConfig:
    @classmethod
    def test_main(cls):
        cli.main()

    @classmethod
    def test_config_gen(cls):
        d = [
            {
                'name': 'Lemmy World',
                'url': 'https://lemmy.world'
            },            {
                'name': 'Lemmy ML',
                'url': 'https://lemmy.ml'
            }
        ]
        out = config_gen.generate_endpoints(d)
        f = open("test.yaml", "w")
        f.write(out)
        f.close()


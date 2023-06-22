from fedi_gatus import __main__ as cli


class TestConfig:
    @classmethod
    def test_main(cls):
        cli.main()

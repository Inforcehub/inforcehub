"""
Tests for `inforcehub` module.
"""


class TestInforcehub(object):
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_color_import(self):
        """ Confirm imports are available for modules """
        from inforcehub import InforcehubColors

        c = InforcehubColors()
        c.list()

    def test_anon_import(self):
        """ Confirm imports are available for modules """
        from inforcehub import Anonymize

        anon = Anonymize()
        anon.salt

"""
Tests for `inforcehub` module.
"""
# import pytest
from inforcehub import inforcehub


class TestInforcehub(object):
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_color_imports(self):
        """ Confirm imports are available for color modules """
        from inforcehub.colors import InforcehubColors

        c = InforcehubColors()
        c.list()


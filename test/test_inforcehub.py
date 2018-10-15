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

    def test_helloworld(self):
        """ Tests the helloworld method """
        assert "installed" in inforcehub.helloworld()

    def test_color_imports(self):
        """ Confirm imports are available for color modules """
        from inforcehub import colors

        assert isinstance(colors.ifh(), str)
        assert isinstance(colors.ifhlist(), list)

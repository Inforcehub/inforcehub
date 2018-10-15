"""
Tests for `inforcehub` module.
"""
import pytest
from inforcehub import inforcehub


class TestInforcehub(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_helloworld(self):
        """ Tests the helloworld method used to check installation was successful """
        assert "installed" in inforcehub.helloworld()

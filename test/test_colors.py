"""
Tests for color module.
"""
import pytest
from inforcehub.colors import InforcehubColors


class TestInforcehubColors(object):
    @classmethod
    def setup_class(cls):

        cls.c = InforcehubColors()

        cls.core_colors = [
            ("pink", "#CB1B64"),
            ("blue", "#0593CF"),
            ("green", "#079921"),
            ("yellow", "#F3B80C"),
            ("cyan", "#0BD0B1"),
        ]

        cls.neutral_colors = [
            ("mid", "#8C8C8C"),
            ("dark", "#4D4D4D"),
            ("light", "#CCCCCC"),
            ("black", "#011329"),
            ("white", "#FCFCFC"),
        ]

        cls.extra_colors = [
            ("purple", "#5E2099"),
            ("forest", "#137748"),
            ("teal", "#117789"),
            ("violet", "#5446A0"),
            ("orange", "#FC5507"),
            ("red", "#E52019"),
        ]

    @classmethod
    def teardown_class(cls):
        pass

    def test_attributes_return_correct_hex_codes(self):
        """ Tests if all colors return the right hex values """
        for color in self.core_colors:
            assert getattr(self.c, color[0]) == color[1]
        for color in self.neutral_colors:
            assert getattr(self.c, color[0]) == color[1]
        for color in self.extra_colors:
            assert getattr(self.c, color[0]) == color[1]

    def test_returns_valid_hex(self):
        """ Tests if the format is correct """
        for hexcode in self.c.list():
            assert isinstance(hexcode, str)
            assert len(hexcode) == 7
            assert hexcode[0] == "#"
            assert isinstance(int(hexcode[1:], 16), int)  # Checks it is valid hex

    def test_show_method(self):
        """ Tests that the show returns a list """
        assert isinstance(self.c.show(), list)
        assert len(self.c.show()) == 16
        assert self.core_colors[1][0] in self.c.show()
        assert self.neutral_colors[3][0] in self.c.show()
        assert self.extra_colors[0][0] in self.c.show()

    def test_show_method_sublists(self):
        """ Tests that the sublists can be called effectively on the method """
        assert len(self.c.show("all")) == 16
        assert len(self.c.show("colors")) == 11
        assert len(self.c.show("core")) == 5
        assert self.core_colors[4][0] in self.c.show("core")
        assert len(self.c.show("neutral")) == 5
        assert self.neutral_colors[1][0] in self.c.show("neutral")

    def test_show_method_exception(self):
        """ Tests the exceptions are raised for invalid color list """
        with pytest.raises(Exception):
            self.c.show("invalid text")

    def test_list_method(self):
        """ Tests that the list method returns hex value lists correctly """
        assert isinstance(self.c.list(), list)
        assert len(self.c.list()) == 16
        assert self.core_colors[1][1] in self.c.list()
        assert self.neutral_colors[1][1] in self.c.list()
        assert self.extra_colors[1][1] in self.c.list()

    def test_list_method_sublists(self):
        """ Tests that the sublists can be called effectively on the method """
        assert len(self.c.list("all")) == 16
        assert len(self.c.list("colors")) == 11
        assert len(self.c.list("core")) == 5
        assert self.core_colors[3][1] in self.c.list("core")
        assert len(self.c.list("neutral")) == 5
        assert self.neutral_colors[0][1] in self.c.list("neutral")

    def test_list_method_exception(self):
        """ Tests the exceptions are raised for invalid color list """
        with pytest.raises(Exception):
            self.c.list("invalid text")

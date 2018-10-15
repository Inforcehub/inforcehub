"""
Tests for `color` module.
"""
import pytest
from inforcehub import colors


class TestInforcehub(object):
    @classmethod
    def setup_class(cls):

        cls.core_colors = [
            ("pink", "#cb1b64"),
            ("blue", "#0593cf"),
            ("green", "#079921"),
            ("yellow", "#f3b80c"),
            ("cyan", "#0bd0b1"),
        ]

        cls.neutral_colors = [
            ("mid", "#8c8c8c"),
            ("dark", "#4d4d4d"),
            ("light", "#cccccc"),
            ("black", "#011329"),
            ("white", "#fcfcfc"),
        ]

        cls.extra_colors = [
            ("purple", "#5e2099"),
            ("forrest", "#137748"),
            ("teal", "#117789"),
            ("violet", "#5446a0"),
            ("orange", "#FC5507"),
            ("red", "#e52019"),
        ]

    @classmethod
    def teardown_class(cls):
        pass

    def test_ifh_color_return_values(self):
        """ Tests if all colors return the right hex values """
        for color in self.core_colors:
            assert colors.ifh(color[0]) == color[1]
        for color in self.neutral_colors:
            assert colors.ifh(color[0]) == color[1]

    def test_ifh_color_help(self):
        """ Tests the help text """
        assert isinstance(colors.ifh(), str)
        assert "Available" in colors.ifh()

    def test_ifh_color_exception(self):
        """ Tests the exceptions are raised for invalid colours """
        with pytest.raises(Exception):
            colors.ifh("not_a_real_color")

    def test_ifh_color_spot_check(self):
        """ Tests a specific color call """
        assert colors.ifh("pink") == "#cb1b64"

    def test_ifh_color_list(self):
        """ Tests the return values for the color list function """
        assert isinstance(colors.ifhlist(), list)
        assert len(colors.ifhlist()) == len(self.core_colors + self.extra_colors)
        assert colors.ifhlist()[1] == self.core_colors[1][1]
        assert colors.ifhlist()[7] == self.extra_colors[2][1]


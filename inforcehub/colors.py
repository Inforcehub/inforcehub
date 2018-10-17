class InforcehubColors:
    """
    A class that will return the inforcehub brand colors as single hex codes
    or lists for use in various packages such as matplotlib.

    The objective of this package is to make it easier and quicker to create
    consistent-looking charts using branded colors
    """

    # Core colors
    pink = "#CB1B64"
    blue = "#0593CF"
    green = "#079921"
    yellow = "#F3B80C"
    cyan = "#0BD0B1"
    core = ["pink", "blue", "green", "yellow", "cyan"]

    # Neutral colors
    mid = "#8C8C8C"
    dark = "#4D4D4D"
    light = "#CCCCCC"
    black = "#011329"
    white = "#FCFCFC"
    neutral = ["mid", "dark", "light", "black", "white"]

    # Extra colors (not core but useful when we need more colors)
    forest = "#137748"
    purple = "#5E2099"
    teal = "#117789"
    violet = "#5446A0"
    orange = "#FC5507"
    red = "#E52019"
    extra = ["forest", "purple", "teal", "violet", "orange", "red"]

    colors = core + extra
    all = core + extra + neutral

    @classmethod
    def show(cls, sublist="all"):
        """
        Returns a list of the color names

        :param: str sublist: (default='all') options 'colors'/'core'/'neutral'/'all'

        :returns: a list of color names
        :rtype: list

        """
        if sublist is not None:
            if sublist not in ["core", "neutral", "colors", "all"]:
                raise Exception(
                    'List type can only be "core", "neutral", "colors", or "all"'
                )

        list_ = []
        for color in getattr(cls, sublist):
            list_.append(color)
        return list_

    @classmethod
    def list(cls, sublist="all"):
        """
        Returns a list of the color hex codes for use in Matplotlib
        or other tools which want a set of colors to choose from

        :param: str sublist: (default='all') options 'colors'/'core'/'neutral'/'all'

        :returns: a list of color hex codes
        :rtype: list

        """
        if sublist is not None:
            if sublist not in ["core", "neutral", "colors", "all"]:
                raise Exception(
                    'List type can only be "core", "neutral", "colors", or "all"'
                )

        list_ = []
        for color in getattr(cls, sublist):
            list_.append(getattr(cls, color))
        return list_

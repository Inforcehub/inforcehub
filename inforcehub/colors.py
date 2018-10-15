# A dictionary of colors with the name and hexcode

# CORE_COLORS - for the core brand colors
CORE_COLORS = {
    "pink": "#cb1b64",
    "blue": "#0593cf",
    "green": "#079921",
    "yellow": "#f3b80c",
    "cyan": "#0bd0b1",
}

# NEUTRAL_COLORS - neutrals for the core brand
NEUTRAL_COLORS = {
    "mid": "#8c8c8c",
    "dark": "#4d4d4d",
    "light": "#cccccc",
    "black": "#011329",
    "white": "#fcfcfc",
}

# EXTRA_COLORS - for additional colors when a list is required
EXTRA_COLORS = {
    "purple": "#5e2099",
    "forrest": "#137748",
    "teal": "#117789",
    "violet": "#5446a0",
    "orange": "#FC5507",
    "red": "#e52019",
}

ALL_COLORS = CORE_COLORS.copy()
ALL_COLORS.update(EXTRA_COLORS)
ALL_COLORS.update(NEUTRAL_COLORS)


def ifh(color_name=None):
    """
    Function to return the hex color code of a specific IFH branded color.

    :param: str color_name: the name of the color to be returned

    If left blank the function will return a list of all available colors

    :returns: a color hex code, or a list of colors
    :rtype: str
    """
    if color_name is None:
        message = f'Available colours: {", ".join(ALL_COLORS.keys())}'
        return message

    result = ALL_COLORS.get(color_name)
    if result is not None:
        return result
    else:
        raise Exception("Invalid color - try ifh_color() for help")


def ifhlist():
    """
    Returns a list of hex color codes for use in charts such as matplotlib.

    :returns: a list of color hex codes
    :rtype: list
    """
    colors = []
    colors.extend(CORE_COLORS.values())
    colors.extend(EXTRA_COLORS.values())
    return colors

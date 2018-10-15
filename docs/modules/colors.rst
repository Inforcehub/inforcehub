=============
Colors module
=============

This provides simple utilities to return **inforcehub branded colors** for
use across applications such as matplotlib.

Sub-modules
===========

colors.ifh()
------------

**Returns a single color hex code** for an inforcehub branded color
with name *color_name*::

    colors.ifh(color_name)

To see a list of available colors, call the function without any *color_name*::

    colors.ifh()


colors.ifhlist()
----------------

**Returns a list of hex color codes** using inforcehub branded colors.
This can be passed to matplotlib charts with multiple series to automatically
color series in the branded colors::

    colors.ifhlist()


Importing
=========

To use the color utilities import the functions you need::

    from inforcehub import colors



Details
=======

.. automodule:: inforcehub.colors
   	:members:
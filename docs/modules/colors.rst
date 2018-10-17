.. _inforcehubcolors:

================
InforcehubColors
================

This provides simple utilities to return **inforcehub branded colors** for
use across applications such as matplotlib.

Usage
=====

Import the color class and create an instance::

    from inforcehub import InforcehubColors
    
    ifh = InforcehubColors()

On this you can then get the specific colors by name::

    ifh.pink                # Hex code for our pink
    ifh.blue                # Hex code for our blue

Or you can see the list of colors available::

    ifh.show()              # Names of all colors and neutrals 
    ifh.show('core')        # Names of core colors only
    ifh.show('neutral')     # Names of neutral colors only

Or you can get multiple color hexcodes in a list::

    ifh.list()              # Hex codes for everything
    ifh.list('core')        # Hex codes for core colors
    ifh.list('colors')      # Hex codes for all colors
    ifh.list('neutral')     # Hex codes for neutral colors

Note that these methods are class methods on the **InforcehubColors** object.
So you do not have to create an instance first. But we suggest doing it using an 
instance as above as it will keep your code neater.


Module details
==============

.. automodule:: inforcehub.colors
   	:members:
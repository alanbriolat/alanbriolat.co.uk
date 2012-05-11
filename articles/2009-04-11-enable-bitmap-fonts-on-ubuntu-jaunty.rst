Enable Bitmap Fonts on Ubuntu Jaunty
====================================

:date: 2009-04-11
:category: linux
:tags: ubuntu, fonts

I like to use tiny bitmap fonts like MonteCarlo_ for programming, but by default Ubuntu has bitmap 
font support turned off.  From (at least) Gutsy through to Intrepid, `this method`__ worked for 
enabling bitmap font support, but after installing the Jaunty beta I found this no longer works.

__ http://www.nazgum.com/2007/12/09/ubuntu-pcf-fonts/

Luckily, after a brief look in ``/etc/fonts``, I found that font configuration now follows the nice 
pattern of a ``conf.avail`` directory containing all the available configuration parts, and 
``conf.d`` containing symlinks to these parts.  This makes enabling bitmap fonts even simpler now:

.. code-block:: bash

    # "Un-disable" bitmap fonts
    sudo rm /etc/fonts/conf.d/70-no-bitmaps.conf
    # Clear the font cache
    sudo fc-cache -f -v

Now you should be able to drop bitmap (i.e. PCF) fonts into ``~/.fonts`` as you would with TTF fonts 
and be able to use them with no extra hassle.

**Update:** Andreas asked in the comments if there was a way to do this that doesn't require root 
access.  In fact there is!  If you copy ``/etc/fonts/conf.avail/70-force-bitmaps.conf`` to 
``~/.fonts.conf`` then it has the same effect.  (If you already have a ``~/.fonts.conf`` then you'll 
want to merge them together; copy everything inside ``<fontconfig>...</fontconfig>`` from 
``70-force-bitmaps.conf`` and put it just before ``</fontconfig>`` in ``~/.fonts.conf``.)


.. _MonteCarlo: http://www.bok.net/MonteCarlo/

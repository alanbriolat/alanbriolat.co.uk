Remapping Mouse Buttons on Ubuntu Lucid
=======================================

:date: 2010-04-23
:category: linux
:tags: ubuntu, xorg

For ergonomic reasons `(discussed previously) <../mouse-button-remapping-with-hal.html>`_ I like a 
side button on my mouse to act as a middle button instead.  Unfortunately there still doesn't seem 
to be an "easy" way to remap mouse buttons in Linux, and what's more the method of changing such 
settings seems to keep changing.  To achieve the same results in Ubuntu Lucid, I added an Xorg 
configuration fragment at ``/usr/lib/X11/xorg.conf.d/20-logitech-mx1100.conf``::

    Section "InputClass" 
            Identifier "Logitech MX1100 button remap" 
            MatchProduct "Logitech USB Receiver" 
            MatchDevicePath "/dev/input/event*" 
            Option "ButtonMapping" "1 2 3 4 5 6 7 2 9 10" 
    EndSection

As with the previous method, ``>xinput list`` should give you the product string to use for 
``MatchProduct``.

.. note::

    In Ubuntu 10.10 ``/usr/lib/X11/xorg.conf.d/`` became ``/usr/share/X11/xorg.conf.d/``.  Since at 
    least 11.04 ``/etc/X11/xorg.conf.d/`` is read in the same way, if it exists, and preferably this 
    configuration snippet should live there.

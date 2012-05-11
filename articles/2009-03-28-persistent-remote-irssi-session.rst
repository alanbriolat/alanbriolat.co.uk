Persistent Remote irssi Session
===============================

:date: 2009-03-28
:tags: screen, irssi, bash

I've recently moved back to using irssi as my IRC client, because when combined with `GNU screen`_ 
it can be kept independent of a graphical session, or even better, of a particular client machine 
(if you have a server somewhere).  Since I have a home fileserver at the moment, I want my IRC 
client to always be running there.  However, my usual workflow to do this is to open a terminal, SSH 
to the server, resume screen, move the window and resize it.  This is far from optimal for something 
I usually want open...

Instead, I pieced together a command that I can use as a panel shortcut to do it all for me:

.. code-block:: bash

    gnome-terminal --geometry 100x30-0-0 -x \
            ssh <hostname> -t "screen -D -RR -S irssi irssi"

``gnome-terminal --geometry 100x30-0-0 -x``
    Open "gnome-terminal" at the bottom right of the screen with a size of 100 characters by 30.  
    Run the rest of the command inside the terminal.
``ssh <hostname> -t``
    Connect to ``<hostname>`` and execute the supplied command in an interactive pseudo-TTY.
``screen -D -RR -S irssi irssi``
    Do whatever necessary to gain control of the "irssi" screen session if it exists, otherwise 
    create it and run irssi inside it.

.. _`GNU screen`: http://www.gnu.org/software/screen/

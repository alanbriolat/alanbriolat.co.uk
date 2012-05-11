Spoofing MAC address on Ubuntu Maverick
=======================================

:date: 2010-10-12
:category: linux
:tags: ubuntu, networkmanager

Continuing the trend of accidentally disabling hacks that people rely on, it now no longer appears 
to be possible to set your network card's MAC by adding a line like the following to 
``/etc/rc.local``::

    ifconfig eth0 hw ether 00:0C:xx:xx:xx:xx

It seems that for some reason something (presumably NetworkManager) is resetting the device's MAC 
address when the computer wakes from suspend.  However, at the same time, the "Cloned MAC address" 
field has been added to NetworkManager's "Edit connection" dialog, and this is where your desired 
MAC address should be entered.

My painless Linux "upgrade" process
===================================

:date: 2009-01-07
:category: linux

I like to keep up to date with the latest version of any Linux distro I use (naturally), but for 
some reason I don't trust the upgrade process to work properly and/or not leave a load of cruft 
behind.  I've actually attempted an upgrade once just to try and get over my upgrade fear, but 
instead it went horribly wrong and convinced me to not try again for a long time.

There is a simple way to make reinstallations painless enough that you don't need to offer yourself 
up to the upgrade gods, and it takes only a small amount of forward planning.  **Always always 
always use a separate home partition!** Keeping your home partition separate allows you to go as far 
as reformatting your main operating system partition without losing any of the data you really care 
about.

Here is my typical upgrade/reinstall process.  If you're planning on using this method, please read 
the *whole thing* before starting and make sure you understand what you're doing and why.  A lot of 
this is done as root and mistakes can be painful.

.. note::

    Just in case it's not obvious, my username is ``alan`` - replace it with your own username!  If 
    you have multiple users, repeat operations on each user's home directory.


1 - Prepare
-----------

Your ``/home`` partition isn't going to be reformatted if everything is done correctly, so if you 
know what you're doing you shouldn't even need to do a full backup.  However, you've probably got 
some other things on the root partition that have been changed that you want to keep, at least for 
future reference.

.. code-block:: bash

    # Backup /etc
    sudo tar czvpf /home/etc.tar.gz /etc
    # Backup root's home directory
    sudo tar czvpf /home/root.tar.gz /root
    # Backup anything else you might want to /home, for example MySQL databases
    # (maybe backup /var the same way as above?)
    # ...

Next you need to make a note of which partition is which so you don't accidentally format the wrong 
one.

.. code-block:: bash

    $ df
    /dev/sda5             11718932   2419420   9299512  21% /
    ...
    /dev/sda7             44133352    219500  41671984   1% /home

So in this case, ``/dev/sda5`` is what you'll be reformatting and installing your new operating 
system on, and ``/dev/sda7`` is the one you don't want to touch in any way whatsoever.

Next you'll want to write the fstab line for your home partition somewhere so you can use it on your 
new installation.  The following command will get that from ``/etc/fstab`` for you::

    $ grep "/home" /etc/fstab
    /dev/sda7      /home      ext3     defaults,relatime      0     2

The final preparation step is to move your old home directory somewhere.  To do this you'll need to 
be logged in directly as root.  If you're running an Ubuntu-based distribution and haven't set the 
root password before, do so::

    sudo passwd

Log out of your graphical session, switch to a virtual terminal (e.g. press *Ctrl-Alt-F2*), and log 
in as root.  Move your old home directory::

    mv /home/alan /home/alan-old

Everything should be ready now - time to reboot into the installer of your distro of choice!


2 - Installation
----------------

Just install as usual, feel free to obliterate your old root partition but *make sure you don't 
touch your home partition!* Install as if your home directory will be on your root partition along 
with everything else.  (It's possible to just use your old home partition at this point, but most 
installers will format any partition you choose to use by default.  This way, there is no risk of 
that happening.)  Reboot into your new fresh Linux installation.


3 - Juggling
------------

Now all that's left to do is get your home directory onto your home partition, get your home 
partition mounted and move all your files back to their rightful places.

Yet again, this process will require you to log in directly as root to move the home directory 
around, so set the root password as before if necessary for your distribution.

Now log in as root on a virtual terminal (e.g. *Ctrl-Alt-F2*) to mount your home partition 
somewhere, copy your new home directory across, and unmount it again::

    mount /dev/sda7 /mnt
    cp -a /home/alan /mnt/
    umount /mnt

Now we want to make sure the home partition get's mounted at ``/home`` as it should.  Edit 
``/etc/fstab`` with your editor of choice and add the fstab line from earlier.  To make sure 
everything is correct, mount the home partition in a way that'll use fstab, and check that both the 
old and new home directories are there::

    $ mount /home
    $ ls /home/
    alan   alan-old

Just in case your user ID has changed, make sure your old home directory is owned by your new user::

    chown -R alan:alan /home/alan-old

At this point, you should be finished with using the root account, and can log in as normal.  If you 
want to lock the root account (in the way Ubuntu does by default), run::

    sudo usermod -L root


4 - Get your files
------------------

Now you should be able to browse both your new and old home directories using your file manager of 
choice.  Open one for each, show hidden files, and start dragging stuff around!

This step might take some time, but has the added advantage that you get to learn where every 
application stores its user files, and also gives you the opportunity to clear out some junk you 
didn't need, clean up your directory structure, or whatever else.


Final notes
-----------

This process is probably slower than an upgrade, especially considering the step of sorting your old 
files into your new home directory.  However, it gives you very direct control over the process, 
lets you start with a nice clean copy of your operating system, and if done correctly doesn't 
require a full backup to be made.

I much prefer this method to doing an upgrade because it leaves you free of the "old version cruft" 
that accumulates when you upgrade---an operating system upgrade is a complex process and is never 
going to handle every edge case.

If you trust all of your applications to handle old configuration files etc. correctly and you want 
to save some time, you can skip all of the steps relating to moving/copying of your user's home 
directory, so that when you mount your home partition your old home directory is used.  If 
reinstalling rather than upgrading, I tend to do this.

.. caution::

    While I mention that this can be done without a backup, doing so is at your own risk.  Generally 
    speaking it is prudent to backup anything important to somewhere outside of your machine before 
    doing any operating system installation to protect against mistakes.  Otherwise, be extremely 
    careful!  I do things this way because my home directory is always too large to backup anywhere, 
    but I also run an automated nightly backup of the small, important stuff.

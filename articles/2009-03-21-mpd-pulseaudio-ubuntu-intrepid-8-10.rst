MPD + PulseAudio + Ubuntu Intrepid (8.10)
=========================================

:date: 2009-03-21
:category: linux
:tags: ubuntu, pulseaudio, mpd

.. admonition:: Update (2009/04/12)

    It appears that as of Ubuntu Jaunty everything now obeys the system-wide setting properly, so 
    you only need to edit ``/etc/default/pulseaudio`` and add the user to ``pulse-access``.

I'm a big fan of MPD_, and up until the last few months I used it almost exclusively.  It's 
lightweight, it's good at what it does, and there are a lot of different frontends available.  One 
of the things I like most is that it's not tied to a graphical session in any way---you don't need a 
GUI open for it to be playing music.  Normal usage of MPD involves it being started and stopped as a 
system service.

Unfortunately, this doesn't play too nice with the concept of how PulseAudio_ should be used.  
PulseAudio is very user- and session-centric, and the recommended setup means than when nobody is 
logged in, no sound is going to be playing.  While MPD is capable of `playing to a PulseAudio 
server`__ just fine, having the sound server tied to the graphical session means it doesn't have a 
sound device to attach to at boot, and the sound device suddenly disappears if the user logs off.

__ http://mpd.wikia.com/wiki/PulseAudio

Ubuntu has used PulseAudio for as many applications as possible by default since Hardy (8.04), and 
while it can be removed, doing so can make life difficult.  This led me to pursue the option of a 
system-wide instance which everything uses, and which is always running.  But no matter how hard I 
tried, I got stuck with the same bug: starting GNOME would always result in a per-session instance 
being spawned in addition to the system-wide one, the two would fight over the sound card, and I 
would have to manually kill the new one every time I logged in.  Eventually I'd had enough of this 
and started using something else.

Today, I decided to take another stab at getting this set up properly and finding out where that 
second PulseAudio instance was coming from.  Thanks to the help of a couple of people in 
`#pulseaudio on FreeNode IRC`_, I was able to figure out how to do this, so here is the method I 
used for the benefit of anybody else in the same position.


Stop PulseAudio spawning per-session
------------------------------------

By default PulseAudio puts a script in ``/etc/X11/Xsession.d`` which causes a ``pulseaudio`` 
instance to be spawned with every X session.  The first step is to move this script somewhere else 
so it's never run::

    sudo mv /etc/X11/Xsession.d/70pulseaudio /root/

The second cause of ``pulseaudio`` being spawned is less obvious.  There is an Esound_ compatibility 
layer for PulseAudio so that applications depending on it still work, transparently::

    $ ls -l /usr/bin/esd
    lrwxrwxrwx 1 root root 9 2009-03-04 11:03 /usr/bin/esd -> esdcompat

However, as of Ubuntu Intrepid (8.10) there is pretty much nothing which depends solely on Esound, 
but it still gets spawned when GNOME starts.  This causes a PulseAudio session to be spawned for the 
current user if one can't be found.  The simple but ugly fix is to move this link to somewhere 
else::

    sudo mv /usr/bin/esd /usr/bin/esd.bak


Set up a system-wide PulseAudio instance
----------------------------------------

To get PulseAudio to actually start on boot, you need to set a variable to tell the init script you 
want this to happen. Make sure you have the following line in ``/etc/default/pulseaudio``::

    PULSEAUDIO_SYSTEM_START=1

Any users that will be using the system-wide PulseAudio instance need to be members of the correct 
groups. This will most likely be your own user, plus whatever user MPD is running as (``mpd`` by 
default). For each of these users, do::

    sudo usermod -aG pulse-access,pulse,pulse-rt <user>


Getting it up and running
-------------------------

First thing's first, you need to tell MPD to use PulseAudio. This can be achieved by adding the 
following to ``/etc/mpd.conf``::

    audio_output {
        type    "pulse"
        name    "My MPD PulseAudio Output"
    }

If you're feeling lazy, the easiest thing to do right now would be reboot. Otherwise, you'll need to 
kill all ``pulseaudio`` instances, restart the system-wide instance, and restart MPD::

    $ sudo /etc/init.d/mpd stop
     * Stopping Music Player Daemon mpd                   [ OK ]
    $ sudo killall -KILL pulseaudio
    $ sudo /etc/init.d/pulseaudio restart
     * Stopping PulseAudio Daemon                         [ OK ]
     * Starting PulseAudio Daemon                         [ OK ]
    $ sudo /etc/init.d/mpd start
     * Starting Music Player Daemon mpd                   [ OK ]

Finally, log out and log back in again to allow your per-session ``pulseaudio`` instance to die and 
for your new group memberships to take effect.


Caveats
-------

* You get "real-time" processing without any extra effort; by default the system-wide instance will 
  run with priority -11.
* Some apps are not PulseAudio-aware, but they can usually use an ALSA output; `this guide`__ shows 
  you how to redirect ALSA through PulseAudio if you have any problems with the default setup.
* Updates may undo the moving-a-file type of changes.

__ http://www.pulseaudio.org/wiki/PerfectSetup#ALSAApplications

.. _MPD: http://www.musicpd.org/
.. _PulseAudio: http://www.pulseaudio.org/
.. _#pulseaudio on FreeNode IRC: irc://irc.freenode.net/#pulseaudio
.. _Esound: http://en.wikipedia.org/wiki/Enlightened_Sound_Daemon

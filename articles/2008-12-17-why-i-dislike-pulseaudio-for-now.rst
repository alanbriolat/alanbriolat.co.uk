Why I dislike PulseAudio (for now)
==================================

:date: 2008-12-17
:tags: linux, pulseaudio

Before this sounds like a rant, I'd like to first say that I think PulseAudio_ is a very nice 
concept, from a technical perspective.  It's about time Linux got a manageable sound subsystem, and 
some of the features---such as network streaming and synchronised playback---are quite impressive.

However, one thing that really irks me is that, as deployed by major_ distributions_, it appears to 
enforce the narrow-minded view that a desktop is used by only one person, and that sound is only 
ever going to play when somebody is logged in to a graphical session.  Anybody who uses MPD_ has 
probably experienced the pain caused by this already.  Unfortunately my experience so far with 
Ubuntu Intrepid is that trying to change this results in even more pain.  Having set up a 
system-wide instance I'm now in the position where the first time I attempt to play sound works 
correctly, but any subsequent attempts fail until I kill a per-session PulseAudio instance that has 
magically spawned (even though I've set it not to).  Once the per-session instance is dead, I have 
no more problems and everything works perfectly until the next time I log in.

I'm currently trialling Fedora 10 on my desktop, so I'll update this post if I have any more luck 
there.  Feel free to correct me in the comments if I'm just being stupid or missing something!

**Update:** `I've since fixed this problem  
<|filename|/articles/2009-03-21-mpd-pulseaudio-ubuntu-intrepid-8-10.rst>`_.

.. _PulseAudio: http://pulseaudio.org/
.. _major: http://ubuntu.com/
.. _distributions: http://fedoraproject.org/
.. _MPD: http://mpd.wikia.com/wiki/

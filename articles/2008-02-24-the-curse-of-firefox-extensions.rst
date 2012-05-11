The curse of Firefox extensions
===============================

:date: 2008-02-24
:tags: firefox

Today is my first day of Firefox usage after a three-week break - a break which taught me 
something...

First, a little background. I've been using Firefox since 0.9, and generally its always been the 
best browser for me. However, recently I lost my taste for it due to the monumental lack of speed it 
can display sometimes. I mean things like a half-second delay between hitting *Ctrl-T* and being 
able to type in the address bar of the new tab, really long page rendering times, etc. I know that 
Firefox slowness is generally due to extensions, but I relied on most of my extensions. Here is a 
list of the extensions I can remember having:

* AdBlock Plus
* AdBlock Filterset.G updater
* CustomiseGoogle
* Download statusbar
* Firebug
* Flashblock
* Foxmarks
* NoScript
* QuickRestart
* Stop Autoplay
* Stylish
* Tab Mix Plus
* Tiny Menu
* Web developer toolbar

Then I remembered I had tried the Epiphany_ browser (for GNOME_) at some point in the past, and that 
it had been quite snappy. To put it simply, Epiphany is a browser that uses the Gecko rendering 
engine, but doesn't include all the other stuff that slows down Firefox (which I can only assume to 
be the Extension framework and XUL). The upside is that its blindingly fast. The downside is that 
you no longer have all the amazing Firefox extensions you've become used to. One other advantage 
over Firefox is that it already has working tag-based bookmarking (slated for Firefox 3.0).

After forcing myself to cope without my extensions for a day, I started to really enjoy the speed 
and lack of wait-induced stress - Epiphany stays out of my way and gets stuff done really fast. Once 
I had the momentum, I just kept going. I discovered nice stuff like the fact typing in the address 
bar also searches your bookmarks as well as your history (something also in Firefox 3.0). Epiphany's 
UI is reasonably customisable, but not to the extent that Firefox's is.

Eventually I had an epiphany (terrible pun, I know...) - I had just survived 3 weeks without the 
huge number of extensions I came to think I *needed* in Firefox. I now realised I could go back to 
Firefox and use it more sensibly. I threw out my old Firefox profile and started again. I now have 
only the following well-justified extensions:

* Flashblock - on a laptop, unexpected Flash ads = bye-bye battery life
* Foxmarks - because I want my bookmarks on at least 3 different machines
* QuickRestart - no real effect on performance, and sometimes you want to restart Firefox quickly!

.. image:: images/ff-layout.png
    :alt: Condensed Firefox layout
    :width: 100%

I'm happier with this setup than I was with Epiphany, and it's a good trade-off between fancy 
features and responsiveness. One thing I really like about Firefox is the ability to put anything 
anywhere on the toolbars, and I use a fairly condensed layout, so I was also really happy to go back 
to the layout I liked.

In my opinion, the best thing to do when deciding if an extension is worth installing is ask 
yourself the following questions:

* Does it analyse and/or change what I am viewing?
* Does it make comparisons against a large whitelist/blacklist?

Extensions doing either of the above will almost certainly slow your browser down to some extent.  
You will notice that the only content-sensitive extension I have is Flashblock, which is really 
worth it on a laptop.

Another option is to have multiple Firefox profiles, one of which is clean (like my current setup), 
and the other having big slow extensions that you sometimes need, like Firebug. Using the ``-P`` 
option to Firefox you can set up a launcher that starts your second profile instead of the default.

.. _Epiphany: http://www.gnome.org/projects/epiphany/
.. _GNOME: http://www.gnome.org/

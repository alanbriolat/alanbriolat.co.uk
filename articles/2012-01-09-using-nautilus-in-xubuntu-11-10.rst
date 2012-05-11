Using Nautilus in Xubuntu 11.10
===============================

:date: 2012-01-09
:category: linux
:tags: ubuntu, xubuntu, xfce, nautilus
:slug: using-nautilus-in-xubuntu-11-10

Like many people, I've found the new things in the Linux desktop environment world - i.e. GNOME 3 
and Unity - to be more of a hindrance than a help. For this reason I've switched to Xubuntu, which 
allows me to stick to my previous multi-window multi-desktop multi-monitor workflow.

People making this transition might not find themselves too comfortable with XFCE's file manager, 
Thunar. Switching the default file manager to Nautilus (GNOME's file manager) is actually pretty 
simple, however there are a few issues with correctly handling the desktop background and icons. The 
setup described here will switch the default file manager to Nautilus, but leave XFCE and Thunar in 
control of the desktop. This is because Nautilus, if allowed to control the desktop icons, will also 
try and set the desktop background. Complete control of its background settings  is only possible by 
manually editing dconf settings, or using ``gnome-control-center`` which depends on the whole of 
GNOME being installed. Of course if you already have desktop icons disabled you won't notice any 
change in desktop handling at all.

So on with the show.  Obviously, you first need to install Nautilus::

    sudo apt-get install nautilus

Next, you need to tell XFCE to use Nautilus as the default file manager. This can be done through: 
XFCE menu -> Settings -> Settings Manager -> Preferred Applications -> "Utilities" tab -> "File 
Manager" drop-down.

Now any time you open a folder you should get Nautilus instead of Thunar. Unfortunately the first 
time you do this Nautilus will realise it isn't managing the desktop and will try to do so. This 
behaviour can be disabled by setting the appropriate dconf entry::

    sudo apt-get install dconf-tools
    dconf write /org/gnome/desktop/background/show-desktop-icons false

If you have desktop icons enabled in XFCE what you have is an instance of Thunar displaying the 
contents of ``~/Desktop``, which means any directory you double-click on will also launch in Thunar.  
This probably isn't what we want, but unfortunately we can't change this default behaviour.  What we 
can do is make it easier to launch the directory in Nautilus by adding a "custom action" - the end 
result will be a "Open in Nautilus" item in the context menu when you right click directories on the 
desktop.

Launch Thunar and open the "Custom Actions" dialog (Edit -> Configure custom actions...). Add a new 
action, setting the command to ``nautilus %F`` and making sure only "Directories" is checked on the 
"Appearance Conditions" tab. Also check "Startup notification" and set the icon to be the correct 
one for Nautilus.

Of course the nicest result would have been to have Nautilus managing the desktop instead. At first 
glance this looks like it should be possible, since there is a 
``/org/gnome/desktop/background/draw-background``
setting in dconf, however changing this setting has no effect on Nautilus' behaviour.

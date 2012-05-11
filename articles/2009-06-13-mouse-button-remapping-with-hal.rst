Mouse Button Remapping with HAL
===============================

:date: 2009-06-13
:category: linux
:tags: ubuntu, xorg, hal

I've had a Logitech MX1000 mouse for a few years now, and the two most important features for me 
have been the ergonomic build and the few extra buttons.  Something I've always found with 
many-buttoned mice is that the side button closest to the thumb is a much more ergonomic way to 
"middle click" than the actual middle mouse button---it's a much more natural motion.  Middle clicks 
are quite useful these days, especially with them being a standard way of closing tabs (and opening 
them in browsers), and having such a popular button perched on a rocking and rolling peak is far 
from ideal.

Since I'm primarily a Linux user, I don't have Logitech's own SetPoint software at my disposal, so 
I've always had to find a way to get this functionality in some other way.  When I first got the 
mouse, this method involved deliberately using a "basic" mouse driver (referred to in ``xorg.conf`` 
as "IMPS/2"), which didn't support many mouse buttons.  The effect was that the button mappings 
wrapped around, leaving button 8, my preferred "middle click", mapped to button 2 (8 mod 3), the 
real middle button.

Unfortunately, newer Xorg versions became smarter and better capable of handling more buttons, and 
this workaround ceased to function.  For the next while, I used something even more hackish: 
xbindkeys_ combined with xmacroplay_ to simulate a middle click with the following part of my 
.xbindkeysrc::

    "echo ButtonRelease 8 ButtonPress 2 ButtonRelease 2 | xmacroplay -d 0 :0.0 &"
        b:8

The downside to this solution is that there are some cases where the button events don't work 
correctly, one of them being open-in-tab from a bookmark menu in Firefox.  It seemed the best 
solution would be to get Xorg to remap the buttons in such a way that button 8 really was just an 
extra button 2.  The "xinput" utility lets you set button maps in this way---`this wiki entry`__ 
shows how to remap mouse buttons (even if for a different purpose).

__ https://wiki.ubuntu.com/X/Config/Input#Example:_Disabling_middle-mouse_button_paste_on_a_scrollwheel_mouse

This method worked fine, and I put it in my startup programs for GNOME, but it didn't persist after 
suspend/resume.  It appears that when resuming, USB devices get "reattached", and therefore don't 
keep the settings applied to them the last time they were attached.  The workaround for this is to 
set a policy using a HAL (Hardware Abstraction Layer) ``.fdi`` file.  These files live in 
``/etc/hal/fdi/policy`` (at least they do on Ubuntu) and allow you to set various properties on 
input devices.  `This page on the Ubuntu wiki`__ gave me the recipe I needed to remap buttons based 
on the device name.  I ended up with the following ``.fdi`` file (which I saved at 
``/etc/hal/fdi/policy/logitech-mx1000.fdi``):

.. code-block:: xml

    <deviceinfo version="0.2">

    <!-- Remap Logitech MX1000 buttons so that the most accessible side button
         acts as a middle button -->

      <device>
        <match key="info.product" string="Logitech USB RECEIVER">
          <merge key="input.x11_options.ButtonMapping" type="string">1 2 3 4 5 6 7 2</merge>
        </match>
      </device>

    </deviceinfo>

__ https://help.ubuntu.com/community/Logitech_Marblemouse_USB

Now, whenever my Logitech mouse is connected, it gets the buttons remapped---this includes when 
resuming from suspend.  Problem solved... until things are changed again of course!

.. _xbindkeys: http://freshmeat.net/projects/xbindkeys/
.. _xmacroplay: http://xmacro.sourceforge.net/

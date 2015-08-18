(X)ubuntu Linux 14.04 on Asus N550JK laptop
===========================================

:category: linux

I've just acquired a new work laptop (Asus N550JK-CM604H) and for my job the first step was getting 
my preferred Linux distro (Xubuntu 14.04 LTS) up and running on it. However, the laptop is newer 
than the distro release, so I didn't expect it to all be smooth sailing...

The hardware
------------

CPU
    `Intel i7-4720HQ <http://ark.intel.com/products/78934/>`_: 2.6 GHz (3.6 GHz turbo), 4 cores, 8 
    threads, 6MB cache
RAM
    2x4GB DDR3 1600 MHz (`replaced with 2x8GB <http://uk.crucial.com/gbr/en/n550jk/CT5826612>`_)
GPU
    NVIDIA Optimus dual GPU setup:

    * `Intel HD 4600 <http://ark.intel.com/products/78934/>`_, by default using 64MB of system 
      memory as VRAM.
    * NVIDIA GeForce 850M, 2GB dedicated VRAM

    HDMI and mini-DisplayPort external outputs. By default everything goes through Intel GPU; see 
    below for NVIDIA Optimus support.
Display
    15.6" LED-backlit 1080p IPS
Hard drive
    Seagate Momentus ST1000LM024: 1TB SATA-II 5400rpm (replaced with Samsung 850 EVO 500GB)
Wired network
    Realtek RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller; supported by ``r8169`` driver 
    without intervention
Wireless network
    Intel 7260; supported by ``iwlwifi`` driver without intervention
Touchpad
    FocalTech touchpad; see below
Touchscreen
    Atmel maXTouch Digitizer; using ``evdev`` without intervention
Keyboard
    It's a keyboard; see below for details of function keys
Webcam
    Generic USB video class (UVC) 720p webcam; works without intervention (tested in ``camorama``)
Audio/microphone
    Intel High-Definition Audio; using ``snd_hda_intel`` without intervention

LTS Hardware Enablement Stack (HWE)
-----------------------------------

When using an older Linux distro release on a brand new machine, it's likely that some things won't 
be very well supported by whichever kernel and Xorg versions that release froze on. Ubuntu's answer 
to the problem is the `LTS Hardware Enablement Stack 
<https://wiki.ubuntu.com/Kernel/LTSEnablementStack>`_. At the time of writing, the stack based on 
15.04 (Vivid) was the latest, so the following command was used::

    sudo apt-get install --install-recommends \
        linux-generic-lts-vivid xserver-xorg-core-lts-vivid xserver-xorg-lts-vivid \
        xserver-xorg-video-all-lts-vivid xserver-xorg-input-all-lts-vivid \
        libwayland-egl1-mesa-lts-vivid

The only problem with this is that some packages might not be able to build drivers against the new 
kernel. I found this to be the case for VirtualBox, but using the latest version available from the 
VirtualBox site gets around this.

Suspend
-------

I decided to try out suspend and resume early on, since historically it's been a fairly quirky area 
of hardware support. In this case, the ``nouveau`` driver barfed into the logs and prevented sleep. 
Blacklisting it seems to fix the problem: add ``blacklist nouveau`` to 
``/etc/modprobe.d/blacklist-nouveau.conf``. This was no big deal, since I'm either using the Intel 
GPU or the proprietary NVIDIA drivers.

Graphics driver
---------------

Like a lot of decent modern laptops, this one has a dual-GPU setup: the Intel HD 4600 as part of the 
CPU, and an NVIDIA 850M.

As is to be expected, the Intel GPU just works. The HWE upgrade enabled DisplayPort 1.2 Multi-Stream 
Transport (MST) support, which allowed me to daisy-chain my `Dell U2515H 
<http://www1.euro.dell.com/uk/en/home/Peripherals/dell-u2515h-monitor/pd.aspx>`_ monitors which 
support this feature. (Note: the monitors ship with this feature disabled, you need to enable it in 
the OSD on each monitor.)

The NVIDIA GPU was less straightforward: at the time of installing, the latest NVIDIA drivers in the 
Ubuntu 14.04 repos would not build against the 3.19 kernel from 15.04. Luckily, the backported newer 
drivers were added within a couple of weeks.

There are two ways to enable NVIDIA support on a laptop like this: using "Bumblebee" to allow 
per-application use of the NVIDIA GPU, or using "NVIDIA Prime" to switch the entire desktop 
environment between GPUs (requires logging out and back in again). Because I don't intend to make 
much use of the NVIDIA GPU, I opted for the latter::

    sudo apt-get install nvidia-346-updates nvidia-prime

By default the Intel GPU should remain selected. The GPU can be switched from the 
``nvidia-settings`` control panel.

Touchpad driver
---------------

The laptop has a FocalTech touchpad, which I hadn't heard of before, and which isn't handled 
properly even in the 3.19 kernel from Ubuntu 15.04. Luckily, these touchpads seem to be used in 
multiple Asus laptops now, and Ask Ubuntu had an answer: `Asus X750JA and Ubuntu Gnome 14.04 
<http://askubuntu.com/a/611936/12021>`_.  Following those instructions and rebooting, the touchpad 
had gained two-finger vertical scrolling, edge scrolling, and also the ability to use ``synclient`` 
to tweak the settings.

In terms of customising the touchpad behaviour, I put the following in my ``~/.xprofile``::

    synclient HorizTwoFingerScroll=1 \
              VertEdgeScroll=0 \
              TapButton3=2 \
              PalmDetect=1

* Enable 2-finger scrolling horizontally (vertical 2-finger scroll is enabled by default)
* Disable vertical edge scrolling, since I'm just going to be using 2-finger scrolling all the time
* Turn 3-finger taps into a "middle button" click (2-finger taps are "right click" by default)
* Enable palm detection, to try and get rid of spurious inputs when typing


Keyboard
--------

It's a keyboard. It generally works as well as you'd expect for one of the oldest standard bits of 
computer hardware. What tends to vary these days is of course the special/"fn" keys on the keyboard.  
This one has several. Going left-to-right, top-to-bottom:

Sleep key
    Is recognised by power management functionality: if you have it set to suspend when the sleep 
    button is pressed, pressing this key will suspend the same as via any other route.
Wireless toggle
    Not registered at all; see below for fix.
Decrease/increase display brightness
    Not registered at all; see below for fix.
Toggle display
    Seems to switch the laptop screen off and on, not sure where this is handled.
Select display mode
    This key is horrible. Really really horrible. So horrible it needs its own subsection (see 
    below).  Needless to say, it doesn't work properly.
Toggle touchpad
    Recognised as ``XF86TouchpadToggle``, but nothing actually uses it.
Mute/increase/decrease volume
    Recognised and behave as expected.
Box with an "S" in it?
    Recognised as ``XF86Launch1``.
Camera
    Recognised as ``XF86WebCam``.
Running person?
    Recognised as ``XF86Launch6``.
Stop/prev/play-pause/next
    Recognised as ``XF86AudioStop``, ``XF86AudioPrev``, ``XF86AudioPlay`` and ``XF86AudioNext``.
Calculator
    Launches calculator.

Wireless toggle and display brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Out of the box, the display brightness and wireless toggle keys are completely unrecognised and 
generate no events. It seems that this is a bit of ACPI quirkiness that is documented here: `Fixing 
Display Backlight Hotkeys on ASUS N550JK 
<http://blog.yjwong.name/fixing-display-backlight-hotkeys-on-asus-n550jk/>`_. The TL;DR is:

* add ``acpi_osi=`` to your ``GRUB_CMDLINE_LINUX_DEFAULT`` in ``/etc/default/grub``
* run ``sudo update-grub``
* reboot

That horrible "Select display mode" key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In Windows, there is a ``Win + P`` combination that opens a quick display selector (for handling an 
external monitor).  This key seems to try and emulate pressing this key combination. When you press 
``Fn + F8`` to use this function, it seems to emit the following keycode events:

* 133 down
* 33 down
* 33 up
* 133 up

Keycode 133 is known as ``Super_L`` in Linux, or the left Windows key in common parlance. Keycode 33 
is the ``P`` key. But those are keycode events, which means if you use an alternative keyboard 
layout (e.g. Dvorak) you get a different effect (e.g. ``Win+L``). I give up on doing anything useful 
with this key.

Final words
-----------

The laptop makes a pretty adequate desktop replacement, and all of the hardware should be 
well-supported by an up-to-date Linux distro. However, for those that opt for a long-term stable 
releases, I hope documenting the quirks I encountered will help somebody in a similar situation.

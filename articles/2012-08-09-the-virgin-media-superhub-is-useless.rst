The Virgin Media "Superhub" is Useless
======================================

:date: 2012/06/12
:status: draft

I'm sure if I'd listened other people would have told me this, but instead I've had to find out for 
myself: the Virgin Media Superhub is a shining example of all that is wrong with "consumer" network 
equipment.  The goal is the cheapest possible piece of equipment, and the result is something which 
takes any shortcut possible to get there, including giving all accepted practices the middle finger.

ARP? Who needs ARP?
-------------------

To actually get Ethernet packets to their destination the MAC address needs to be known.  Address 
Resolution Protocol, or ARP_, is the standard way that network devices resolve IP (network layer) 
addresses to MAC (link layer) addresses.  If you run wireshark (or another packet logger) you'll 
probably see ARP broadcasts, usually phrased like ``Who has 192.168.0.2?  Tell 192.168.0.1``.  This 
is how one network interface discovers another when all it knows is the IP address.

But, if we take a step back, there's another way that a router might already know the associated MAC 
address for an IP address: if it assigned that IP address over DHCP.  If you make the assumption 
that there is only one DHCP server, and all IP addresses are assigned by that DHCP server, then the 
DHCP server sort of has a complete picture of the network.

Well, it looks like the Superhub uses this as a wholly inappropriate shortcut.  If a machine uses 
DHCP then it's always accessible just fine.  If you set a static IP, the machine should send an ARP 
announcement and the Superhub will see it for a while.  However, once the Superhub clears its ARP 
cache it will forget about the machine *and never try and find it again*.  They seem to have assumed 
the DHCP server has the complete picture and didn't bother to implement ARP properly.  If you use 
static IPs (different to static DHCP leases!) your machines will disappear off the network for no 
obvious reason.

HTTP Error Codes? Meh.
----------------------

The web interface of the router is laughable.  Let's skip over the way they manage to break standard 
browser functionality and make usability a nightmare, and instead focus on the technical problems.  
When an HTTP server gets an invalid HTTP request, it should return an error that signifies as such.  
But why bother if you stupidly think you're in control of every request that could possibly go to 
the router?

So this is what the Superhub does: on an unrecognised GET request, it just terminates the 
connection.  No 404, no 500, nothing useful, just terminated.  On an invalid POST request it crashes 
the router.  Not an error.  Not even crashing the web interface.  It crashes the router, rendering 
it completely useless until it's power cycled.

Conclusion
----------

From the behaviour I've experienced so far, I can only conclude that the Superhub's software has 
been cobbled together by a team with a serious case of Not Invented Here syndrome but lacking the 
actual competency to implement things for themselves.  The end result is a very fragile system that 
only works correctly in an extremely limited set of use cases, and falls over the moment anything 
other than "person points laptop at wireless" happens.  (Although by all accounts it's not 
particularly good at that either.)

This gets to join my long list of ISP routers that get put in modem/bridged mode, attached to a 
*real* router and forgotten about.


.. _ARP: http://en.wikipedia.org/wiki/Address_Resolution_Protocol

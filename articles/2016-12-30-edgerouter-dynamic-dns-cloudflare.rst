EdgeRouter + Dynamic DNS + Cloudflare
=====================================

.. note::

    This no longer works. The version of ``ddclient`` in EdgeOS uses the CloudFlare v1 API, which 
    was `deprecated November 2016 
    <https://blog.cloudflare.com/sunsetting-api-v1-in-favor-of-cloudflares-current-client-api-api-v4/>`_ 
    and finally retired June 2018. I now use `cloudflare-ddns 
    <https://github.com/ethaligan/cloudflare-ddns>`_ running on a server inside my network.

My home network sits on a fast internet connection behind an Ubiquiti Networks `EdgeRouter X`_ but
doesn't have the benefit of a static IP address.  I've been meaning to set up a dynamic DNS entry
for it for a while, but really wanted to make use of the fact I already manage my DNS with
Cloudflare, which has a very capable API.  Ubiquiti's EdgeOS has support for dynamic DNS by
generating ``ddclient`` configurations and running them when the IP address changes, however the web
GUI doesn't support everything that is possible with its ``ddclient`` version.

There are existing solutions to this problem, for example this `support article`_
easily found through a search engine.  However, the solutions I've found are clunky hacks that will
be missed by configuration backups, and therefore more confusing to reproduce in the future if
necessary.  I wanted something that would exist properly within the EdgeOS configuration system.

Through trial and error, I found there are only two small things preventing Cloudflare support from
working, and both can be easily sidestepped.

1. The web GUI doesn't provide the ``cloudflare`` protocol in the drop-down.  Using the EdgeOS
   configuration CLI allows this value to be specified manually.
2. The EdgeOS configuration schema doesn't allow for the ``zone`` setting required by the
   ``cloudflare`` protocol.  Because ``ddclient`` configuration is basically a comma-separated
   list of ``option=value`` pairs, the setting can be injected as part of another setting, as long
   as the schema validation doesn't prevent it.  The ``host-name`` setting currently allows it, e.g.
   ``home.example.com`` becomes ``zone=example.com,home.example.com``.

Armed with this knowledge, the dynamic DNS client can be configured with the following commands::

    configure
    set service dns dynamic interface eth0 service custom-cloudflare login {{EMAIL}}
    set service dns dynamic interface eth0 service custom-cloudflare password {{API_KEY}}
    set service dns dynamic interface eth0 service custom-cloudflare protocol cloudflare
    set service dns dynamic interface eth0 service custom-cloudflare server www.cloudflare.com
    set service dns dynamic interface eth0 service custom-cloudflare host-name zone={{DNS_ZONE}},{{HOSTNAME}}
    commit
    save
    exit

``eth0``
    On my EdgeRouter X, ``eth0`` is configured as the WAN link.  Replace as appropriate on other
    setups, this should be the interface that will have your external public IP address.
``{{EMAIL}}``
    The email address you use to login to Cloudflare.
``{{API_KEY}}``
    Your Cloudflare "Global API Key", which you can get at https://www.cloudflare.com/a/account/my-account.
``{{DNS_ZONE}}``
    The Cloudflare-managed domain that the desired DNS entry exists under, e.g. ``example.com``.
``{{HOSTNAME}}``
    The DNS entry that should be modified, e.g. ``home.example.com``.

.. note::

    This article is based on my experience with an EdgeRouter X running EdgeOS 1.9.0.  The
    instructions may work with older versions of EdgeOS and should work on other EdgeRouter models,
    but I haven't tested those other possibilities.

.. _EdgeRouter X: https://www.ubnt.com/edgemax/edgerouter-x/
.. _support article: https://help.ubnt.com/hc/en-us/articles/204976324-EdgeMAX-Custom-Dynamic-DNS-with-Cloudflare

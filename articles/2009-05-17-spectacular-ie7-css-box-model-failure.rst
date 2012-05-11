Spectacular IE7 CSS box model failure
=====================================

:date: 2009-05-17
:category: programming
:tags: css, internet explorer

When re-theming DokuWiki_ to fit in with the general look-and-feel of my blog, I thought it would 
look good to have buttons with images relevant to what they did.  Having created the necessary, CSS, 
I subjected it to my `multi-browser test bed`_ (actually a Windows XP virtual machine with the 
latest versions of the top 5 browsers running in it).  The CSS I used was along the lines of this:

.. code-block:: css

    div.dokuwiki form.btn_show .button {
        padding: 1px 0 1px 16px;
        background: transparent url(images/page.png) 0px 1px no-repeat;
        border: none;
    }

One thing that became apparent is that IE7 has absolutely no idea how to render this.  The correct 
rendering (as produced by Firefox 3 and all the other browsers) is this:

.. image:: images/button-background-image-ff3.png
    :align: center

IE7's take on rendering this looked more like this:

.. image:: images/button-background-image-ie7.png
    :align: center

After a bit more experimentation, I came up with the following illustration which roughly shows what 
is happening:

.. image:: images/IE7-button-rendering.png
    :align: center

The nice thing is that this is fixed in the upcoming IE8, so I've taken the stress-free approach; 
since it's a relatively "minor" visual bug, there's no sense it tearing my hair out trying to make 
it render correctly everywhere.  On this occasion I've decided that people can either deal with the 
fact their browser is behind the times, or upgrade, or wait for the upgrade to happen for them.

.. _DokuWiki: http://dokuwiki.org/
.. _multi-browser test bed: http://iris.codescape.net/~alan/IE-rendering-fail-3.png

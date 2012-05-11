Tpl - A tiny PHP template engine
================================

:date: 2009-04-30
:category: programming
:tags: php

While developing `CodeScape Framework`_ I came up with a simple template engine that instead of 
implementing it's own language just provided some structure-related hooks, and I've now got around 
to separating out and releasing Tpl_, a simple, self-contained, hierarchical template engine for 
PHP.

Tpl's role is centred around template structure, not content---it's not a huge library of helper 
functions for creating links, displaying images, etc.  Like any template engine, the aim is to 
separate presentation logic from application logic, but it doesn't attempt this by creating a 
template language.  PHP is designed__ to be interleaved with "static" output, which means it's 
already a template language.  Trying to replace it for the purpose of templating rarely adds 
anything useful, incurs hefty performance overheads (which you then have to mitigate with caching) 
and usually is more restrictive than PHP.  To me, that doesn't seem like a sensible application of 
effort.  Instead Tpl provides its functionality in the form of hooks---functions which are called 
from within the template to specify the structure.  Instead of PHP being replaced, it is extended.

__ http://php.net/manual/en/history.php.php

The main motivating factor for creating Tpl is that all PHP template engines seem to be centred 
around *inclusion* rather than *inheritance*, something I only noticed after spending time working 
with Django_.  For example, a typical PHP template might look like this:

.. code-block:: php

    <!-- header.php -->
    <html>
        <head><title><?=$title?></title></head>
        <body>
            <div id="header">Website Name</div>   

.. code-block:: php

    <!-- footer.php -->
            <div id="footer">Some footer text</div>
        </body>
    </html>

.. code-block:: php

    <!-- content.php -->
    <? include('header.php'); ?>

    <div id="content">
        Some content
    </div>

    <? include('footer.php'); ?>

The main problem with this is that it bears no real relation to the logical structure of the page, 
just the order in which stuff should appear in the HTML.  If you modify something in the header, you 
need to make sure you've updated the footer too.  The equivalent Django template would look like 
this:

.. code-block:: django

    {# base.html #}
    <html>
        <head><title>{{ title }}</title></head>
        <body>
            <div id="header">Website Name</div>

            {% block content %}{% endblock %}

            <div id="footer">Some footer text</div>
        </body>
    </html>

.. code-block:: django

    {# content.html #}
    {% extends "base.html" %}

    {% block content %}
    <div id="content">
        Some content
    </div>
    {% endblock %}


The point to note is that the structure is coherent and in one place, and the parts that change are 
defined as logical blocks which can be replaced.  This is the method I've adopted in Tpl---the 
equivalent template would look like this:

.. code-block:: php

    <!-- base.php -->
    <html>
        <head><title><?=$C['title']?></title></head>
        <body>
            <div id="header">Website Name</div>

            <? Tpl::block('content'); ?><? Tpl::endblock(); ?>

            <div id="footer">Some footer text</div>
        </body>
    </html>

.. code-block:: php

    <!-- content.php -->
    <? Tpl::inherit('base.php'); ?>

    <? Tpl::block('content'); ?>
    <div id="content">
        Some content
    </div>
    <? Tpl::endblock(); ?>

More information about Tpl and how to download it can be found at the `Tpl project page`__.

__ Tpl_

.. _CodeScape Framework: http://codescape.net/csf/
.. _Tpl: http://codescape.net/tpl/
.. _Django: http://www.djangoproject.com/

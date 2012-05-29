Optional Positional Arguments with argparse
===========================================

:date: 2012-05-29
:category: programming
:tags: python

Today I helped somebody in the Python IRC channel with a question about
combining required, optional and multi-value positional arguments in Python's
argparse_ module.  This is actually pretty easy to do, but not immediately
obvious, so here's the example I put together.  I took hints from the first
example in the argparse_ documentation, and also `this StackOverflow answer`_.

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('foo', default='a')
    parser.add_argument('bar', default='b', nargs='?')
    parser.add_argument('baz', default=[], nargs='*')
    print parser.parse_args()

And does it work?  Apparently so.  Some example output from running this
script::

    $ python test.py
    usage: test.py [-h] foo [bar] [baz [baz ...]]
    test.py: error: too few arguments

    $ python test.py x
    Namespace(bar='b', baz=[], foo='x')

    $ python test.py x y
    Namespace(bar='y', baz=[], foo='x')

    $ python test.py x y z
    Namespace(bar='y', baz=['z'], foo='x')

    $ python test.py x y z a
    Namespace(bar='y', baz=['z', 'a'], foo='x')

.. _argparse: http://docs.python.org/library/argparse.html
.. _this StackOverflow answer: http://stackoverflow.com/a/4480202/373258

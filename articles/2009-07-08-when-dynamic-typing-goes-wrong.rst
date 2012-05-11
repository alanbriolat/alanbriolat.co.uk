When Dynamic Typing Goes Wrong
==============================

:date: 2009-07-08
:category: programming
:tags: php

Yesterday I found out first-hand how using a dynamically typed language can get you into trouble in 
unexpected ways whilst writing unit tests for CSF_ (my PHP framework).

Take a look at this code---what do you think it should do?

.. code-block:: php

    $foo = 'bar';
    var_dump(isset($foo['xyz']));
    var_dump($foo['xyz']);

Most people would assume that indexing a string on another string is nonsensical, and they would be 
right---in PHP you can only index a string with an integer.  The logical extension would be that 
``isset($foo['xyz']``) would be false and/or any attempt to index using a string would raise an 
error.  And that is where they would be wrong.  In fact, ``isset($foo['xyz'])`` is ``true``, and 
``$foo['xyz']`` is ``"b"``.

PHP is `weakly typed`_, which generally means there is a lot of implicit casting between types going 
on.  In this case, while indexing a string can only be done with an integer, there is an implicit 
cast from a string to an integer, so this cast is performed and the result used as the index.  
However, the usual way of converting from a string to an integer is to use digits (0--9) up until 
the first non-digit character (after taking the minus sign into account if there is one).  This 
means the integer value of 'xyz' is 0, since there are no digits to add up.

When explained, this may seem like sensible behaviour, but let's think about the effect this has 
when coding and debugging: if you accidentally index a string with another string somewhere, you 
won't know about it straight away.  Instead, you'll just be getting "wrong" values and scratching 
your head over where they could be coming from.  I'm of the opinion that if you can only index a 
string on an integer, then indexing it on a string should be at the very least a warning.  Silently 
doing something completely different isn't very helpful.

And so that this doesn't seem like a nonsensical contrived example, here's a reduced version of the 
code that raised the issue:

.. code-block:: php

    function get_item($array, $path, $default)
    {
        $item = $array;
        foreach (explode('.', $path) as $p)
        {
            if (!isset($item[$p]))
            {
                if (func_num_args() < 3)
                    throw new ItemNotFound($path);
                else
                    return $default;
            }
            else
            {
                $item = $item[$p];
            }
        }
        return $item;
    }

What this function does is traverse a multi-dimensional array with a "key path", i.e.  
``"key1.key2"`` gets ``$array['key1']['key2']``.  Since ``isset()`` is the most common way people 
check the existence of an array, this is what I used here.  However, things break down in this 
example:

.. code-block:: php

    $array = array('foo' => 'bar');
    $x = get_item($array, 'foo.xyz');

The expected behaviour is that the exception should be thrown, since ``$array['foo']`` is not an 
array with a ``"xyz"`` key, but the issue described above instead leads this to return ``"b"``.

In this case, there is a way around it: what I really should have been using is the following check:

.. code-block:: php

    if (is_array($item) && array_key_exists($p, $item))

This has more interesting consequences---it means that a very very large number of people are using 
``isset()`` where they mean ``is_array() && array_key_exists()``.  As for me, I just fixed a bug in 
my code exposed by a unit test, so I'm happy (even if a little bewildered by PHP).

.. _CSF: http://codescape.net/csf/
.. _weakly typed: http://en.wikipedia.org/wiki/Weak_typing

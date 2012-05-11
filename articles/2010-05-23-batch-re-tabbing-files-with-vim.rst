Batch Re-tabbing Files with Vim
===============================

:date: 2010-05-23
:tags: vim, bash

So you have your favourite tabbing convention, but you've ended up with some files in some other 
convention, for example tabs instead of 4 spaces.  If you use Vim and already have it set up to your 
liking, the ``:retab`` command will replace indents in the current buffer with those matching your 
convention.  It's a bit tedious to do this manually for each file, so if you trust Vim not to make a 
mistake (or you're using version control) you can use a bit of scripting-fu to make it easier:

.. code-block:: bash

    for F in *.{c,h}pp ; do vim -c ":retab" -c ":wq" "$F" ; done

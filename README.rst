How to develop/deploy
=====================

Why would you want to deploy my website?  Probably only if you're me.  So
assuming I'm my own audience, I'm going to write a reminder of how I checkout
and build this damned thing.

::

    virtualenv2 virtualenv
    source virtualenv/bin/activate
    pip install -r requirements.txt
    pelican -s pelican.conf.py -v
    cd output/
    python -m SimpleHTTPServer 8000

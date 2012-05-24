How to develop/deploy
=====================

Why would you want to deploy my website?  Probably only if you're me.  So
assuming I'm my own audience, I'm going to write a reminder of how I checkout
and build this damned thing.

::

    virtualenv virtualenv
    source virtualenv/bin/activate
    git submodule init
    git submodule update
    pushd pelican
    python setup.py develop
    popd
    npm install less
    pelican -s pelican.conf.py -v --theme=themes/digitalambulation/
    cd output/
    python -m SimpleHTTPServer 8000

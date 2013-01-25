Arch Linux + nginx + Passenger + Redmine
========================================

:date: 2012/06/12
:category: linux
:status: draft

The general procedure:

::

    sudo pacman -S nginx passenger
    sudo mkdir -p /webapps/redmine
    cd /webapps
    sudo chown alan:users -R redmine
    git clone https://github.com/redmine/redmine.git redmine
    cd redmine
    git checkout -b deploy origin/2.0-stable
    # Install as normal
    chmod go-rwx db config

Arch Linux makes life easy for us: the nginx in the repositories is built with Passenger support.  
We just need to install both::

    sudo pacman -S nginx passenger

In ``nginx.conf``::

    # Somewhere in the "http" section
    passenger_root /usr/lib/passenger;

    # The redmine "server" section
    server {
        listen 80;
        server_name redmine.example.com;
        root /webapps/redmine/public;
        passenger_enabled on;
    }

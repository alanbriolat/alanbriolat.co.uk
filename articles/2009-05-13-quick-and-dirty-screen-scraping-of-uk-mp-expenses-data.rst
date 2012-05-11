Quick and dirty screen scraping of UK MP expenses data
======================================================

:date: 2009-05-13
:category: programming
:tags: python

A dominating story in the news recently has been that of UK Members of Parliament "abusing" the 
expenses system.  As part of this, expense claims data has been released to the public, but 
unsurprisingly not in a simple CSV format that just anybody can play with.  All I could find were 
PDF files and news sites representing the data in their own way.

This led me to wonder how easy it would be to "scrape" the data from one of these sites.  Having 
heard about BeautifulSoup_, a Python HTML "tag soup" parser, I opened up an interactive Python 
session and started to play with the data from `this BBC News page`__.  Luckily for me, the BBC 
page's HTML isn't *too* ugly, so figuring out how to get the data rows wasn't that hard.

__ http://news.bbc.co.uk/1/hi/uk_politics/8044207.stm

The end result is the following Python script which scrapes the data from the BBC News page and 
saves it in both CSV and JSON formats

* `mp-expenses-extract.py <downloads/mp-expenses-extract.py>`_
* `mp-expenses.csv <downloads/mp-expenses.csv>`_
* `mp-expenses.json <downloads/mp-expenses.json>`_

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/

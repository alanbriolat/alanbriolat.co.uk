#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib, json, string

# Get the content of the page
print "Fetching page from http://news.bbc.co.uk/1/hi/uk_politics/8044207.stm ..."
doc = urllib.urlopen('http://news.bbc.co.uk/1/hi/uk_politics/8044207.stm').read()
print "Done!"

# Strip non-ASCII characters - life's just easier this way...
doc = filter(lambda c: ord(c) < 128, doc)

# Parse the HTML
print "Parsing HTML with BeautifulSoup"
soup = BeautifulSoup(doc)

# Get the rows of the table
rows = soup.find('table', id='expenses_table').find('tbody').findAll('tr')

# Lets get some tuples!
print 'Extracting data from <table id="expenses_table">'
raw = list()
for r in rows:
    items = r.findAll('td')
    raw.append( (items[0].string if items[0].string else items[0].find('a').string,
                 items[1].find('span').string,
                 items[2].string.replace('&amp;', '&') if items[2].string else '',
                 int(str(items[3].string).translate(None, '*,')),
                 int(str(items[4].string).translate(None, '*,')),
                 int(str(items[5].string).translate(None, '*,')),
                 int(str(items[6].string).translate(None, '*,')),
                 int(str(items[7].string).translate(None, '*,')),
                 int(str(items[8].string).translate(None, '*,')),
                 int(str(items[9].string).translate(None, '*,')),
                 int(str(items[10].string).translate(None, '*,')),
                 int(str(items[11].string).translate(None, '*,')),
                 int(str(items[12].string).translate(None, '*,')),
                 int(str(items[13].find('strong').string).translate(None, '*,'))) )

fields = ('MP',
          'Party',
          'Seat',
          '2nd home allowance',
          'London supplement',
          'Office',
          'Staffing',
          'Central stationery',
          'Stationery & postage',
          'IT provision',
          'Staff cover',
          'Communications',
          'Travel',
          'Total')

# Print as CSV
import csv
csvwriter = csv.writer(open('mp-expenses.csv', 'w'))
csvwriter.writerow(fields)
csvwriter.writerows(raw)
print "Wrote CSV data to mp-expenses.csv"

# Print as JSON
import json
asdicts = [dict(zip(fields, values)) for values in raw]
json.dump(asdicts, open('mp-expenses.json', 'w'), indent = 1)
print "Wrote JSON data to mp-expenses.json"

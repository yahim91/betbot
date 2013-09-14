#!/usr/bin/env python
import urllib
import urllib2
from bs4 import BeautifulSoup
from lxml import etree

query = urllib.urlencode(dict(html=1, id=1827, language="en", clientid=4, state="2_1,3_77,22_1,5_6545,9_fixtures,231_full,23_1", callback="d1638d1b7124469e2d6570b99c04829b1c5be"))
url = "http://s4dev.betradar.com/gismo.php?"
resp = urllib2.urlopen("http://s4dev.betradar.com/gismo.php?" + query)
year_queries = {'11/12': urllib.urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_3539,9_fixtures,231_full,23_1",
                                                callback="70d11da1bff5b9fe44d6317c913875cad0f39e7a"
                                               )
                                          ),
                '12/13': urllib.urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_4682,9_fixtures,231_full,23_1",
                                                callback="f0c0834608f53b75ccfdde88d432405dce3b0add"
                                               )
                                          )
                }

exact_goals = dict()
total_fixtures = 0
for year, query in year_queries.items():
    data = urllib2.urlopen(url + query)
    print 'Gathered data for ' + year
    root = etree.XML(data.read())
    tree = etree.ElementTree(root)
    raw_fixtures = root.findall(".//n[@c='couch_fixtures']/c")[0].text
    fixtures = BeautifulSoup(raw_fixtures)
    for result in fixtures.find_all("td", attrs = {'class': 'nt ftx '}):
        if (result.text == 'Postponed'):
            continue
        total_fixtures += 1
        space = result.text.find(':')
        goals = int(result.text[:space]) + int(result.text[space + 1:])
        if (goals not in exact_goals):
            exact_goals[goals] = {'amount': 1, 'last_occurence': total_fixtures}
        else:
            exact_goals[goals]['amount'] += 1
            exact_goals[goals]['last_occurence'] = total_fixtures

for key, value in exact_goals.items():
    exact_goals[key]['prob'] = (float(value['amount'])/total_fixtures) * 100
    exact_goals[key]['#_of_fixt_since_last'] = total_fixtures - exact_goals[key]['last_occurence']
print exact_goals

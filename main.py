#!/usr/bin/env python
import urllib
import urllib2
from bs4 import BeautifulSoup
from lxml import etree
from collections import OrderedDict

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
                                          ),
                '13/14': urllib.urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_6545,9_fixtures,231_full,23_1",
                                                callback="98ad1638d1b7124469e2d6570b99c04829b1c5be"
                                               )
                                          )
                }

exact_goals = dict()
over_goals = {'3.5': {'amount': 0, 'value': 3.5}}
half_time = {'home wins': {'amount':0},
             'draws': {'amount': 0},
             'away wins': {'amount': 0}}

full_time = {'home wins': {'amount':0},
             'draws': {'amount': 0},
             'away wins': {'amount': 0}}

half_full_time = {'1-1':{'amount': 0},
                  '1-X':{'amount': 0},
                  '1-2':{'amount': 0},
                  'X-X':{'amount': 0},
                  'X-1':{'amount': 0},
                  'X-2':{'amount': 0},
                  '2-2':{'amount': 0},
                  '2-X':{'amount': 0},
                  '2-1':{'amount': 0}}

correct_score = {}
total_fixtures = 0
for year, query in OrderedDict(sorted(year_queries.items(), key=lambda t: t[0])).items():
    data = urllib2.urlopen(url + query)
    print 'Gathered data for ' + year
    root = etree.XML(data.read())
    tree = etree.ElementTree(root)
    raw_fixtures = root.findall(".//n[@c='couch_fixtures']/c")[0].text
    fixtures = BeautifulSoup(raw_fixtures)
    for result in fixtures.find_all("td", attrs = {'class': 'nt ftx '}):
        if (result.text == 'Postponed' or result.text == ''):
            continue
        total_fixtures += 1
        #Computing half time result
        half_time_result = result.find_previous_sibling('td', attrs={'class': 'p1 '})
        space = half_time_result.text.find(':')
        half_time_exists = False
        if (space != -1):
            half_time_exists = True
            half_time_home_goals = int(half_time_result.text[:space])
            half_time_away_goals = int(half_time_result.text[space + 1:])

            #Computing half_time stats
            if (half_time_home_goals > half_time_away_goals):
                half_time['home wins']['amount'] += 1
                half_time['home wins']['last_occurence'] = total_fixtures
            elif (half_time_home_goals == half_time_away_goals):
                half_time['draws']['amount'] += 1
                half_time['draws']['last_occurence'] = total_fixtures
            else:
                half_time['away wins']['amount'] += 1
                half_time['away wins']['last_occurence'] = total_fixtures


        #Computing final result
        space = result.text.find(':')
        full_time_home_goals = int(result.text[:space])
        full_time_away_goals = int(result.text[space + 1:])
        goals = full_time_home_goals + full_time_away_goals

        #Computing full_time stats
        if (full_time_home_goals > full_time_away_goals):
            full_time['home wins']['amount'] += 1
            full_time['home wins']['last_occurence'] = total_fixtures

            #Computing half_full_time stats
            if (half_time_home_goals > half_time_away_goals):
                half_full_time['1-1']['amount'] += 1
                half_full_time['1-1']['last_occurence'] = total_fixtures
            elif (half_time_home_goals == half_time_away_goals):
                half_full_time['X-1']['amount'] += 1
                half_full_time['X-1']['last_occurence'] = total_fixtures
            else:
                half_full_time['2-1']['amount'] += 1
                half_full_time['2-1']['last_occurence'] = total_fixtures

        elif (full_time_home_goals == full_time_away_goals):
            full_time['draws']['amount'] += 1
            full_time['draws']['last_occurence'] = total_fixtures

            #Computing half_full_time stats
            if (half_time_home_goals > half_time_away_goals):
                half_full_time['1-X']['amount'] += 1
                half_full_time['1-X']['last_occurence'] = total_fixtures
            elif (half_time_home_goals == half_time_away_goals):
                half_full_time['X-X']['amount'] += 1
                half_full_time['X-X']['last_occurence'] = total_fixtures
            else:
                half_full_time['2-X']['amount'] += 1
                half_full_time['2-X']['last_occurence'] = total_fixtures

        else:
            full_time['away wins']['amount'] += 1
            full_time['away wins']['last_occurence'] = total_fixtures

            #Computing half_full_time stats
            if (half_time_home_goals > half_time_away_goals):
                half_full_time['1-2']['amount'] += 1
                half_full_time['1-2']['last_occurence'] = total_fixtures
            elif (half_time_home_goals == half_time_away_goals):
                half_full_time['X-2']['amount'] += 1
                half_full_time['X-2']['last_occurence'] = total_fixtures
            else:
                half_full_time['2-2']['amount'] += 1
                half_full_time['2-2']['last_occurence'] = total_fixtures


        # Computing exact_goals stats
        if (goals not in exact_goals):
            exact_goals[goals] = {'amount': 1, 'last_occurence': total_fixtures}
        else:
            exact_goals[goals]['amount'] += 1
            exact_goals[goals]['last_occurence'] = total_fixtures

        #Computing over ? goals stats
        for key, value in over_goals.items():
            if (value['value'] < goals):
                over_goals[key]['amount'] += 1
                over_goals[key]['last_occurence'] = total_fixtures

        #Computing correct_score stats

        score = repr(full_time_home_goals) + '-' + repr(full_time_away_goals)
        if (score not in correct_score):
            correct_score[score] = {'amount': 1, 'last_occurence': total_fixtures}
        else:
            correct_score[score]['amount'] += 1
            correct_score[score]['last_occurence'] = total_fixtures


#Computing half_time probability
for key, value in half_time.items():
    half_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    half_time[key]['#_of_fixt_since_last'] = total_fixtures - half_time[key]['last_occurence'] + 1
    half_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100

#Computing full_time probability
for key, value in full_time.items():
    full_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    full_time[key]['#_of_fixt_since_last'] = total_fixtures - full_time[key]['last_occurence'] + 1
    full_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100

#Computing half_full_time probability
for key, value in half_full_time.items():
    half_full_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    half_full_time[key]['#_of_fixt_since_last'] = total_fixtures - half_full_time[key]['last_occurence'] + 1
    half_full_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100

#Computing exact_goals probability
for key, value in exact_goals.items():
    exact_goals[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    exact_goals[key]['#_of_fixt_since_last'] = total_fixtures - exact_goals[key]['last_occurence'] + 1
    exact_goals[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100

#Computing over_goals probability
for key, value in over_goals.items():
    over_goals[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    over_goals[key]['#_of_fixt_since_last'] = total_fixtures - over_goals[key]['last_occurence'] + 1
    over_goals[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100

#Computing correct_score probability
for key, value in correct_score.items():
    correct_score[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
    correct_score[key]['#_of_fixt_since_last'] = total_fixtures - correct_score[key]['last_occurence'] + 1
    correct_score[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100
    print '{0}   {1}   {2}   {3}\n'.format(key, value['amount'], value['stat'], value['prob'])

print exact_goals

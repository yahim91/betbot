#!python
from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from lxml import etree
from collections import OrderedDict

url = "http://s4dev.betradar.com/gismo.php?"
plimit = 95
output_file = open('bets', 'w')
countries = {'Romania':{}, 'Argentina':{}, 'Rusia':{}, 'Poland':{}, 'Portugal': {}, 'Latvia': {}, 'Lithuania': {}, 'Spain': {},
             'Chile': {}, 'Austria': {}, 'Italy': {}, 'Turkey': {}, 'Costa Rica': {}, 'Colombia': {}, 'USA': {}, 'U.A.E.': {},
             'Switzerland': {}, 'Bulgaria': {}, 'Denmark': {}}


countries['Denmark']['Superligaen'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_8,22_1,5_3376,9_fixtures,231_full,23_1",
                                                callback="23789ea295988edf6c38dee0719dcb8ecf55a484"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_8,22_1,5_4660,9_fixtures,231_full,23_1",
                                                callback="10ab1e6f05d28176b63acd4446a10901f0aa419d"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_8,22_1,5_6203,9_fixtures,231_full,23_1",
                                                callback="88963d3e98997e7c38a0a60cf39644d2264fb27e"
                                               )
                                          )
                }

countries['Bulgaria']['A PFG'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_78,22_1,5_3472,9_fixtures,231_full,23_1",
                                                callback="8aff0f4f2dd21f2e6fbadcd30d98687744d0f38d"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_78,22_1,5_5029,9_fixtures,231_full,23_1",
                                                callback="2d45f8d0d5cc637dc754bfbb97e1e131a4a8dc92"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_78,22_1,5_6279,9_fixtures,231_full,23_1",
                                                callback="3eb343fb39bf4a99f4ca6c843eca3b29fda3c484"
                                               )
                                          )
                }
countries['Switzerland']['Super League'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_25,22_1,5_3388,9_fixtures,231_full,23_1",
                                                callback="651876027b0763dcfb3b8616f81e16ea3e321d50"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_25,22_1,5_4702,9_fixtures,231_full,23_1",
                                                callback="651876027b0763dcfb3b8616f81e16ea3e321d50"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_25,22_1,5_6285,9_fixtures,231_full,23_1",
                                                callback="646e6395789ba8a9365f58cece9a013ddc3a923a"
                                               )
                                          )
                }
countries['U.A.E.']['Arabian Gulf League'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_299,22_5,5_4007,9_fixtures,231_full,23_1",
                                                callback="c29b06eb80edd3b5b769dea2252fbfc50dfce0e1"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_299,22_5,5_5501,9_fixtures,231_full,23_1",
                                                callback="3dfef7e812c59342730f5f18420873e308f7aa1d"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_299,22_5,5_6985,9_fixtures,231_full,23_1",
                                                callback="2e66d8c0095f440cc090f8f9e2ebdf5147dfa780"
                                               )
                                          )
                }
countries['USA']['MLS'] = {'11': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_26,22_2,5_3263,9_fixtures,231_full,23_2",
                                                callback="52f9bff95beca7167ebccaf37c21bee541038a71"
                                               )
                                          ),
                '12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_26,22_2,5_4262,9_fixtures,231_full,23_2",
                                                callback="af2c457ab98f70052069be46d7418e1082150150"
                                               )
                                          ),
                '13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_26,22_2,5_5790,9_fixtures,231_full,23_2",
                                                callback="9da4e02e3e986ffe490f6067c650775981b130aa"
                                               )
                                          )
                }
countries['Colombia']['Liga Postobon'] = {'12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_274,22_3,5_5095,9_fixtures,231_full,23_1",
                                                callback="12b1072c39113f6a81d27d4170b42ab98c1dfdcb"
                                               )
                                          ),
                '13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_274,22_3,5_5914,9_fixtures,231_full,23_1",
                                                callback="f5a1b0dd5fa372c86c63287add170629ea852b37"
                                               )
                                          ),
                '13-2': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_274,22_3,5_6665,9_fixtures,231_full,23_1",
                                                callback="6c83c58b22240d20b17de2ec29d1cec0959f73cb"
                                               )
                                          )
                }
countries['Romania']['Liga I'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_3539,9_fixtures,231_full,23_1",
                                                callback="70d11da1bff5b9fe44d6317c913875cad0f39e7a"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_4682,9_fixtures,231_full,23_1",
                                                callback="f0c0834608f53b75ccfdde88d432405dce3b0add"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_77,22_1,5_6545,9_fixtures,231_full,23_1",
                                                callback="98ad1638d1b7124469e2d6570b99c04829b1c5be"
                                               )
                                          )
                }

countries['Argentina']['Primera Division'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_3613,9_fixtures,231_full,23_1",
                                                callback="4d6288cb024c98fd480df77fc2e021030a72b84f"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_5103,9_fixtures,231_full,23_1",
                                                callback="e30d5c969c553afed56c4cb777b7d4d7f12ae456"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_6455,9_fixtures,231_full,23_1",
                                                callback="a737e54cb0084b4d09c76cbe49cc2ce777ab6168"
                                               )
                                          )
                }

countries['Argentina']['Primera B Nacional'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_3635,9_fixtures,231_full,23_1",
                                                callback="7a2630d4aa8a037d619c5f76715e1e6a094819d4"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_5097,9_fixtures,231_full,23_1",
                                                callback="6fa1108ba300fad5b00dddbb55082570bbca2d03"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_48,22_3,5_6459,9_fixtures,231_full,23_1",
                                                callback="43dde24a7800f732f16fe9e9d39497a7141787b6"
                                               )
                                          )
                }

countries['Rusia']['Premier League'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_21,22_1,5_3288,9_fixtures,231_full,23_1",
                                                callback="1037b31897f30d6c73563f9a9ea69be40a116480"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_21,22_1,5_4596,9_fixtures,231_full,23_1",
                                                callback="d57f0506dd926a259e6f520af30e02e90c17ce99"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_21,22_1,5_6325,9_fixtures,231_full,23_1",
                                                callback="b87e0a603b39e8577bf6ae97b8c3b08af5848168"
                                               )
                                          )
                }

countries['Poland']['Ekstraklasa'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_47,22_1,5_3411,9_fixtures,231_full,23_1",
                                                callback="8d95ec9dfd3002985996ba11a5b46722c8167161"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_47,22_1,5_4634,9_fixtures,231_full,23_1",
                                                callback="8d87fac6be3ae347648377bdde55fc140506b89f"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_47,22_1,5_6261,9_fixtures,231_full,23_1",
                                                callback="6bc5ddd7e56880ad14c35494a76f66b44729a026"
                                               )
                                          )
                }

countries['Portugal']['Primeira Liga'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_44,22_1,5_3462,9_fixtures,231_full,23_1",
                                                callback="96de9750520ab3f0396f2dda2f5f49e30ce746c6"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_44,22_1,5_4907,9_fixtures,231_full,23_1",
                                                callback="4e604f60573ea0e73b6685ea95767fb45462ac3a"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_44,22_1,5_6483,9_fixtures,231_full,23_1",
                                                callback="b444d06679218c820b830a89daecb4f3372c2837"
                                               )
                                          )
                }

countries['Latvia']['Virsliga'] = {'11': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_163,22_1,5_3314,9_fixtures,231_full,23_1",
                                                callback="58fda50d914d692c9d24b3d71aadd952e885479d"
                                               )
                                          ),
                '12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_163,22_1,5_4340,9_fixtures,231_full,23_1",
                                                callback="d6926311909fa96296e643e16699ff6950cf7b62"
                                               )
                                          ),
                '13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_163,22_1,5_6065,9_fixtures,231_full,23_1",
                                                callback="e963834f6b7f245be294881a514093486fc7dd2d"
                                               )
                                          )
                }

countries['Lithuania']['A Lyga'] = {'11': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_160,22_1,5_3308,9_fixtures,231_full,23_1",
                                                callback="3152c8d2ac071812a50bad4637d13ba99b4c43e1"
                                               )
                                          ),
                '12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_160,22_1,5_4378,9_fixtures,231_full,23_1",
                                                callback="648e54fce420178653572e74936bc3b7c75a027e"
                                               )
                                          ),
                '13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_160,22_1,5_6004,9_fixtures,231_full,23_1",
                                                callback="937222ffafd33bc798a843222d16291cfe44ad9b"
                                               )
                                          )
                }

countries['Spain']['Primera Division'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_32,22_1,5_3502,9_fixtures,231_full,23_1",
                                                callback="47dd99d3c176af68bc4a2e5fc10dccf832d020d8"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_32,22_1,5_4959,9_fixtures,231_full,23_1",
                                                callback="55d28a5a5c9fed35e82413b9c53d75f83c2a2c30"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_32,22_1,5_6559,9_fixtures,231_full,23_1",
                                                callback="6b9f96c057bbfd1f1b582acef97f77fee11e6846"
                                               )
                                          )
                }

countries['Chile']['Primera Division'] = {'12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_49,22_3,5_4268,9_fixtures,231_full,23_1",
                                                callback="3f21ec79edf8592a223f73bbf824f4b7238fac13"
                                               )
                                          ),
                '13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_49,22_3,5_5844,9_fixtures,231_full,23_1",
                                                callback="18e1a58ab1b99b63f7a6b2c6ae0a27a2e402a2e0"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_49,22_3,5_6647,9_fixtures,231_full,23_1",
                                                callback="33f18df3532e87cae82383f6eb246cd15fef45b7"
                                               )
                                          )
                }

countries['Austria']['Bundesliga'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_17,22_1,5_3416,9_fixtures,231_full,23_1",
                                                callback="9506f8ab2cc7bf7d96ddfd749a74be3545bcf025"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_17,22_1,5_4752,9_fixtures,231_full,23_1",
                                                callback="591a648764e7ca4abcd2aa8a26bc878634ed6263"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_17,22_1,5_6347,9_fixtures,231_full,23_1",
                                                callback="6378a3ae473359994e192551256a7f34d6b76032"
                                               )
                                          )
                }

countries['Italy']['Serie A'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_31,22_1,5_3639,9_fixtures,231_full,23_1",
                                                callback="21bcfc25d0677d2ee486016b577f179c101a3fda"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_31,22_1,5_5145,9_fixtures,231_full,23_1",
                                                callback="c10fce44e3fe5c3983bcd059fb660f848222e089"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_31,22_1,5_6797,9_fixtures,231_full,23_1",
                                                callback="762c9cbec6692d8617ed5d764320a16dabfd1457"
                                               )
                                          )
                }

countries['Turkey']['Super Lig'] = {'11/12': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_46,22_1,5_3831,9_fixtures,231_full,23_1",
                                                callback="eba40a67824ad1cf71ce6b197afb1fc7976d1c3c"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_46,22_1,5_4993,9_fixtures,231_full,23_1",
                                                callback="3cf3c35f695b34da35d0c952fc7d7d5cedf22afc"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_46,22_1,5_6673,9_fixtures,231_full,23_1",
                                                callback="fb1f0fe1f75674e506220d6c0c969cb2bc600746"
                                               )
                                          )
                }

countries['Costa Rica']['Primera Division'] = {'11': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_289,22_2,5_3558,9_fixtures,231_full,23_1",
                                                callback="34f2507bfea8f4d17593e6bab35522e60b427d3c"
                                               )
                                          ),
                '12/13': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_289,22_2,5_4995,9_fixtures,231_full,23_1",
                                                callback="0b775a181a97e3ae0dde8c02bcafad537b3c064a"
                                               )
                                          ),
                '13/14': urlencode(dict (html=1,
                                                id=1827,
                                                language="en",
                                                clientid=4,
                                                state="2_1,3_289,22_2,5_6549,9_fixtures,231_full,23_1",
                                                callback="d6defb2d3c5edbfa41b2e18d39ed029e47499d65"
                                               )
                                          )
                }

for country, value in countries.items():
    print (country)
    output_file.write(country + '\n')
    for competition, queries in value.items():
        output_file.write(competition + '\n')
        exact_goals = dict()
        over_goals = {'2.5': {'amount': 0, 'value': 2.5}, '3.5': {'amount': 0, 'value': 3.5}, '4.5': {'amount': 0, 'value': 4.5}}
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
        for year, query in OrderedDict(sorted(queries.items(), key=lambda t: t[0])).items():
            data = urllib2.urlopen(url + query)
            print ('Gathered data for ' + year)
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
                after_penalty = result.text.find('(AP)')
                if(after_penalty == -1):
                    after_penalty = result.text.find('(OT)')
                full_time_home_goals = int(result.text[:space])
                if (after_penalty != -1):
                    full_time_away_goals = int(result.text[space + 1:after_penalty])
                else:
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
        printed_header = False
        for key, value in half_time.items():
            half_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            half_time[key]['#_of_fixt_since_last'] = total_fixtures - half_time[key]['last_occurence'] + 1
            half_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100
            if (half_time[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tH/T events :\n')
                    printed_header = True
                output_file.write('\t\t{0}  probability: {1:.2f}%\n'.format(key, half_time[key]['prob']))


        #Computing full_time probability

        printed_header = False
        for key, value in full_time.items():
            full_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            full_time[key]['#_of_fixt_since_last'] = total_fixtures - full_time[key]['last_occurence'] + 1
            full_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100
            if (full_time[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tFT events :\n')
                    printed_header = True
                output_file.write('\t\t{0}  probability: {1:.2f}%\n'.format(key, full_time[key]['prob']))

        #Computing half_full_time probability

        printed_header = False
        for key, value in half_full_time.items():
            half_full_time[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            half_full_time[key]['#_of_fixt_since_last'] = total_fixtures - half_full_time[key]['last_occurence'] + 1
            half_full_time[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'])) * 100
            if (half_full_time[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tHalf/Full time events :\n')
                    printed_header = True
                output_file.write ('\t\t{0}  probability: {1:.2f}% last_matches# {2}\n'.format(key, half_full_time[key]['prob'], half_full_time[key]['#_of_fixt_since_last']))

        #Computing exact_goals probability

        printed_header = False
        for key, value in exact_goals.items():
            exact_goals[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            exact_goals[key]['#_of_fixt_since_last'] = total_fixtures - exact_goals[key]['last_occurence'] + 1
            exact_goals[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100
            if (exact_goals[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tExact Goal events :\n')
                    printed_header = True
                output_file.write ('\t\t{0}  probability: {1:.2f}%\n'.format(key, exact_goals[key]['prob']))

        #Computing over_goals probability

        printed_header = False
        for key, value in over_goals.items():
            over_goals[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            over_goals[key]['#_of_fixt_since_last'] = total_fixtures - over_goals[key]['last_occurence'] + 1
            over_goals[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100
            if (over_goals[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tOver X goals events :\n')
                    printed_header = True
                output_file.write('\t\t{0}  probability: {1:.2f}%\n'.format(key, over_goals[key]['prob']))


        #Computing correct_score probability

        printed_header = False
        for key, value in correct_score.items():
            correct_score[key]['stat'] = (float(value['amount'])/total_fixtures) * 100
            correct_score[key]['#_of_fixt_since_last'] = total_fixtures - correct_score[key]['last_occurence'] + 1
            correct_score[key]['prob'] = (1 - pow(float(100 - value['stat'])/100, value['#_of_fixt_since_last'] + 1)) * 100
            if (correct_score[key]['prob'] > plimit):
                if (not printed_header):
                    output_file.write('\tCorrect score events:\n')
                    printed_header = True
                output_file.write('\t\t{0}  probability: {1:.2f}%\n'.format(key, correct_score[key]['prob']))
output_file.close()

OK_FORMAT = True

test = {   'name': 'q1_11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Incorrect labels for columns\n'
                                               '>>> t = stats_for_year(1990)\n'
                                               ">>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # Incorrect number of rows\n>>> t = stats_for_year(1990)\n>>> t.num_rows == 25\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 25, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'egy  | 27072397         | 6.63                               | 312.8\n'
                                               'ind  | 449661874        | 5.87                               | 247.7\n'
                                               'mmr  | 21486424         | 6.05                               | 276.7\n'
                                               'tha  | 27397178         | 6.15                               | 147.9\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 25, 5)))\n"
                                               'geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born\n'
                                               'cod  | 65938712         | 6.25                               | 116.1\n'
                                               'gbr  | 62716684         | 1.9                                | 5.2\n'
                                               'jpn  | 127319802        | 1.37                               | 3.2\n'
                                               'phl  | 93038902         | 3.15                               | 31.9\n'
                                               'vnm  | 88357775         | 1.82                               | 24.8\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

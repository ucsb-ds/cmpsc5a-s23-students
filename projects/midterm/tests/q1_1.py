OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling\n>>> ind_pop.labels == ('time', 'population_total')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Times should range from 1960 through 2015\n>>> all(ind_pop.sort("time").column("time") == np.arange(1960, 2016))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

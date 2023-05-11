OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> county_employees.num_columns == 2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> county_employees.num_rows == 24\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure that you have the correct column labels!\n>>> np.asarray(county_employees.labels).item(1) != "name identity"\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that you have the correct column labels!\n>>> np.asarray(county_employees.labels).item(0) != "Positions"\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

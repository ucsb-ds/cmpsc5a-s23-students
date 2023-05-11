OK_FORMAT = True

test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you are using the date range 1980-2015\n>>> post_1979_fertility_and_child_mortality.num_rows == 36\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check your column labels and spelling\n'
                                               ">>> all([label in post_1979_fertility_and_child_mortality.labels for label in ['Children per woman', 'Child deaths per 1000 born']])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

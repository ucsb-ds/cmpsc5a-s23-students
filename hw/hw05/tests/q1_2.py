OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> final_scores.num_columns == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> set(['Opponent', 'UCSB Score', 'Opponent Score']) == set(final_scores.labels)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> sum([109^ord(i) for i in tuple(final_scores.take(range(5, 11)).column(0).item(0))]) % 593\n190', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

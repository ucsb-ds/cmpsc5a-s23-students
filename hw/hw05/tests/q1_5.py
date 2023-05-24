OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> 0 <= ucsb_wins <= 10\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 <= ucsb_losses <= 10\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (109**(ucsb_wins) +  109 **ucsb_losses )%593\n231', 'hidden': False, 'locked': False},
                                   {   'code': ">>> (109 ** int(''.join('1' if b else '0' for b in won_games), 2) + int(''.join('1' if b else '0' for b in tied_games), 2) ^ 109)% 593\n7",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

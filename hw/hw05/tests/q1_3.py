OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> 'did_ucsb_win' in globals()\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> did_ucsb_win(final_scores.row(1)) == False\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> (109 ** int(''.join('1' if b else '0' for b in final_scores.apply(did_ucsb_win)), 2)) % 593\n296", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

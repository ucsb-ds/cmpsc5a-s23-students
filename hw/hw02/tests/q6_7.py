OK_FORMAT = True

test = {   'name': 'q6_7',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # It looks like your table doesn't have all 3 columns that are in the inventory table.\n>>> remaining_inventory.num_columns == 3\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # It looks like you forgot to subtract off the sales.\n>>> remaining_inventory.column("count").item(0) != 45\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> remaining_inventory.where(1, 'grape').column(2).item(0) == 162\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}


from solera_log import SoleraLog

def test_only_add():

    tests = [
        {
            'new_entry': {
                'date': '2020-01-01',
                'desc': 'Port A',
                'delta': 5
            },
            'expected': [
                { 'desc': 'Port A', 'amount': 5 }
            ]
        },
        {
            'new_entry': {
                'date': '2019-01-02',
                'desc': 'Port B',
                'delta': 10
            },
            'expected': [
                { 'desc': 'Port A', 'amount': 5 },
                { 'desc': 'Port B', 'amount': 10 }
            ]
        },
        {
            'new_entry': {
                'date': '2019-01-03',
                'desc': 'Sample 1',
                'delta': -3
            },
            'expected': [
                { 'desc': 'Port A', 'amount': 4.0 },
                { 'desc': 'Port B', 'amount': 8.0 }
            ]
        },
        {
            'new_entry': {
                'date': '2020-01-04',
                'desc': 'Port C',
                'delta': 3
            },
            'expected': [
                { 'desc': 'Port A', 'amount': 4.0 },
                { 'desc': 'Port B', 'amount': 8.0 },
                { 'desc': 'Port C', 'amount': 3.0 }
            ]
        },
        {
            'new_entry': {
                'date': '2020-01-05',
                'desc': 'Sample 2',
                'delta': -3
            },
            'expected': [
                { 'desc': 'Port A', 'amount': 3.2 },
                { 'desc': 'Port B', 'amount': 6.4 },
                { 'desc': 'Port C', 'amount': 2.4 }
            ]
        }
    ]

    log = SoleraLog()
    for test in tests:
        log.add(**test.get('new_entry'))
        assert log.summary() == test.get('expected')

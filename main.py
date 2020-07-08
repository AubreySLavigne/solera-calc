#!/usr/bin/env python3
# All units are in cL
import json

import texttable as tt

from solera_log import SoleraLog


def main() -> None:

    log = SoleraLog()
    with open('entries.json') as json_file:
        entries = json.load(json_file)
        for entry in entries:
            log.add(**entry)

    tab = tt.Texttable()
    tab.header(['Name', 'Amount (cL)', 'Percentage'])

    total = log.total()
    summary = log.summary()
    for entry in summary:
        entry['percent'] = 100 * (entry.get('amount') / total)
        tab.add_row((
            entry.get('desc'),
            entry.get('amount'),
            entry.get('percent')
        ))

    print(tab.draw())

if __name__ == '__main__':
    main()

# solera-calc

Calculating percentages of a mixture

## Info

A solera is a method of mixed aging (often Sherry or other wines) by
continually including portion of the previous in following batches.

Relatedly, the term can refer to an "infinity bottle", a personal blend of
multiple wines that is continuing evolving as new wines are added. As long as
the bottle is never fully emptied, it'll continue its story with the original
contributions lasting.

More info can be found here: https://en.wikipedia.org/wiki/Solera

## Calculating the mixture

This script calculates the amount and percentage for each contributed wine,
as provided in sequential order.

This can also be generalized to any other method, not just wine.

### Sample output

```
+-------------------------------------+-------------+------------+
|                Name                 | Amount (cL) | Percentage |
+=====================================+=============+============+
| Noval Black Ruby Reserve            | 2.380       | 9.153      |
+-------------------------------------+-------------+------------+
| Noval 10-year Tawny                 | 2.380       | 9.153      |
+-------------------------------------+-------------+------------+
| Sandeman 10-year Tawny              | 2.856       | 10.984     |
+-------------------------------------+-------------+------------+
| Fonseca Bin 27 Ruby                 | 3.264       | 12.553     |
+-------------------------------------+-------------+------------+
| Croft Purple Velvet Reserve         | 3.264       | 12.553     |
+-------------------------------------+-------------+------------+
| Quinta Das Varvalhas Ruby Reserve   | 3.857       | 14.835     |
+-------------------------------------+-------------+------------+
| Penfold's Grandfather 20-year Tawny | 2           | 7.692      |
+-------------------------------------+-------------+------------+
| Taylor Fladgate 10-year Tawny       | 6           | 23.077     |
+-------------------------------------+-------------+------------+
```

---
tag: ~1eee8b5f
kind: statement
role: proposition
name: Triangle-free graphs of every chromatic number
msc: [05C15, 05C69]
uses: [0C5M7AM6FH, 0WCKRBHFFD, 0JD5C82QMB]
about: [0VHJRXNAAS, 04MQSQ1F5Q]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_graphs_color.ptx#L200
    locator: source/s_graphs_color.ptx:200
---

## Statement

Let $t \ge 3$ be an integer.
Then there is a finite [[graph|0JD5C82QMB]] $G_t$ whose [[chromatic number|0C5M7AM6FH]] is $t$ and whose [[clique number|0WCKRBHFFD]] is $2$.

## Remarks

A graph with clique number $2$ has an edge but no triangle.
So the chromatic number is not bounded above by the clique number.
The gap $\chi(G_t) - \omega(G_t) = t - 2$ can be as large as we wish.
For $t = 3$ the cycle $C_5$ works.

---
tag: 5SKPQNWNGD
kind: statement
role: theorem
name: Erdős theorem on graphs of large girth and large chromatic number
msc: [05C15, 05C38, 05C80]
uses: [0C5M7AM6FH, WZ4JGTG6ZD, 0JD5C82QMB]
about: [0VHJRXNAAS, D13K9GJT0B]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_ramsey_girth.ptx#L12
    locator: source/s_ramsey_girth.ptx:12
---

## Statement

Let $g \ge 3$ and $t$ be integers.
Then there is a [[graph|0JD5C82QMB]] $G$ whose [[chromatic number|0C5M7AM6FH]] satisfies $\chi(G) > t$ and whose [[girth|WZ4JGTG6ZD]] is greater than $g$.

## Remarks

So a graph can need many colours even though it has no short cycles at all.
Large chromatic number does not force a small cycle, such as a triangle, into the graph.
The classical proof uses the probabilistic method on a random graph.

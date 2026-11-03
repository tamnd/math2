---
tag: ~ce4eb3df
kind: statement
name: Chromatic number is at least the clique number
msc:
- 05C15
- 05C69
role: theorem
sources:
- locator: ptx/sec_gt-coloring.ptx:468
  url: https://github.com/oscarlevin/discrete-book/blob/a8e4949bc45daf100930c1182983778f56ab689f/ptx/sec_gt-coloring.ptx#L468
uses:
- 0C5M7AM6FH
- 0WCKRBHFFD
about:
- 0VHJRXNAAS
- 04MQSQ1F5Q
---

## Statement

Let $G$ be a graph.
Then the [[chromatic number|0C5M7AM6FH]] of $G$ is at least the [[clique number|0WCKRBHFFD]] of $G$.

## Remarks

Take a clique with $k$ vertices. Any two of its vertices are adjacent, so they must get different colours in a proper colouring.
Hence a proper colouring of $G$ uses at least $k$ colours.
Apply this to a largest clique.

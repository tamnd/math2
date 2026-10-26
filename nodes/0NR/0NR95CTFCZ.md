---
tag: 0NR95CTFCZ
kind: example
name: Petersen graph
msc: [05C99]
instance_of: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Petersen_graph
    locator: Constructions
same_as:
  wikidata: Q835614
  wikipedia: Petersen graph
---

## Example

The Petersen graph is the [[graph|0JD5C82QMB]] whose vertices are the $2$-element subsets of $\{1, 2, 3, 4, 5\}$.
Two vertices are adjacent if and only if they are disjoint subsets.

It has $\binom{5}{2} = 10$ vertices and $15$ edges, and it is $3$-[[regular|0KA4S8R39M]].

## Remarks

Its shortest cycle has length $5$. It is not [[Hamiltonian|090WPKFABX]], and it is not [[planar|029JQEK15B]].
Its [[chromatic number|0C5M7AM6FH]] is $3$, and its edges cannot be coloured with $3$ colours.
A common drawing shows it as a pentagon outside, a pentagram inside, and five spokes.

## Explanations

### L1 human

The Petersen graph is a small graph with $10$ vertices and $15$ edges.
It is a standard counterexample: many statements that seem true for all cubic graphs fail for it.

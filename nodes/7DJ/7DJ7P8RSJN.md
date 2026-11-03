---
tag: 7DJ7P8RSJN
kind: concept
name: Hungarian algorithm
msc: [90C27, 05C70, 90B80]
sources:
  - url: https://en.wikipedia.org/wiki/Hungarian_algorithm
same_as:
  wikidata: Q281922
  wikipedia: Hungarian algorithm
---

## Summary

The Hungarian algorithm solves the [[assignment problem|K65YS73SBW]]: it finds a minimum-cost [[perfect matching|0NHK9MFFW9]] in a complete [[bipartite graph|0ZVQKTRKVQ]] with $n$ vertices on each side.
It is a primal-dual method that keeps feasible dual prices on the vertices.
It looks for a perfect matching that uses only edges whose cost equals the sum of the prices at their ends.
Harold W. Kuhn published it in 1955 and named it after the earlier work of the Hungarian mathematicians Dénes Kőnig and Jenő Egerváry.
It can be implemented with $O(n^3)$ arithmetic operations, and it was one of the first polynomial-time algorithms in combinatorial optimization.

## Explanations

### L1 human

Workers must be paired with jobs at the least total cost.
The method gives each worker and each job a price, chosen so that no pairing costs less than the sum of its two prices.
It then tries to pair everyone using only pairings whose cost equals the sum exactly.
If that fails, it shifts the prices a little, which makes new exact pairings appear, and tries again.
Once everyone is paired, the prices prove that no other pairing is cheaper.

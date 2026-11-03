---
tag: GEPM2KPAD8
kind: concept
name: Held–Karp algorithm
msc: [90C27, 90C39, 68W40]
specializes: [R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
same_as:
  wikidata: Q20203442
  wikipedia: Held–Karp algorithm
---

## Summary

The Held–Karp algorithm solves the [[travelling salesman problem|XJRHJX2241]] exactly by [[dynamic programming|R3FXF08WBH]] over subsets of the cities.
For $n$ cities it runs in $O(n^2 2^n)$ steps, far fewer than the $(n-1)!/2$ tours of a brute-force search.
It was found independently by Bellman and by Held and Karp in 1962.
No exact algorithm with a better exponential base is known for the general problem.

## Explanations

### L1 human

Instead of trying every round trip, the algorithm remembers, for each set of visited cities and each last city, the shortest way to get there from the start.
A longer route is built from shorter ones by adding one more city at the end.
The best way to finish a route depends only on which cities were visited and where the route ends.
It does not depend on the order of the earlier visits.
For $20$ cities this means about $20^2 \cdot 2^{20}$, roughly $4 \times 10^8$, steps, while there are about $6 \times 10^{16}$ tours.
The price is memory: the table has one entry for each set and each end city.

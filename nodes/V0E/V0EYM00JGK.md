---
tag: V0EYM00JGK
kind: concept
name: Borda count
msc: [91B12, 91B14]
sources:
  - url: https://en.wikipedia.org/wiki/Borda_count
same_as:
  wikidata: Q576578
  wikipedia: Borda count
---

## Summary

The Borda count is a voting rule in which each voter ranks the candidates and each rank earns a fixed number of points.
With $m$ candidates, a first place earns $m - 1$ points, a second place $m - 2$, and so on down to $0$ for last place.
The candidate with the largest total wins.
It is a positional scoring rule, and it is used in elections, sports polls and rank aggregation.

## Explanations

### L1 human

Each voter's ballot is a full list of the candidates from best to worst.
A candidate collects more points the higher she appears on each ballot, and the points are added up.
With three candidates a first place is worth $2$, a second place $1$ and a last place $0$.
Unlike plurality voting, a candidate who is everyone's second choice can win.

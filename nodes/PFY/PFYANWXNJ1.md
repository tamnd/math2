---
tag: PFYANWXNJ1
kind: concept
name: Edmonds–Karp algorithm
msc: [90C35, 05C21, 05C85]
specializes: [9P19SEYN1R]
sources:
  - url: https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
same_as:
  wikidata: Q1302658
  wikipedia: Edmonds–Karp algorithm
---

## Summary

The Edmonds–Karp algorithm solves the [[maximum flow problem|EXMR7RYRTP]] by the [[Ford–Fulkerson method|9P19SEYN1R]], always augmenting along a shortest augmenting path.
The shortest path is found by [[breadth-first search|52XF4HS0X3]] in the residual network.
This rule makes the number of augmentations at most $O(\abs{V} \abs{A})$, whatever the capacities, so the running time is $O(\abs{V} \abs{A}^2)$.
It was published by Jack Edmonds and Richard Karp in 1972, and independently earlier by Yefim Dinitz.

## Explanations

### L1 human

The Ford–Fulkerson idea is to keep pushing extra flow along some path from the source to the sink that still has room.
With a bad choice of paths, this can take very many rounds, or even never stop when capacities are irrational.
Edmonds and Karp fix this with a simple rule: always use a path with the fewest edges.
Then the distances from the source in the residual network never decrease, and each edge can be the bottleneck only a limited number of times.
This gives a bound on the work that depends only on the size of the network, not on the capacities.

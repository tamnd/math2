---
tag: 0ZKPH2BD1T
kind: concept
name: Cycle notation
msc: [20B30]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Cycle notation
---

## Summary

Cycle notation writes a permutation as a list of cycles.
The cycle $(a_1\ a_2\ \dots\ a_k)$ sends $a_i$ to $a_{i+1}$ for $i < k$, sends $a_k$ to $a_1$, and fixes all other points.
A cycle with $k$ entries is a $k$-cycle, and a $1$-cycle is the identity, so it is usually not written.

## Remarks

The same cycle has $k$ different notations, because you can start the list at any entry: $(1\ 2\ 3) = (2\ 3\ 1) = (3\ 1\ 2)$.
The inverse of $(a_1\ a_2\ \dots\ a_k)$ is $(a_k\ \dots\ a_2\ a_1)$.
Each permutation of a finite set is a product of [[disjoint cycles|0YWDAZPRPQ]], so cycle notation can show each permutation.
For example, in $S_5$ the permutation with $1 \mapsto 3$, $3 \mapsto 1$, $2 \mapsto 4$, $4 \mapsto 5$, $5 \mapsto 2$ is $(1\ 3)(2\ 4\ 5)$.

## Explanations

### L1 human

Cycle notation follows each symbol to where it goes, until you come back to the start.
Each round trip is a cycle, and you write it in parentheses.
This is shorter than a table, and it shows the structure of the permutation directly.

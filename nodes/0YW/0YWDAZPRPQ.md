---
tag: 0YWDAZPRPQ
kind: statement
role: theorem
name: Decomposition of a permutation into disjoint cycles
msc: [20B30]
uses: [0RJMNEN3BJ, 0ZKPH2BD1T, 07E6D8R4D6]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Cycle notation
---

## Statement

Let $X$ be a finite set and let $\sigma \in \operatorname{Sym}(X)$.
Then $\sigma$ is a product of cycles of length at least $2$ whose sets of moved points are pairwise disjoint.
This product is unique up to the order of the factors.

## Remarks

The cycles come from the orbits of $\langle \sigma \rangle$ on $X$: each orbit with more than one point gives one cycle.
The order of the factors does not matter, because [[disjoint cycles commute|07E6D8R4D6]].
For example, the permutation $1 \mapsto 2$, $2 \mapsto 1$, $3 \mapsto 4$, $4 \mapsto 5$, $5 \mapsto 3$ in $S_5$ is $(1\ 2)(3\ 4\ 5)$.

## Explanations

### L1 human

Start at a point and follow the permutation until you return.
This gives one cycle; then start again at a point that you did not visit yet.
When all points are visited, the permutation is the product of the cycles that you found.

---
tag: 06HTJNCMPA
kind: statement
role: theorem
name: Dimension formula for sums of subspaces
aliases: [grassmann-formula, dimension-formula]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [03GSZ8RTZJ]
uses: [0RMKABS2S5, 0V33SPH7RR, 05G2G0P224]
proofs: [75VVYAZBK3]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.finrank_sup_add_finrank_inf_eq
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6, exercises
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be finite-dimensional [[linear subspaces|0EPTJA5QV4]] of $V$.
Then $U + W$ is finite-dimensional, and
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W,$$
where $U + W$ is the [[sum of the subspaces|0RMKABS2S5]] and $\dim$ is the [[dimension|05G2G0P224]].

## Remarks

### Why each hypothesis is needed

Finite dimension is needed for the subtraction form $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.
For infinite cardinals, $\aleph_0 + \aleph_0 = \aleph_0 + 0$, so the term $\dim(U \cap W)$ cannot be recovered from the others.
The formula is for two subspaces only.
For three lines $U_1, U_2, U_3$ in $\R^2$, the inclusion-exclusion formula gives $1 + 1 + 1 - 0 - 0 - 0 + 0 = 3$, but $\dim(U_1 + U_2 + U_3) = 2$; see [[three lines in the plane|38AKN9MG6J]].

### Consequences

1. Two planes through the origin in $\R^3$ with $U \ne W$ have $\dim(U + W) = 3$, so $\dim(U \cap W) = 2 + 2 - 3 = 1$: they meet in a line.
2. $\dim(U + W) \le \dim U + \dim W$, with equality if and only if $U \cap W = \set{0}$, that is, the sum is direct.
3. In $F^n$, two subspaces with $\dim U + \dim W > n$ have a nonzero common vector, because $\dim(U \cap W) \ge \dim U + \dim W - n \ge 1$.

### Converse

Equality in consequence 2 characterizes direct sums: $U + W$ is direct if and only if $\dim(U + W) = \dim U + \dim W$.

### Generalizations

1. For arbitrary subspaces, the formula holds as an equation of cardinals, by the same proof.
2. The [[rank-nullity theorem|0W4FSW1TVB]] applied to $U \times W \to V$, $(u, w) \mapsto u - w$, gives a second proof: the image is $U + W$ and the kernel is isomorphic to $U \cap W$.
3. In lattice terms, the subspaces form a modular lattice, and $\dim$ is a valuation on it.

## History

The formula is named after Grassmann, whose Ausdehnungslehre of 1844 and 1862 studied linear spaces of any finite dimension.

## Explanations

### L1 human

The formula counts dimensions like a count of elements in a union of two sets.
We add the two dimensions, but then the common part is counted twice, so we subtract it once.
Two different planes through the origin in space always share at least a line.

### L2 human

Example in $\R^4$: let $U = \operatorname{span}(e_1, e_2, e_3)$ and $W = \operatorname{span}(e_3, e_4)$.
Then $U + W = \R^4$, with dimension $4$, and $U \cap W = \operatorname{span}(e_3)$, with dimension $1$.
Check: $4 + 1 = 5 = 3 + 2$.

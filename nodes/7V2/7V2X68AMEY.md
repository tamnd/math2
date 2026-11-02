---
tag: 7V2X68AMEY
kind: statement
role: theorem
name: Hadwiger's theorem
msc: [52A22, 52B45, 52A39]
uses: [V0RBKHYTV7, C2CK6KSSTV, F79WYYC07C, 0H3YY8CPKH]
about: [V0RBKHYTV7, C2CK6KSSTV]
sources:
  - url: https://en.wikipedia.org/wiki/Hadwiger's_theorem
same_as:
  wikidata: Q5638112
  wikipedia: Hadwiger's theorem
---

## Statement

Let $n \ge 1$ and let $\mathcal{K}^n$ be the set of nonempty compact convex subsets of $\R^n$, with the [[Hausdorff distance|F79WYYC07C]].
Let $\varphi \colon \mathcal{K}^n \to \R$ be a [[valuation|V0RBKHYTV7]] that is continuous and invariant under the [[rigid motions|0H3YY8CPKH]] of $\R^n$.
Then there are real numbers $c_0, c_1, \dots, c_n$ such that
$$\varphi(K) = \sum_{j=0}^n c_j V_j(K) \quad \text{for all } K \in \mathcal{K}^n,$$
where $V_0, \dots, V_n$ are the [[intrinsic volumes|C2CK6KSSTV]].

## Remarks

Conversely, each $V_j$ is a continuous valuation invariant under rigid motions, so these valuations form a real vector space of dimension $n + 1$ with basis $V_0, \dots, V_n$.
A short proof by Klain rests on a lemma about simple valuations.
The lemma says: a continuous valuation invariant under rigid motions that vanishes on all sets of dimension below $n$ is a multiple of volume.
Induction on $n$ then handles the restriction of $\varphi$ to lower-dimensional sets.

Example: surface area in $\R^n$ is a continuous valuation invariant under rigid motions, and the theorem identifies it as $2 V_{n-1}$.

Invariance under rotations is needed.
In $\R^2$ the width in the direction of the first axis, $\varphi(K) = \max_{x \in K} x_1 - \min_{x \in K} x_1$, is a continuous valuation invariant under translations.
It gives $1$ to the segment $[0,1] \times \set{0}$ and $0$ to the congruent segment $\set{0} \times [0, 1]$, so it is not a combination of intrinsic volumes.

## Explanations

### L1 human

There are many ways to measure the size of a convex shape.
Suppose a measure is additive like an area, does not change when the shape is moved, and changes little when the shape changes little.
Hadwiger's theorem says that such a measure is built from a short list of basic measures.
In space the list has four entries: volume, surface area, mean width and the Euler characteristic.

### L2 human

The theorem is the foundation of integral geometry in Euclidean space.
It gives quick proofs of the principal kinematic formula and of Crofton-type formulas: one checks that both sides are such valuations and compares them on balls.
It also explains why intrinsic volumes appear in probability, for example in the expected Euler characteristic of random sets.
Its classification has been extended by Alesker and others to valuations invariant under smaller groups.

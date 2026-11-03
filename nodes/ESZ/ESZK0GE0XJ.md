---
tag: ESZK0GE0XJ
kind: definition
name: Causality conditions
msc: ["53C50", "83C99"]
defines: EKA74X1SYS
uses: [KZWG5F0TSB, DCM7BJ25R8, BY4QYYS788, G49G4R1K04]
sources:
  - url: https://en.wikipedia.org/wiki/Causality_conditions
---

## Definition

Let $(M, g)$ be a time-oriented [[Lorentzian manifold|BY4QYYS788]], with chronological and causal futures and pasts $I^\pm(p)$, $J^\pm(p)$ as in the [[causal structure|KZWG5F0TSB]].
The main *causality conditions* are the following.

1. $(M, g)$ is *chronological* if it contains no [[closed timelike curve|DCM7BJ25R8]].
2. $(M, g)$ is *causal* if it contains no closed future-directed causal curve.
3. $(M, g)$ is *distinguishing* if for all $p, q \in M$, $I^+(p) = I^+(q)$ implies $p = q$, and $I^-(p) = I^-(q)$ implies $p = q$.
4. $(M, g)$ is *strongly causal* if every point has arbitrarily small open neighbourhoods $U$ that no causal curve leaves and then re-enters.
5. $(M, g)$ is *stably causal* if, for some continuous timelike vector field $X$, the metric $g - X^\flat \otimes X^\flat$ has no closed timelike curve. Here $X^\flat = g(X, \cdot)$; the new metric has wider light cones than $g$.
6. $(M, g)$ is *causally simple* if it is causal and the sets $J^+(p)$ and $J^-(p)$ are closed for every $p$.

## Remarks

Each condition in the list implies the previous one.
Global hyperbolicity is stronger than all of them.
Stable causality is equivalent to the existence of a time function, a continuous function on $M$ that strictly increases along every future-directed causal curve.
For a compact spacetime the chronology condition always fails: every compact Lorentzian manifold contains a closed timelike curve.

Example: [[Minkowski space|G49G4R1K04]] satisfies all six conditions; the coordinate $t$ is a time function, and $J^\pm(p)$ are closed cones.

Non-example: the quotient of Minkowski space by the translation $(t, x) \mapsto (t + 1, x)$ is not chronological.
The curve $s \mapsto (s, 0)$, $s \in [0, 1]$, becomes a closed timelike curve.

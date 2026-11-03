---
tag: 36B7JZE3KD
kind: definition
name: Causal structure
msc: ["53C50", "83C99"]
defines: KZWG5F0TSB
uses: [BY4QYYS788, JZ9ADDZX8D, G49G4R1K04, Z788G6MJ9E]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_structure
---

## Definition

Let $(M, g)$ be a [[Lorentzian manifold|BY4QYYS788]] of dimension $n \ge 2$ with signature $(-, +, \dots, +)$.
A tangent vector $v \in T_pM$ is *timelike* if $g(v, v) < 0$, *null* if $g(v, v) = 0$ and $v \ne 0$, *causal* if it is timelike or null, and *spacelike* if $g(v, v) > 0$.
A *time orientation* is a continuous timelike vector field $\tau$ on $M$; given one, a causal vector $v$ is *future-directed* if $g(v, \tau) < 0$.
Assume $(M, g)$ is time-oriented.
A piecewise smooth curve is a *future-directed timelike* (resp. *causal*) *curve* if all its tangent vectors are future-directed timelike (resp. causal).
At break points this is required of both one-sided tangents.
For $p, q \in M$:

1. $p \ll q$ if there is a future-directed timelike curve from $p$ to $q$;
2. $p \le q$ if $p = q$ or there is a future-directed causal curve from $p$ to $q$;
3. the *chronological future* of $p$ is $I^+(p) = \set{q : p \ll q}$ and the *causal future* is $J^+(p) = \set{q : p \le q}$; the pasts $I^-(p)$ and $J^-(p)$ are defined with the reversed relations.

The *causal structure* of $(M, g)$ is the pair of relations $\ll$ and $\le$ on $M$.

## Remarks

The sets $I^\pm(p)$ are always open, but $J^\pm(p)$ need not be closed.
Two metrics $g$ and $\Omega^2 g$ with $\Omega > 0$ have the same timelike, null and causal vectors, and hence the same causal structure.

Example: in [[Minkowski space|G49G4R1K04]] $\R^{1,3}$ with $\tau = \partial_t$, one has $I^+(0) = \set{(t, x) : t > \abs{x}}$ and $J^+(0) = \set{(t, x) : t \ge \abs{x}}$, the inside of the future [[light cone|JZ9ADDZX8D]] and its closure.
The [[world line|Z788G6MJ9E]] $t \mapsto (t, vt, 0, 0)$ with $\abs{v} < 1$ is a future-directed timelike curve, so $0 \ll (1, v, 0, 0)$.

Non-example: the curve $s \mapsto (s, 2s, 0, 0)$ in Minkowski space has tangent $v = (1, 2, 0, 0)$ with $g(v, v) = -1 + 4 = 3 > 0$, so it is spacelike and is not a causal curve.
Also, $J^+(p)$ need not be closed: remove the point $(1, 1, 0, 0)$ from Minkowski space.
Then a point $(t, t, 0, 0)$ with $t > 1$ is a limit of points of $J^+(0)$.
The only causal curve from $0$ to it is the null line through the removed point, so it is not in $J^+(0)$.

---
tag: AMDN6PK5RA
kind: definition
name: Steenrod reduced power
msc: [55S10, 55S05]
defines: EZYHSE1E8P
uses: [K8T15QHN3W, 6N7BC70CX0, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/Steenrod_algebra
---

## Definition

Let $p$ be an odd prime, and write $H^n(X)$ for the [[singular cohomology|6N7BC70CX0]] group $H^n(X; \F_p)$ of a space $X$.
The *Steenrod reduced powers* are the unique family of homomorphisms
$$P^i \colon H^n(X) \to H^{n + 2i(p-1)}(X), \qquad i \ge 0,\ n \ge 0,$$
defined for all spaces $X$, with the following properties.

1. Each $P^i$ is natural: $f^* \circ P^i = P^i \circ f^*$ for every continuous map $f \colon Y \to X$.
2. Each $P^i$ commutes with the suspension isomorphism $H^n(X) \cong H^{n+1}(SX)$ in reduced cohomology.
3. $P^0$ is the identity.
4. If $x \in H^{2i}(X)$, then $P^i x = x^p$, the $p$-th [[cup product|JX47MS1R1H]] power of $x$.
5. If $x \in H^n(X)$ and $2i > n$, then $P^i x = 0$.
6. (Cartan formula) $P^k(x \smile y) = \sum_{i + j = k} P^i x \smile P^j y$ for all $x, y \in H^*(X)$.

## Remarks

Existence of such a family is a theorem of Steenrod; uniqueness follows from the axioms by evaluating on products of Eilenberg–MacLane spaces.
The operations also exist on cohomology of pairs and commute with the coboundary maps of pairs.

Example: on $X = \C P^\infty$, with $H^*(X) = \F_p[x]$ and $\deg x = 2$, clauses 4 and 6 give $P^i(x^m) = \binom{m}{i} x^{m + i(p-1)}$.
For instance $P^1 x = x^p$, which is nonzero.

Non-example: let $Q^0$ be the identity and $Q^i = 0$ for $i > 0$.
This family satisfies clauses 1, 2, 3, 5 and 6.
It fails clause 4: on $\C P^\infty$ one has $Q^1 x = 0$, while $x^p \neq 0$.

The operation $P^i$ is a [[cohomology operation|K8T15QHN3W]] of type $(\F_p, n; \F_p, n + 2i(p-1))$.
For $p = 2$ the analogous operations are the Steenrod squares $Sq^i$, with $Sq^{2i}$ playing the role of $P^i$.

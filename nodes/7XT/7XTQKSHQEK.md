---
tag: 7XTQKSHQEK
kind: definition
name: Kervaire invariant
msc: [55Q45, 57R15]
defines: P4YXE08ZXF
uses: [F45VQ47GPV, 0RBQS1JJCR, 6N7BC70CX0, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/Kervaire_invariant
---

## Definition

Let $k \ge 0$ and let $M$ be a closed [[smooth manifold|F45VQ47GPV]] of dimension $4k + 2$ with a framing of its stable normal bundle.
Let $V = H^{2k+1}(M; \F_2)$ be its middle [[singular cohomology|6N7BC70CX0]] with coefficients in $\F_2$.
The [[cup product|JX47MS1R1H]] followed by evaluation on the fundamental class gives a nondegenerate bilinear form $x \cdot y$ on $V$, and $x \cdot x = 0$ for all $x$.
The framing determines a function $q \colon V \to \F_2$ such that
$$q(x + y) = q(x) + q(y) + x \cdot y \quad \text{for all } x, y \in V.$$
Choose a basis $a_1, \dots, a_m, b_1, \dots, b_m$ of $V$ with $a_i \cdot b_j = \delta_{ij}$ and $a_i \cdot a_j = b_i \cdot b_j = 0$.
The *Kervaire invariant* of $M$ is the Arf invariant of the [[quadratic form|0RBQS1JJCR]] $q$:
$$\Phi(M) = \sum_{i=1}^{m} q(a_i)\, q(b_i) \in \F_2.$$

## Remarks

The Arf invariant does not depend on the choice of the symplectic basis.
It is the value that $q$ takes on more than half of the elements of $V$.

Example: let $M = S^1 \times S^1$ with the framing given by its Lie group structure, so $k = 0$.
Here $V = \F_2^2$ with basis $a$, $b$ dual to the two circle factors, and $a \cdot b = 1$.
For this framing $q(a) = q(b) = 1$, so $\Phi(M) = 1$.

Non-example: a closed framed manifold of dimension $4$ has no Kervaire invariant, since $4$ is not of the form $4k + 2$.
The construction needs an odd middle degree $2k + 1$.

The Kervaire invariant is a framed cobordism invariant.
By the Pontryagin–Thom construction it defines a homomorphism $\pi^s_{4k+2} \to \Z/2$ on the stable homotopy groups of spheres.

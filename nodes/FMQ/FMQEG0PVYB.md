---
tag: FMQEG0PVYB
kind: definition
name: Abel–Jacobi map
msc: [14H40, 30F30]
defines: HE8F7KBF42
uses: [5K0N8QMV6Q, P014C13K5H]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%E2%80%93Jacobi_map
---

## Definition

Let $X$ be a compact [[Riemann surface|5K0N8QMV6Q]] of genus $g \ge 1$.
Let $\omega_1, \ldots, \omega_g$ be a basis of the space of holomorphic [[Abelian differentials|P014C13K5H]] on $X$.
Let $\Lambda \subset \C^g$ be the set of vectors $\left( \int_\gamma \omega_1, \ldots, \int_\gamma \omega_g \right)$, where $\gamma$ runs over the closed loops in $X$.
Then $\Lambda$ is a lattice of rank $2g$ in $\C^g$, and $J(X) = \C^g / \Lambda$ is the Jacobian variety of $X$.
Fix a base point $P_0 \in X$.
The *Abel–Jacobi map* is
$$A \colon X \to J(X), \qquad A(P) = \left( \int_{P_0}^{P} \omega_1, \ldots, \int_{P_0}^{P} \omega_g \right) \bmod \Lambda,$$
where each integral is taken along the same path from $P_0$ to $P$.
It extends to divisors by $A\left( \sum_i n_i P_i \right) = \sum_i n_i A(P_i)$.

## Remarks

The map is well defined: two paths from $P_0$ to $P$ differ by a closed loop, which changes the vector of integrals by an element of $\Lambda$.
On divisors of degree $0$ the result does not depend on $P_0$.

Example: let $X = \C / \Lambda'$ be a complex torus with $g = 1$ and $\omega_1 = dz$.
The integral from $P_0$ to $P$ is $P - P_0$ modulo the periods of $dz$, which form $\Lambda'$.
So $A(P) = P - P_0$ is an isomorphism from $X$ onto $J(X) = \C / \Lambda'$.

Non-example: the map $P \mapsto \left( \int_{P_0}^{P} \omega_i \right)_i$ into $\C^g$ itself, without the quotient by $\Lambda$, is not well defined on $X$.
Going once around a loop with a nonzero period changes its value.

Abel's theorem: a divisor $D$ of degree $0$ is the divisor of a meromorphic function if and only if $A(D) = 0$.
Jacobi inversion: the induced map from effective divisors of degree $g$ to $J(X)$ is surjective.
For $g \ge 1$ the map $A \colon X \to J(X)$ is injective, and for $g \ge 2$ it is a holomorphic embedding.

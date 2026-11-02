---
tag: 35KB1QCD3Z
kind: statement
role: theorem
name: Abel–Jacobi theorem
msc: [14H40, 30F30]
uses: [HE8F7KBF42, ZQ84M9D9TC, 5K0N8QMV6Q, Z9DN23DAE2, 0ZZ7ZYDR8W]
about: [HE8F7KBF42, ZQ84M9D9TC]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%E2%80%93Jacobi_map
---

## Statement

Let $X$ be a compact connected [[Riemann surface|5K0N8QMV6Q]] of genus $g \ge 1$, with [[Jacobian variety|ZQ84M9D9TC]] $J(X)$.
Fix $P_0 \in X$, and let $A$ be the [[Abel–Jacobi map|HE8F7KBF42]], extended additively to [[divisors|Z9DN23DAE2]] on $X$.

1. (Abel) A divisor $D$ of degree $0$ on $X$ is the divisor of a [[meromorphic function|0ZZ7ZYDR8W]] on $X$ if and only if $A(D) = 0$ in $J(X)$.
2. (Jacobi inversion) Every point of $J(X)$ equals $A(P_1 + \cdots + P_g) - g A(P_0)$ for some points $P_1, \ldots, P_g \in X$.

Let $\operatorname{Pic}^0(X)$ be the group of divisors of degree $0$ modulo divisors of meromorphic functions.
Then $A$ induces an isomorphism of groups $\operatorname{Pic}^0(X) \to J(X)$.

## Remarks

For the direct half of Abel's theorem, let $D = \operatorname{div}(f)$ and consider the fibres $f^{-1}(t)$ for $t \in \mathbb{P}^1$, counted with multiplicity.
The map $t \mapsto A(f^{-1}(t))$ is a holomorphic map from $\mathbb{P}^1$ to the torus $J(X)$, so it is constant, and $A(D) = A(f^{-1}(0)) - A(f^{-1}(\infty)) = 0$.
The converse builds $f$ as the exponential of an integral of a meromorphic differential with prescribed residues, whose periods are adjusted using $A(D) = 0$.
Jacobi inversion follows from a dimension count: the map from the $g$-fold symmetric product of $X$ to $J(X)$ has invertible differential at a general point, by Riemann–Roch.
So its image is a compact analytic subset of dimension $g$ in the connected torus $J(X)$ of dimension $g$, which must be all of $J(X)$.
Example: take $g = 1$ and $X = \C / \Lambda$ with base point $0$.
Abel's theorem says that $\sum n_i [z_i]$ with $\sum n_i = 0$ is the divisor of an elliptic function exactly when $\sum n_i z_i \in \Lambda$.

## Explanations

### L1 human

On a compact surface, a meromorphic function must have as many zeros as poles.
Abel's theorem gives the exact extra condition that a choice of zeros and poles must satisfy to come from a function: a certain sum of integrals must vanish modulo periods.
Jacobi inversion says that the target of these sums is completely filled out by sums of $g$ points.
So the group of divisor classes of degree zero is the same as the Jacobian torus.

### L2 human

The theorem identifies an algebraic object, the Picard group of degree $0$, with an analytic one, the torus of periods.
This identification is how one proves that the Jacobian is an algebraic variety and how one studies linear systems on curves through the geometry of theta divisors.
For an elliptic curve it gives the isomorphism between the curve with its group law and $\C / \Lambda$.
It is the starting point of Brill–Noether theory and of the Torelli theorem.

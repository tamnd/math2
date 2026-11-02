---
tag: DRY1HXP1W9
kind: statement
role: theorem
name: Hopf's theorem on cohomology of compact Lie groups
msc: [57T10, 57T05]
uses: [9TFC6ADC1C, HKZABKRPN6, 0MDMZ965VE, WJXK0V9NE9]
about: [9TFC6ADC1C, HKZABKRPN6]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Statement

Let $G$ be a connected [[compact Lie group|9TFC6ADC1C]] and let $k$ be a field of characteristic $0$.
Then the [[cohomology|HKZABKRPN6]] $H^*(G; k)$ is isomorphic, as a graded $k$-algebra, to an [[exterior algebra|0MDMZ965VE]] $\Lambda_k(x_1, \dots, x_r)$ on finitely many generators $x_i$ of odd degrees $d_1, \dots, d_r$.

## Remarks

Hopf's proof uses only the [[Hopf algebra|WJXK0V9NE9]] structure given by the multiplication of $G$, together with finite-dimensionality.
Over a field of characteristic $0$, a connected graded-commutative Hopf algebra is free as a graded-commutative algebra.
That is, it is a polynomial algebra on generators of even degree tensored with an exterior algebra on generators of odd degree.
A polynomial generator of even degree would have infinitely many nonzero powers, which is impossible in finite dimension.
So all generators have odd degree.
The same argument works for any connected H-space with finite-dimensional rational cohomology.

Further facts: the number $r$ of generators equals the rank of $G$, the dimension of a maximal torus, and $d_1 + \cdots + d_r = \dim G$, since the product $x_1 \cdots x_r$ spans the top cohomology.

Example: for $G = \mathrm{SU}(n)$, the degrees are $3, 5, \dots, 2n - 1$, with $r = n - 1$ and $3 + 5 + \cdots + (2n - 1) = n^2 - 1 = \dim \mathrm{SU}(n)$.
For $G = \mathrm{SU}(2) \cong S^3$, this is $H^*(S^3; \Q) = \Lambda(x_3)$.

The characteristic $0$ hypothesis is needed.
The group $\mathrm{SO}(3)$ is homeomorphic to $\R P^3$, and $H^*(\R P^3; \F_2) = \F_2[x]/(x^4)$ with $\abs{x} = 1$, which is not an exterior algebra since $x^2 \ne 0$.

## Explanations

### L1 human

The holes of a compact connected Lie group have a very simple pattern.
There are a few basic holes, all of odd dimension, and every other hole is a combination of distinct basic holes.
For the group $\mathrm{SU}(2)$, a $3$-sphere, there is just one basic hole of dimension $3$.

### L2 human

The theorem explains why the rational cohomology of a compact Lie group looks like that of a product of odd spheres.
For example $H^*(\mathrm{U}(n); \Q)$ is that of $S^1 \times S^3 \times \cdots \times S^{2n-1}$.
The degrees $d_i$ are $2m_i + 1$, where the $m_i$ are the exponents of the Weyl group, and the $m_i + 1$ are the degrees of its basic invariant polynomials.
With integer or mod $p$ coefficients the cohomology can have torsion, and its study is much harder.

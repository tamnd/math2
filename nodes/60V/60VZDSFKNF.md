---
tag: 60VZDSFKNF
kind: definition
name: Projective line over a ring
msc: [51C05]
defines: M6BN1K0B30
uses: [0B1261B5ED, 07C6ECNJET, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_line_over_a_ring
---

## Definition

Let $R$ be an associative [[ring|0B1261B5ED]] with identity, and let $U$ be its [[group of units|07C6ECNJET]].
A pair $(a, b) \in R^2$ is *admissible* if there are $c, d \in R$ such that the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ lies in the [[general linear group|0FCHE902D7]] $\mathrm{GL}(2, R)$.
The *projective line over $R$* is the set
$$\mathrm{P}(R) = \set{U(a, b) : (a, b) \in R^2 \text{ admissible}},$$
where $U(a, b) = \set{(ua, ub) : u \in U}$.

## Remarks

The group $\mathrm{GL}(2, R)$ acts on $\mathrm{P}(R)$ by $U(a, b) \mapsto U\big((a, b) M\big)$.
If $R$ is commutative, $(a, b)$ is admissible if and only if $aR + bR = R$.
Indeed, if $ax + by = 1$ then $\begin{pmatrix} a & b \\ -y & x \end{pmatrix}$ has determinant $1$; conversely the first row of an invertible matrix generates $R$, by expanding its determinant.

Example: if $R$ is a field $F$, every $(a, b) \ne (0, 0)$ is admissible, and $\mathrm{P}(F)$ is the usual projective line $\set{U(x, 1) : x \in F} \cup \set{U(1, 0)}$.

Example: for $R = \Z$, admissible means $\gcd(a, b) = 1$ and $U = \set{1, -1}$, so $\mathrm{P}(\Z)$ is in bijection with $\Q \cup \set{\infty}$ by $U(a, b) \mapsto a / b$.

Non-example: in $\Z$, the pair $(2, 0)$ is not admissible, because $2\Z + 0\Z = 2\Z \ne \Z$.

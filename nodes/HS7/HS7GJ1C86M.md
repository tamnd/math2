---
tag: HS7GJ1C86M
kind: definition
name: Jónsson terms
msc: [08B05, 08B10]
defines: 3M8Y76E4AG
uses: [AJNZJD8442, PKD440G2XW, 9GZ7F6ETC6]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_lattice
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras and let $n \ge 1$.
*Jónsson terms* for $\mathcal{V}$ are ternary terms $d_0, d_1, \dots, d_n$ such that $\mathcal{V}$ satisfies the following [[identities|PKD440G2XW]]:

1. $d_0(x, y, z) = x$ and $d_n(x, y, z) = z$.
2. $d_i(x, y, x) = x$ for every $i \le n$.
3. $d_i(x, x, z) = d_{i+1}(x, x, z)$ for every even $i < n$.
4. $d_i(x, z, z) = d_{i+1}(x, z, z)$ for every odd $i < n$.

## Remarks

Jónsson's theorem says that $\mathcal{V}$ is a [[congruence-distributive variety|9GZ7F6ETC6]] if and only if $\mathcal{V}$ has Jónsson terms for some $n$.
Example: lattices have Jónsson terms with $n = 2$: $d_0 = x$, $d_1 = (x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$, $d_2 = z$.
The checks are $d_1(x, y, x) = x$, $d_0(x, x, z) = x = d_1(x, x, z)$, and $d_1(x, z, z) = z = d_2(x, z, z)$.
More generally, a majority term $m$ always gives Jónsson terms $x, m, z$.
Non-example: for groups, the terms $x$, $x y^{-1} z$, $z$ are not Jónsson terms.
Clause 2 fails for the middle term: in the group $\Z$, the value $x - y + x$ differs from $x$ when $y \ne x$.

## Explanations

### L1 human

Jónsson terms are a chain of three-input formulas that witness, by equations alone, that a variety has distributive congruence lattices.

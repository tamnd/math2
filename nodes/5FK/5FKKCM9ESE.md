---
tag: 5FKKCM9ESE
kind: definition
name: Quasi-projective variety
msc: [14A10, 14N05]
defines: EQSHJPE7H8
uses: [A4H4CZ2V35, ZT9A6JK8QF, 02BH3MCBQB, 0WS9P12FQR, JERVQT4C12, SY2MWC434Z]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-projective_variety
---

## Definition

Let $k$ be an algebraically closed field and let $\mathbb{P}^n$ be the [[projective space|ZT9A6JK8QF]] over $k$ with the Zariski topology.
A *quasi-projective variety* is a nonempty [[open subset|02BH3MCBQB]] $X$ of a [[projective variety|A4H4CZ2V35]] $Y \subseteq \mathbb{P}^n$, with the [[subspace topology|0WS9P12FQR]].

## Remarks

Equivalently, $X$ is an [[irreducible|SY2MWC434Z]] subset of $\mathbb{P}^n$ of the form $Y \setminus Z$, where $Y$ and $Z$ are projective algebraic sets.
A nonempty open subset of an irreducible space is irreducible and dense, so $X$ is irreducible and its closure is $Y$.

Example: every [[affine variety|JERVQT4C12]] $X \subseteq k^n$ is quasi-projective.
Identify $k^n$ with the chart $U_0 = \set{x_0 \ne 0}$ of $\mathbb{P}^n$; then $X$ is open in its closure $\overline{X} \subseteq \mathbb{P}^n$, which is a projective variety.
Every projective variety is quasi-projective, taking $X = Y$.

Example: $k^2 \setminus \set{(0, 0)}$ is quasi-projective, as an open subset of $\mathbb{P}^2$; it is neither affine nor projective.

Non-example: $V(xy) \setminus \set{[0 : 0 : 1]} \subseteq \mathbb{P}^2$ is open in a projective algebraic set but is not a quasi-projective variety, because it is the union of two proper closed subsets, the two punctured lines.

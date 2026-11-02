---
tag: CECPTP66EK
kind: definition
name: Algebraic variety
msc: [14A10]
defines: HV6YBS0YDH
uses: [0PF6TM8TWT, JERVQT4C12, A4H4CZ2V35, EQSHJPE7H8, SY2MWC434Z]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_variety
---

## Definition

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]].
An *algebraic variety* over $k$ (in the classical sense) is one of the following, with its Zariski topology:

1. an [[affine variety|JERVQT4C12]], that is, an irreducible algebraic set in $k^n$;
2. a quasi-affine variety, that is, a nonempty open subset of an affine variety;
3. a [[projective variety|A4H4CZ2V35]], that is, an irreducible projective algebraic set in $\mathbb{P}^n$;
4. a [[quasi-projective variety|EQSHJPE7H8]], that is, a nonempty open subset of a projective variety.

## Remarks

Each of the four kinds is a quasi-projective variety, so the definition says that a variety is a quasi-projective variety.
Every variety is [[irreducible|SY2MWC434Z]] and its topology is Noetherian.

Example: the affine line $k$, the projective plane $\mathbb{P}^2$, and the punctured plane $k^2 \setminus \set{(0, 0)}$ are varieties.

Non-example: $V(xy) \subseteq k^2$ is not a variety in this sense, since it is reducible.

Other conventions exist.
Some authors allow reducible varieties.
In the language of schemes, a variety over any field $k$ is often an integral separated scheme of finite type over $k$.
This includes abstract varieties that are not quasi-projective.

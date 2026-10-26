---
tag: 0AH9Q6YNMT
kind: statement
role: proposition
name: If G modulo its centre is cyclic then G is abelian
msc: [20A05]
uses: [0S7Y9Q990Q, 0YYWCNTPWR, 0B85Q41RP6]
sources:
  - url: https://en.wikipedia.org/wiki/Center_(group_theory)
    locator: Examples
---

## Statement

Let $G$ be a [[group|G5S1M9]] with [[centre|0DZ93493VN]] $Z(G)$.
If the [[quotient group|0KYX2N69J0]] $G/Z(G)$ is [[cyclic|0KVGH0J5B3]], then $G$ is [[abelian|082GHNPJ53]].

## Remarks

Let $gZ(G)$ generate $G/Z(G)$; then each element of $G$ is $g^k z$ with $k \in \mathbb{Z}$ and $z \in Z(G)$, and two such elements commute.
In that case $G = Z(G)$, so in fact $G/Z(G)$ is trivial.
A consequence is that $G/Z(G)$ is never cyclic of order greater than $1$. For example, the centre of a group never has prime index.

## Explanations

### L1 human

If the elements of $G$ are powers of one element, up to central elements, then all elements commute.
Powers of one element commute with each other, and central elements commute with everything.
So the quotient by the centre cannot be a nontrivial cyclic group.

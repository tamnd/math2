---
tag: 2XCJ8NNMXP
kind: statement
role: theorem
name: Z* theorem
msc: [20D20, 20C20]
uses: [G5S1M9, 0CB0DX5BVV, 0053CQE9Y2, 0DXD4QSZ8A, 0DZ93493VN, 0KYX2N69J0, 0WE2NHZJ7B, 0YMYMNQ0QZ, H1BSG0J5G1]
about: [0053CQE9Y2, 0DZ93493VN]
sources:
  - url: https://en.wikipedia.org/wiki/Z*_theorem
same_as:
  wikidata: Q8062800
  wikipedia: Z* theorem
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], and let $O(G)$ be the largest [[normal subgroup|0CB0DX5BVV]] of $G$ of odd order.
Let $T$ be a [[Sylow $2$-subgroup|0053CQE9Y2]] of $G$, and let $t \in T$ be an involution, that is, an element of [[order|0WE2NHZJ7B]] $2$.
Suppose that no element of $T$ other than $t$ is [[conjugate|0DXD4QSZ8A]] to $t$ in $G$.
Then $t \, O(G)$ lies in the [[centre|0DZ93493VN]] of the [[quotient group|0KYX2N69J0]] $G/O(G)$.

## Remarks

The theorem is due to George Glauberman, and its proof uses modular representation theory, in particular Brauer's theory of blocks.
The notation comes from $Z^*(G)$, the subgroup of $G$ containing $O(G)$ with $Z^*(G)/O(G) = Z(G/O(G))$; the conclusion says $t \in Z^*(G)$.

Example: $G = S_3$ and $t = (1\,2)$ in $T = \set{e, (1\,2)}$.
No other element of $T$ is conjugate to $t$, and $O(S_3) = A_3$.
Indeed $S_3 / A_3$ has order $2$, so it is abelian and $t A_3$ is central.

Corollary: if $G$ is a nonabelian [[simple group|0YMYMNQ0QZ]], then every involution $t$ in a Sylow $2$-subgroup $T$ is conjugate in $G$ to another element of $T$.
Indeed, $G$ has even order because it contains $t$, so $O(G) \ne G$; hence $O(G) = \set{e}$ by simplicity, and the centre of $G$ is trivial, so $t$ cannot be central.

## Explanations

### L1 human

An involution is an element that undoes itself, like a reflection.
Call an involution isolated if conjugation never moves it onto another element of its Sylow $2$-subgroup.
The Z* theorem says that an isolated involution becomes central after dividing out the largest normal subgroup of odd order.
So isolated involutions cannot exist in a nonabelian simple group.

### L2 human

The Z* theorem is a result about fusion of $2$-elements, like the [[focal subgroup theorem|H1BSG0J5G1]] but for single involutions.
It was an important tool in the classification of finite simple groups, where it rules out isolated involutions.
The proof by modular character theory is a striking case where representation theory is needed for a statement about conjugacy in a group.

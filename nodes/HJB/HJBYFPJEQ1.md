---
tag: HJBYFPJEQ1
kind: definition
name: Fraïssé limit
msc: [03C15, 03C52]
defines: HJVRBDQSGG
uses: [983GZBQYT4, 676H7EGTKJ, XSCSX39GEZ, 01TQB88H4C, 0K1SCPBNKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
---

## Definition

Let $L$ be a countable signature.
The *age* of an [[$L$-structure|983GZBQYT4]] $M$ is the class of all finitely generated $L$-structures that embed into $M$.
Let $\mathcal{K}$ be a class of finitely generated $L$-structures, closed under isomorphism.
A *Fraïssé limit* of $\mathcal{K}$ is an $L$-structure $M$ such that:

1. $M$ is [[countable|01TQB88H4C]];
2. the age of $M$ is $\mathcal{K}$;
3. $M$ is ultrahomogeneous: every isomorphism between two finitely generated [[substructures|676H7EGTKJ]] of $M$ extends to an [[automorphism|0K1SCPBNKJ]] of $M$.

## Remarks

Fraïssé's theorem: suppose $\mathcal{K}$ is nonempty and has countably many isomorphism types.
Suppose it has the hereditary property, the joint embedding property and the [[amalgamation property|XSCSX39GEZ]].
Then $\mathcal{K}$ has a Fraïssé limit, and any two Fraïssé limits of $\mathcal{K}$ are isomorphic.
Conversely, the age of a countable ultrahomogeneous structure has these properties.

Example: $(\Q, <)$ is the Fraïssé limit of the class of finite linear orders.
Every finite linear order embeds in $\Q$, so clause 2 holds.
For clause 3, an order isomorphism between finite subsets of $\Q$ extends piecewise linearly to an order automorphism of $\Q$.

Non-example: $(\Z, <)$ is countable and its age is again the class of finite linear orders, but it fails clause 3.
The map $0 \mapsto 0$, $1 \mapsto 2$ is an isomorphism between the substructures $\set{0, 1}$ and $\set{0, 2}$.
It has no extension to an automorphism, because no integer lies strictly between $0$ and $1$, while $1$ lies strictly between $0$ and $2$.

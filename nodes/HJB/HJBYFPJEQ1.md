---
tag: HJBYFPJEQ1
kind: definition
name: Fraïssé limit
msc: ["03C15", "03C52"]
topics: [ZS8X8KS54R]
audience: grad
defines: HJVRBDQSGG
uses: [983GZBQYT4, 676H7EGTKJ, XSCSX39GEZ, 01TQB88H4C, DSQ17TNW1C, ~41dc9926, ~7468669e]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Fraïssé's theorem
  - book: isbn:9780521587136
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.IsFraisseLimit
    match: exact
---

## Definition

Let $L$ be a countable signature.
The *age* of an [[$L$-structure|983GZBQYT4]] $M$ is the class of all finitely generated $L$-structures that embed into $M$.
Let $\mathcal{K}$ be a class of finitely generated $L$-structures, closed under isomorphism.
A *Fraïssé limit* of $\mathcal{K}$ is an $L$-structure $M$ such that:

1. $M$ is [[countable|01TQB88H4C]];
2. the [[age|~41dc9926]] of $M$ is $\mathcal{K}$;
3. $M$ is [[ultrahomogeneous|~7468669e]]: every isomorphism between two finitely generated [[substructures|676H7EGTKJ]] of $M$ extends to an [[automorphism|DSQ17TNW1C]] of $M$.

## Notation

The limit is written $\operatorname{Flim}(\mathcal{K})$.
A class with the hypotheses of Fraïssé's theorem is called a *Fraïssé class*.

## Remarks

[[Fraïssé's theorem|~8123841a]]: suppose $\mathcal{K}$ is nonempty and has countably many isomorphism types.
Suppose it has the hereditary property, the joint embedding property and the [[amalgamation property|XSCSX39GEZ]].
Then $\mathcal{K}$ has a Fraïssé limit, and any two Fraïssé limits of $\mathcal{K}$ are isomorphic.
Conversely, the age of a countable ultrahomogeneous structure has these properties.

Example: $(\Q, <)$ is the Fraïssé limit of the class of finite linear orders.
Every finite linear order embeds in $\Q$, so clause 2 holds.
For clause 3, an order isomorphism between finite subsets of $\Q$ extends piecewise linearly to an order automorphism of $\Q$.

Non-example: $(\Z, <)$ is countable and its age is again the class of finite linear orders, but it fails clause 3.
The map $0 \mapsto 0$, $1 \mapsto 2$ is an isomorphism between the substructures $\set{0, 1}$ and $\set{0, 2}$.
It has no extension to an automorphism, because no integer lies strictly between $0$ and $1$, while $1$ lies strictly between $0$ and $2$.

## Explanations

### L1 human

A Fraïssé limit of a class of finite pieces is a countable structure whose finite pieces are exactly the members of the class, and in which any two copies of the same piece are related by a symmetry.

### L2 human

We check the three clauses for a countably infinite set $M$ in the empty signature, with $\mathcal{K}$ the finite sets.

1. $M$ is countable.
2. Every finite set embeds into $M$, and every subset of $M$ is a set, so the age is $\mathcal{K}$.
3. A bijection between finite subsets of $M$ extends to a permutation of $M$, since the complements are both countably infinite.

A trap is to drop clause 3; for the finite linear orders, $(\Z, <)$ would then count as a limit, and uniqueness would fail.

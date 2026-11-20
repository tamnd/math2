---
tag: 00MS9VMQ9Z
kind: statement
role: theorem
name: Every vector space has a basis
msc: ["15A03", "03E25"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV]
proofs: [YVM74DY0WD]
formal:
  - system: lean4
    library: mathlib
    decl: Module.Basis.ofVectorSpace
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
  - url: https://en.wikipedia.org/wiki/Axiom_of_choice
    locator: Equivalents
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Statement

Let $F$ be a field and let $V$ be a vector space over $F$.
Then $V$ has a [[basis|0VTQTPQGAV]].

## Remarks

### Why each hypothesis is needed

The hypothesis that $F$ is a field is needed: the $\Z$-module $\Z/2$ has no basis, because $1 \cdot \bar 1 \ne 0$ but $2 \cdot \bar 1 = 0$ with $2 \ne 0$ in $\Z$.
So every nonempty family in $\Z/2$ fails independence, and the empty family fails spanning.
For infinite-dimensional $V$, the proof needs the [[axiom of choice|0HTGB13FE2]], in the form of [[Zorn's lemma|04RXTQA5ZA]].
For finite-dimensional $V$, no choice is needed; see [[every spanning set contains a basis|06MRNP4BNT]].
The zero space is no exception: its basis is the empty set.

### Consequences

1. Each vector space over $F$ is isomorphic to $F^{(B)}$, the space of finitely supported functions on a basis $B$.
2. Each vector space has a [[dimension|03GSZ8RTZJ]], and each subspace has a complement.
3. $\R$ has a basis over $\Q$, a Hamel basis; see the [[Hamel basis example|~2a984d12]].
4. There are additive maps $f \colon \R \to \R$ that are not of the form $f(x) = cx$: choose a Hamel basis $B$ and let $f$ act on the coordinates.

### Converse

Blass proved the converse over set theory without choice.
Exact form: in ZF, if every vector space over every field has a basis, then the axiom of choice holds.
The reference is Blass, "Existence of bases implies the axiom of choice", Contemporary Mathematics 31 (1984), 31 to 33.
His proof derives the axiom of multiple choice, which is equivalent to the axiom of choice over ZF.
So, over ZF, "every vector space has a basis" is equivalent to the axiom of choice.

### Generalizations

1. Each independent set extends to a basis; see [[the extension theorem|0M4SXE5WW3]].
2. Each vector space over a division ring has a basis, by the same proof.
3. Each module over a ring $R$ is free if and only if $R$ is a division ring.

## History

Hamel used a well-ordering of $\R$ in 1905 to build a basis of $\R$ over $\Q$.
Blass proved the converse in 1984.

## Explanations

### L1 human

Every vector space has a set of building blocks that is independent and reaches every vector.
For finite-dimensional spaces, we can find one by hand.
For very large spaces, we must use the axiom of choice, and we may not be able to write the basis down.

### L2 human

Nobody can write down a basis of $\R$ over $\Q$ explicitly.
The theorem gives one, but without a formula, because the axiom of choice gives no construction.
Over ZF alone, the existence of such a basis cannot be proved.
This is also why the Mathlib name is `Module.Basis.ofVectorSpace`: it is a noncomputable definition.

### L3 human

The proof shows more: a maximal independent set is a basis.
Blass's converse shows that the axiom of choice is the exact price of this theorem.
Weaker forms, such as "each vector space over $\Q$ has a basis", are also studied; their exact strength over ZF is a separate question.

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

No matter how large a vector space is, it has a set of building blocks: an independent set that reaches every vector.
Let $F$ be a field and let $V$ be a vector space over $F$.
Then $V$ has a [[basis|0VTQTPQGAV]].

## Remarks

### From small spaces to large ones

For the spaces met first, a basis is in plain sight.
The space $F^n$ has the standard basis $e_1, \dots, e_n$, and the polynomials $F[x]$ have the monomials $1, x, x^2, \dots$, an infinite but explicit basis.
The zero space has the empty set as its basis, since the empty set is independent and its span is $\{0\}$.
The theorem says that the same is true for every vector space, including spaces such as $\mathbb{R}$ over $\mathbb{Q}$ where nobody can name a basis.
The [[proof by Zorn's lemma|YVM74DY0WD]] takes a maximal independent set and shows that it spans.

### Why the scalars must form a field

Over a ring that is not a field, a module can have no basis at all.
Take the group $\mathbb{Z}/2$ with the integers as scalars.
Every element $\bar a$ satisfies $2 \cdot \bar a = \bar 0$ with $2 \ne 0$, so every nonempty family is dependent.
The empty family spans only $\{\bar 0\}$, so it is not a basis either.

The rationals over the integers fail in a different way.
Any two nonzero rationals $\tfrac{p}{q}$ and $\tfrac{r}{s}$ satisfy
$$rq \cdot \frac{p}{q} - ps \cdot \frac{r}{s} = rp - pr = 0,$$
a relation with nonzero integer coefficients, so an independent set has at most one element.
One element $\tfrac{a}{b}$ does not span, because $\tfrac{a}{2b}$ is not an integer multiple of it.
So $\mathbb{Q}$ has no basis over $\mathbb{Z}$.
Both failures come from the same place: the proof divides by a nonzero coefficient, and in $\mathbb{Z}$ we cannot divide.

### The role of the axiom of choice

For a space with a finite spanning set, [[every spanning set contains a basis|06MRNP4BNT]] by removing vectors one at a time, and no choice principle is needed.
In general the proof uses [[Zorn's lemma|04RXTQA5ZA]], which is equivalent to the [[axiom of choice|0HTGB13FE2]].
The converse is also true.
Blass proved in 1984 that, in Zermelo-Fraenkel set theory without choice, the statement "every vector space over every field has a basis" implies the axiom of choice.
So over that set theory the theorem and the axiom of choice are equivalent.
His proof derives the axiom of multiple choice, which is known to be equivalent to the axiom of choice over the same theory.

### What it gives you

Fix a basis $B$ of $V$.
Each vector is a unique finite combination of elements of $B$, so $V$ is isomorphic to the space $F^{(B)}$ of functions $B \to F$ that are zero outside a finite set.
Every vector space therefore has a [[dimension|03GSZ8RTZJ]], and the [[extension theorem|0M4SXE5WW3]] gives every subspace a complement.
For $\mathbb{R}$ over $\mathbb{Q}$ the theorem gives a [[Hamel basis|ZCBD0GRGVA]], and with it [[additive functions that are not continuous|FFTNS66XG6]].

### Watch out

The theorem gives a basis, not a formula for one.
In the zero space the basis is empty, which surprises many readers, but the definition of a basis needs no vectors there.
And a basis here means finite combinations only, so a [[Schauder basis|RZT4WMH4SG]] of a Banach space, which allows infinite sums, is a different notion.

### Generalizations

The same proof works over a division ring, so every module over a division ring is free.
The converse also holds for rings: if every module over a ring $R$ with $1 \ne 0$ is free, then $R$ is a division ring.
The stronger form, that every independent set extends to a basis, is the [[extension theorem|0M4SXE5WW3]].

## History

Hamel used a well-ordering of $\mathbb{R}$ in 1905 to build a basis of $\mathbb{R}$ over $\mathbb{Q}$, and he used it to find discontinuous solutions of $f(x + y) = f(x) + f(y)$.
Blass proved in 1984 that the existence of bases for all vector spaces implies the axiom of choice.

## Explanations

### L1 human

A basis is a set of building blocks: every vector is made from them in exactly one way.
For the plane, the two arrows $(1, 0)$ and $(0, 1)$ do the job.
The theorem says that every vector space has such a set, even a huge one.
For very large spaces, the proof shows that a basis exists but does not tell us what it is.
The real numbers, seen as a space over the fractions, have a basis, but nobody can list its elements.

### L2 human

Why can the proof not be turned into a construction for $\mathbb{R}$ over $\mathbb{Q}$?
The finite procedure says: keep picking a vector outside the span of those picked so far.
Start with $1$, then $\sqrt{2}$, then $\sqrt{3}$, and so on.
Any countable list of reals spans only a countable set, because there are countably many finite combinations with rational coefficients.
Since $\mathbb{R}$ is uncountable, the picking never ends after countably many steps, and the proof needs a choice principle to finish.
It is consistent with Zermelo-Fraenkel set theory without choice that $\mathbb{R}$ has no basis over $\mathbb{Q}$, so no construction can exist.
This is also why the Mathlib definition `Module.Basis.ofVectorSpace` is marked noncomputable.

### L3 human

A basis of $V$ is an isomorphism $F^{(B)} \cong V$, so the theorem says that every vector space is free, and that the category of vector spaces over $F$ is classified by one cardinal, the dimension.
The proof is the standard first use of Zorn's lemma in algebra, and the same pattern gives maximal ideals in rings and algebraic closures of fields.
Blass's converse shows that the axiom of choice is exactly the price of the theorem.
Later sub-areas use bases of infinite-dimensional spaces freely, for example to build [[dual spaces|07JBSZE0V4]] and [[quotient spaces|0BR3FY5Q8M]].

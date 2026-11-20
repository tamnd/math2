---
tag: 0P9T8WHNMH
kind: statement
role: theorem
name: Existence of a complementary subspace
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0M83V17KHX]
uses: [04C3BAHV03, 0EPTJA5QV4, 05EGHEQZAW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.exists_isCompl
    match: stronger
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

Let $F$ be a field, let $V$ be a [[vector space|05EGHEQZAW]] over $F$, and let $U$ be a [[subspace|0EPTJA5QV4]] of $V$.
Then $U$ has a [[complement|04C3BAHV03]] in $V$: there is a subspace $W$ of $V$ with $V = U \oplus W$.

If $V$ is finite-dimensional, then every complement $W$ satisfies $\dim W = \dim V - \dim U$.

## Remarks

### Why each hypothesis is needed

- $F$ must be a field. Over the ring $\Z$, the submodule $2\Z$ of $\Z$ [[has no complement|~16a41b18]]. The proofs divide by a nonzero scalar, which needs a field.
- $U$ must be a subspace. A subset that is not a subspace, such as a line not through $0$, cannot be one of the summands of a direct sum.
- No finite-dimensionality is needed for existence. In infinite dimension, the proof uses Zorn's lemma, and it cannot be done without some form of the axiom of choice.

### Consequences

- Every subspace is the [[image of a projection|033DA1WE8Y]]: take the projection onto $U$ along a complement.
- Every linear map $g \colon U \to X$ extends to a linear map $V \to X$: set it equal to $0$ on a complement.
- Every injective linear map $f \colon U \to V$ has a left inverse, and every surjective linear map has a right inverse. So every [[short exact sequence|~5d243d10]] of vector spaces splits.
- Every quotient $V / U$ is isomorphic to a subspace of $V$, namely to any complement, by the [[theorem on complements and quotients|~7fe638c8]].

### Converse

The complement is unique only when $U = \{0\}$ or $U = V$.
In the other cases, over an infinite field, there are infinitely many complements, as for [[the x-axis in the plane|~1703fda9]].

### Generalizations

- Over any division ring the same proof works.
- For modules over a ring $R$, every submodule of every module has a complement exactly when $R$ is semisimple.
- For closed subspaces of a Banach space, a closed complement need not exist.

## History

In finite dimension, the result follows from the extension of a basis, which goes back to Steinitz's exchange lemma of 1913.
For infinite-dimensional spaces, Hamel used the well-ordering theorem in 1905 to build a basis of $\R$ over $\mathbb{Q}$.
Later proofs of the existence of bases and complements use Zorn's lemma.
It is now known that "every vector space has a basis" is equivalent to the axiom of choice, a result of Blass from 1984.

## Explanations

### L1 human

Every subspace has a partner subspace that fills up the rest of the space.
We find it by completing a basis of the subspace and taking the span of the new vectors.
The partner is not unique, but in finite dimension its dimension is fixed.

### L2 human

The [[proof by extending a basis|K653S85P27]] is a recipe.

1. Take $U = \{(x, y, z) : x + y + z = 0\}$ in $\R^3$, with basis $(1, -1, 0)$ and $(0, 1, -1)$.
2. Add $e_1 = (1, 0, 0)$. The three vectors are independent, so they form a basis of $\R^3$.
3. Then $W = \R e_1$ is a complement, as worked out in [[the example of a plane in R³|~09539e17]].

The trap is to look for "the" complement: the line $\R(1, 1, 1)$ is another one.

### L3 human

There are two standard proofs.
The [[first proof|K653S85P27]] extends a basis of $U$ to a basis of $V$, which in infinite dimension rests on Zorn's lemma.
The [[second proof|~b831b6bc]] applies Zorn's lemma directly to the subspaces that meet $U$ only in $0$.
The statement says that the lattice of subspaces is complemented, and together with modularity this makes it a projective geometry.
In category theory, it says that every object of the category of vector spaces is injective and projective.

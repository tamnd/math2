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

Every subspace of a vector space has a partner subspace that completes it to a direct sum.
Let $F$ be a field, let $V$ be a [[vector space|05EGHEQZAW]] over $F$, and let $U$ be a [[subspace|0EPTJA5QV4]] of $V$.
Then $U$ has a [[complement|04C3BAHV03]] in $V$: there is a subspace $W$ of $V$ with $V = U \oplus W$.
If $V$ is finite-dimensional, then every complement $W$ of $U$ satisfies $\dim W = \dim V - \dim U$.

## Remarks

### Two proofs

In finite dimension the [[proof by extending a basis|K653S85P27]] is a recipe that you can carry out by hand.
Take a basis of $U$, add vectors until you have a basis of $V$, and let $W$ be the span of the added vectors.
For the plane $U$ given by $x + y + z = 0$ in $\R^3$, the basis $(1, -1, 0), (0, 1, -1)$ of $U$ together with $e_1 = (1, 0, 0)$ is a basis of $\R^3$, so $W = \R e_1$ is a complement; [[two complements of a plane in R³|DVP2D04EZD]] checks this.

In infinite dimension the same recipe works, but the extension of a basis needs Zorn's lemma.
The [[proof by Zorn's lemma|P9V296DEAX]] applies Zorn's lemma directly to the subspaces that meet $U$ only in $0$ and takes a maximal one.
For example, in the space $F[x]$ of polynomials, the subspace of polynomials with $p(0) = 0$ has the constants as a complement, and no choice principle is needed to see this.
For a subspace of a large space with no explicit basis, such as $\mathbb{Q}$ inside $\R$ over $\mathbb{Q}$, a complement exists, but the proof gives no explicit description of it.

### Why each hypothesis is needed

The scalars must form a field.
Over the ring $\Z$, the submodule $2\Z$ of $\Z$ [[has no complement|XK7YECSHR9]], because every nonzero submodule $n\Z$ contains the nonzero even number $2n$.
Both proofs divide by a nonzero scalar at one step, and that step fails over $\Z$.

The set $U$ must be a subspace.
A line that misses the origin is not a subspace, and it cannot be a summand of a direct sum, since every summand contains $0$.

Finite dimension is not needed for existence, only for the dimension formula.
In infinite dimension the proof uses Zorn's lemma, which is equivalent to the [[axiom of choice|0HTGB13FE2]].

### What it gives you

Every subspace is the image of a [[projection|033DA1WE8Y]]: take the projection onto $U$ along a complement.
Every linear map $g \colon U \to X$ extends to a linear map $V \to X$: define it as $g$ on $U$ and as $0$ on a complement.
Every injective linear map has a left inverse, and every surjective linear map has a right inverse, so every [[short exact sequence|1GYTT98CC5]] of vector spaces splits.
Every quotient $V / U$ is isomorphic to a subspace of $V$, namely to any complement, by the theorem that [[every complement is isomorphic to the quotient|244KTXDJHW]].

### Uniqueness fails

The theorem gives existence, not uniqueness.
A complement is unique only when $U = \{0\}$ or $U = V$.
In every other case there are at least two complements, and over an infinite field there are infinitely many, as for [[the x-axis in the plane|S8TRB7953Y]], whose complements are the lines $\R(m, 1)$.

### Generalizations

The same proofs work over a division ring, since they only divide by nonzero scalars.
For modules over a ring $R$, every submodule of every module has a complement exactly when $R$ is a [[semisimple ring|NY25HXA478]].
For a closed subspace of a [[Banach space|06GZ956657]], one asks for a closed complement, and it need not exist; this is the subject of [[complemented subspaces|Q0TY362K0V]].

## History

In finite dimension the theorem follows from the extension of an independent list to a basis, which rests on the [[exchange lemma|08ZDRN6H41]] named after Ernst Steinitz.
For infinite-dimensional spaces, Georg Hamel used the well-ordering theorem in 1905 to construct a basis of $\R$ over $\mathbb{Q}$.
Andreas Blass proved in 1984 that the statement "every vector space has a basis" implies the axiom of choice, so some choice principle is unavoidable for bases in general.

## Explanations

### L1 human

Every subspace has a partner subspace that fills up the rest of the space.
To find one, list a basis of the subspace and keep adding new directions until you have a basis of the whole space.
The new directions span the partner.
In space, a plane through the origin has the partner "any line through the origin that leaves the plane".

### L2 human

Here is the recipe for $U = \operatorname{span}\{(1, 2, 0), (0, 1, 1)\}$ in $\R^3$.
We try to add $e_1 = (1, 0, 0)$ and compute the determinant of the matrix with columns $(1, 2, 0)$, $(0, 1, 1)$ and $e_1$:
$$\det \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 0 & 1 & 0 \end{pmatrix} = 1 \cdot \det \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = 2.$$
The determinant is not $0$, so the three vectors form a basis, and $W = \R e_1$ is a complement of $U$.
If we had tried $(1, 3, 1) = (1, 2, 0) + (0, 1, 1)$, the determinant would be $0$, because that vector already lies in $U$.
The typical use is to start a proof with "choose a complement $W$ of $U$", and then to work in $U$ and $W$ separately.
The trap is to look for "the" complement: the $z$-axis is also a complement of this $U$, as is every line through $0$ outside $U$.

### L3 human

The theorem says that the lattice of subspaces of $V$ is complemented, and this lattice is also modular.
In the language of categories, every short exact sequence of vector spaces splits, so every vector space is both an injective and a projective object.
This is why the groups $\operatorname{Ext}^n_F(X, U)$ vanish for $n \ge 1$, and why a [[short exact sequence|1GYTT98CC5]] $0 \to U \to V \to X \to 0$ always gives $V \cong U \oplus X$.
For modules over $\Z$ the same question leads to the theory of direct summands of abelian groups, where complements are rare.

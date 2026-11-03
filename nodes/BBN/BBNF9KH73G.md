---
tag: BBNF9KH73G
kind: statement
role: theorem
name: Quillen's localization theorem
msc: [19D06, 18F25]
uses: [Y9CZ3MTNF1, CSD6W0JV0P, J9XP7CS943, 4F3KWXYXBA, JB7ZBFBA9C, 7NPY2CN5KB, YZSR4QKDQQ, DYV91576BQ, DFRVP07PV3, J8AN2M19DD]
about: [J9XP7CS943]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $\mathcal{A}$ be a small [[abelian category|Y9CZ3MTNF1]], and let $\mathcal{B}$ be a [[Serre subcategory|CSD6W0JV0P]] of $\mathcal{A}$.
Let $\mathcal{A}/\mathcal{B}$ be the quotient abelian category, in which the objects of $\mathcal{B}$ become zero.
View each of these abelian categories as an exact category with all short exact sequences, and let $K_n$ denote Quillen K-groups, defined by the [[Q-construction|J9XP7CS943]].
Then the exact functors $\mathcal{B} \to \mathcal{A} \to \mathcal{A}/\mathcal{B}$ induce a homotopy fibration
$$BQ\mathcal{B} \to BQ\mathcal{A} \to BQ(\mathcal{A}/\mathcal{B}),$$
that is, $BQ\mathcal{B}$ is homotopy equivalent to the [[homotopy fiber|4F3KWXYXBA]] of the second map.
Hence there is a long [[exact sequence|JB7ZBFBA9C]]
$$\cdots \to K_n(\mathcal{B}) \to K_n(\mathcal{A}) \to K_n(\mathcal{A}/\mathcal{B}) \to K_{n-1}(\mathcal{B}) \to \cdots \to K_0(\mathcal{B}) \to K_0(\mathcal{A}) \to K_0(\mathcal{A}/\mathcal{B}) \to 0.$$

## Remarks

Quillen proved the theorem with his Theorem B, applied to the functor $Q\mathcal{A} \to Q(\mathcal{A}/\mathcal{B})$: he showed that its homotopy fibres are equivalent to $BQ\mathcal{B}$.

Example: let $R$ be a [[Dedekind domain|7NPY2CN5KB]] with fraction field $F$.
Take for $\mathcal{A}$ the finitely generated $R$-modules and for $\mathcal{B}$ the torsion ones; then $M \mapsto M \otimes_R F$ identifies $\mathcal{A}/\mathcal{B}$ with the finite-dimensional $F$-vector spaces.
Every finitely generated torsion module has a finite filtration with quotients $R/\mathfrak{m}$, so [[dévissage|DFRVP07PV3]] gives $K_n(\mathcal{B}) \cong \bigoplus_{\mathfrak{m}} K_n(R/\mathfrak{m})$, the sum over maximal ideals.
Since $R$ is regular, the [[resolution theorem|DYV91576BQ]] gives $K_n(\mathcal{A}) = K_n(R)$.
The result is the localization sequence
$$\cdots \to \bigoplus_{\mathfrak{m}} K_n(R/\mathfrak{m}) \to K_n(R) \to K_n(F) \to \bigoplus_{\mathfrak{m}} K_{n-1}(R/\mathfrak{m}) \to \cdots.$$

## Explanations

### L1 human

When some objects of an abelian category are declared to be zero, the K-theory changes in a controlled way.
The theorem says that the K-theory of the small category, of the big category, and of the quotient fit into one long exact sequence.
So knowing two of them tells a lot about the third.

### L2 human

The main use is in [[G-theory|YZSR4QKDQQ]]: for a Noetherian scheme $X$, a closed subscheme $Z$ and the open complement $U$, it gives the sequence $\cdots \to G_n(Z) \to G_n(X) \to G_n(U) \to G_{n-1}(Z) \to \cdots$.
Together with dévissage and the resolution theorem it computes K-groups of Dedekind domains from those of their fraction fields and residue fields.
It is also a key step in Quillen's proof of the fundamental theorem for polynomial and Laurent polynomial rings.
For K-theory of vector bundles instead of coherent sheaves, the right analogue is the [[Thomason–Trobaugh localization theorem|J8AN2M19DD]].

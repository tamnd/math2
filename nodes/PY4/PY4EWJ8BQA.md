---
tag: PY4EWJ8BQA
kind: statement
role: theorem
name: Dold–Kan correspondence
msc: [18G31, 18N50, 55U10]
uses: [WK0A32TZHB, WQ82C0M3QB, Y9CZ3MTNF1, K7A04ZBD92, S417YNEJ6M, 2J4JJJYP22, 4EBHAWJJ8C]
about: [WK0A32TZHB, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Dold–Kan_correspondence
same_as:
  wikidata: Q16962174
  wikipedia: Dold–Kan correspondence
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]].
Let $s\mathcal{A}$ be the category of [[simplicial objects|WK0A32TZHB]] in $\mathcal{A}$, and let $\mathrm{Ch}_{\ge 0}(\mathcal{A})$ be the category of [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$ concentrated in degrees $n \ge 0$.
For $A \in s\mathcal{A}$ with face maps $d_i \colon A_n \to A_{n-1}$, let the normalized chain complex $N(A)$ be
$$N(A)_n = \bigcap_{i=1}^{n} \ker\left(d_i \colon A_n \to A_{n-1}\right), \qquad \partial_n = d_0 \colon N(A)_n \to N(A)_{n-1},$$
with $N(A)_0 = A_0$, where $\ker$ denotes the [[kernel|S417YNEJ6M]].
Then $N \colon s\mathcal{A} \to \mathrm{Ch}_{\ge 0}(\mathcal{A})$ is an [[equivalence of categories|K7A04ZBD92]].

## Remarks

A quasi-inverse $\Gamma$ is given by
$$\Gamma(C)_n = \bigoplus_{[n] \twoheadrightarrow [k]} C_k.$$
The sum runs over all surjective order-preserving maps from $\set{0, \ldots, n}$ onto $\set{0, \ldots, k}$.
The face and degeneracy maps are defined from the simplicial identities and the differential of $C$.
To see that $N$ is an equivalence, one shows that every $A_n$ splits as the direct sum of the images of $N(A)_k$ under the iterated degeneracies, indexed by these surjections.

The equivalence carries more structure.
For a simplicial abelian group $A$, the homotopy groups $\pi_n(A)$ are the [[homology|2J4JJJYP22]] groups $H_n(N(A))$.
Simplicial homotopies correspond to [[chain homotopies|4EBHAWJJ8C]].
The normalized complex $N(A)$ is a direct summand of the unnormalized complex with differential $\sum_i (-1)^i d_i$, and the inclusion is a chain homotopy equivalence.

Example: for an abelian group $M$ and $n \ge 0$, the chain complex $M[n]$ with $M$ in degree $n$ and $0$ elsewhere corresponds to a simplicial abelian group $K(M, n) = \Gamma(M[n])$.
Its geometric realization is an Eilenberg–MacLane space for $M$ in degree $n$.

## Explanations

### L1 human

Simplicial abelian groups are combinatorial models of spaces that carry an addition.
Chain complexes are the basic objects of homological algebra.
The Dold–Kan correspondence says that the two are the same thing, once one discards the redundant degenerate simplices.
This lets one move freely between homotopy theory and homological algebra.

### L2 human

The correspondence turns homotopy groups of simplicial abelian groups into homology of chain complexes.
It is used to build Eilenberg–MacLane spaces, to define derived functors of non-additive functors, as Dold and Puppe did, and to compare simplicial and differential graded algebra.
The functors $N$ and $\Gamma$ are not monoidal equivalences; the Eilenberg–Zilber and Alexander–Whitney maps relate the tensor products only up to homotopy.
The statement extends to any idempotent complete additive category, and it has an $\infty$-categorical version for stable $\infty$-categories.

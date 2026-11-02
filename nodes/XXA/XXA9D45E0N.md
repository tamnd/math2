---
tag: XXA9D45E0N
kind: statement
role: theorem
name: Kontsevich formality theorem
msc: [53D55, 16S80, "16E40"]
uses: [JZEK70CH3G, S5H153HFWC, A2KQ49Y4NF, 3MKSJ1J04K]
about: [3MKSJ1J04K]
sources:
  - url: https://en.wikipedia.org/wiki/Kontsevich_quantization_formula
---

## Statement

Let $M = \R^d$.
Let $T_{\mathrm{poly}}$ be the differential graded Lie algebra of polyvector fields on $M$, with zero differential and the Schouten–Nijenhuis bracket.
Let $D_{\mathrm{poly}}$ be the differential graded Lie algebra of polydifferential operators on $M$, with the Hochschild differential and the Gerstenhaber bracket.
Both carry the grading in which $k$-vector fields, and polydifferential operators with $k$ arguments, have degree $k - 1$.

1. There is an $L_\infty$ quasi-isomorphism $T_{\mathrm{poly}} \to D_{\mathrm{poly}}$ whose first component is the Hochschild–Kostant–Rosenberg map.
2. As a consequence, every [[Poisson manifold|A2KQ49Y4NF]] structure on $M$ admits a [[star product|3MKSJ1J04K]].
Moreover, equivalence classes of star products on $M$ correspond bijectively to classes of formal Poisson structures $\hbar \pi_1 + \hbar^2 \pi_2 + \cdots$ under formal diffeomorphisms.

## Remarks

The Hochschild–Kostant–Rosenberg map identifies the cohomology of $D_{\mathrm{poly}}$ with $T_{\mathrm{poly}}$, but it does not respect the brackets; the theorem corrects it by higher terms.
Kontsevich built these terms from integrals over configuration spaces of points in the upper half-plane, indexed by graphs.
Star products correspond to Maurer–Cartan elements of $\hbar D_{\mathrm{poly}}[\![\hbar]\!]$, formal Poisson structures to those of $\hbar T_{\mathrm{poly}}[\![\hbar]\!]$, and an $L_\infty$ quasi-isomorphism matches their equivalence classes.
For a constant Poisson bivector on $\R^{2n}$, [[Kontsevich's quantization formula|JZEK70CH3G]] gives the Moyal product.
The result was later extended from $\R^d$ to all smooth manifolds.

## Explanations

### L1 human

The theorem says that every Poisson manifold, a space with a classical bracket of observables, can be quantized in the formal sense.
One can always find a noncommutative product of functions whose first correction is the given bracket.
It also says that the two kinds of data, Poisson structures and star products, are classified by the same thing.
Maxim Kontsevich proved it with an explicit formula built from graphs.

### L2 human

Deformation theory says that deformations of an algebraic structure are governed by a differential graded Lie algebra through its Maurer–Cartan equation.
For the algebra of functions on $M$, this algebra is $D_{\mathrm{poly}}$, whose cohomology is $T_{\mathrm{poly}}$ by the Hochschild–Kostant–Rosenberg theorem.
Formality means that $D_{\mathrm{poly}}$ is equivalent, as an $L_\infty$ algebra, to its cohomology with the induced bracket.
Equivalent $L_\infty$ algebras have the same deformation theory, which gives the classification of star products.
The same circle of ideas links to the Gerstenhaber structure on Hochschild cohomology and to the Deligne conjecture.

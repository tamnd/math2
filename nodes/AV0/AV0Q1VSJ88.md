---
tag: AV0Q1VSJ88
kind: statement
role: theorem
name: Atiyah–Bott theorem on Yang–Mills over Riemann surfaces
msc: ["58E15", 53C07, 14H60]
uses: [CKGDR9P9PA, JJWETW5AT8, 5K0N8QMV6Q, 8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, TKA958Z4KZ, RQRJ5H4Y3E, C7MZ3SFGYF, 707DEWCCFX, FJZRW9P0K3]
about: [CKGDR9P9PA, JJWETW5AT8]
sources:
  - url: https://en.wikipedia.org/wiki/Yang–Mills_equations
---

## Statement

Let $M$ be a closed [[Riemann surface|5K0N8QMV6Q]] of genus $g$ with a compatible Riemannian metric and area form $\omega$.
Let $P \to M$ be a [[principal $U(n)$-bundle|8E37E74XVP]] of degree $d$, let $\mathcal{A}$ be the space of [[connections|NJ21PN5ZGJ]] on $P$, and let $\mathcal{G}$ be its [[gauge group|707DEWCCFX]].
Each $A \in \mathcal{A}$ defines a [[holomorphic structure|TKA958Z4KZ]] $E_A$ on the associated vector bundle $E$ of rank $n$.

1. A connection $A$ satisfies the [[Yang–Mills equations|JJWETW5AT8]] if and only if $E$ splits in the following way.
There is an orthogonal direct sum $E = E_1 \oplus \cdots \oplus E_r$ of subbundles preserved by $A$.
On each $E_j$ the [[curvature|ZAJFW1S078]] of $A$ equals $c_j \, \mathrm{id}_{E_j} \otimes \omega$ for a constant $c_j$.
2. The stratification of $\mathcal{A}$ by the Harder–Narasimhan type of $E_A$ is $\mathcal{G}$-equivariantly perfect for rational coefficients.
So the [[Yang–Mills functional|CKGDR9P9PA]] behaves on $\mathcal{A}$ like an equivariantly perfect Morse function.
3. Let $n$ and $d$ be coprime.
The [[moduli space|FJZRW9P0K3]] of [[stable bundles|RQRJ5H4Y3E]] of rank $n$ and degree $d$ on $M$ has integral cohomology without torsion.
Its Poincaré polynomial is determined by an explicit recursion over Harder–Narasimhan types.

## Remarks

On a surface, the Yang–Mills equation $d_A^* F_A = 0$ says that the function $\star F_A$, a section of the adjoint bundle, is covariantly constant.
Its eigenvalues are therefore constant and its eigenspaces give the parallel splitting of part 1.
By the Narasimhan–Seshadri theorem, the connections of constant central curvature correspond to polystable holomorphic bundles, so the critical sets are described by stable bundles of lower rank.

For part 2 one compares the [[equivariant cohomology|C7MZ3SFGYF]] of $\mathcal{A}$, which is the cohomology of the classifying space of $\mathcal{G}$ because $\mathcal{A}$ is contractible, with that of the strata.
Perfection means that the Thom–Gysin sequences of the strata split into short exact sequences.
The open stratum consists of the semistable bundles, and in the coprime case the gauge group acts on it with constant stabiliser $U(1)$, which gives part 3.

## Explanations

### L1 human

Atiyah and Bott treated the Yang–Mills functional over a surface as a height function on an infinite-dimensional space.
Its critical points can be listed completely, and they correspond to bundles that split into pieces of constant curvature.
The way the space breaks into pieces flowing to each critical point is as efficient as possible.
This lets one compute the topology of the space of stable vector bundles on a curve.

### L2 human

The work links gauge theory on surfaces with algebraic geometry of vector bundles on curves through the Narasimhan–Seshadri theorem.
It is a model of infinite-dimensional Morse theory with a symmetry group, carried out through equivariant cohomology.
The Harder–Narasimhan stratification it uses also appears in moment map geometry, where the curvature plays the role of a moment map for the gauge group.

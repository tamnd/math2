---
tag: M1C142YAPZ
kind: statement
role: theorem
name: Dilogarithm and K3
msc: ["19F27", "11G55", "11R42"]
uses: [EC11MFYFYM, Q8K5MWEXB9, 5GVFZWMWC8, MWBDFS2KJ5, KXS5DQDFYD, E0VZTNPJXA]
about: [EC11MFYFYM, Q8K5MWEXB9, KXS5DQDFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch_group
---

## Statement

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] with $r_1$ real embeddings, $r_2$ pairs of complex conjugate non-real embeddings and discriminant $d_F$.
Choose embeddings $\sigma_1, \ldots, \sigma_{r_2} \colon F \to \C$, one from each complex pair.
Let $\mathcal{B}(F)$ be the [[Bloch group|EC11MFYFYM]] of $F$, and let $D$ be the [[Bloch–Wigner function|Q8K5MWEXB9]], extended additively to the symbols $[x]$.
Then:

1. $\mathcal{B}(F) \otimes \Q \cong K_3(F) \otimes \Q$, and both have dimension $r_2$.
2. The map $\mathcal{B}(F) \to \R^{r_2}$, $\xi \mapsto (D(\sigma_1(\xi)), \ldots, D(\sigma_{r_2}(\xi)))$, has torsion kernel and its image is a lattice of rank $r_2$.
3. If $\xi_1, \ldots, \xi_{r_2}$ in $\mathcal{B}(F)$ are linearly independent modulo torsion, then
$$\zeta_F(2) = q \, \frac{\pi^{2(r_1 + r_2)}}{\sqrt{\abs{d_F}}} \det\big(D(\sigma_j(\xi_i))\big)_{1 \le i, j \le r_2}$$
for some nonzero rational number $q$, where $\zeta_F$ is the [[Dedekind zeta function|KXS5DQDFYD]].

## Remarks

Part 1 is due to Suslin, who related $\mathcal{B}(F)$ to the indecomposable part of $K_3(F)$ for every infinite field $F$; for a number field the decomposable part is torsion.
Part 2 holds because $D$ composed with this identification is the [[Borel regulator|D22EZ3CNAF]] on $K_3$, up to a nonzero factor, and Borel's theorem says that its image is a lattice.
Part 3 is Zagier's theorem, which follows from Borel's theorem relating the covolume of this lattice to $\zeta_F(2)$.
Geometrically, $D(z)$ is the hyperbolic volume of an ideal tetrahedron with cross-ratio $z$, and the Borel class in degree $3$ is the volume class of hyperbolic space.

Example: for $F = \Q(\sqrt{-3})$, $r_1 = 0$, $r_2 = 1$ and $d_F = -3$.
Let $z = e^{i\pi/3}$, a root of unity in $F$; then $1 - z = z^{-1}$, so $\delta([z]) = z \wedge z^{-1} = 0$ and $[z]$ lies in $\mathcal{B}(F)$.
Here $\zeta_F(2) = \frac{2\pi^2}{9\sqrt{3}} D(z)$, with $D(z) \approx 1.0149$.

## Explanations

### L1 human

The dilogarithm is a special function, and the third K-group of a number field is an abstract algebraic invariant.
This theorem says that they meet: the Bloch–Wigner dilogarithm, evaluated on elements of the Bloch group, measures $K_3$ of the field.
As a consequence the value of the Dedekind zeta function at $2$ is a determinant of dilogarithm values, up to simple factors.

### L2 human

The result is the first nontrivial case of Borel's regulator theorem made explicit with classical functions.
It also links number theory with hyperbolic geometry, because $D$ computes volumes of hyperbolic tetrahedra, and hyperbolic $3$-manifolds give elements of Bloch groups.
Zagier's conjecture on polylogarithms predicts the analogous statement for $\zeta_F(m)$ with $m \ge 3$ and higher polylogarithms.

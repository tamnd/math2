---
tag: V8D4T4Z8NR
kind: definition
name: Reidemeister torsion
msc: ["57Q10", 19J10]
defines: MEPXWR00K7
uses: [5W95QFHXPR, S1XK3HXHFX, Y1YPE6PM52, 4NMTSX0XDS, WQ82C0M3QB, 04C5ZBG1WT, 0VTH8KPCG2, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_torsion
---

## Definition

Let $X$ be a finite connected [[CW complex|5W95QFHXPR]] with [[fundamental group|S1XK3HXHFX]] $\pi$ and [[universal cover|Y1YPE6PM52]] $\tilde X$.
Let $F$ be a [[field|04C5ZBG1WT]] and let $\rho \colon \Z[\pi] \to F$ be a [[ring homomorphism|0VTH8KPCG2]] from the [[group ring|4NMTSX0XDS]].
The twisted [[chain complex|WQ82C0M3QB]] is $C_*(X; \rho) = F \otimes_{\Z[\pi]} C_*(\tilde X)$, a complex of finite-dimensional $F$-vector spaces with a basis given by lifts of the cells of $X$.
Assume $C_*(X; \rho)$ is acyclic, and choose maps $\delta \colon C_i \to C_{i+1}$ with $d \delta + \delta d = \mathrm{id}$.
The *Reidemeister torsion* of $(X, \rho)$ is
$$\Delta_\rho(X) = \det\Bigl(d + \delta \colon \bigoplus_i C_{2i+1}(X; \rho) \to \bigoplus_i C_{2i}(X; \rho)\Bigr) \in F^\times / \set{\pm \rho(g) : g \in \pi},$$
the [[determinant|00KDZRW4C0]] taken in the given bases.

## Remarks

The class does not depend on the choice of $\delta$, and a change of the lifts or orientations of cells multiplies it by some $\pm \rho(g)$.
It is invariant under subdivision and under simple homotopy equivalence.
Example: for the circle with one $0$-cell and one $1$-cell, and $\rho(t) = \lambda \ne 1$ for a generator $t$ of $\pi = \Z$, the complex is $F \xrightarrow{\lambda - 1} F$, so $\Delta_\rho(S^1) = (\lambda - 1)^{\pm 1}$, depending on the convention.
Non-example: for $\rho(t) = 1$, the twisted complex of the circle is $F \xrightarrow{0} F$, which is not acyclic, so the torsion is not defined.
Conventions differ: some authors take the inverse, and some use representations $\pi \to GL_n(F)$ instead of ring homomorphisms to $F$.
Reidemeister torsion is the key invariant in the classification of lens spaces: $L(p, q)$ and $L(p, q')$ are homeomorphic if and only if $q' \equiv \pm q^{\pm 1} \pmod p$.

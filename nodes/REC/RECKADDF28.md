---
tag: RECKADDF28
kind: definition
name: Whitehead torsion
msc: [19J10, "57Q10"]
defines: 4QMDFYEK3T
uses: [5W95QFHXPR, XZG6MTSWCN, S1XK3HXHFX, Y1YPE6PM52, EQVVDS0ZQT, WQ82C0M3QB, 4NMTSX0XDS, SXVNJY4XFY, 8SY3AC4KW3]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead_torsion
---

## Definition

Let $R$ be a ring and let $C_*$ be a [[chain complex|WQ82C0M3QB]] of $R$-modules with only finitely many nonzero terms.
Each term is a finitely generated free module with a chosen basis.
Assume $C_*$ is acyclic, and choose a chain contraction $\delta$, that is, maps $\delta \colon C_i \to C_{i+1}$ with $d \delta + \delta d = \mathrm{id}$.
The map $d + \delta \colon \bigoplus_i C_{2i+1} \to \bigoplus_i C_{2i}$ is an isomorphism, and the *torsion* $\tau(C_*)$ is the class of its matrix in $\tilde K_1(R) = K_1(R)/\set{\pm 1}$, using [[K1 of a ring|SXVNJY4XFY]].

Now let $f \colon K \to L$ be a cellular [[homotopy equivalence|XZG6MTSWCN]] of finite connected [[CW complexes|5W95QFHXPR]].
Let $\pi$ be the [[fundamental group|S1XK3HXHFX]] of $L$, and let $M_f$ be the [[mapping cylinder|EQVVDS0ZQT]] of $f$.
Pass to [[universal covers|Y1YPE6PM52]].
The relative cellular complex $C_*(\tilde M_f, \tilde K)$ is an acyclic complex of finitely generated free modules over the [[group ring|4NMTSX0XDS]] $\Z[\pi]$.
It has a basis given by lifts of the cells of $M_f$ not in $K$.
The *Whitehead torsion* $\tau(f)$ is the image of $\tau(C_*(\tilde M_f, \tilde K))$ in the [[Whitehead group|8SY3AC4KW3]] $\mathrm{Wh}(\pi)$.

## Remarks

Changing the lifts of cells or their orientations multiplies basis elements by $\pm g$ with $g \in \pi$.
This is why the class is taken in $\mathrm{Wh}(\pi)$; the class does not depend on the chain contraction.
Example: the identity map of a finite CW complex has a mapping cylinder that collapses onto $K$, and its torsion is $0$.
Non-example: a homotopy equivalence between the lens spaces $L(7,1)$ and $L(7,2)$ exists, but its torsion is nonzero, so it is not a simple homotopy equivalence.
Whitehead's theorem says $\tau(f) = 0$ if and only if $f$ is a simple homotopy equivalence.
Sign and inversion conventions differ between authors.

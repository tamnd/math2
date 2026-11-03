---
tag: NABBCET5WH
kind: example
name: Spherical harmonics as representations of SO(3)
msc: ["43A85", "33C55", "22E70"]
illustrates: [5NVQWPD35X, W38ZDXDVYC]
uses: [263GGJFA21, P9CM4GQ2T0, 3F32Y21HP4, MVYFSYMECG, 0E0B6RA8K0, QFYGJVA996, FX3NEFYFFN, BKZNC76RC8]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_harmonics
---

## Example

Let $G = \mathrm{SO}(3)$ ([[rotation group|263GGJFA21]]) act on the unit [[sphere|P9CM4GQ2T0]] $S^2 \subset \R^3$, and let $\sigma$ be the rotation-invariant surface measure.
The stabilizer of the north pole $e_3$ is the subgroup $K \cong \mathrm{SO}(2)$ of rotations about the $z$-axis, so $S^2 = G / K$.
The group acts unitarily on $L^2(S^2, \sigma)$ by $(g f)(x) = f(g^{-1} x)$.

For $\ell \ge 0$, let $\mathcal{H}_\ell$ be the space of restrictions to $S^2$ of [[harmonic polynomials|MVYFSYMECG]] on $\R^3$ that are homogeneous of degree $\ell$.
Its elements are the [[spherical harmonics|3F32Y21HP4]] of degree $\ell$.
Then:

1. $\dim \mathcal{H}_\ell = 2\ell + 1$, and $\mathcal{H}_\ell$ is invariant under $G$.
2. Each $\mathcal{H}_\ell$ is an [[irreducible|FX3NEFYFFN]] representation of $G$, and the $\mathcal{H}_\ell$ are pairwise non-isomorphic. Every irreducible continuous representation of $\mathrm{SO}(3)$ is isomorphic to one of them.
3. $L^2(S^2) = \widehat{\bigoplus}_{\ell \ge 0} \mathcal{H}_\ell$, an orthogonal Hilbert direct sum.
4. The spherical [[Laplacian|0E0B6RA8K0]] acts on $\mathcal{H}_\ell$ as multiplication by $-\ell(\ell + 1)$.

A check of the multiplicity one in 3: the functions in $\mathcal{H}_\ell$ fixed by $K$ form a line.
This line is spanned by the zonal harmonic $x \mapsto P_\ell(x_3)$, where $P_\ell$ is the [[Legendre polynomial|QFYGJVA996]].
For example, for $\ell = 1$ the space $\mathcal{H}_1$ is spanned by $x_1, x_2, x_3$, and it is the standard representation of $\mathrm{SO}(3)$ on $\C^3$.
Its $K$-fixed line is spanned by $x_3 = P_1(x_3)$.
The [[spherical functions|BKZNC76RC8]] of the pair $(\mathrm{SO}(3), \mathrm{SO}(2))$ are $g \mapsto P_\ell(\ip{g e_3}{e_3})$, one for each $\ell$.

## Explanations

### L1 human

Functions on the sphere can be expanded in spherical harmonics, much as functions on a circle are expanded in sines and cosines.
Rotating a spherical harmonic of degree $\ell$ gives another spherical harmonic of the same degree, so each degree forms a representation of the rotation group.
These representations have dimensions $1, 3, 5, \dots$ and are exactly the irreducible representations of $\mathrm{SO}(3)$, each appearing once.
This is the mathematics behind the shapes of atomic orbitals.

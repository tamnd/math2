---
tag: AMF7G7X0CR
kind: definition
name: Birefringence
msc: [78A10, 78A40]
defines: 8CWCYQJ44T
uses: [F768YN0P2V, 9VGK0SP6EQ, PJ8ZSJ0QDW, NRF1ESCGMR, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Birefringence
---

## Definition

Let a linear, non-magnetic, transparent medium have a relative [[permittivity|F768YN0P2V]] tensor $\varepsilon$, a real symmetric positive definite $3 \times 3$ matrix.
Let $\varepsilon_1, \varepsilon_2, \varepsilon_3$ be its eigenvalues, and let $n_j = \sqrt{\varepsilon_j}$ be the *principal refractive indices*.
The medium is *birefringent* when $\varepsilon$ is not a multiple of the identity, that is, when the $n_j$ are not all equal.
It is *uniaxial* when exactly two of the $n_j$ are equal, and *biaxial* when all three are distinct.

## Remarks

In a birefringent medium, for each direction of propagation there are two [[plane-wave|NM024G378A]] modes with orthogonal directions of $\mathbf{D}$ and, in general, different [[refractive indices|9VGK0SP6EQ]].
The [[index ellipsoid|NRF1ESCGMR]] gives both indices and both polarizations.
In a uniaxial medium with $\varepsilon = \mathrm{diag}(n_o^2, n_o^2, n_e^2)$, the $z$-axis is the *optic axis*, $n_o$ is the ordinary index and $n_e$ the extraordinary index, and $\Delta n = n_e - n_o$ is the birefringence.

Example: take $\varepsilon = \mathrm{diag}(n_o^2, n_o^2, n_e^2)$ with $n_o \ne n_e$ and light travelling along the $x$-axis.
Light polarized along $y$ sees the index $n_o$, and light polarized along $z$ sees $n_e$.
For light travelling along the optic axis $z$, both polarizations see $n_o$, so there is no splitting in that one direction.

Non-example: ordinary glass has $\varepsilon = n^2 I$, a multiple of the identity, so it is not birefringent.

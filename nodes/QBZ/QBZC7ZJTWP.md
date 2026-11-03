---
tag: QBZC7ZJTWP
kind: definition
name: Moment tensor
msc: [86A15, 74J05, 86A22]
defines: ZNN5WAT301
uses: [88YRH7XQDX, 0VR671PHE5, SH6JY9RN2E, 9636MFFSGC, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Focal_mechanism
---

## Definition

Let an elastic medium have elastodynamic [[Green's function|SH6JY9RN2E]] $G_{np}(x, t; \xi, \tau)$.
It is the $n$-th component of displacement at $(x, t)$ due to a unit impulsive force in direction $p$ at $(\xi, \tau)$.
A point source at $\xi$ has *moment tensor* $M_{pq}(t)$, a real [[symmetric|0VR671PHE5]] $3 \times 3$ matrix for each time $t$, if the displacement it produces is
$$u_n(x, t) = \sum_{p,q} \int M_{pq}(\tau)\, \frac{\partial G_{np}}{\partial \xi_q}(x, t; \xi, \tau)\, d\tau.$$
The entry $M_{pq}$ is the strength of a couple of forces in direction $p$ separated in direction $q$.

## Remarks

Symmetry, $M_{pq} = M_{qp}$, says the source exerts no net [[torque|9636MFFSGC]]; an internal source cannot change the angular momentum of the body.
Example: slip in the unit direction $d$ on a small fault with unit normal $n \perp d$ and [[seismic moment|88YRH7XQDX]] $M_0$ has $M = M_0 (n d^T + d n^T)$.
This is symmetric, and its [[trace|07PTPSZPME]] is $2 M_0\, n \cdot d = 0$, so the source causes no volume change.
An explosion has $M = M_0 I$, with trace $3M_0 \ne 0$.
Non-example: a single couple, $M = M_0\, e_1 e_2^T$, is not symmetric, so it is not a moment tensor; it would exert a net torque.
Every moment tensor splits as an isotropic part $\frac13 (\tr M) I$ plus a deviatoric part of trace zero.

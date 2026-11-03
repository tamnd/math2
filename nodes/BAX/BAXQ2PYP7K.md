---
tag: BAXQ2PYP7K
kind: definition
name: ADM formalism
msc: ["83C05", "70H45", "83C45"]
defines: CFAFAPV7HB
uses: [D1SYF8F8RQ, SA5ZDFBHNZ, GP0SM9D9X0, A9514690T3, SB7BVCZJ3F]
sources:
  - url: https://en.wikipedia.org/wiki/ADM_formalism
---

## Definition

Let $(M, g)$ be a 4-dimensional [[Lorentzian manifold|D1SYF8F8RQ]] of signature $(-,+,+,+)$, with $M = \R \times \Sigma$ and each slice $\Sigma_t = \set{t} \times \Sigma$ spacelike.
In local coordinates $(t, x^1, x^2, x^3)$ the metric can be written uniquely as
$$g = -N^2 \, dt^2 + h_{ij} \, (dx^i + N^i dt)(dx^j + N^j dt).$$
Here $N > 0$ is the *lapse*, $N^i$ is the *shift* and $h_{ij}$ is the metric induced on $\Sigma_t$.
Let $D$ be the Levi-Civita connection of $h$, and let
$$K_{ij} = \frac{1}{2N} \bigl( \partial_t h_{ij} - D_i N_j - D_j N_i \bigr)$$
be the [[second fundamental form|A9514690T3]] of $\Sigma_t$, with $K = h^{ij} K_{ij}$.
In units with $16 \pi G = 1$, the *ADM momentum* is $\pi^{ij} = \sqrt{h} \, (K^{ij} - K h^{ij})$, where $h = \det(h_{ij})$.
The *ADM formalism* is the Hamiltonian description of general relativity in the variables $(h_{ij}, \pi^{ij})$, with Lagrangian density
$$\mathcal{L} = \pi^{ij} \partial_t h_{ij} - N \mathcal{H} - N_i \mathcal{H}^i,$$
$$\mathcal{H} = \frac{1}{\sqrt{h}} \Bigl( \pi^{ij} \pi_{ij} - \tfrac12 \pi^2 \Bigr) - \sqrt{h} \, R(h), \qquad \mathcal{H}^i = -2 D_j \pi^{ij}.$$
Here $\pi = h_{ij} \pi^{ij}$ and $R(h)$ is the scalar curvature of $h$.

## Remarks

The density $\mathcal{L}$ equals the [[Einstein–Hilbert action|SA5ZDFBHNZ]] density $\sqrt{-g} \, R(g)$ up to a total derivative, since $\sqrt{-g} = N \sqrt{h}$.
The lapse and shift appear without time derivatives, so they act as Lagrange multipliers.
Varying them gives the constraints $\mathcal{H} = 0$ and $\mathcal{H}^i = 0$, the constraint equations of the [[initial value formulation|SB7BVCZJ3F]].
Varying $h_{ij}$ and $\pi^{ij}$ gives [[Hamilton's equations|GP0SM9D9X0]], which are the remaining six Einstein equations.
Example: for Minkowski space in inertial coordinates, $N = 1$, $N^i = 0$, $h_{ij} = \delta_{ij}$, so $K_{ij} = 0$ and $\pi^{ij} = 0$.
Non-example: a slicing by null hypersurfaces, such as $t - x^3 = \text{const}$ in Minkowski space, has no such decomposition, since the induced metric is degenerate.

## Explanations

### L1 human

The ADM formalism writes Einstein's theory as the evolution of the geometry of space, step by step in time, in the language of Hamiltonian mechanics.

---
tag: 1CCFRPM31P
kind: definition
name: Hořava–Lifshitz gravity
msc: [83D05, 83C45]
defines: KWB5PVKW6B
uses: [CFAFAPV7HB, 384JFR3K6X, 98HTB7MSPX]
sources:
  - url: https://en.wikipedia.org/wiki/Hořava–Lifshitz_gravity
---

## Definition

Let $M = \R \times \Sigma$ be a four-dimensional manifold with a fixed [[foliation|98HTB7MSPX]] by the slices $\set{t} \times \Sigma$, where $\Sigma$ is a three-manifold.
The fields are, as in the [[ADM formalism|CFAFAPV7HB]], a lapse function $N$, a shift vector $N^i$ and a Riemannian metric $g_{ij}$ on each slice.
The symmetry group is the group of foliation-preserving diffeomorphisms $t \mapsto t'(t)$, $x^i \mapsto x'^i(t, x)$.
*Hořava–Lifshitz gravity* is the theory with the action
$$S = \frac{2}{\kappa^2} \int dt \, d^3x \, \sqrt{g} \, N \left( K_{ij} K^{ij} - \lambda K^2 \right) - \int dt \, d^3x \, \sqrt{g} \, N \, V[g_{ij}],$$
where:

1. $K_{ij} = \frac{1}{2N} \left( \dot g_{ij} - \nabla_i N_j - \nabla_j N_i \right)$ is the extrinsic curvature of the slice and $K = g^{ij} K_{ij}$;
2. $\kappa$ and $\lambda$ are real coupling constants;
3. the potential $V[g_{ij}]$ is a scalar built from the spatial metric, its curvature and their spatial covariant derivatives, with up to six derivatives.

At short distances the theory is required to be invariant under the anisotropic scaling $t \mapsto b^3 t$, $x^i \mapsto b x^i$, that is, it has dynamical critical exponent $z = 3$.

## Remarks

Example: take $\lambda = 1$ and $V = -\frac{2}{\kappa^2} (R - 2\Lambda)$, where $R$ is the scalar curvature of $g_{ij}$ and $\Lambda$ a constant.
Then $S$ is $\frac{2}{\kappa^2}$ times the ADM form of the Einstein–Hilbert action with cosmological constant, so general relativity sits inside this family at long distances.
Non-example: the Einstein–Hilbert action alone has only terms with two derivatives, so it does not have the $z = 3$ scaling required at short distances.
Hořava's original proposal also imposed a "detailed balance" condition on $V$, and the "projectable" version requires $N$ to depend on $t$ only.

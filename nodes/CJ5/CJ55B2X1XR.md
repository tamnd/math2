---
tag: CJ55B2X1XR
kind: definition
name: Causal dynamical triangulation
msc: [83C45, 83C27]
defines: 2Y9VNGWFTS
uses: [D1SK2X66FE, 1NYTFT5NPE, G686S8SEK0, V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_dynamical_triangulation
---

## Definition

Fix a spatial topology $\Sigma$ (for example the three-sphere), a number $t$ of time steps, a lattice spacing $a > 0$ and a constant $\alpha > 0$.
A *causal triangulation* is a [[simplicial complex|V8GZ0W1ZZ5]] $T$ homeomorphic to $\Sigma \times [0, t]$ (or $\Sigma \times S^1$) with the following properties.

1. Its vertices lie on slices labelled $0, 1, \dots, t$, and each slice is a triangulation of $\Sigma$.
2. Every simplex has its vertices on one slice or on two adjacent slices.
3. Every spacelike edge, joining two vertices of one slice, has squared length $a^2$, and every timelike edge, joining adjacent slices, has squared length $-\alpha a^2$.

*Causal dynamical triangulation* defines the gravitational [[path integral|1NYTFT5NPE]] as
$$Z = \sum_{T} \frac{1}{C_T} e^{i S_R(T)},$$
where the sum runs over causal triangulations $T$.
Here $S_R$ is the Lorentzian [[Regge action|D1SK2X66FE]] with cosmological term and $C_T$ is the order of the automorphism group of $T$.
After the [[Wick rotation|G686S8SEK0]] $\alpha \mapsto -\alpha$ each term becomes a real weight $e^{-S_E(T)}$.
The continuum limit $a \to 0$ is then studied.

## Remarks

All simplices have the same few shapes, so the Regge action of $T$ depends only on the numbers of simplices of each type.
So $Z$ becomes a statistical sum that can be evaluated by Monte Carlo methods.
Example: in $1 + 1$ dimensions, the triangles lie in strips between adjacent circles, each with one edge on a circle and two timelike edges.
This model can be solved exactly, and it gives a two-dimensional quantum gravity different from Liouville gravity.
Non-example: a triangulation of $S^4$ with all edges of length $a$, as in Euclidean dynamical triangulations, is not a causal triangulation.
It has no foliation into slices, so it fails clause 1.
Simulations in four dimensions find a phase with a large-scale four-dimensional geometry close to a de Sitter universe, and a spectral dimension near $2$ at short distances.

---
tag: AZF9TXV5C0
kind: statement
role: theorem
name: Ebin's slice theorem
msc: [58D17, 58D19, 58D05]
uses: [F45VQ47GPV, Q61VFHCH2J, WTCNKST134, 0RGGF8ZS6D, 02HPP5VCZH, BW12J14X0Z]
about: [Q61VFHCH2J, WTCNKST134]
sources:
  - url: https://en.wikipedia.org/wiki/Slice_theorem_(differential_geometry)
---

## Statement

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary.
Let $\mathcal{M}$ be the space of smooth [[Riemannian metrics|Q61VFHCH2J]] on $M$, an open subset of the Fréchet space of smooth symmetric $2$-tensors.
Let $\mathcal{D}$ be the [[diffeomorphism group|WTCNKST134]] of $M$, acting on $\mathcal{M}$ on the right by pullback, $(\gamma, \eta) \mapsto \eta^* \gamma$.
For $\gamma \in \mathcal{M}$, let $I_\gamma \subseteq \mathcal{D}$ be its [[isometry|02HPP5VCZH]] group, which is the [[stabiliser|0RGGF8ZS6D]] of $\gamma$.
Then there is a submanifold $S_\gamma$ of $\mathcal{M}$ containing $\gamma$, the *slice* at $\gamma$, such that:

1. If $\eta \in I_\gamma$, then $\eta^* S_\gamma = S_\gamma$.
2. If $\eta \in \mathcal{D}$ and $\eta^* S_\gamma \cap S_\gamma \neq \emptyset$, then $\eta \in I_\gamma$.
3. There are a neighbourhood $U$ of the identity coset in $\mathcal{D} / I_\gamma$ and a local section $\chi \colon U \to \mathcal{D}$ of the projection $\mathcal{D} \to \mathcal{D} / I_\gamma$.
For these, the map $U \times S_\gamma \to \mathcal{M}$, $(u, s) \mapsto \chi(u)^* s$, is a homeomorphism onto a neighbourhood of $\gamma$.


## Remarks

The theorem is due to Ebin.
The tangent space to the orbit of $\gamma$ consists of the Lie derivatives $L_X \gamma$ of $\gamma$ along vector fields $X$.
Its $L^2$-orthogonal complement is the space of symmetric $2$-tensors $h$ with $\delta_\gamma h = 0$, where $\delta_\gamma$ is the divergence.
The slice is the image of a small ball in this complement under the exponential map of an $I_\gamma$-invariant metric on $\mathcal{M}$.
The analysis is carried out on Sobolev completions of $\mathcal{M}$ and $\mathcal{D}$, which are Hilbert manifolds, and then passed to the smooth case.
Compactness of $I_\gamma$, which is a compact Lie group because $M$ is compact, is used to average and to make the slice invariant.
It is the infinite-dimensional analogue of the [[slice theorem|VQB2N60ARE]] for actions of compact Lie groups on finite-dimensional manifolds.

Example: suppose that $\gamma$ has trivial isometry group.
Then near $\gamma$ the action is free, and a neighbourhood of the class of $\gamma$ in $\mathcal{M} / \mathcal{D}$ is homeomorphic to the slice $S_\gamma$.

## Explanations

### L1 human

Two Riemannian metrics that differ by a change of coordinates describe the same geometry.
So the space of geometries on $M$ is the space of metrics divided by the action of diffeomorphisms.
Ebin's theorem says that near any metric this division can be done cleanly.
There is a transversal family of metrics, the slice, that meets each nearby orbit in an orbit of the finite-dimensional isometry group.

### L2 human

The slice theorem is the basic tool for describing the moduli space of Riemannian metrics, sometimes called superspace in general relativity.
It shows that this space splits into pieces according to the isometry group of the metric.
Near a metric whose only isometry is the identity, the space is locally modelled on the slice.
The same pattern reappears for connections modulo gauge: an infinite-dimensional group acts with a slice built from an elliptic gauge condition.
There the Coulomb gauge plays the role of the divergence-free condition.


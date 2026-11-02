---
tag: A5TDM8F4KB
kind: definition
name: Dirac operator on a spin manifold
msc: [53C27, 58J60, 15A66]
defines: QMRAVX14BJ
uses: [7CBT4SM83Y, RSPZ9TCFQ8, PYYQQKAZ0C, A38B1QFK20, CAZYGE1T4E, 3DXGJTEQZH, MT9P2X85V8]
sources:
  - url: https://en.wikipedia.org/wiki/Spinor_bundle
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$ with a [[spin structure|RSPZ9TCFQ8]].
Let $S \to M$ be the complex [[spinor bundle|PYYQQKAZ0C]], with its Clifford multiplication $T M \otimes S \to S$, $v \otimes \psi \mapsto v \cdot \psi$, which satisfies $v \cdot v \cdot \psi = -g(v, v) \, \psi$, as in the [[Clifford algebra|A38B1QFK20]].
Let $\nabla^S$ be the spin connection on $S$, the connection induced by the [[Levi-Civita connection|CAZYGE1T4E]].
The *Dirac operator* of $M$ is the operator $D \colon \Gamma(S) \to \Gamma(S)$ given by
$$D \psi = \sum_{i=1}^{n} e_i \cdot \nabla^S_{e_i} \psi,$$
where $e_1, \ldots, e_n$ is any local orthonormal frame of $TM$.

## Remarks

The right side does not depend on the frame, because it is the contraction of $\nabla^S \psi \in \Gamma(T^*M \otimes S)$ with Clifford multiplication, after identifying $T^*M$ with $TM$ by the metric.
The principal symbol of $D$ at $\xi$ is Clifford multiplication by the vector dual to $\xi$, up to a factor $i$ in some conventions, and its square is $-\abs{\xi}^2$.
So $D$ is an [[elliptic operator|MT9P2X85V8]] and a [[Dirac operator|3DXGJTEQZH]] in the general sense.
It is formally self-adjoint for the Hermitian metric on $S$.
In even dimension $S = S^+ \oplus S^-$, and $D$ maps $\Gamma(S^\pm)$ to $\Gamma(S^\mp)$.

Example: on $\R^n$ with the flat metric and the trivial spin structure, $S = \R^n \times \C^N$, the spin connection is the ordinary derivative, and $D = \sum_j \gamma_j \partial_j$, where $\gamma_j$ are complex $N \times N$ matrices with $\gamma_j \gamma_k + \gamma_k \gamma_j = -2 \delta_{jk} I$.
For $n = 1$ one can take $N = 1$ and $\gamma_1 = i$, which gives $D = i \, d/dx$ and $D^2 = -d^2/dx^2$.

Non-example: the complex projective plane $\C P^2$ with the Fubini–Study metric has no spin structure, since its second Stiefel–Whitney class is nonzero.
So it has no spinor bundle, and the definition does not apply; one uses a spin$^c$ structure instead.

## Explanations

### L1 human

The Dirac operator of a spin manifold differentiates a spinor field in each direction of an orthonormal frame and multiplies by the matching Clifford element, then sums.

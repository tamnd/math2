---
tag: 6VC9QE39XH
kind: statement
role: theorem
name: Peter–Weyl theorem
msc: [22C05, 43A77, 22D10]
uses: [EVHCE5VR6Y, VY0HXD3GC4, 74BPYJNZTM, FX3NEFYFFN, HM2HHE3J51]
about: [EVHCE5VR6Y, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Peter%E2%80%93Weyl_theorem
same_as:
  wikidata: Q1529941
  wikipedia: Peter–Weyl theorem
---

## Statement

Let $G$ be a [[compact group|EVHCE5VR6Y]] with normalised [[Haar measure|VY0HXD3GC4]].
Let $\widehat{G}$ be a set of representatives of the isomorphism classes of continuous [[irreducible|FX3NEFYFFN]] [[unitary representations|74BPYJNZTM]] of $G$.
Each $\pi \in \widehat{G}$ is finite-dimensional; let $d_\pi$ be its dimension, and let $\pi_{ij}(g)$ be its matrix entries in an orthonormal basis.
A matrix coefficient of $\pi$ is a function $g \mapsto \ip{\pi(g)u}{v}$ for vectors $u, v$ of its space.

1. The matrix coefficients of the finite-dimensional continuous unitary representations of $G$ span a dense subspace of $C(G)$, with the supremum norm.
2. The functions $\sqrt{d_\pi}\, \pi_{ij}$, for $\pi \in \widehat{G}$ and $1 \le i, j \le d_\pi$, form an orthonormal basis of the [[Hilbert space|HM2HHE3J51]] $L^2(G)$.
3. Every continuous unitary representation of $G$ on a Hilbert space is a Hilbert direct sum of finite-dimensional irreducible representations.

## Remarks

The proof applies the spectral theorem to self-adjoint convolution operators $f \mapsto k * f$ on $L^2(G)$ with continuous kernels $k$.
Such operators are compact and commute with right translations, so their eigenspaces for nonzero eigenvalues are finite-dimensional invariant subspaces.
Letting $k$ run through an approximate identity shows that these subspaces span a dense subspace, which gives parts 1 and 2.
Part 3 follows by applying the same idea to a general representation.
Orthonormality in part 2 is the [[Schur orthogonality for compact groups|ETNDTECY97]].
Example: for $G = \mathbb{T}$ the irreducible representations are the characters $z \mapsto z^n$, $n \in \Z$, and part 2 says that the functions $e^{in\theta}$ form an orthonormal basis of $L^2(\mathbb{T})$, the completeness of Fourier series.
For a finite group, the theorem reduces to the decomposition of the regular representation, with $\sum_\pi d_\pi^2 = \abs{G}$.

## Explanations

### L1 human

On the circle, every reasonable function is a sum of waves $e^{in\theta}$.
The Peter–Weyl theorem says the same for every compact group, where the waves are replaced by the entries of the matrices of irreducible representations.
These matrix entries are like a complete set of perpendicular axes for the space of functions on the group.

### L2 human

Part 1 implies that every compact Lie group has a faithful finite-dimensional representation, so it is isomorphic to a closed subgroup of some unitary group $U(n)$.
Part 3 reduces the study of unitary representations of compact groups to finite-dimensional ones, where [[complete reducibility|N6JC6KNXJJ]] and characters are available.
In terms of the left and right regular actions, part 2 says that $L^2(G)$ is the Hilbert direct sum over $\pi \in \widehat{G}$ of the spaces $\End(V_\pi)$, each of dimension $d_\pi^2$.

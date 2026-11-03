---
tag: ETNDTECY97
kind: statement
role: theorem
name: Schur orthogonality for compact groups
msc: [22C05, 43A77, 22D10]
uses: [EVHCE5VR6Y, VY0HXD3GC4, 74BPYJNZTM, FX3NEFYFFN, RMWMYBY8TC]
about: [RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_orthogonality_relations
---

## Statement

Let $G$ be a [[compact group|EVHCE5VR6Y]] with normalised [[Haar measure|VY0HXD3GC4]] $dg$, and for $\alpha, \beta \in L^2(G)$ write $\ip{\alpha}{\beta} = \int_G \alpha(g)\overline{\beta(g)} \, dg$.
Let $\pi$ and $\sigma$ be finite-dimensional continuous [[irreducible|FX3NEFYFFN]] [[unitary representations|74BPYJNZTM]] of $G$, of dimension $d_\pi$ and $d_\sigma$.
Let $\pi_{ij}$ and $\sigma_{kl}$ be their [[matrix coefficients|J85Q7QGGHS]] in orthonormal bases.

1. If $\pi$ and $\sigma$ are not isomorphic, then $\ip{\pi_{ij}}{\sigma_{kl}} = 0$ for all indices.
2. For all indices $i, j, k, l$, one has $\ip{\pi_{ij}}{\pi_{kl}} = \delta_{ik}\delta_{jl}/d_\pi$.
3. The [[characters|RMWMYBY8TC]] $\chi_\pi = \tr \pi$ and $\chi_\sigma = \tr \sigma$ satisfy $\ip{\chi_\pi}{\chi_\sigma} = 1$ if $\pi \cong \sigma$ and $\ip{\chi_\pi}{\chi_\sigma} = 0$ otherwise.

## Remarks

For a linear map $A$ between the two spaces, the average $\int_G \sigma(g) A \pi(g)^{-1} \, dg$ intertwines $\pi$ and $\sigma$.
By Schur's lemma it is $0$ when they are not isomorphic and a scalar when $\pi = \sigma$.
Taking $A$ to be a matrix unit gives parts 1 and 2, the scalar being found by taking traces; summing over $i = j$ and $k = l$ gives part 3.
Example: for $G = \mathbb{T}$ with the characters $\chi_n(z) = z^n$, part 3 reads $\frac{1}{2\pi}\int_0^{2\pi} e^{in\theta} e^{-im\theta} \, d\theta = \delta_{nm}$.
For a finite group with Haar measure the counting measure divided by $\abs{G}$, the statement is the [[Schur orthogonality relations|AY0B20QC04]] of finite groups.
A consequence: a finite-dimensional continuous representation with character $\chi$ is irreducible if and only if $\ip{\chi}{\chi} = 1$.

## Explanations

### L1 human

The matrix entries of different irreducible representations of a compact group are perpendicular to each other as functions on the group.
The characters of irreducible representations are perpendicular unit vectors.
So one can find how often an irreducible piece occurs in a representation by an integral, just like taking a coordinate.

### L2 human

These relations give the orthonormality half of the [[Peter–Weyl theorem|6VC9QE39XH]]; the completeness half is the harder part.
For compact connected Lie groups, the [[Weyl integration formula|QMH530N27M]] turns the character relation into an integral over a maximal torus, which is the route to the [[Weyl character formula|230F5FXPMQ]].
The relations apply to every finite-dimensional continuous representation after a change of basis, since each one is unitary for a suitable inner product by [[complete reducibility|N6JC6KNXJJ]].

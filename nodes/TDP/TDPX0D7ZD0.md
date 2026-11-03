---
tag: TDPX0D7ZD0
kind: object
name: Gamma matrices
msc: [15A66, 81R20, 81R25]
uses: [A38B1QFK20, XAQCW3D4QQ, XNZX7VXXR2]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_matrices
same_as:
  wikidata: Q1151645
  wikipedia: Gamma matrices
---

## Description

Let $\eta = \mathrm{diag}(1, -1, -1, -1)$ be the Minkowski metric, with indices $\mu, \nu \in \set{0, 1, 2, 3}$.
*Gamma matrices*, or Dirac matrices, are four complex $4 \times 4$ matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ that satisfy
$$\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2\eta^{\mu\nu} I_4 \qquad \text{for all } \mu, \nu.$$
The standard choice, the Dirac representation, is written in $2 \times 2$ blocks as
$$\gamma^0 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2 \end{pmatrix}, \qquad \gamma^k = \begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix} \quad (k = 1, 2, 3),$$
where $\sigma_1, \sigma_2, \sigma_3$ are the [[Pauli matrices|XAQCW3D4QQ]].

Check: $(\gamma^0)^2 = I_4$.
Since $\sigma_k^2 = I_2$, the block product gives $(\gamma^k)^2 = \mathrm{diag}(-\sigma_k^2, -\sigma_k^2) = -I_4$.
The product $\gamma^0\gamma^k$ has off-diagonal blocks $\sigma_k$ and $\sigma_k$, and $\gamma^k\gamma^0$ has off-diagonal blocks $-\sigma_k$ and $-\sigma_k$, so they anticommute.
For $j \ne k$, $\gamma^j\gamma^k + \gamma^k\gamma^j = -\mathrm{diag}(\sigma_j\sigma_k + \sigma_k\sigma_j, \sigma_j\sigma_k + \sigma_k\sigma_j) = 0$, since distinct Pauli matrices anticommute.

## Remarks

The relations say that sending the generators $e_\mu$ of the real [[Clifford algebra|A38B1QFK20]] of the form $\eta$ to $\gamma^\mu$ defines a representation of this algebra on $\C^4$.
The complexified Clifford algebra is isomorphic to $M_4(\C)$, and this is its only irreducible representation up to equivalence.
Any two sets of $4 \times 4$ matrices that satisfy the relations are conjugate by an invertible matrix.
In the Dirac representation $\gamma^0$ is Hermitian and each $\gamma^k$ is anti-Hermitian.

The fifth gamma matrix $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ satisfies $(\gamma^5)^2 = I_4$ and anticommutes with every $\gamma^\mu$; its eigenspaces give the two chiralities.
Another common choice is the Weyl (chiral) representation, in which $\gamma^0$ has off-diagonal blocks $I_2$ and $\gamma^5$ is diagonal.

With the gamma matrices the [[Dirac equation|XNZX7VXXR2]] reads $(i\gamma^\mu \partial_\mu - m)\psi = 0$, summed over $\mu$, in units with $\hbar = c = 1$.
Applying $(i\gamma^\nu\partial_\nu + m)$ and using the relations gives $(\partial^\mu\partial_\mu + m^2)\psi = 0$, the Klein–Gordon equation for each component.

## Explanations

### L1 human

Dirac wanted an equation that is first order in time and space and still agrees with $E^2 = p^2 + m^2$.
That needs four objects whose squares are $\pm 1$ and which anticommute with each other, which no ordinary numbers can do.
The smallest matrices that work are $4 \times 4$, and these are the gamma matrices.
They are built from the $2 \times 2$ Pauli matrices that describe spin.

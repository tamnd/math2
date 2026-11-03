---
tag: KMA1HCE104
kind: definition
name: Fixed point of the renormalization group
msc: [82B28, 82B27]
defines: H0B5TN4139
uses: [5XTSCZCF7Z, H5PQFQS6CE, ENWMTRJRND]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
---

## Definition

Let $\mathcal K$ be a space of coupling constants, each $K \in \mathcal K$ describing a Hamiltonian $H_K$ of a lattice system.
Let $b > 1$ and let $R_b \colon \mathcal K \to \mathcal K$ be a [[renormalization group|5XTSCZCF7Z]] transformation with scale factor $b$, such as a [[block spin transformation|H5PQFQS6CE]].
A *fixed point* of $R_b$ is a point $K^* \in \mathcal K$ with
$$R_b(K^*) = K^*.$$
A fixed point is *critical* if the correlation length $\xi(K^*)$ of $H_{K^*}$, the decay length of its [[correlation function|ENWMTRJRND]], is infinite, and *trivial* if $\xi(K^*) = 0$.

## Remarks

The transformation rescales lengths by $b$, so $\xi(R_b K) = \xi(K)/b$.
At a fixed point this gives $\xi(K^*) = \xi(K^*)/b$, so $\xi(K^*)$ is $0$ or $\infty$.

Example: for the Ising model with coupling $K$, the point $K = 0$ of independent spins is a trivial fixed point of the majority-rule block spin transformation.
Check: let the spins be independent and uniform.
The block spins are functions of disjoint sets of spins, so they are again independent.
Each block spin is uniform by the symmetry $\sigma \mapsto -\sigma$.

Non-example: for the two-dimensional Ising model at a coupling $K$ with $0 < K < K_c$, the correlation length is finite and positive, so $K$ is not a fixed point.
Under repeated transformations it flows toward the high-temperature trivial fixed point.

The set of couplings that flow to a critical fixed point under iteration is its *critical surface*.

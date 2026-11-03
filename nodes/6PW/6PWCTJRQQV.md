---
tag: 6PWCTJRQQV
kind: definition
name: Density matrix renormalization group
msc: [82B20, 65Z05, 81P40]
defines: 1DHYFN8KT5
uses: [H578T160KS, 0P17NGQQMQ, 09VMDSRXWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Density_matrix_renormalization_group
---

## Definition

Let $\mathcal{H} = (\C^d)^{\otimes N}$ and let $H$ be a [[Hermitian|0P17NGQQMQ]] operator on $\mathcal{H}$, the Hamiltonian.
Fix a bond dimension $D \ge 1$.
The *density matrix renormalization group* (in its two-site form) is the following iterative method.
It approximates the least eigenvalue of $H$ and an eigenvector for it.

1. Start from a [[matrix product state|H578T160KS]] $\psi$ of bond dimension at most $D$.
2. Choose two adjacent sites $k, k+1$, and keep the matrices of all other sites fixed, in a gauge where the left and right parts are orthonormal.
3. Merge the matrices of sites $k$ and $k+1$ into one tensor $\Theta$. The energy $\langle \psi, H\psi \rangle / \langle \psi, \psi \rangle$ is then a Rayleigh quotient $\langle \Theta, H_{\mathrm{eff}} \Theta \rangle / \langle \Theta, \Theta \rangle$ of an effective Hermitian matrix $H_{\mathrm{eff}}$. Replace $\Theta$ by an eigenvector for the least eigenvalue of $H_{\mathrm{eff}}$.
4. Split $\Theta$ again by a [[singular value|09VMDSRXWJ]] decomposition and keep only the $D$ largest singular values.
5. Move to the next pair of sites and repeat, sweeping from left to right and back, until the energy stops decreasing.

The squares of the singular values in step 4 are the eigenvalues of the reduced density matrix of the left part of the chain.
So step 4 keeps the states of largest weight in that density matrix.

## Remarks

Each energy obtained is $\langle \psi, H\psi \rangle / \langle \psi, \psi \rangle$ for some nonzero $\psi$, so it is an upper bound on the least eigenvalue of $H$.

Example: if $D \ge d^{\floor{N/2}}$, every vector of $\mathcal{H}$ is a matrix product state of bond dimension at most $D$.
Then no truncation happens in step 4, and the method searches the whole space.

Non-example: some schemes keep, for a block of the chain, the lowest eigenvectors of the block Hamiltonian.
They do not keep the dominant eigenvectors of the reduced density matrix, so they are not DMRG.
Such older real-space renormalization schemes give poor results even for a single particle hopping on a chain, which was the motivation for White's method.

The method is mainly used for one-dimensional systems, where ground states of gapped Hamiltonians have bounded entanglement across a cut.

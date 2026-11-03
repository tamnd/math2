---
tag: Z0ZHN80F2B
kind: statement
role: theorem
name: Lieb–Schultz–Mattis theorem
msc: [82B20, 82B10, 82D40]
uses: [5QG15H8P5J]
about: [5QG15H8P5J]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Heisenberg_model
---

## Statement

Let $S$ be a half-odd-integer, let $L$ be an even integer, and let $J > 0$.
Let $H_L = J \sum_{j=1}^{L} \mathbf{S}_j \cdot \mathbf{S}_{j+1}$ be the antiferromagnetic spin-$S$ [[quantum Heisenberg model|5QG15H8P5J]] on a ring of $L$ sites, with $\mathbf{S}_{L+1} = \mathbf{S}_1$, and let $E_0(L)$ be its ground-state energy.
Let $\psi_L$ be a ground state of $H_L$ that is an eigenvector of the translation and of the total magnetization $S^z_{\mathrm{tot}}$ with eigenvalue $0$.
Then there is a constant $C$, independent of $L$, and a unit vector $\varphi_L$ orthogonal to $\psi_L$ such that
$$\langle \varphi_L, H_L \varphi_L \rangle - E_0(L) \le \frac{C}{L}.$$
Consequently, in the limit $L \to \infty$, either the ground state is degenerate or there is no spectral gap above it.

## Remarks

The idea of the proof is a twist.
Let $\psi$ be the ground state, which for the Heisenberg antiferromagnet on an even ring is a unique total-spin singlet invariant under translation up to a phase.
Set $U = \exp\big(\tfrac{2\pi i}{L}\sum_{j} j\, S^z_j\big)$, which rotates the spins slowly along the chain.
Each bond energy changes by $O(1/L^2)$, so $\langle U\psi, H_L U\psi \rangle - E_0(L) = O(1/L)$.
The translation $T$ satisfies $TUT^{-1} = U e^{-2\pi i S^z_{\mathrm{tot}}/L} e^{2\pi i S^z_1}$, and $e^{2\pi i S^z_1} = -1$ for half-odd-integer $S$; since $S^z_{\mathrm{tot}}\psi = 0$ and $T\psi$ is a multiple of $\psi$, this gives $\langle \psi, U\psi \rangle = -\langle \psi, U\psi \rangle$, so $\varphi = U\psi$ is orthogonal to $\psi$.
Lieb, Schultz and Mattis proved the case $S = \tfrac12$ in 1961, and Affleck and Lieb extended it to all half-odd-integer $S$ in 1986.
The argument fails for integer $S$, where $e^{2\pi i S^z_1} = 1$, and indeed the spin-$1$ AKLT chain has a gap.

## Explanations

### L1 human

The theorem says that a ring of half-integer quantum spins coupled antiferromagnetically cannot have a unique ground state separated by an energy gap from everything else.
One builds a low-energy excitation by twisting the spins very slowly around the ring.
The cost of the twist shrinks as the ring grows, and for half-integer spins the twisted state is different from the ground state.

### L2 human

The result is a constraint from symmetry and filling: it relates translation symmetry, spin rotation symmetry and the half-integer spin per unit cell.
For the spin-$\tfrac12$ chain the exact solution confirms the gapless option.
For integer spins the argument breaks down, and Haldane's prediction of a gap is consistent with it.
Modern generalizations, by Oshikawa and by Hastings in higher dimensions, give similar constraints for lattices with a fractional filling per unit cell.

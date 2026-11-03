---
tag: 8H0DJFKRZ0
kind: definition
name: Hückel method
msc: [81V55, "92E10", 05C50]
defines: FXW4C6DPNF
uses: [08B9CX109G, 0BQAA2BK3Q, 0VR671PHE5, AE724Y8CQX]
sources:
  - url: https://en.wikipedia.org/wiki/Hückel_method
---

## Definition

Let a planar conjugated hydrocarbon have $n$ carbon atoms that each carry one $\pi$-electron.
Let $G$ be the graph on these atoms whose edges are the carbon–carbon bonds.
Let $A$ be the [[adjacency matrix|08B9CX109G]] of $G$, a real [[symmetric matrix|0VR671PHE5]] of size $n$.
Fix two real parameters, the Coulomb integral $\alpha$ and the resonance integral $\beta < 0$.
The *Hückel method* takes as Hamiltonian matrix
$$H = \alpha I + \beta A.$$
Let $\lambda_1 \ge \cdots \ge \lambda_n$ be the [[eigenvalues|0BQAA2BK3Q]] of $A$.
The eigenvalues $E_k = \alpha + \beta \lambda_k$ of $H$ are the energies of the $\pi$-molecular orbitals.
Orthonormal eigenvectors give the coefficients of these orbitals on the atoms.
The $n$ electrons fill the orbitals in increasing order of energy, at most two per orbital.
The *total $\pi$-electron energy* is the sum of the energies of the electrons.

## Remarks

Example: for ethylene, $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $\pm 1$, so the levels are $\alpha + \beta < \alpha - \beta$, and the two electrons give energy $2\alpha + 2\beta$.
For benzene, $G$ is the cycle $C_6$, with eigenvalues $2\cos(2\pi k/6)$ for $k = 0, \dots, 5$, that is $2, 1, 1, -1, -1, -2$.
The six electrons fill the three lowest levels, giving $2(\alpha + 2\beta) + 4(\alpha + \beta) = 6\alpha + 8\beta$.
Three separate double bonds would give $6\alpha + 6\beta$, so the delocalization energy is $2\beta < 0$, a gain in stability.
Non-example: in a saturated molecule such as ethane there are no $\pi$-electrons, so the method does not apply.
When the electron count is even and the occupied levels are full, the total energy is $n\alpha + 2\beta \sum_{k \le n/2} \lambda_k$.

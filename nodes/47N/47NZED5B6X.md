---
tag: 47NZED5B6X
kind: definition
name: Born–Oppenheimer approximation
msc: [81V55, 81Q15, 81Q20]
defines: E6ZF252YH2
uses: [VXDEQB46GV, 0NEGN5CRSC, 0N6960W0BV, E9WK6KJ4SM]
sources:
  - url: https://en.wikipedia.org/wiki/Born%E2%80%93Oppenheimer_approximation
---

## Definition

Consider a molecule with nuclei of masses $M_1, \ldots, M_K$ at positions $R = (R_1, \ldots, R_K) \in \R^{3K}$ and $N$ electrons of mass $m$ at positions $r = (r_1, \ldots, r_N) \in \R^{3N}$.
Write its [[Hamiltonian|VXDEQB46GV]] as
$$H = -\sum_{k=1}^{K} \frac{\hbar^2}{2M_k} \Delta_{R_k} + H_{\mathrm{el}}(R).$$
The electronic Hamiltonian $H_{\mathrm{el}}(R)$ is the kinetic energy of the electrons plus all Coulomb interactions.
It acts on functions of $r$ for fixed $R$.
The *Born–Oppenheimer approximation* consists of two steps:

1. For each $R$, find an eigenvalue $E_j(R)$ and a normalised [[eigenvector|0N6960W0BV]] $\phi_j(r; R)$ of $H_{\mathrm{el}}(R)$; the function $R \mapsto E_j(R)$ is the $j$-th potential energy surface.
2. Let $\chi$ be an eigenfunction, with eigenvalue $E$, of the nuclear Hamiltonian $-\sum_k \frac{\hbar^2}{2M_k} \Delta_{R_k} + E_j(R)$.
   Approximate the eigenfunctions of $H$ by the products $\Psi(r, R) = \chi(R)\, \phi_j(r; R)$, and the eigenvalues of $H$ by these $E$.

## Remarks

The approximation drops the terms where the nuclear kinetic energy differentiates $\phi_j(r; R)$ in $R$.
These terms carry a factor $m/M_k$ and contain the couplings $\ip{\phi_i}{\nabla_{R} \phi_j}$, which can be written as $\ip{\phi_i}{(\nabla_R H_{\mathrm{el}}) \phi_j} / (E_j - E_i)$ for $i \ne j$.

Example: take the hydrogen molecular ion $\mathrm{H}_2^+$.
The electronic problem for two fixed protons at distance $\rho$ gives a ground energy curve $E_0(\rho)$ with a minimum.
The nuclear problem in this curve gives the vibrational and rotational levels of the ion.

Non-example: consider a configuration where two surfaces meet, $E_i(R) = E_j(R)$, for instance a conical intersection.
Near it the couplings above blow up, step 2 fails, and the nuclei can switch from one surface to the other.

Since $H_{\mathrm{el}}(R)$ is a real operator, $\phi_j$ can be chosen real; around a conical intersection such a real eigenfunction changes sign, which is a [[geometric phase|7BJM2TRPK2]] of $\pi$.

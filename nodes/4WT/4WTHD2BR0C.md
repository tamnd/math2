---
tag: 4WTHD2BR0C
kind: definition
name: Time reversal symmetry
msc: [81R05, 81Q10]
defines: N8P02NZGZS
uses: [HM2HHE3J51, VXDEQB46GV, 7XAKGQQWTP, 5WG6YTAA6J, YBS1CHXFTW, WN6C2BJDZT]
sources:
  - url: https://en.wikipedia.org/wiki/Time-reversal_symmetry
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]].
An operator $\Theta \colon \mathcal{H} \to \mathcal{H}$ is *antiunitary* if it is bijective, $\Theta(a\psi + b\phi) = \bar{a}\Theta\psi + \bar{b}\Theta\phi$, and $\ip{\Theta\psi}{\Theta\phi} = \overline{\ip{\psi}{\phi}}$ for all $a, b \in \C$ and $\psi, \phi \in \mathcal{H}$.
A *time reversal operator* for a system of particles is an antiunitary $\Theta$ such that

1. $\Theta x_k \Theta^{-1} = x_k$ for each [[position operator|7XAKGQQWTP]] component,
2. $\Theta p_k \Theta^{-1} = -p_k$ for each [[momentum operator|5WG6YTAA6J]] component,
3. $\Theta S_k \Theta^{-1} = -S_k$ for each [[spin|YBS1CHXFTW]] operator component.

The system with [[Hamiltonian|VXDEQB46GV]] $H$ has *time reversal symmetry* if $\Theta D(H) = D(H)$ and $\Theta H \Theta^{-1} = H$, so that $\Theta$ is an antiunitary [[symmetry|WN6C2BJDZT]] of the system.

## Remarks

If $\Theta$ commutes with $H$ and $\psi(t)$ solves $i\hbar \partial_t \psi = H\psi$, then $\phi(t) = \Theta\psi(-t)$ solves it too, because $\Theta$ turns $i$ into $-i$; this is why $\Theta$ must be antiunitary.

Example: for one spinless particle on $L^2(\R^3)$, complex conjugation $\Theta\psi = \bar{\psi}$ satisfies the clauses, since $\overline{-i\hbar\nabla\psi} = -(-i\hbar\nabla\bar{\psi})$, and $\Theta^2 = I$.
The Hamiltonian $-\frac{\hbar^2}{2m}\Delta + V(x)$ with a real potential $V$ commutes with it, so this system has time reversal symmetry.
For a spin one-half particle on $L^2(\R^3) \otimes \C^2$, one can take $\Theta = -i\sigma_2 K$, where $K$ is complex conjugation and $\sigma_2$ the second Pauli matrix; then $\Theta^2 = -I$.

Non-example: for a charged particle in a magnetic field with vector potential $A$, $H = \frac{1}{2m}(p - qA(x))^2$.
Conjugation by $\Theta$ gives $\frac{1}{2m}(-p - qA(x))^2 = \frac{1}{2m}(p + qA(x))^2$, which differs from $H$ when the magnetic field $\nabla \times A$ is nonzero, so the system has no time reversal symmetry.

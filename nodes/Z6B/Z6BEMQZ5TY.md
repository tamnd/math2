---
tag: Z6BEMQZ5TY
kind: definition
name: Heisenberg picture
msc: ["81Q05", "81S05"]
defines: TAFA5VK0ST
uses: [VXDEQB46GV, MM0EJ2GDE4, DF5RN297GE, GEHZ2CCH2J, 0PXW0BN7DW]
sources:
  - url: https://en.wikipedia.org/wiki/Heisenberg_picture
---

## Definition

Let $H$ be the [[Hamiltonian|VXDEQB46GV]] of a quantum system with Hilbert space $\mathcal{H}$, let $\hbar > 0$, and let $U(t) = e^{-itH/\hbar}$, a [[unitary operator|MM0EJ2GDE4]] for each $t \in \R$.
In the *Heisenberg picture*:

1. a state vector $\psi$, or a density operator $\rho$, does not depend on time;
2. an [[observable|DF5RN297GE]] $A$ at time $t$ is $A_H(t) = U(t)^* A\, U(t)$, with domain $U(t)^* D(A)$;
3. the expectation value of $A$ at time $t$ is $\ip{\psi}{A_H(t)\psi}$, or $\operatorname{tr}(\rho A_H(t))$.

## Remarks

Since $\ip{\psi}{U(t)^* A U(t)\psi} = \ip{U(t)\psi}{A U(t)\psi}$, the expectation values agree with those of the [[Schrödinger picture|GEHZ2CCH2J]].
Each $A_H(t)$ is again self-adjoint, with the same spectrum as $A$, and $H_H(t) = H$.
If $\mathcal{H}$ is finite-dimensional, $A_H$ solves the Heisenberg equation $\frac{d}{dt}A_H(t) = \frac{i}{\hbar}[H, A_H(t)]$, with the [[commutator|0PXW0BN7DW]] $[H, B] = HB - BH$.

Example: on $\C^2$ let $H = \frac{\hbar\omega}{2}\sigma_z$, so $U(t) = \mathrm{diag}(e^{-i\omega t/2}, e^{i\omega t/2})$.
A direct computation gives $(\sigma_x)_H(t) = \cos(\omega t)\, \sigma_x - \sin(\omega t)\, \sigma_y$.
For $\psi = (1, 1)/\sqrt{2}$ one has $\ip{\psi}{\sigma_x\psi} = 1$ and $\ip{\psi}{\sigma_y\psi} = 0$, so the expectation value is $\cos \omega t$, as in the Schrödinger picture.

Non-example: the rule $A \mapsto U(t) A\, U(t)^*$, with the factors in the other order, gives $\ip{U(-t)\psi}{A U(-t)\psi}$, the expectation value at time $-t$.

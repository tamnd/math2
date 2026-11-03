---
tag: ZJJGJ94XVG
kind: definition
name: Quantum decoherence
msc: [81S22, 81P05]
defines: AN414B0M5X
uses: [HM2HHE3J51, EY0X2NKA3S, 0S9GGTR0EX, MM0EJ2GDE4, V1JTB52E8C, SQ3J7AVMKM]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_decoherence
---

## Definition

Let $\mathcal{H}_S$ be a finite-dimensional complex [[Hilbert space|HM2HHE3J51]] for a system $S$, and let $\mathcal{H}_E$ be a complex Hilbert space for its environment $E$.
Let $\set{e_1, \dots, e_n}$ be an [[orthonormal basis|0S9GGTR0EX]] of $\mathcal{H}_S$.
Let $t \mapsto U(t)$ be the [[unitary|MM0EJ2GDE4]] time evolution on the [[tensor product|EY0X2NKA3S]] $\mathcal{H}_S \otimes \mathcal{H}_E$, and let the initial state be $\rho_S \otimes \rho_E$, with $\rho_S$ and $\rho_E$ [[density matrices|V1JTB52E8C]].
The reduced state of $S$ at time $t$ is the [[partial trace|SQ3J7AVMKM]]
$$\rho_S(t) = \tr_E\big(U(t)(\rho_S \otimes \rho_E)U(t)^*\big).$$
The system undergoes *decoherence in the basis* $(e_i)$ if, for every initial $\rho_S$:

1. the diagonal entries are kept: $\langle e_i, \rho_S(t) e_i \rangle = \langle e_i, \rho_S e_i \rangle$ for all $i$ and $t$;
2. the off-diagonal entries decay: $\langle e_i, \rho_S(t) e_j \rangle \to 0$ for all $i \ne j$ as $t \to \infty$.

The basis $(e_i)$ is then called the *pointer basis*.

## Remarks

Example: let $\rho_E = \lvert \chi \rangle\langle \chi \rvert$ and let $U(t)(e_i \otimes \chi) = e_i \otimes \chi_i(t)$ with unit vectors $\chi_i(t) \in \mathcal{H}_E$.
Then $\langle e_i, \rho_S(t) e_j \rangle = \langle e_i, \rho_S e_j \rangle \langle \chi_j(t), \chi_i(t) \rangle$, so clause 1 holds.
Clause 2 holds exactly when the overlaps $\langle \chi_j(t), \chi_i(t) \rangle$ tend to $0$, that is, when the environment records which $e_i$ the system is in.
Non-example: if $U(t) = V(t) \otimes W(t)$ is a product of unitaries, then $\rho_S(t) = V(t)\rho_S V(t)^*$ stays pure for pure $\rho_S$.
A pure state with fixed diagonal entries $p_i$ has off-diagonal entries of modulus $\sqrt{p_i p_j}$, so clause 2 fails.
Let $\mathcal{H}_E$ be finite-dimensional and $U(t) = e^{-itH}$ for a fixed Hamiltonian $H$.
Then the entries of $\rho_S(t)$ are almost periodic in $t$, so they cannot tend to $0$ unless they vanish, and clause 2 fails.
Exact decay therefore needs an environment with infinitely many degrees of freedom, and in physical models it is often exponential, with a rate called the decoherence rate.
This is one common way to make the notion precise.
In physics, the word is often used more loosely, for the approximate suppression of off-diagonal entries.

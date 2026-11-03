---
tag: Q5EJDFZRF0
kind: definition
name: Open quantum system
msc: [81S22]
defines: 6D9YCNZ7X9
uses: [HM2HHE3J51, EY0X2NKA3S, 0NEGN5CRSC, V1JTB52E8C, SQ3J7AVMKM, VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Open_quantum_system
---

## Definition

Let $\mathcal{H}_S$ and $\mathcal{H}_E$ be complex [[Hilbert spaces|HM2HHE3J51]] for a system $S$ and an environment $E$.
Let $H$ be a [[self-adjoint operator|0NEGN5CRSC]] on the [[tensor product|EY0X2NKA3S]] $\mathcal{H}_S \otimes \mathcal{H}_E$, the total [[Hamiltonian|VXDEQB46GV]].
Assume that it has the form
$$H = H_S \otimes I_E + I_S \otimes H_E + H_I,$$
where $H_S$ and $H_E$ act on $\mathcal{H}_S$ and $\mathcal{H}_E$, and $H_I$ is the interaction.
Let $\rho(0)$ be a [[density operator|V1JTB52E8C]] on $\mathcal{H}_S \otimes \mathcal{H}_E$ and $U(t) = e^{-itH/\hbar}$.
The system $S$ is then an *open quantum system*.
Its state at time $t$ is the reduced density operator
$$\rho_S(t) = \tr_E\big(U(t)\rho(0)U(t)^*\big),$$
where $\tr_E$ is the [[partial trace|SQ3J7AVMKM]] over $\mathcal{H}_E$.
The special case with $H_I = 0$ and $\rho(0) = \rho_S(0) \otimes \rho_E(0)$ is a *closed* system, with $\rho_S(t) = e^{-itH_S/\hbar}\rho_S(0)e^{itH_S/\hbar}$.

## Remarks

Example: a qubit coupled to a second qubit by $H_I = g\, Z \otimes X$, with $H_S = H_E = 0$, $\rho(0) = \rho_S \otimes e_0e_0^*$ and $\hbar = 1$.
Then $U(t) = e_0e_0^* \otimes e^{-igtX} + e_1e_1^* \otimes e^{igtX}$, and the off-diagonal entries of $\rho_S(t)$ get multiplied by $\langle e^{igtX}e_0, e^{-igtX}e_0 \rangle = \cos(2gt)$.
So the reduced dynamics is not unitary: a pure superposition becomes mixed, for instance completely dephased at $t = \pi/(4g)$.
Non-example: with $H_I = 0$ and a product initial state, the reduced dynamics is the unitary evolution of $S$ alone, so the system is closed.
When $\rho(0) = \rho_S(0) \otimes \rho_E$ with $\rho_E$ fixed, each map $\rho_S(0) \mapsto \rho_S(t)$ is a [[quantum channel|10VZYJ4552]].

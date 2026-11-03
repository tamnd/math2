---
tag: 7NW2C10YSR
kind: concept
name: Canonical quantization
msc: [81S08, 81S05]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_quantization
same_as:
  wikidata: Q5961083
  wikipedia: Canonical quantization
---

## Summary

Canonical quantization turns a classical Hamiltonian system into a quantum one.
The canonical coordinates $q_j$ and momenta $p_j$ of [[phase space|CPEC2NW2KF]] become self-adjoint operators $Q_j$ and $P_j$ on a Hilbert space.
The [[Poisson bracket|2S0MXDT4YH]] $\{q_j, p_k\} = \delta_{jk}$ becomes the commutator $[Q_j, P_k] = i\hbar\, \delta_{jk}$.
Other observables, such as the Hamiltonian, are then replaced by functions of $Q$ and $P$, which needs an ordering rule such as [[Weyl quantization|RFNGJ09WDR]].
[[Groenewold's theorem|EDPPWXMXA4]] shows that no rule can turn all Poisson brackets into commutators exactly.

## Explanations

### L1 human

Classical mechanics describes a particle by its position and momentum, two numbers.
Quantum mechanics replaces them by two operators acting on wave functions: multiplication by $x$ and $-i\hbar$ times the derivative.
These two operators do not commute, and their commutator is $i\hbar$, the quantum counterpart of the classical bracket $\{q, p\} = 1$.
For the harmonic oscillator, the energy $p^2/2m + m\omega^2 q^2/2$ becomes the operator $-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + \frac{m\omega^2}{2} x^2$.
Its eigenvalues are the quantized energies $\hbar\omega(n + \tfrac12)$.

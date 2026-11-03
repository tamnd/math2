---
tag: 5P82FXVCCR
kind: definition
name: Quantum Turing machine
msc: [68Q12, 68Q09, 81P68]
defines: E1P61VYRRD
uses: [758EYCN27B, HM2HHE3J51, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Turing_machine
---

## Definition

Let $\tilde{\C}$ be the set of complex numbers $\alpha$ whose real and imaginary parts are efficiently computable.
This means they can be computed to precision $2^{-n}$ in time polynomial in $n$.
A *quantum Turing machine* is a tuple $M = (\Sigma, Q, \delta, q_0, q_f)$ with these parts.

1. $\Sigma$ is a finite tape alphabet with a blank symbol, and $Q$ is a finite set of states with $q_0, q_f \in Q$.
2. $\delta$ is a quantum transition function $\delta \colon Q \times \Sigma \times \Sigma \times Q \times \set{L, R} \to \tilde{\C}$.
3. The value $\delta(p, \sigma, \tau, q, d)$ is the amplitude of this move: in state $p$ reading $\sigma$, write $\tau$, enter $q$ and move in direction $d$.

A *configuration* is a state, a tape content with finitely many non-blank cells, and a head position, as for a [[Turing machine|758EYCN27B]].
Let $\mathcal H$ be the [[Hilbert space|HM2HHE3J51]] with orthonormal basis indexed by the configurations.
The function $\delta$ defines a linear operator $U_\delta$ on $\mathcal H$ that sends each configuration to the superposition of its successors, weighted by their amplitudes.
The condition on $M$ is that $U_\delta$ is a [[unitary operator|MM0EJ2GDE4]].

## Remarks

A computation starts from the basis vector of the start configuration and applies $U_\delta$ once per step.
Measuring a state $\sum_c \alpha_c \lvert c \rangle$ gives configuration $c$ with probability $\abs{\alpha_c}^2$.

Example: every reversible deterministic Turing machine is a quantum Turing machine with amplitudes in $\set{0, 1}$.
Its step map permutes the configurations, so $U_\delta$ is unitary.

Non-example: a deterministic machine that erases a cell fails the condition.
Say that in state $p$ it writes a blank over both $0$ and $1$, enters the same state and moves the same way.
Two distinct configurations then have the same successor, so $U_\delta$ is not injective and hence not unitary.

The restriction to $\tilde{\C}$ prevents amplitudes from encoding uncomputable information.

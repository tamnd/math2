---
tag: ABJPBAQAGC
kind: definition
name: Quantum dynamical semigroup
msc: [81S22, 47D07, 46L57]
defines: EQDPM8894B
uses: [10VZYJ4552, EVF180QJXY, Z2CP530WDE, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Markov_semigroup
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $\mathcal{T}(\mathcal{H})$ be the space of [[trace class operators|Z2CP530WDE]] with the trace norm $\norm{\cdot}_1$.
A *quantum dynamical semigroup* on $\mathcal{H}$, in the Schrödinger picture, is a family $(T_t)_{t \ge 0}$ of linear maps $T_t \colon \mathcal{T}(\mathcal{H}) \to \mathcal{T}(\mathcal{H})$ such that:

1. each $T_t$ is a [[quantum channel|10VZYJ4552]], that is, completely positive and trace-preserving;
2. $T_0 = \id$ and $T_{s+t} = T_s \circ T_t$ for all $s, t \ge 0$;
3. $\norm{T_t(\rho) - \rho}_1 \to 0$ as $t \to 0^+$, for every $\rho \in \mathcal{T}(\mathcal{H})$.

Clauses 2 and 3 say that $(T_t)$ is a [[C0-semigroup|EVF180QJXY]] on $\mathcal{T}(\mathcal{H})$.
In the Heisenberg picture one uses instead the adjoint maps on bounded operators.
These are unital, completely positive and normal, and continuous in the weak* topology.

## Remarks

Example: on $\C^2$ with $\gamma > 0$, let $T_t(\rho) = \tfrac{1 + e^{-\gamma t}}{2}\rho + \tfrac{1 - e^{-\gamma t}}{2} Z\rho Z$, where $Z = \operatorname{diag}(1, -1)$.
Each $T_t$ is a mixture of the unitary conjugations by $I$ and $Z$, so it is a channel.
It keeps the diagonal of $\rho$ and multiplies the off-diagonal entries by $e^{-\gamma t}$.
Since $e^{-\gamma s}e^{-\gamma t} = e^{-\gamma(s+t)}$ and $T_t(\rho) \to \rho$ as $t \to 0^+$, clauses 2 and 3 hold.
Non-example: the channels $S_t(\rho) = \tfrac{1 + \cos t}{2}\rho + \tfrac{1 - \cos t}{2}Z\rho Z$ satisfy $S_0 = \id$ and multiply the off-diagonal entries by $\cos t$.
Then $S_{\pi/2} \circ S_{\pi/2}$ multiplies them by $0$ while $S_\pi$ multiplies them by $-1$, so clause 2 fails.
When $\mathcal{H}$ is finite-dimensional, $T_t = e^{t\mathcal{L}}$ for a generator $\mathcal{L}$, and the Gorini–Kossakowski–Sudarshan–Lindblad theorem gives the possible forms of $\mathcal{L}$.

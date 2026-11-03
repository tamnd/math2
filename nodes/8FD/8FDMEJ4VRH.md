---
tag: 8FDMEJ4VRH
kind: statement
role: theorem
name: Superposition theorem
msc: [94C05]
uses: [9B0V41V2F8, 0GT4WWGWH2, 0F2VBPXNP9]
about: [9B0V41V2F8]
sources:
  - url: https://en.wikipedia.org/wiki/Superposition_principle
---

## Statement

Consider a circuit made of linear resistors and of independent voltage and current sources with values $s_1, \dots, s_m \in \R$.
Assume that, for every choice of the source values, [[Kirchhoff's circuit laws|9B0V41V2F8]] together with the element laws have exactly one solution.
Then every branch current and every branch voltage is a linear function of $(s_1, \dots, s_m)$.
For each $k$, let circuit $k$ be the circuit in which source $k$ keeps the value $s_k$ and every other source is set to zero.
In particular, each branch current or voltage of the full circuit equals the sum over $k$ of its values in circuit $k$.

## Remarks

Kirchhoff's laws and Ohm's law form a [[system of linear equations|0GT4WWGWH2]] $M u = B s$ for the vector $u$ of branch currents and voltages.
The matrices $M$ and $B$ do not depend on $s$.
Unique solvability for all $s$ means that $M$ has a left inverse $M^{+}$.
Then $u = M^{+} B s$ is linear in $s$.
Setting a voltage source to zero replaces it by a short circuit, and setting a current source to zero replaces it by an open circuit.
For two voltage sources $E_1, E_2$ in series with a resistor $r$, the current is $(E_1 + E_2)/r$, the sum of $E_1 / r$ and $E_2 / r$.
The theorem fails for nonlinear elements: for a diode the current in response to two sources is not the sum of the responses.
Power is quadratic in the sources, so powers do not superpose.
The same idea for linear differential equations is the [[superposition principle|0F2VBPXNP9]].

## Explanations

### L1 human

If a circuit is built only from linear parts, the effect of several sources together is the sum of the effects of each source alone.
To analyse a circuit with three batteries, you can solve three easier circuits with one battery each and add the answers.

### L2 human

The superposition theorem is the linearity of the solution map of the circuit equations.
It is the basis of [[Thévenin's theorem|FD73GQDXYR]] and of [[Norton's theorem|Y24JQJPVX3]], where the external load is treated as one more source.
For circuits with capacitors and inductors in sinusoidal steady state, the same statement holds with complex impedances, for sources of one common frequency.

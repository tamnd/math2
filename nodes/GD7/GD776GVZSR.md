---
tag: GD776GVZSR
kind: statement
role: fact
name: d'Alembert's principle
msc: [70F20, 70H30, 49S05]
uses: [PS0VV149ET]
about: [PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/D%27Alembert%27s_principle
same_as:
  wikidata: Q753007
  wikipedia: D'Alembert's principle
---

## Statement

Consider $N$ particles with masses $m_i > 0$, positions $r_i(t) \in \R^3$ and accelerations $a_i = \ddot r_i$, for $i = 1, \dots, N$.
Let $F_i$ be the applied force on particle $i$.
Let the particles be subject to ideal constraints, that is, constraints whose reaction forces do no work on any virtual displacement.
A virtual displacement at time $t$ is a family $(\delta r_1, \dots, \delta r_N)$ of vectors tangent to the constraints at fixed time $t$.
Then the motion satisfies
$$\sum_{i=1}^{N} (F_i - m_i a_i) \cdot \delta r_i = 0$$
for every virtual displacement $(\delta r_1, \dots, \delta r_N)$.

## Remarks

By Newton's second law, $m_i a_i = F_i + R_i$, where $R_i$ is the constraint force on particle $i$.
So the sum equals $-\sum_i R_i \cdot \delta r_i$, which is zero exactly because the constraints are ideal.
The gain is that the unknown constraint forces disappear from the equations.
For a holonomic system with generalised coordinates $q^1, \dots, q^n$, the virtual displacements are $\delta r_i = \sum_k \frac{\partial r_i}{\partial q^k} \delta q^k$ with arbitrary $\delta q^k$.
Inserting them gives Lagrange's equations $\frac{d}{dt}\frac{\partial T}{\partial \dot q^k} - \frac{\partial T}{\partial q^k} = Q_k$, with $T$ the kinetic energy and $Q_k = \sum_i F_i \cdot \frac{\partial r_i}{\partial q^k}$ the generalised forces.
If the applied forces come from a potential $V$, these are the [[Euler–Lagrange equations|PS0VV149ET]] of $L = T - V$.
Example: take a bead of mass $m$ on a fixed smooth horizontal wire along the $x$-axis, under gravity.
The virtual displacements are $(\delta x, 0, 0)$, and the principle gives $m\ddot x = 0$.
The vertical reaction force never enters.
Without the ideal hypothesis the principle fails: sliding friction does work on virtual displacements along the wire.

## Explanations

### L1 human

A constrained system, like a bead on a wire or a pendulum on a rod, feels forces from its constraints.
These forces are hard to know in advance.
Suppose the constraints do no work in the allowed directions.
D'Alembert's principle says that then one may test Newton's law only in the allowed directions, and the constraint forces drop out.

### L2 human

D'Alembert's principle is the bridge from Newton's laws to Lagrangian mechanics.
It extends the principle of virtual work from statics to dynamics by treating $-m_i a_i$ as an extra force, the inertial force.
Integrating it in time over variations with fixed endpoints gives [[Hamilton's principle|FAQ9CH2Z76]] for holonomic systems with a potential.
It also holds for nonholonomic constraints linear in the velocities, where it leads to the equations with multipliers.

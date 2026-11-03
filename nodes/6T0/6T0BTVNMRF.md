---
tag: 6T0BTVNMRF
kind: statement
role: theorem
name: Virial theorem
msc: [70F10, 70A05]
uses: [KNBP19FG6K, 4NMMPYCK2C, 5T5GAKQD3S, 0NHGY0N0JB]
about: [C9YCMAPKMT, DF7DKHTQ7A]
sources:
  - url: https://en.wikipedia.org/wiki/Virial_theorem
same_as:
  wikidata: Q620602
  wikipedia: Virial theorem
---

## Statement

Let $N$ point particles have masses $m_i > 0$ and positions $x_i(t) \in \R^3$ for $t \ge 0$, and let their motion obey [[Newton's second law|KNBP19FG6K]] with net forces $F_i(t)$.
Suppose that the positions and velocities stay bounded for $t \ge 0$.
For a function $f$ of $t$, write $\langle f \rangle = \lim_{\tau \to \infty} \frac{1}{\tau}\int_0^\tau f(t)\, dt$ when the limit exists.
Let $T = \sum_i \frac12 m_i \abs{\dot x_i}^2$ be the [[kinetic energy|4NMMPYCK2C]].

1. If one of $\langle T \rangle$ and $\langle \sum_i F_i \cdot x_i \rangle$ exists, then so does the other, and $2 \langle T \rangle = -\big\langle \sum_{i=1}^{N} F_i \cdot x_i \big\rangle$.
2. Let $U \subseteq \R^{3N}$ be an open set that contains the motion, with $\lambda U = U$ for all $\lambda > 0$.
   Suppose moreover that $F_i = -\nabla_{x_i} V$ for a [[potential energy|5T5GAKQD3S]] $V \colon U \to \R$ of class $C^1$.
   Suppose that $V(\lambda x) = \lambda^k V(x)$ for all $\lambda > 0$ and $x \in U$.
   Then $2 \langle T \rangle = k \langle V \rangle$, in the same sense as in part 1.

## Remarks

Let $G(t) = \sum_i m_i \dot x_i \cdot x_i$.
Then $\dot G = 2T + \sum_i F_i \cdot x_i$, and $\frac1\tau \int_0^\tau \dot G\, dt = (G(\tau) - G(0))/\tau \to 0$, since $G$ is bounded; this gives part 1 by the [[fundamental theorem of calculus|0NHGY0N0JB]].
For part 2, Euler's identity for homogeneous functions gives $\sum_i x_i \cdot \nabla_{x_i} V = k V$, so $\sum_i F_i \cdot x_i = -kV$.
Example: for the Kepler problem, $k = -1$ and $2\langle T \rangle = -\langle V \rangle$; for a harmonic oscillator, $k = 2$ and $\langle T \rangle = \langle V \rangle$.
Boundedness is needed: for a free particle $x(t) = t v$ with $v \ne 0$, one has $F = 0$ but $\langle T \rangle = \frac12 m \abs{v}^2 \ne 0$.

## Explanations

### L1 human

For a system that stays in a bounded region forever, such as a planet on its orbit, the average energy of motion is tied to the average of the forces.
For gravity, the average kinetic energy is exactly half the average of minus the potential energy.

### L2 human

The theorem relates averages without solving the equations of motion, which makes it useful for many-body systems.
Astronomers use it to estimate the masses of star clusters and galaxies from the speeds of their members.
For bound Kepler orbits it combines with energy conservation to give $\langle T \rangle = -E$ and $\langle V \rangle = 2E$, where $E$ is the energy.

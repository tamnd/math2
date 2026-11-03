---
tag: FZ6XTJ3FT9
kind: example
name: Brusselator
msc: ["92E20", 34C23, 37N25]
illustrates: [F5H8GW1XYS]
uses: [KCGE92DJ1W, 0N8NGKDZDZ, F5H8GW1XYS, 0AAQ73WRFB, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Brusselator
same_as:
  wikidata: Q906505
  wikipedia: Brusselator
---

## Example

The *Brusselator* is the [[reaction network|KCGE92DJ1W]]
$$A \to X, \qquad 2X + Y \to 3X, \qquad B + X \to Y + D, \qquad X \to E.$$
The concentrations of $A$ and $B$ are held constant at values $a, b > 0$, and $D, E$ are products that do not react further.
With all rate constants equal to $1$, mass-action kinetics gives for the concentrations $x, y$ of $X, Y$
$$\dot x = a + x^2 y - (b + 1) x, \qquad \dot y = b x - x^2 y.$$
The only [[equilibrium|0N8NGKDZDZ]] is $(x, y) = (a, b/a)$.
Indeed $x = 0$ gives $\dot x = a \ne 0$, so $x \ne 0$ and $\dot y = 0$ forces $xy = b$, and then $\dot x = a - x = 0$ gives $x = a$.
The Jacobian matrix there is
$$J = \begin{pmatrix} b - 1 & a^2 \\ -b & -a^2 \end{pmatrix}, \qquad \det J = a^2 > 0, \qquad \tr J = b - 1 - a^2.$$
So the [[eigenvalues|0BQAA2BK3Q]] of $J$ have negative real parts when $b < 1 + a^2$ and positive real parts when $b > 1 + a^2$.
At $b = 1 + a^2$ they are $\pm i a$, a pair of nonzero imaginary eigenvalues crossing the imaginary axis as $b$ grows: this is a [[Hopf bifurcation|F5H8GW1XYS]].
For $b > 1 + a^2$ the system has a stable [[limit cycle|0AAQ73WRFB]], and the concentrations oscillate forever.

## Explanations

### L1 human

The Brusselator is a toy chemical reaction made to show that chemistry can oscillate.
The step $2X + Y \to 3X$ is autocatalytic: $X$ helps make more of itself.
When the supply $b$ is small, the concentrations settle to a steady state.
When $b$ passes $1 + a^2$, the steady state becomes unstable and the system starts to cycle, like a chemical clock.

---
tag: QPYEYVNJ1S
kind: definition
name: Electric charge
msc: [78A30, 78A25]
defines: 6XPSV47R56
uses: [0698M7C7AX, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Electric_charge
---

## Definition

A *system of point charges* in $\R^3$ is a finite list of distinct points $x_1, \dots, x_n \in \R^3$ together with real numbers $q_1, \dots, q_n$.
The number $q_i$ is the *charge* at $x_i$, and $Q = q_1 + \cdots + q_n$ is the *total charge*.
A *continuous charge distribution* is an integrable function $\rho \colon \R^3 \to \R$, the *charge density*.
The charge in a bounded region $\Omega \subseteq \R^3$ is the [[triple integral|0698M7C7AX]]
$$Q(\Omega) = \int_\Omega \rho(y) \, dy,$$
and the total charge is $Q = \int_{\R^3} \rho(y) \, dy$.

## Remarks

Example: the density $\rho = c$ on the unit ball and $\rho = 0$ outside has total charge $Q = \tfrac{4}{3} \pi c$, the constant times the volume of the ball.
Non-example: the function $\rho(y) = 1$ for all $y \in \R^3$ is not a charge distribution with a total charge, since it is not integrable over $\R^3$.
A point charge $q$ at $x_0$ is often written as the density $q \, \delta(y - x_0)$, with the [[Dirac delta|0KPHENZ5S7]].
Both cases are signed measures on $\R^3$, and many texts define a charge distribution as a finite signed Borel measure.

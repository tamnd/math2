---
tag: WM78WTQG43
kind: statement
role: theorem
name: Equipartition theorem
msc: [82B05, 82B30]
uses: [G1P1A0N7NZ, CPEC2NW2KF, 0WQNRCNY3M]
about: [G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Equipartition_theorem
same_as:
  wikidata: Q255996
  wikipedia: Equipartition theorem
---

## Statement

Let $H \colon \R^n \to \R$ be a $C^1$ function on a [[phase space|CPEC2NW2KF]] with coordinates $x_1, \dots, x_n$.
Let $\beta = 1/(k_B T) > 0$, assume $Z = \int_{\R^n} e^{-\beta H} \, dx < \infty$, and let $\langle \cdot \rangle$ denote the [[expected value|0WQNRCNY3M]] under the [[canonical ensemble|G1P1A0N7NZ]] with density $e^{-\beta H} / Z$.

1. If $H(x) = a x_1^2 + H'(x_2, \dots, x_n)$ with $a > 0$, then $\langle a x_1^2 \rangle = \frac{1}{2} k_B T$.
2. Let $m, k \in \set{1, \dots, n}$. Assume $x_m \, \partial_k H \, e^{-\beta H}$ is integrable on $\R^n$. Assume that $x_m e^{-\beta H(x)} \to 0$ as $x_k \to \pm \infty$, for almost every value of the other coordinates. Then $\langle x_m \, \partial H / \partial x_k \rangle = \delta_{mk} \, k_B T$.

## Remarks

Proof idea: in part 2, integrate by parts in $x_k$, using $\partial_k H \, e^{-\beta H} = -\beta^{-1} \partial_k e^{-\beta H}$; the boundary terms vanish and $\partial_k x_m = \delta_{mk}$ remains.
Part 1 follows from the one-dimensional Gaussian integral $\int x^2 e^{-\beta a x^2} dx \big/ \int e^{-\beta a x^2} dx = 1/(2 \beta a)$.
Example: a classical harmonic oscillator $H = p^2/(2m) + \frac{1}{2} m \omega^2 q^2$ has two quadratic terms, so $\langle H \rangle = k_B T$.
A monatomic ideal gas of $N$ atoms has $3N$ quadratic momentum terms, so its mean energy is $\frac{3}{2} N k_B T$.
The theorem is classical: for a quantum oscillator with $\hbar \omega \gg k_B T$, the mean energy above the ground state is far below $k_B T$.
This explains the low heat capacity of solids at low temperature.

## Explanations

### L1 human

In thermal equilibrium, energy is shared evenly among the independent ways a system can store it quadratically.
Each such way, for example each direction of motion of a molecule, holds on average $\frac{1}{2} k_B T$.
So one can predict heat capacities by counting degrees of freedom.

### L2 human

The general form $\langle x_m \partial_k H \rangle = \delta_{mk} k_B T$ also gives the virial theorem of statistical mechanics when applied to positions.
It predicts the heat capacity $\frac{3}{2} N k_B$ of a monatomic gas and the Dulong–Petit value $3 N k_B$ for a solid of $N$ atoms modelled as oscillators.
Its failure for radiation and for solids at low temperature was a historical motivation for quantum theory.
In the quantum canonical ensemble the theorem holds only in the limit of high temperature.

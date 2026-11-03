---
tag: 9ZGVBTS931
kind: conjecture
name: Maxwell's conjecture on point charges
msc: [78A30, 31B05]
uses: [6XPSV47R56, YZ7Q9DP8RT, SAEDXNM3Y1]
about: [YZ7Q9DP8RT]
sources:
  - url: https://en.wikipedia.org/wiki/A_Treatise_on_Electricity_and_Magnetism
history:
  posed_by: "James Clerk Maxwell"
  first_stated: "1873"
---

## Statement

Let $n \ge 2$, and let $q_1, \dots, q_n$ be nonzero real numbers, point [[charges|6XPSV47R56]] fixed at distinct points $x_1, \dots, x_n \in \R^3$.
Let $E$ be their [[electric field|YZ7Q9DP8RT]] on $\R^3 \setminus \set{x_1, \dots, x_n}$.
Then the number of isolated points $x$ with $E(x) = 0$ is at most $(n - 1)^2$.

## Remarks

The zeros of $E$ are the critical points of the [[electric potential|SAEDXNM3Y1]] $\varphi$, so they are the equilibrium points of a test charge.
Maxwell stated the bound in his Treatise on Electricity and Magnetism, with a heuristic argument but no proof.
The conjecture is open in general.
It was brought to wide attention by Gabrielov, Novikov and Shapiro in 2007, who studied it with methods of real algebraic geometry.
Example: two equal charges $q$ at $(\pm 1, 0, 0)$ give a single zero of $E$, at the midpoint, and $(2 - 1)^2 = 1$.

## Explanations

### L1 human

Fix a few charged particles in space.
At some points their pushes and pulls cancel exactly, and a test charge put there would stay at rest.
Maxwell guessed that with $n$ charges there are at most $(n-1)^2$ such isolated balance points.
This simple-sounding claim has not been proved in general.

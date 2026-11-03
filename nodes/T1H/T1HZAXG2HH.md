---
tag: T1HZAXG2HH
kind: statement
role: theorem
name: Competitive exclusion principle
msc: [92D25, 92D40, 34D23]
uses: [2ZJ3H7MNGC, 0N8NGKDZDZ, 0JW6MDHAZD]
about: [2ZJ3H7MNGC]
sources:
  - url: https://en.wikipedia.org/wiki/Competitive_exclusion_principle
  - url: https://en.wikipedia.org/wiki/Competitive_Lotka%E2%80%93Volterra_equations
---

## Statement

Let $r_1, r_2, K_1, K_2 > 0$ and $\alpha_{12}, \alpha_{21} > 0$, and consider the two-species [[competitive Lotka–Volterra equations|2ZJ3H7MNGC]]
$$x' = r_1 x \left(1 - \frac{x + \alpha_{12} y}{K_1}\right), \qquad y' = r_2 y \left(1 - \frac{y + \alpha_{21} x}{K_2}\right),$$
with initial values $x(0) > 0$ and $y(0) > 0$.

1. If $K_1 > \alpha_{12} K_2$ and $K_2 < \alpha_{21} K_1$, then $(x(t), y(t)) \to (K_1, 0)$ as $t \to \infty$.
2. If $K_1 < \alpha_{12} K_2$ and $K_2 > \alpha_{21} K_1$, then $(x(t), y(t)) \to (0, K_2)$.
3. If $K_1 > \alpha_{12} K_2$ and $K_2 > \alpha_{21} K_1$, then $(x(t), y(t))$ tends to the positive [[equilibrium point|0N8NGKDZDZ]]
$$\left( \frac{K_1 - \alpha_{12} K_2}{1 - \alpha_{12} \alpha_{21}}, \ \frac{K_2 - \alpha_{21} K_1}{1 - \alpha_{12} \alpha_{21}} \right).$$
4. If $K_1 < \alpha_{12} K_2$ and $K_2 < \alpha_{21} K_1$, the positive equilibrium is a [[saddle|0JW6MDHAZD]], and every solution not on its stable manifold tends to $(K_1, 0)$ or to $(0, K_2)$.

In particular, for initial values off the stable manifold in case 4, the two species coexist in the long run only in case 3.
There each species limits its own growth more than it limits the other.

## Remarks

The proof uses the nullclines $x + \alpha_{12} y = K_1$ and $y + \alpha_{21} x = K_2$, two straight lines in the quadrant.
The four cases are the four ways in which these lines can be placed, and the direction of the vector field in the regions between them decides the limits.
A planar competitive system has no periodic orbits, which rules out other limit behaviours.
Example: with $K_1 = K_2 = 10$ and $\alpha_{12} = \alpha_{21} = 0.5$, case 3 holds and the limit is $(20/3, 20/3)$.
Take $\alpha_{12} = \alpha_{21} = 1$, two species that use the resources in the same way.
Then the species with the larger carrying capacity wins, by case 1 or 2.
When moreover $K_1 = K_2$, the equilibria form a line and no species is excluded, so the strict inequalities are needed.

## Explanations

### L1 human

The competitive exclusion principle says that two species that compete for exactly the same resources cannot live together for ever: the better competitor wins.
Coexistence is possible only when the species differ enough, so that each one hurts itself more than it hurts the other.
Georgii Gause tested the idea with two species of Paramecium in the laboratory.

### L2 human

In the Lotka–Volterra model the principle becomes a classification of the phase portraits by the four inequalities above.
Case 3 is mutual invasibility: each species can grow when it is rare and the other one sits at its carrying capacity.
Case 4 is bistability, where the winner depends on the starting point.
The ecological principle is broader than this model, but the model shows its main mechanism in the simplest setting.

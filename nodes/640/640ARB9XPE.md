---
tag: 640ARB9XPE
kind: definition
name: Correlated equilibrium
msc: [91A10, 91A28]
defines: F4GH3T905G
uses: [5MZTZRC3CZ, 0DVDCMA2DK, P01KKHB155, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Correlated_equilibrium
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a finite [[normal-form game|5MZTZRC3CZ]] with $S = S_1 \times \cdots \times S_n$.
A [[probability distribution|0DVDCMA2DK]] $p$ on $S$ is a *correlated equilibrium* if, for every player $i$ and all $s_i, t_i \in S_i$,
$$\sum_{s_{-i} \in S_{-i}} p(s_i, s_{-i}) \big( u_i(s_i, s_{-i}) - u_i(t_i, s_{-i}) \big) \ge 0.$$
Here $S_{-i}$ is the product of the $S_j$ with $j \ne i$.

## Remarks

The inequality says that a player told to play $s_i$ does not gain on average by playing $t_i$ instead.
The conditions are linear in $p$, so the correlated equilibria form a convex polytope, and linear programming finds one.
If $\sigma$ is a [[Nash equilibrium|745WYP9YJ0]] in [[mixed strategies|P01KKHB155]], the product distribution $p(s) = \prod_i \sigma_i(s_i)$ is a correlated equilibrium.
Example: in the game of chicken with strategies Swerve and Straight, put $p = 1/2$ on each of (Swerve, Straight) and (Straight, Swerve).
A player told Swerve knows the other goes Straight, and swerving is her best reply; a player told Straight knows the other swerves, and going straight is best.
So both inequalities hold for each player.
Non-example: in the same game put $p = 1$ on (Swerve, Swerve).
A player told Swerve gains by going Straight, so the inequality fails.

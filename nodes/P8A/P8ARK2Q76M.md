---
tag: P8ARK2Q76M
kind: statement
role: theorem
name: Folk theorem of evolutionary game theory
msc: [91A22, 37N25]
uses: [42AC07NXK0, 745WYP9YJ0, P01KKHB155, 0N8NGKDZDZ, 0F2SYCKDT2, 0NB689782W, 9ECGX1RGGT, DECWPTFMJ6]
about: [42AC07NXK0, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Replicator_equation
---

## Statement

Let $A$ be a real $n \times n$ matrix, the payoff matrix of a symmetric two-player game, and consider the [[replicator equation|42AC07NXK0]] $\dot x_i = x_i ((A x)_i - x^T A x)$ on the simplex $\Delta_n$.
Call $p \in \Delta_n$ a *Nash equilibrium* if $(p, p)$ is a symmetric [[Nash equilibrium|745WYP9YJ0]], that is, $(A p)_i \le p^T A p$ for all $i$.
Then:

1. every Nash equilibrium is an [[equilibrium point|0N8NGKDZDZ]] (rest point) of the replicator equation;
2. if $p$ is the limit of a solution $x(t)$ with $x(0)$ in the interior of $\Delta_n$, then $p$ is a Nash equilibrium;
3. every [[Lyapunov stable|0F2SYCKDT2]] rest point is a Nash equilibrium;
4. every strict Nash equilibrium is [[asymptotically stable|0NB689782W]].

## Remarks

For 1: if $p$ is a Nash equilibrium, then $(A p)_i = p^T A p$ for every $i$ with $p_i > 0$, so every right-hand side vanishes.
For 2 and 3: if a rest point $p$ is not Nash, some strategy $i$ has $(A p)_i > p^T A p$, and then $p_i = 0$.
Near $p$ the share $x_i$ grows at an exponential rate whenever it is positive, which prevents nearby interior solutions from converging to $p$ or staying close to it.
For 4: a strict Nash equilibrium is a pure strategy, and every other strategy earns strictly less near it, so the other shares decay.

More is true: every [[evolutionarily stable strategy|9ECGX1RGGT]] is asymptotically stable for the replicator equation.
The converses fail: a rest point need not be Nash, since every vertex of $\Delta_n$ is a rest point.
In rock–paper–scissors with win $1$, loss $-1$ and tie $0$, the uniform strategy is a Nash equilibrium that is stable but not asymptotically stable, since interior solutions cycle around it.

## Explanations

### L1 human

The theorem connects two views of strategic behaviour.
In the first, rational players choose best responses, which leads to Nash equilibria.
In the second, unthinking populations just copy what does well, which is modelled by the replicator equation.
The theorem says the two views mostly agree: wherever the population dynamics settles in a stable way, the result is a Nash equilibrium.

### L2 human

The name recalls the [[folk theorem|DECWPTFMJ6]] of repeated games, but the content is unrelated.
The four parts give a dictionary between game-theoretic and dynamic notions: Nash equilibria and rest points, strict equilibria and asymptotic stability.
The dictionary is not exact, which is why one studies further refinements such as evolutionarily stable strategies.
Similar results hold for many other evolutionary dynamics that favour strategies with higher payoffs.

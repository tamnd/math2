---
tag: 66YSZP2ZQH
kind: definition
name: Carrying capacity
msc: [92D25, 92D40]
defines: X23CRWHRCH
uses: [1YEMFQ1H32, 0N8NGKDZDZ, 0NB689782W, 0CC4VC7KR3]
sources:
  - url: https://en.wikipedia.org/wiki/Carrying_capacity
---

## Definition

Consider a single-species [[population model|1YEMFQ1H32]] of the form $N'(t) = N(t) \, g(N(t))$, where $N \ge 0$ is the population size and $g \colon [0, \infty) \to \R$ is a continuous per capita growth rate.
A number $K > 0$ is the *carrying capacity* of the model if:

1. $g(K) = 0$, so that $K$ is an [[equilibrium point|0N8NGKDZDZ]];
2. $g(N) > 0$ for $N$ in an interval $(K - \delta, K)$ and $g(N) < 0$ for $N > K$, for some $\delta > 0$.

Clause 2 makes $K$ an [[asymptotically stable|0NB689782W]] equilibrium, and it means that the population declines whenever it is above $K$.

## Remarks

Example: for the [[logistic equation|0CC4VC7KR3]] $N' = r N (1 - N/K)$ with $r, K > 0$, we have $g(N) = r(1 - N/K)$, so $g(K) = 0$, $g > 0$ on $(0, K)$ and $g < 0$ on $(K, \infty)$; the carrying capacity is $K$.
Non-example: for the Malthusian model $N' = rN$ with $r > 0$, $g(N) = r$ never vanishes, so there is no carrying capacity.
In the ecological literature the term is also used in a looser sense, for the maximal population that the resources of a habitat can support.

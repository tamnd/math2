---
tag: D5VAHN51HT
kind: definition
name: Competitive Lotka–Volterra equations
msc: [92D25, 92D40, 34C60]
defines: 2ZJ3H7MNGC
uses: [4SFBZ8FJF1, X23CRWHRCH, 0CC4VC7KR3]
sources:
  - url: https://en.wikipedia.org/wiki/Competitive_Lotka%E2%80%93Volterra_equations
---

## Definition

Let $n \ge 2$ be a number of species.
For each $i$, let $r_i > 0$ be the intrinsic growth rate and $K_i > 0$ the [[carrying capacity|X23CRWHRCH]] of species $i$.
For $i \ne j$, let $\alpha_{ij} \ge 0$ be the competition coefficient of species $j$ on species $i$, and put $\alpha_{ii} = 1$.
It measures the effect of one individual of species $j$ on species $i$, in individuals of species $i$.
The *competitive Lotka–Volterra equations* are the system
$$x_i' = r_i \, x_i \left( 1 - \frac{1}{K_i} \sum_{j=1}^{n} \alpha_{ij} x_j \right), \qquad i = 1, \ldots, n,$$
for $x = (x_1, \ldots, x_n) \in \R_{\ge 0}^n$.

## Remarks

It is the [[generalized Lotka–Volterra equation|4SFBZ8FJF1]] with growth rates $r_i$ and interaction coefficients $a_{ij} = -r_i \alpha_{ij} / K_i \le 0$.
Example: for $n = 2$, the system $x' = x(1 - (x + 0.5 y)/10)$, $y' = y(1 - (y + 0.5 x)/10)$ has $r_i = 1$, $K_i = 10$ and $\alpha_{12} = \alpha_{21} = 0.5$; its positive equilibrium is $(20/3, 20/3)$, since $20/3 + 0.5 \cdot 20/3 = 10$.
In the absence of the other species, each $x_i$ follows the [[logistic equation|0CC4VC7KR3]] with carrying capacity $K_i$.
Non-example: the predator–prey system $x' = x(1 - y)$, $y' = y(x - 1)$ is not competitive, because the predator gains from the prey, so the corresponding coefficient is positive.

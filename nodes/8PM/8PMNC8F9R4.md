---
tag: 8PMNC8F9R4
kind: statement
role: proposition
name: Maximum sustainable yield
msc: [92D25, 91B76, 34C60]
uses: [0CC4VC7KR3, X23CRWHRCH, 0N8NGKDZDZ, 0NB689782W]
about: [0CC4VC7KR3, X23CRWHRCH]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_sustainable_yield
same_as:
  wikidata: Q3425223
  wikipedia: Maximum sustainable yield
---

## Statement

Let $r > 0$ and $K > 0$, and let $h \ge 0$ be a constant harvest rate.
Consider the harvested [[logistic equation|0CC4VC7KR3]]
$$N' = r N \left(1 - \frac{N}{K}\right) - h, \qquad N \ge 0.$$

1. If $h < rK/4$, the equation has two positive [[equilibrium points|0N8NGKDZDZ]] $N_- < K/2 < N_+$; the larger one $N_+$ is [[asymptotically stable|0NB689782W]] and the smaller one $N_-$ is unstable.
2. If $h = rK/4$, the only equilibrium is $N = K/2$, and it is not asymptotically stable.
3. If $h > rK/4$, there is no equilibrium, and every solution reaches $N = 0$ in finite time.

So a stable positive equilibrium exists exactly when $h < rK/4$.
The bound $h_{\mathrm{MSY}} = rK/4$ of these harvest rates is the *maximum sustainable yield*, and it is the growth rate at the population size $K/2$.

## Remarks

The equilibria solve $r N (1 - N/K) = h$.
The left side is a downward parabola in $N$ with its maximum $rK/4$ at $N = K/2$, which gives the three cases.
Between the two roots the right side of the equation is positive, and outside them it is negative, which gives the stability claims.
Example: with $r = 1$ and $K = 1000$, the maximum sustainable yield is $250$ per unit of time; with $h = 210$ the equilibria are $N_- = 300$ and $N_+ = 700$.
If the harvest is proportional to the stock, $h = E N$ with an effort $E < r$, the stable equilibrium is $K(1 - E/r)$ and the yield $E K (1 - E/r)$ is again largest, equal to $rK/4$, when $E = r/2$.

## Explanations

### L1 human

A fishery takes fish out of a lake, and the fish grow back.
If you take too many, the stock collapses; if you take very few, you catch less than the lake could give.
The logistic model says that the stock grows fastest at half of the [[carrying capacity|X23CRWHRCH]], so the largest catch that can go on forever is the growth at that size.

### L2 human

The result is a saddle-node bifurcation in the parameter $h$: as $h$ rises to $rK/4$, the stable and unstable equilibria merge and vanish.
Fishing exactly at the maximum is dangerous, because the equilibrium $K/2$ is then only semi-stable and any shock below it leads to collapse.
For this reason, and because $r$ and $K$ are uncertain, management rules aim at harvests below $h_{\mathrm{MSY}}$.
The same reasoning works for any growth law $N' = N g(N)$: the sustainable yield is the maximum of $N g(N)$.

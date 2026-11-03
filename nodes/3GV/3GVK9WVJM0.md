---
tag: 3GVK9WVJM0
kind: statement
role: proposition
name: Paradox of enrichment
msc: [92D25, 92D40, 34C23]
uses: [KRBTBHGC5K, X23CRWHRCH, 0N8NGKDZDZ, 0NB689782W, F5H8GW1XYS, 0AAQ73WRFB]
about: [KRBTBHGC5K, X23CRWHRCH]
sources:
  - url: https://en.wikipedia.org/wiki/Paradox_of_enrichment
same_as:
  wikidata: Q7134450
  wikipedia: Paradox of enrichment
---

## Statement

Let $r, K, a, h, e, m > 0$ with $e > m h$.
Consider the Rosenzweig–MacArthur predator–prey model with a type II [[Holling functional response|KRBTBHGC5K]],
$$N' = r N \left(1 - \frac{N}{K}\right) - \frac{a N P}{1 + a h N}, \qquad P' = \frac{e \, a N P}{1 + a h N} - m P,$$
for the prey density $N \ge 0$ and the predator density $P \ge 0$.
Put $N^* = \dfrac{m}{a (e - m h)}$ and assume $N^* < K$, so that there is a positive [[equilibrium point|0N8NGKDZDZ]] $(N^*, P^*)$.

1. If $K < 2 N^* + \dfrac{1}{a h}$, the positive equilibrium is [[asymptotically stable|0NB689782W]].
2. If $K > 2 N^* + \dfrac{1}{a h}$, the positive equilibrium is unstable, and the system has a stable [[limit cycle|0AAQ73WRFB]].

So raising the [[carrying capacity|X23CRWHRCH]] $K$ of the prey, with the other parameters fixed, turns a stable coexistence into oscillations.
The stability is lost at $K_c = 2 N^* + 1/(a h)$ through a [[Hopf bifurcation|F5H8GW1XYS]].

## Remarks

At the equilibrium the predator equation forces $N = N^*$, which does not depend on $K$.
The Jacobian matrix there has a zero entry in place $(2, 2)$ and a positive determinant, so stability is decided by the sign of the entry in place $(1, 1)$.
This entry equals $\dfrac{r N^* (a h K - 1 - 2 a h N^*)}{K (1 + a h N^*)}$, which is negative exactly in case 1.
Geometrically, the prey nullcline is a hump with its top at $N = (K - 1/(ah))/2$.
The equilibrium is stable when the vertical predator nullcline $N = N^*$ crosses the hump to the right of the top.
As $K$ grows the cycles get larger and come close to $N = 0$ and $P = 0$, so in a real population with random effects enrichment can lead to extinction.

## Explanations

### L1 human

One would think that giving more food to the prey makes an ecosystem healthier.
In this model it does the opposite: with too much food, prey and predators swing in large cycles and can come close to extinction.
Michael Rosenzweig named this effect the paradox of enrichment.

### L2 human

The result is a standard exercise in linear stability analysis and Hopf bifurcation of planar systems.
It shows that the saturating type II response is destabilising, since it lets the prey escape control at high densities.
Whether real ecosystems show the paradox is debated, and many model changes, such as prey that are inedible or a type III response, can remove it.

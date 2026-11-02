---
tag: 8R4H8GW1CD
kind: example
name: Ricker model
msc: [92D25, 39A60, 39A33]
instance_of: [7C7FBZGERM]
sources:
  - url: https://en.wikipedia.org/wiki/Ricker_model
same_as:
  wikidata: Q7331913
  wikipedia: Ricker model
---

## Example

Let $r > 0$ and $K > 0$ be constants.
The *Ricker model* is the [[nonlinear difference equation|7C7FBZGERM]]
$$N_{t+1} = f(N_t), \qquad f(N) = N\, e^{r (1 - N/K)},$$
for a population size $N_t \ge 0$.
Its [[equilibria|D62PEKHRV5]] are the solutions of $f(N) = N$, namely $N = 0$ and $N = K$.
The derivative is $f'(N) = e^{r(1 - N/K)} (1 - r N / K)$, so $f'(0) = e^r > 1$ and $f'(K) = 1 - r$.
Hence the equilibrium $0$ is unstable, and the equilibrium $K$ is asymptotically [[stable|CHEQ235HW9]] when $\abs{1 - r} < 1$, that is, when $0 < r < 2$.
At $r = 2$ one has $f'(K) = -1$, and as $r$ increases past $2$ the solutions go through a [[period-doubling cascade|NQDTTZ59X8]] towards chaotic behaviour.

## Explanations

### L1 human

The Ricker model describes a population, such as a fish stock, that reproduces once per season.
When the population is far below $K$, it grows by about the factor $e^r$; above $K$, the exponential factor is less than $1$ and the population shrinks.
For a small growth rate $r$, the population settles at $K$.
For larger $r$, it overshoots and undershoots, first in a regular cycle of period $2$, then $4$, and finally erratically.

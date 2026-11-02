---
tag: CSRSDP9PXJ
kind: example
name: Beverton–Holt model
msc: [92D25, 39A60]
instance_of: [D4Q8VM7826]
sources:
  - url: https://en.wikipedia.org/wiki/Beverton%E2%80%93Holt_model
same_as:
  wikidata: Q4899640
  wikipedia: Beverton–Holt model
---

## Example

Let $R_0 > 1$ and $M > 0$ be constants, and let $K = (R_0 - 1) M$.
The *Beverton–Holt model* is the recurrence
$$n_{t+1} = \frac{R_0\, n_t}{1 + n_t / M} \qquad (t \ge 0)$$
for a population size $n_t \ge 0$.
It is a [[Riccati difference equation|D4Q8VM7826]] with $a = R_0$, $b = 0$, $c = 1/M$, $d = 1$, so $c \ne 0$ and $ad - bc = R_0 \ne 0$.
For $n_0 > 0$, the solution is
$$n_t = \frac{K\, n_0}{n_0 + (K - n_0)\, R_0^{-t}}.$$
Check: $z_t = 1/n_t$ satisfies the linear recurrence $z_{t+1} = z_t / R_0 + 1/(R_0 M)$, whose solution is $z_t = R_0^{-t} z_0 + (1 - R_0^{-t})/K$; inverting gives the formula.
Since $R_0^{-t} \to 0$, every solution with $n_0 > 0$ tends to the [[equilibrium|D62PEKHRV5]] $K$, the carrying capacity.

## Explanations

### L1 human

This is a discrete-time model of a population with limited resources, used in fisheries.
When the population is small, it grows by the factor $R_0$ each generation.
As it grows, crowding reduces the growth, and the population levels off at the carrying capacity $K$.
Unlike many nonlinear models, it has an exact formula for its solution, because taking reciprocals makes it linear.

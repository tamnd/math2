---
tag: Z9EXV19CK2
kind: statement
role: theorem
name: Aizenman–Higuchi theorem
msc: [82B20, 82B26, 60K35]
uses: [R0KGM32QN6, DG9F3W6MZM]
about: [R0KGM32QN6, DG9F3W6MZM]
sources:
  - url: https://en.wikipedia.org/wiki/Ising_model
---

## Statement

Consider the [[Ising model|R0KGM32QN6]] on $\Z^2$ with nearest-neighbour coupling $J > 0$ and no external field, at inverse temperature $\beta$.
Let $\mu^+_\beta$ and $\mu^-_\beta$ be the infinite-volume [[Gibbs measures|DG9F3W6MZM]] obtained as limits of finite boxes with all boundary spins $+1$, respectively $-1$.
Then every Gibbs measure $\mu$ of the model at inverse temperature $\beta$ is a convex combination
$$\mu = \lambda \mu^+_\beta + (1 - \lambda) \mu^-_\beta \qquad \text{for some } \lambda \in [0, 1].$$

## Remarks

For $\beta \le \beta_c$ the two measures coincide and the Gibbs measure is unique, so the content is in the low-temperature phase $\beta > \beta_c$.
In particular, every Gibbs measure of the two-dimensional model is translation invariant.
Michael Aizenman (1980) and Yasunari Higuchi (1981) proved the theorem independently.
Both proofs use percolation of plus and minus spins and the topology of the plane, which together rule out a stable interface in two dimensions.
The dimension is necessary.
On $\Z^3$, Dobrushin showed in 1972 that at low temperature there are Gibbs measures with a stable flat interface between a plus and a minus region.
These measures are not translation invariant, so they are not of this form.

## Explanations

### L1 human

At low temperature a two-dimensional Ising magnet has two pure states, mostly plus and mostly minus.
The theorem says there is nothing else: every equilibrium state is just a random choice between these two.
In particular, a state that is plus on one side and minus on the other cannot be stable in the plane, because the interface between them wanders too much.

### L2 human

The result gives a complete description of the Gibbs measures of the two-dimensional Ising model, which is rare for a model with a phase transition.
It contrasts with three dimensions, where Dobrushin states with rigid interfaces exist at low temperature.
A later proof by Coquille and Velenik gives a shorter argument, and Georgii and Higuchi extended the percolation approach.
The theorem is a good example of how planar topology helps in two-dimensional statistical mechanics.

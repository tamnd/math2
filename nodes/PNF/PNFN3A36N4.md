---
tag: PNFN3A36N4
kind: statement
role: theorem
name: Peierls argument
msc: [82B20, 82B26, 60K35]
uses: [R0KGM32QN6, DG9F3W6MZM]
about: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Ising_model
---

## Statement

Let $d \ge 2$, and consider the [[Ising model|R0KGM32QN6]] on $\Z^d$ with nearest-neighbour coupling $J > 0$ and no external field.
For a finite box $\Lambda \subset \Z^d$ and $\beta \ge 0$, let $\mu^+_{\Lambda, \beta}$ be the Ising measure on $\set{-1, +1}^\Lambda$ with plus boundary condition.
In it, every spin outside $\Lambda$ is fixed to $+1$.
Then there is $\beta_0 < \infty$ such that for all $\beta > \beta_0$,
$$\sup_{\Lambda \ni 0} \mu^+_{\Lambda, \beta}(\sigma_0 = -1) < \frac12,$$
where the supremum is over the boxes $\Lambda$ containing the origin.
Consequently, for $\beta > \beta_0$ the infinite-volume limits with plus and with minus boundary conditions are two different [[Gibbs measures|DG9F3W6MZM]], and the model has a phase transition.

## Remarks

Under the plus boundary condition, if $\sigma_0 = -1$ then the origin is enclosed by a contour: a closed surface of dual plaquettes separating minus spins from plus spins.
Flipping all spins inside a given contour $\gamma$ of size $\abs{\gamma}$ removes it and lowers the energy by $2J\abs{\gamma}$, so the probability that $\gamma$ is present is at most $e^{-2 \beta J \abs{\gamma}}$.
The number of contours of size $\ell$ around the origin grows at most exponentially in $\ell$, say like $C^\ell$.
So for $\beta$ large, $\mu^+_{\Lambda, \beta}(\sigma_0 = -1) \le \sum_\ell C^\ell e^{-2\beta J \ell}$, which is small uniformly in $\Lambda$.
The argument uses $d \ge 2$: on $\Z$ a contour is just two points, and its energy cost does not grow with the enclosed region.
Indeed the one-dimensional Ising model has a unique Gibbs measure at every temperature.

## Explanations

### L1 human

To flip a big island of spins against a sea of plus spins, you pay energy along the whole boundary of the island.
At low temperature such boundaries are very costly, while the number of possible boundaries only grows exponentially in their length.
The cost wins, so the origin is most likely plus when the boundary is plus, however large the box.
This shows that the system remembers its boundary: it is magnetized at low temperature.

### L2 human

Rudolf Peierls gave the idea in 1936, and R. Griffiths and R. L. Dobrushin made it rigorous in 1964 and 1965.
It is the prototype of contour methods and of Pirogov–Sinai theory for low-temperature phases.
It shows that the critical inverse temperature $\beta_c$ of the Ising model is finite in dimension at least two.
Combined with the high-temperature uniqueness from the Dobrushin criterion, it shows that $0 < \beta_c < \infty$.

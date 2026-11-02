---
tag: E0YVMBPK7A
kind: example
name: Euler–Lotka equation
msc: [45D05, 92D25]
illustrates: [EWVVH3EKMR, SNFYTC1TTA]
uses: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Lotka_equation
same_as:
  wikidata: Q5409005
  wikipedia: Euler–Lotka equation
---

## Example

Consider an age-structured population, and let $a \ge 0$ denote age.
Let $l(a)$ be the probability of surviving to age $a$, and $m(a)$ the birth rate of individuals of age $a$.
Assume $l m$ is nonnegative, integrable on $[0, \infty)$ and not almost everywhere zero.
The birth rate $B(t)$ at time $t \ge 0$ satisfies a [[renewal equation|EWVVH3EKMR]]
$$B(t) = G(t) + \int_0^t B(t - a) \, l(a) \, m(a) \, da,$$
where $G(t)$ collects the births from individuals already alive at time $0$.
This is a [[Volterra equation of convolution type|SNFYTC1TTA]] with kernel $k = l m$.

Looking for exponential solutions $B(t) = Q e^{rt}$ of the equation without the term $G$, with the integral taken over all ages $a \ge 0$, gives the *Euler–Lotka equation*
$$\int_0^\infty e^{-r a} \, l(a) \, m(a) \, da = 1.$$
Its left side is the [[Laplace transform|0V49JEZW06]] $\hat k(r)$ of the kernel, so $r$ is a root of $1 - \hat k(r) = 0$, the denominator of the Laplace transform method.

Check on an instance: let $l(a) m(a) = b \, e^{-\mu a}$ with constants $b > 0$ and $\mu \ge 0$.
For $r > -\mu$ the left side is $\int_0^\infty b \, e^{-(r + \mu) a} \, da = \frac{b}{r + \mu}$.
It equals $1$ exactly when $r = b - \mu$, the birth rate minus the death rate.

## Remarks

The left side is strictly decreasing in real $r$, where it converges, so the Euler–Lotka equation has at most one real root.
This real root is the intrinsic rate of increase of the population.
The net reproduction number is $R_0 = \int_0^\infty l(a) m(a) \, da$, the value of the left side at $r = 0$.
If $R_0 > 1$, the left side tends to $0$ as $r \to \infty$, so there is a real root and it is positive.
If $R_0 \le 1$ and a real root exists, it is not positive.

## Explanations

### L1 human

Each newborn will, over its life, produce offspring at various ages.
If the population grows like $e^{rt}$, then births long ago count less, by the factor $e^{-ra}$, compared with births today.
The Euler–Lotka equation says that, with this discount, each newborn exactly replaces itself.
Solving it gives the long-run growth rate $r$ of the population.

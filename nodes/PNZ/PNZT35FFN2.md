---
tag: PNZT35FFN2
kind: statement
role: theorem
name: Positive definiteness of the energy
msc: [31B15, 31A15]
uses: [SFSRQCM3EG, 6VR8GASZJY, DYR1QFNGNJ, DPVM34ADZV, 0RFWW56Y22]
about: [SFSRQCM3EG, 6VR8GASZJY]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Statement

Let $n \ge 2$ and let $\mu$ and $\nu$ be finite positive [[Borel measures|DYR1QFNGNJ]] on $\R^n$ with compact supports.
Use the kernel $\abs{x}^{2-n}$ when $n \ge 3$ and $\log(1/\abs{x})$ when $n = 2$, and assume that the [[energies|SFSRQCM3EG]] $I(\mu)$ and $I(\nu)$ are finite.
When $n = 2$, assume also that $\mu(\R^2) = \nu(\R^2)$.
Then the [[mutual energy|6VR8GASZJY]] $I(\mu, \nu)$ is finite and
$$I(\mu - \nu) = I(\mu) - 2 I(\mu, \nu) + I(\nu) \ge 0,$$
with equality if and only if $\mu = \nu$.

## Remarks

Proof idea for $n \ge 3$: the [[Fourier transform|DPVM34ADZV]] of $\abs{x}^{2-n}$, as a tempered distribution, is $c_n \abs{\xi}^{-2}$ with a constant $c_n > 0$.
For $\lambda = \mu - \nu$ this gives
$$I(\lambda) = c\, \int_{\R^n} \frac{\abs{\hat{\lambda}(\xi)}^2}{\abs{\xi}^2}\, d\xi$$
with a constant $c > 0$, which is nonnegative and vanishes only when $\hat\lambda = 0$, that is, $\mu = \nu$.
In the plane the logarithmic kernel has a similar representation on measures of total mass $0$, which is why the masses must agree.

The mass condition is necessary in the plane.
Let $\mu$ be the uniform probability measure on the circle $\abs{z} = R$ with $R > 1$, and $\nu = 0$.
Then $I(\mu - \nu) = I(\mu) = \log(1/R) < 0$.

For $n \ge 3$ the theorem implies the [[Cauchy–Schwarz inequality|0RFWW56Y22]] $I(\mu, \nu)^2 \le I(\mu) I(\nu)$, since $I(\mu - t\nu) = I(\mu) - 2t\, I(\mu, \nu) + t^2 I(\nu) \ge 0$ for every $t > 0$ and $I(\mu, \nu) \ge 0$; take $t = I(\mu, \nu)/I(\nu)$ when $I(\nu) > 0$.

## Explanations

### L1 human

The energy of a charge distribution with both positive and negative charges is never negative, as long as the total charge is balanced in the plane.
It is zero only when there is no charge at all.
So energy behaves like the square of a length on the space of charge distributions.

### L2 human

This is the key fact of the energy method in potential theory.
It makes $\sqrt{I(\mu - \nu)}$ a distance on measures of finite energy, and a theorem of Cartan says that positive measures of finite energy are complete for this distance when $n \ge 3$.
Uniqueness of the equilibrium measure follows: if $\mu$ and $\nu$ both minimise the energy among probability measures on a compact set, then the energy of $\frac12(\mu + \nu)$ forces $I(\mu - \nu) = 0$, so $\mu = \nu$.

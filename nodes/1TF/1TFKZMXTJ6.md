---
tag: 1TFKZMXTJ6
kind: definition
name: Press–Schechter formalism
msc: [85A40, 60G60]
defines: SZ3ZJ5MJQN
uses: [FWRHZ27J6Q, A8YJ7EKMV7, 6K40RAVSAT, 05AQE0QR0D, 7Y56QCZSZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Press%E2%80%93Schechter_formalism
---

## Definition

Let $\bar\rho$ be the mean comoving matter density.
Let the linear density contrast, extrapolated to the time $t$, be a Gaussian random field with [[matter power spectrum|FWRHZ27J6Q]] $P(k)$.
For a mass $M$, let $R$ be given by $M = \frac{4\pi}{3} \bar\rho R^3$.
Let $\sigma(M)$ be the standard deviation of the field smoothed with a spherical top hat of radius $R$.
Let $\delta_c \approx 1.686$ be the collapse threshold of the [[spherical collapse model|A8YJ7EKMV7]].
Let $F(> M)$ be the fraction of mass in collapsed halos of mass greater than $M$.
The *Press–Schechter formalism* sets
$$F(> M) = 2 \, \Pr\left(\delta_R > \delta_c\right) = \operatorname{erfc}\left( \frac{\delta_c}{\sqrt{2} \, \sigma(M)} \right).$$
Here $\delta_R$ is the smoothed field, with a [[normal distribution|05AQE0QR0D]] of mean $0$ and variance $\sigma(M)^2$.
The function erfc is the complementary [[error function|7Y56QCZSZJ]].
The resulting [[halo mass function|6K40RAVSAT]] is $n(M) = (\bar\rho / M) \abs{dF/dM}$, that is,
$$n(M) = \sqrt{\frac{2}{\pi}} \, \frac{\bar\rho}{M^2} \, \nu \, \abs{\frac{d \ln \sigma}{d \ln M}} \, e^{-\nu^2/2}, \qquad \nu = \frac{\delta_c}{\sigma(M)} .$$

## Remarks

The factor $2$ makes all mass end up in halos, since $F(> M) \to 1$ as $\sigma(M) \to \infty$.
Press and Schechter added it by hand.
The excursion set approach of Bond, Cole, Efstathiou and Kaiser (1991) derives it by treating the smoothed field as a random walk in the smoothing scale.
The time enters only through $\sigma(M)$, which grows with the linear growth factor.

Example: if $P(k) = A k^n$ with $n > -3$, then $\sigma(M) \propto M^{-(n+3)/6}$, so $\abs{d\ln\sigma/d\ln M} = (n+3)/6$.
Then $n(M)$ is a power law in $M$ times the cut-off $e^{-\nu^2/2}$, which acts above the mass where $\sigma(M) = \delta_c$.

Non-example: for a density field that is far from Gaussian, $\delta_R$ is not normally distributed, so the formula for $F(> M)$ does not apply.

Numerical simulations show that the formula predicts too few massive halos and too many small ones; fits such as the Sheth–Tormen mass function correct this.

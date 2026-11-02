---
tag: HN93ST5CBT
kind: statement
role: theorem
name: Radon inversion formula
msc: [44A12, 92C55]
uses: [VJNZJ352PC, 938SXZQS8G, DPVM34ADZV, GE020MY43M]
about: [VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Statement

Let $n \ge 2$ and let $f$ be in the [[Schwartz space|GE020MY43M]] $\mathcal{S}(\R^n)$.
Let $R$ be the [[Radon transform|VJNZJ352PC]] and $R^*$ the [[dual Radon transform|938SXZQS8G]].
For a function $g(\theta, s)$ on $S^{n-1} \times \R$, let $\Lambda g$ be defined by filtering in $s$ with the multiplier $\abs{\sigma}^{n-1}$:
$$(\Lambda g)(\theta, s) = \frac{1}{2\pi} \int_\R \abs{\sigma}^{n-1}\, \hat g(\theta, \sigma)\, e^{i s \sigma}\, d\sigma, \qquad \hat g(\theta, \sigma) = \int_\R g(\theta, s)\, e^{-i s \sigma}\, ds.$$
Then, for every $x \in \R^n$,
$$f(x) = \frac{1}{2} (2\pi)^{1-n}\, R^* (\Lambda R f)(x).$$
If $n$ is odd, $\Lambda = (-1)^{(n-1)/2} \partial_s^{n-1}$, and the formula reads
$$f(x) = \frac{(-1)^{(n-1)/2}}{2 (2\pi)^{n-1}} \int_{S^{n-1}} \left( \partial_s^{n-1} R f \right)(\theta, x \cdot \theta)\, d\theta.$$

## Remarks

The proof starts from the Fourier inversion formula $f(x) = (2\pi)^{-n} \int_{\R^n} \hat f(\xi)\, e^{i x \cdot \xi}\, d\xi$ in polar coordinates $\xi = \sigma\theta$.
Writing the integral over $\sigma \in \R$ and $\theta \in S^{n-1}$ counts each $\xi$ twice, which gives the factor $\frac12$ and the weight $\abs{\sigma}^{n-1}$.
The [[projection-slice theorem|J7VA040MC3]] replaces $\hat f(\sigma\theta)$ by the Fourier transform of $R_\theta f$, and the remaining $\theta$-integral is $R^*$.

Example: for $n = 3$ the formula is $f(x) = -\frac{1}{8\pi^2} \int_{S^2} (\partial_s^2 R f)(\theta, x \cdot \theta)\, d\theta$, so $f(x)$ depends only on the integrals of $f$ over planes close to $x$.

For even $n$ the multiplier $\abs{\sigma}^{n-1}$ is not a polynomial, $\Lambda$ involves the [[Hilbert transform|NSCEBXM7ZM]] in $s$, and the formula is not local: $f(x)$ depends on integrals over all hyperplanes.

## Explanations

### L1 human

The Radon transform of a function lists its integrals over all hyperplanes, and the formula gets the function back.
First each profile is sharpened by a filter that boosts high frequencies.
Then all sharpened profiles are smeared back over space and added up.
The result is exactly the original function.

### L2 human

The formula is the continuous model of [[filtered back-projection|SJQDDY9FMX]], the standard reconstruction algorithm of computed tomography.
The filter $\abs{\sigma}^{n-1}$ grows at high frequencies, which shows why inversion amplifies noise and why practical filters cut it off.
In odd dimensions the inversion is local, a fact used in three-dimensional imaging; in even dimensions, such as the plane, it is not.
The same formula, read with the Riesz potential, extends to wider classes of functions and to distributions.

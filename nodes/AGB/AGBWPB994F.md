---
tag: AGBWPB994F
kind: statement
role: theorem
name: Binet's formulas for the log-gamma function
msc: [33B15]
uses: [JT95B44G4G, 02QGGD5G87]
about: [JT95B44G4G]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $\operatorname{Log}\Gamma$ be the [[log-gamma function|JT95B44G4G]] and $\operatorname{Log}$ the principal [[complex logarithm|02QGGD5G87]].
For $\operatorname{Re} z > 0$ put
$$\mu(z) = \operatorname{Log}\Gamma(z) - \left(z - \tfrac12\right)\operatorname{Log} z + z - \tfrac12 \ln(2\pi).$$
Then for every $z$ with $\operatorname{Re} z > 0$:

1. (Binet's first formula) $$\mu(z) = \int_0^\infty \left(\frac12 - \frac1t + \frac{1}{e^t - 1}\right)\frac{e^{-zt}}{t}\, dt.$$
2. (Binet's second formula) $$\mu(z) = 2\int_0^\infty \frac{\arctan(t/z)}{e^{2\pi t} - 1}\, dt,$$ where $\arctan(t/z) = \frac{1}{2i}\operatorname{Log}\dfrac{1 + it/z}{1 - it/z}$ is the principal branch.

## Remarks

The integrand of the first formula is bounded near $t = 0$, since $\frac12 - \frac1t + \frac{1}{e^t - 1} = \frac{t}{12} + O(t^3)$.
The first formula comes from integrating the integral representation of the [[digamma function|HWRRXB0YXS]].
The second comes from the Abel–Plana summation formula, or from the first by a partial fraction expansion of $\frac{1}{e^t - 1}$.
The function $\mu$ is called Binet's function; it is positive and decreasing on $(0, \infty)$ and tends to $0$ as $x \to \infty$.
This limit is [[Stirling's formula for the gamma function|53750WSJ6K]] on the real axis, and expanding $\frac12 - \frac1t + \frac{1}{e^t - 1}$ in powers of $t$ gives [[Stirling's series|K29QYWB6A5]] term by term.
For example, the first term $\frac{t}{12}$ contributes $\int_0^\infty \frac{1}{12} e^{-zt}\,dt = \frac{1}{12z}$, the first correction in Stirling's series.

## Explanations

### L1 human

Stirling's formula approximates $\ln\Gamma(z)$ by a simple expression.
Binet's formulas give the exact error of this approximation as an integral.
From the integrals one can read off how small the error is and in which direction it goes.

### L2 human

Binet's first formula is a Laplace transform, so Watson's lemma turns the Taylor series of its integrand directly into the asymptotic expansion of $\mu(z)$.
The second formula is convenient for error bounds in the right half-plane, because the kernel $\frac{1}{e^{2\pi t} - 1}$ is explicit and positive.
Both show that $\mu(x) \to 0$ monotonically, which gives sharp bounds such as $0 < \mu(x) < \frac{1}{12x}$ for $x > 0$.

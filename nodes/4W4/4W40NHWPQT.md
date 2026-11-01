---
tag: 4W40NHWPQT
kind: example
name: Log-normal distribution
msc: ["60E05", "62E15"]
instance_of: [0DVDCMA2DK]
uses: [05AQE0QR0D, 0ZY9DX8FBF, 01XAHPADBA, 0WQVXP7PDB]
sources:
  - url: https://en.wikipedia.org/wiki/Log-normal_distribution
same_as:
  wikidata: Q826116
  wikipedia: Log-normal distribution
---

## Example

Let $\mu \in \R$ and $\sigma > 0$, and let $Y$ be [[normal|05AQE0QR0D]] with mean $\mu$ and variance $\sigma^2$.
The law of $X = e^Y$ is the *log-normal distribution* with parameters $\mu$ and $\sigma^2$; so $X > 0$ and $\ln X$ is normal.
Its [[density|0ZY9DX8FBF]] is
$$f(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2 \sigma^2}\right) \qquad (x > 0),$$
and $f(x) = 0$ for $x \le 0$.
Check: for $0 < a < b$, $P(a < X < b) = P(\ln a < Y < \ln b)$, and the substitution $y = \ln x$, $dy = dx / x$, turns the normal density of $Y$ into $f$.
The [[moments|01XAHPADBA]] are $E[X^n] = E[e^{nY}] = e^{n\mu + n^2 \sigma^2 / 2}$ for every real $n$, by the moment-generating function of the normal law.
So $E[X] = e^{\mu + \sigma^2/2}$ and $\operatorname{Var}(X) = (e^{\sigma^2} - 1) e^{2\mu + \sigma^2}$.
The median is $e^{\mu}$, which is smaller than the mean.

## Remarks

All moments are finite, but the [[moment-generating function|0WQVXP7PDB]] $E[e^{tX}]$ is infinite for every $t > 0$.
The log-normal law is a standard example of a distribution that is not determined by its moments: other distributions have exactly the same moments.
If $X_1$ and $X_2$ are independent and log-normal, then $X_1 X_2$ is log-normal, because $\ln X_1 + \ln X_2$ is normal.

## Explanations

### L1 human

A log-normal quantity is one whose logarithm follows a bell curve.
It arises when many independent factors multiply together, just as the normal law arises when many independent terms add.
Its graph is skewed to the right: it is always positive, has a long tail of large values, and its mean lies above its median.
Sizes of particles, incomes and stock prices in the Black–Scholes model are often modelled with it.

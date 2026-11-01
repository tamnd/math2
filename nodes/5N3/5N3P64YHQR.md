---
tag: 5N3P64YHQR
kind: example
name: Pareto distribution
msc: ["60E05", "62E15"]
instance_of: [0DVDCMA2DK]
uses: [0H8H7ZTHW2, 0ZY9DX8FBF, 01XAHPADBA, 0E99F51GVB]
sources:
  - url: https://en.wikipedia.org/wiki/Pareto_distribution
same_as:
  wikidata: Q837683
  wikipedia: Pareto distribution
---

## Example

Let $x_m > 0$ and $\alpha > 0$.
A random variable $X$ has the *Pareto distribution* with scale $x_m$ and shape $\alpha$ if
$$P(X > x) = \left(\frac{x_m}{x}\right)^{\alpha} \quad \text{for } x \ge x_m, \qquad P(X > x) = 1 \quad \text{for } x < x_m.$$
This is a valid law: the [[distribution function|0H8H7ZTHW2]] $1 - (x_m/x)^\alpha$ is continuous and increasing from $0$ at $x_m$ to the limit $1$ as $x \to \infty$.
Its [[density|0ZY9DX8FBF]] is $f(x) = \alpha x_m^{\alpha} / x^{\alpha + 1}$ for $x \ge x_m$ and $0$ otherwise.
For $k > 0$, $E[X^k] = \int_{x_m}^\infty \alpha x_m^\alpha x^{k - \alpha - 1} \, dx$ is finite if and only if $k < \alpha$, and then equals $\frac{\alpha x_m^k}{\alpha - k}$.
So the mean is $\frac{\alpha x_m}{\alpha - 1}$ for $\alpha > 1$ and infinite for $\alpha \le 1$, and the variance is $\frac{\alpha x_m^2}{(\alpha - 1)^2 (\alpha - 2)}$ for $\alpha > 2$.

## Remarks

The variable $\ln(X / x_m)$ is [[exponential|0E99F51GVB]] with rate $\alpha$, since $P(\ln(X/x_m) > s) = P(X > x_m e^s) = e^{-\alpha s}$ for $s \ge 0$.
The law is scale free in the following sense: for $y \ge x_m$, given $X > y$ the variable $X$ is Pareto with scale $y$ and the same shape $\alpha$.
It is the basic example of a heavy-tailed law, with a tail that decays like a power of $x$; only the [[moments|01XAHPADBA]] of order less than $\alpha$ are finite.

## Explanations

### L1 human

A Pareto variable is at least some minimum value, and the chance that it exceeds $x$ falls like a power $x^{-\alpha}$.
Doubling the threshold always divides the chance of exceeding it by the same factor $2^\alpha$, at every scale.
For small $\alpha$, rare huge values dominate, and the mean can even be infinite.
Vilfredo Pareto used such laws to describe the distribution of wealth, and they also model city sizes and insurance losses.

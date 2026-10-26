---
tag: ~cd613feb
kind: definition
name: Expected value
msc: [60A05]
defines: ~3c30aff0
uses: [~89528024, ~ae896b89, ~04a8fbdd, ~24cf07b9]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_value
    locator: Arbitrary real-valued random variables
---

## Definition

Let $X$ be a real [[random variable|~89528024]] on a [[probability space|~ae896b89]] $(\Omega, \mathcal{F}, P)$.
If $X \ge 0$, the expected value of $X$ is the Lebesgue integral
$$E[X] = \int_\Omega X \, dP \in [0, \infty].$$
In general, write $X = X^+ - X^-$ with $X^+ = \max(X, 0)$ and $X^- = \max(-X, 0)$. If $E[|X|] < \infty$, then $X$ is integrable and $E[X] = E[X^+] - E[X^-]$.

## Remarks

For a [[discrete random variable|~04a8fbdd]] with values $x_1, x_2, \dots$, $E[X] = \sum_i x_i \, P(X = x_i)$ when the series converges absolutely.
For a [[random variable with density|~24cf07b9]] $f$, $E[X] = \int_{-\infty}^{\infty} x f(x) \, dx$ when $\int |x| f(x) \, dx < \infty$.
Other notations are $\mathbb{E}[X]$, $\mathbb{E}X$ and $\mu_X$. The expected value depends only on the law of $X$.
If $E[X^+] = \infty$ and $E[X^-] < \infty$, one sets $E[X] = +\infty$. If both are infinite, $E[X]$ is not defined.

## Explanations

### L1 human

The expected value is the long-run average of many independent repetitions of the experiment.
For a fair die, it is $(1 + 2 + 3 + 4 + 5 + 6)/6 = 3.5$. This value never appears on the die, but it is the center of mass of the distribution.

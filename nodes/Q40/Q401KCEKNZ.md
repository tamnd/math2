---
tag: Q401KCEKNZ
kind: statement
role: theorem
name: Krein's condition
msc: [44A60, 42A65]
uses: [GCTN4BZ1ET, TBNCFXTMMW, 01XAHPADBA, RVZ831CNYW]
about: [GCTN4BZ1ET]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%27s_condition
    locator: Indeterminacy of the moment problem
same_as:
  wikidata: Q6436610
  wikipedia: Krein's condition
---

## Statement

Let $\mu$ be a measure on $\R$ of the form $d\mu(x) = f(x) \, dx$, where $f \ge 0$ is Lebesgue integrable.
Suppose that every [[moment|01XAHPADBA]] $m_n = \int x^n f(x) \, dx$ is finite.
If
$$\int_{-\infty}^{\infty} \frac{-\ln f(x)}{1 + x^2} \, dx < \infty,$$
then the [[Hamburger moment problem|TBNCFXTMMW]] for $\mu$ is [[indeterminate|GCTN4BZ1ET]]: there is a positive measure $\nu \ne \mu$ on $\R$ with the same moments.

## Remarks

The integral is well defined in $(-\infty, \infty]$, since $\ln f \le f$ where $f \ge 1$ and $f$ is integrable.
The result is a corollary of a density theorem of Krein: the integral is infinite if and only if the exponential sums $\sum_k a_k e^{i \lambda_k x}$ with $\lambda_k \ge 0$ are dense in $L^2(\mu)$.
Example: $f(x) = c \, e^{-\abs{x}^{\alpha}}$ with $0 < \alpha < 1$ and $c > 0$ has $-\ln f(x) = \abs{x}^{\alpha} - \ln c$, and $\int \abs{x}^{\alpha}/(1 + x^2) \, dx < \infty$ for $\alpha < 1$, so this density is not determined by its moments.
For $\alpha \ge 1$ the integral diverges, and in fact Carleman's condition shows that the moment problem is determinate.
The condition is sufficient for indeterminacy but not necessary.

## Explanations

### L1 human

A density whose tails are very heavy, but not so heavy that the moments are infinite, can share all its moments with another distribution.
Krein's condition measures heaviness of the tails by how slowly $-\ln f$ grows.
If $-\ln f(x)$ grows more slowly than $\abs{x}$, in the averaged sense of the integral, the moments do not determine the distribution.

### L2 human

It complements [[Carleman's condition|RVZ831CNYW]], which gives determinacy when the moments grow slowly.
The two meet at densities like $e^{-\abs{x}^{\alpha}}$: determinate for $\alpha \ge 1$ and indeterminate for $\alpha < 1$.
Versions for the Stieltjes problem on $[0, \infty)$ and converses under regularity hypotheses on $f$ are known.

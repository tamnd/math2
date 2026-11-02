---
tag: QVCKQ46TFM
kind: definition
name: Continuous q-Hermite polynomials
msc: [33D45]
defines: XFKVZJ55Q5
uses: [YS09Z1YNEK, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_q-Hermite_polynomials
---

## Definition

Let $q \in \C$ with $q^k \ne 1$ for all integers $k \ge 1$, and let $x = \cos\theta$.
For an integer $n \ge 0$, the *continuous $q$-Hermite polynomial* is
$$H_n(x \mid q) = \sum_{k=0}^{n} \binom{n}{k}_q\, e^{i(n - 2k)\theta},$$
where $\binom{n}{k}_q$ is the [[Gaussian binomial coefficient|YS09Z1YNEK]].

## Remarks

The terms for $k$ and $n - k$ have the same coefficient, so they pair to $2\binom{n}{k}_q \cos((n - 2k)\theta)$, and $H_n$ is a polynomial of degree $n$ in $x$ with leading coefficient $2^n$.
They satisfy $H_0 = 1$, $H_1 = 2x$ and the recurrence $2x\, H_n(x \mid q) = H_{n+1}(x \mid q) + (1 - q^n)\, H_{n-1}(x \mid q)$ for $n \ge 1$.
For $\abs{q} < 1$ and $\abs{t} < 1$ the generating function is $\sum_{n \ge 0} \frac{H_n(x \mid q)}{(q; q)_n} t^n = \frac{1}{(t e^{i\theta}; q)_\infty\, (t e^{-i\theta}; q)_\infty}$, with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].

Example: $n = 2$.
With $\binom{2}{1}_q = 1 + q$, $H_2 = e^{2i\theta} + (1 + q) + e^{-2i\theta} = 2\cos 2\theta + 1 + q = 4x^2 - 1 + q$.
The recurrence gives the same: $2x \cdot 2x - (1 - q) \cdot 1 = 4x^2 - 1 + q$.

Non-example: the ordinary Hermite polynomial $4x^2 - 2$ is not $H_2(x \mid q)$ for any $q$: matching constants would need $q = -1$, which is excluded since $q^2 = 1$.

For $-1 < q < 1$ they are orthogonal: $\frac{1}{2\pi} \int_0^{\pi} H_m(\cos\theta \mid q)\, H_n(\cos\theta \mid q)\, (e^{2i\theta}, e^{-2i\theta}; q)_\infty \, d\theta = \delta_{mn} \frac{(q; q)_n}{(q; q)_\infty}$.
As $q \to 1^-$, $\left(\frac{2}{1 - q}\right)^{n/2} H_n\left( x \sqrt{\tfrac{1 - q}{2}} \,\middle|\, q \right)$ tends to the [[Hermite polynomial|MGACY98E9H]] $H_n(x)$.

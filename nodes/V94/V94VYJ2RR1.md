---
tag: V94VYJ2RR1
kind: definition
name: Two-sided Laplace transform
msc: [44A10]
defines: 6J2AGD0BYY
uses: [05XT5AVJBK, 05KQ3F99BQ, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Two-sided_Laplace_transform
---

## Definition

Let $f \colon \R \to \C$ be [[integrable|DWJF7ABPR1]] on each bounded interval.
The *two-sided Laplace transform* of $f$ is the function
$$\mathcal{B}\{f\}(s) = \int_{-\infty}^{\infty} f(t) \, e^{-s t} \, dt = \lim_{T_1, T_2 \to \infty} \int_{-T_1}^{T_2} f(t) \, e^{-s t} \, dt.$$
Here $T_1$ and $T_2$ tend to $\infty$ independently.
The transform is defined at each complex $s$ for which this [[improper integral|05KQ3F99BQ]] converges.

## Remarks

Example: for $f(t) = e^{-\abs{t}}$, the part over $[0, \infty)$ is $1/(1 + s)$ for $\operatorname{Re} s > -1$, and the part over $(-\infty, 0]$ is $1/(1 - s)$ for $\operatorname{Re} s < 1$.
So $\mathcal{B}\{f\}(s) = \frac{2}{1 - s^2}$ for $-1 < \operatorname{Re} s < 1$.
Non-example: for the constant $f = 1$, the part over $[0, \infty)$ needs $\operatorname{Re} s > 0$ and the part over $(-\infty, 0]$ needs $\operatorname{Re} s < 0$, so the integral converges for no $s$.
If $f(t) = 0$ for $t < 0$, the two-sided transform is the one-sided [[Laplace transform|05XT5AVJBK]] of $f$ restricted to $[0, \infty)$.
For a random variable $X$ with density $p$, $\mathcal{B}\{p\}(-s) = \mathbb{E}[e^{s X}]$ is its moment generating function wherever it converges.

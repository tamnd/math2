---
tag: X5JYH26J3M
kind: example
name: Laplace transform of the exponential function
msc: [44A10]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Example

Let $a \in \C$ and $f(t) = e^{at}$ for $t \ge 0$, an [[exponential function|0RMVS7RXZX]].
Its [[Laplace transform|05XT5AVJBK]] is
$$\mathcal{L}\{e^{at}\}(s) = \frac{1}{s - a} \quad (\operatorname{Re} s > \operatorname{Re} a).$$
Check: for $s \ne a$ and $T > 0$,
$$\int_0^T e^{at} e^{-st}\, dt = \frac{1 - e^{-(s - a)T}}{s - a}.$$
Since $\abs{e^{-(s - a)T}} = e^{-\operatorname{Re}(s - a) T}$, this tends to $0$ as $T \to \infty$ exactly when $\operatorname{Re} s > \operatorname{Re} a$, which gives the formula.
When $\operatorname{Re} s < \operatorname{Re} a$ the term $e^{-(s-a)T}$ grows without bound.
When $\operatorname{Re} s = \operatorname{Re} a$ it stays on the unit circle without a limit (or the integrand is $1$ if $s = a$), so the integral diverges.
So the abscissa of convergence is $\operatorname{Re} a$.
The case $a = 0$ gives $\mathcal{L}\{1\}(s) = 1/s$.

## Explanations

### L1 human

The exponential $e^{at}$ is the basic building block of Laplace transform tables.
Its transform $1/(s - a)$ has a single pole at $s = a$, and the location of the pole records the growth rate of $e^{at}$.
Many other entries, such as those for sine, cosine and hyperbolic functions, follow from this one by linearity.

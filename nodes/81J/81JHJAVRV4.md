---
tag: 81JHJAVRV4
kind: example
name: Riemann–Liouville fractional integral equation
msc: [45D05, 26A33]
instance_of: [H6ZGEDM4VV, SNFYTC1TTA]
uses: [JTKCZ44NN3, 0H5SYBSED9, QHNWVSC6AQ]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Liouville_integral
---

## Example

Let $b > 0$ and $0 < \alpha < 1$.
The [[Riemann–Liouville integral|JTKCZ44NN3]] of order $\alpha$ of a continuous function $\varphi$ on $[0, b]$ is
$$(I^\alpha \varphi)(x) = \frac{1}{\Gamma(\alpha)} \int_0^x (x - t)^{\alpha - 1} \varphi(t) \, dt,$$
where $\Gamma$ is the [[Gamma function|0H5SYBSED9]].
The *Riemann–Liouville fractional integral equation* of order $\alpha$ is $I^\alpha \varphi = f$ for a given $f$ on $[0, b]$.
It is a [[Volterra equation of the first kind|H6ZGEDM4VV]] of [[convolution type|SNFYTC1TTA]], with the weakly singular kernel $k(u) = u^{\alpha - 1} / \Gamma(\alpha)$.

Check on power functions: let $\beta > -1$.
The substitution $t = xu$ gives
$$I^\alpha (t^\beta)(x) = \frac{x^{\alpha + \beta}}{\Gamma(\alpha)} \int_0^1 (1 - u)^{\alpha - 1} u^\beta \, du = \frac{x^{\alpha + \beta} B(\alpha, \beta + 1)}{\Gamma(\alpha)} = \frac{\Gamma(\beta + 1)}{\Gamma(\alpha + \beta + 1)} \, x^{\alpha + \beta},$$
using the [[Beta function|QHNWVSC6AQ]].
So for $\mu > \alpha - 1$, the equation $I^\alpha \varphi = x^\mu$ is solved by
$$\varphi(t) = \frac{\Gamma(\mu + 1)}{\Gamma(\mu + 1 - \alpha)} \, t^{\mu - \alpha}.$$
For instance, $\alpha = \tfrac12$ and $\mu = 1$ give $I^{1/2} \varphi = x$ with $\varphi(t) = \frac{\Gamma(2)}{\Gamma(3/2)} t^{1/2} = \frac{2}{\sqrt{\pi}} \sqrt{t}$.

## Remarks

When a continuous solution exists, it is $\varphi = \frac{d}{dx} I^{1 - \alpha} f$, the Riemann–Liouville fractional derivative of order $\alpha$ of $f$.
This follows from the semigroup law $I^{1 - \alpha} I^\alpha = I^1$, and it is the [[Abel inversion formula|TDMXFY06A2]] in other notation.
For $\alpha = \tfrac12$, the equation is [[Abel's integral equation|G4GWBYTW7B]] divided by $\Gamma(\tfrac12) = \sqrt{\pi}$.

## Explanations

### L1 human

Integrating $n$ times can be written as one integral with the kernel $(x - t)^{n - 1}/(n - 1)!$.
Replacing $n$ by a fraction $\alpha$ gives the fractional integral $I^\alpha$.
Solving $I^\alpha \varphi = f$ means taking a derivative of order $\alpha$ of $f$.
The power functions show how this works: integrating to order $\alpha$ raises the exponent by $\alpha$, and solving lowers it by $\alpha$.

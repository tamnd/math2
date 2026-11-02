---
tag: WPESA9XQ8X
kind: example
name: Laplace transform of the Heaviside step function
msc: [44A10]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 09C4JP7Y0M]
sources:
  - url: https://en.wikipedia.org/wiki/Heaviside_step_function
---

## Example

Let $H$ be the [[Heaviside step function|09C4JP7Y0M]], with $H(t) = 0$ for $t < 0$ and $H(t) = 1$ for $t > 0$, and let $a \ge 0$.
The delayed step $f(t) = H(t - a)$ is $0$ on $[0, a)$ and $1$ for $t > a$.
Its [[Laplace transform|05XT5AVJBK]] is
$$\mathcal{L}\{H(t - a)\}(s) = \frac{e^{-as}}{s} \quad (\operatorname{Re} s > 0).$$
Check: for $\operatorname{Re} s > 0$,
$$\int_0^\infty H(t - a) e^{-st}\, dt = \int_a^\infty e^{-st}\, dt = \lim_{T \to \infty} \frac{e^{-as} - e^{-sT}}{s} = \frac{e^{-as}}{s}.$$
The value of $H$ at the single point $0$ does not change the integral.
For $a = 0$ this is $\mathcal{L}\{1\} = 1/s$.
A rectangular pulse $H(t - a) - H(t - b)$ with $0 \le a < b$ has transform $(e^{-as} - e^{-bs})/s$, by linearity.

## Explanations

### L1 human

The step function models a switch turned on at time $a$.
Delaying a signal by $a$ multiplies its transform by $e^{-as}$, and here the undelayed signal is the constant $1$ with transform $1/s$.
Sums of steps describe piecewise constant inputs, and their transforms are sums of terms $e^{-as}/s$.

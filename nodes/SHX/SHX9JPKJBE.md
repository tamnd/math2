---
tag: SHX9JPKJBE
kind: statement
role: proposition
name: Linearity of the Laplace transform
msc: [44A10]
uses: [05XT5AVJBK, 080RWVVSB6, FTHFSJ30WJ]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f, g \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$ with $T > 0$, and let $\alpha, \beta \in \C$.
Let $s \in \C$ be such that the [[Laplace integrals|05XT5AVJBK]] $F(s) = \int_0^\infty f(t) e^{-st}\, dt$ and $G(s) = \int_0^\infty g(t) e^{-st}\, dt$ both converge.
Then the Laplace integral of $\alpha f + \beta g$ converges at $s$, and
$$\mathcal{L}\{\alpha f + \beta g\}(s) = \alpha F(s) + \beta G(s).$$

## Remarks

By [[linearity of the integral|080RWVVSB6]], $\int_0^T (\alpha f + \beta g) e^{-st}\, dt = \alpha \int_0^T f e^{-st}\, dt + \beta \int_0^T g e^{-st}\, dt$ for each $T$, and the limit of a sum is the sum of the limits.
So the identity holds on the half-plane $\operatorname{Re} s > \max(\sigma_c(f), \sigma_c(g))$, where $\sigma_c$ is the [[abscissa of convergence|FTHFSJ30WJ]].
Example: $\cosh t = \frac{1}{2}(e^t + e^{-t})$ has transform $\frac{1}{2}\left(\frac{1}{s - 1} + \frac{1}{s + 1}\right) = \frac{s}{s^2 - 1}$ for $\operatorname{Re} s > 1$.
The transform of $\alpha f + \beta g$ may converge on a larger half-plane than those of $f$ and $g$: for $f(t) = 1 + e^t$ and $g(t) = -e^t$, both have abscissa $1$, while $f + g = 1$ has abscissa $0$.

## Explanations

### L1 human

The transform of a sum is the sum of the transforms, and constants can be pulled out.
This is what lets one use a table: split a function into simple pieces, transform each piece, and add.
It also works backwards, when a transform is split into partial fractions and each fraction is inverted separately.

### L2 human

Linearity is the reason the Laplace transform fits linear differential equations with constant coefficients: together with the rule for derivatives, it turns the equation into an algebraic equation for $F$.
In operator language, $\mathcal{L}$ is a linear map from a space of functions (for instance those of exponential order) to a space of holomorphic functions on half-planes.
Combined with Lerch's uniqueness theorem, linearity also makes the inverse transform linear.

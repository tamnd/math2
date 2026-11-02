---
tag: HYP9AZHD06
kind: statement
role: proposition
name: Iterated Laplace transform equals Stieltjes transform
msc: [44A10, 44A15]
uses: [0V49JEZW06, RG1HFAYD98, D6QKPBS2EN]
about: [RG1HFAYD98, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Stieltjes_transformation
---

## Statement

Let $f \colon (0, \infty) \to \C$ be locally integrable, and let $x > 0$ satisfy
$$\int_0^\infty \frac{\abs{f(t)}}{x + t}\, dt < \infty.$$
Let $(\mathcal{L} f)(s) = \int_0^\infty e^{-st} f(t)\, dt$ denote the [[Laplace transform|0V49JEZW06]].
Then $(\mathcal{L} f)(s)$ converges absolutely for every $s > 0$, the function $\mathcal{L} f$ is integrable against $e^{-xs}\, ds$ on $(0, \infty)$, and
$$\big(\mathcal{L}(\mathcal{L} f)\big)(x) = \int_0^\infty \frac{f(t)}{x + t}\, dt,$$
the [[Stieltjes transform|RG1HFAYD98]] of $f$ at $x$.

## Remarks

The proof is one application of Fubini's theorem.
For $x, t > 0$ one has $\int_0^\infty e^{-xs} e^{-st}\, ds = \frac{1}{x + t}$.
So $\int_0^\infty \int_0^\infty e^{-xs} e^{-st} \abs{f(t)}\, dt\, ds = \int_0^\infty \frac{\abs{f(t)}}{x + t}\, dt < \infty$ by Tonelli, and Fubini allows the exchange of the two integrals.
The inner integral $\int_0^\infty e^{-st} \abs{f(t)}\, dt$ is then finite for almost every $s$, and since it decreases in $s$ it is finite for every $s > 0$.
The hypothesis cannot be dropped: for $f = 1$ the right side diverges for every $x$, while $\mathcal{L} f(s) = 1/s$ is not integrable against $e^{-xs}$ near $s = 0$.

Example: $f(t) = t^{-1/2}$.
Then $\mathcal{L} f(s) = \sqrt{\pi / s}$ and $\mathcal{L}(\mathcal{L} f)(x) = \sqrt{\pi}\, \Gamma(1/2)\, x^{-1/2} = \pi\, x^{-1/2}$.
Directly, the substitution $t = x u^2$ gives $\int_0^\infty \frac{t^{-1/2}}{x + t}\, dt = \frac{2}{\sqrt x} \int_0^\infty \frac{du}{1 + u^2} = \frac{\pi}{\sqrt x}$.

## Explanations

### L1 human

Applying the Laplace transform twice gives another well-known transform, the Stieltjes transform.
The reason is the elementary integral $\int_0^\infty e^{-(x+t)s}\, ds = 1/(x + t)$.

### L2 human

This identity lets one move facts between the two transforms.
Properties of the Stieltjes transform, such as analyticity in $x$ and its behaviour as $x \to 0^+$ or $x \to \infty$, follow from the corresponding properties of the Laplace transform applied twice.
Conversely, inversion formulas for the [[Laplace transform|0V49JEZW06]], such as [[Post's inversion formula|D6QKPBS2EN]], can be applied twice to recover $f$ from its Stieltjes transform.

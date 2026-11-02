---
tag: N2JFN9VHD9
kind: statement
role: proposition
name: Laplace transform tends to zero at infinity
msc: [44A10]
uses: [05XT5AVJBK, YCSH2WK69M, BYNV84PF86]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be measurable, and assume that $\int_0^\infty \abs{f(t)} e^{-\sigma_0 t}\, dt < \infty$ for some real $\sigma_0$.
Let $F(s) = \int_0^\infty f(t) e^{-st}\, dt$ be its [[Laplace transform|05XT5AVJBK]], defined for $\operatorname{Re} s \ge \sigma_0$.
Then
$$\sup_{\operatorname{Re} s = \sigma} \abs{F(s)} \to 0 \quad (\sigma \to +\infty).$$
That is, $F(s) \to 0$ as $\operatorname{Re} s \to +\infty$, uniformly in $\operatorname{Im} s$.

## Remarks

For $\operatorname{Re} s = \sigma \ge \sigma_0$, $\abs{F(s)} \le \int_0^\infty \abs{f(t)} e^{-\sigma t}\, dt$.
The integrand decreases to $0$ for each $t > 0$ as $\sigma \to \infty$ and is bounded by $\abs{f(t)} e^{-\sigma_0 t}$, so the right side tends to $0$ by [[dominated convergence|BYNV84PF86]].
The hypothesis says that $\sigma_0$ lies to the right of the [[abscissa of absolute convergence|YCSH2WK69M]], or on it.
Example: $\mathcal{L}\{e^{at}\}(s) = 1/(s - a)$ tends to $0$ as $\operatorname{Re} s \to \infty$.
Consequence: functions such as $1$, $s$, $e^{s}$ or a rational function $P/Q$ with $P \ne 0$ and $\deg P \ge \deg Q$ are not Laplace transforms of any such $f$.
The constant $1$ is the transform of the Dirac delta, which is a measure and not a function.

## Explanations

### L1 human

As $\operatorname{Re} s$ grows, the weight $e^{-st}$ crushes everything except what happens at times very close to $0$.
An ordinary function has no mass concentrated at a single instant, so the transform dies out.
This gives a quick test: if a candidate $F(s)$ does not go to zero, it cannot be the transform of a function.

### L2 human

The test is used in partial fraction inversion: only proper rational functions, with numerator degree less than denominator degree, are inverted to ordinary functions.
Improper parts correspond to the Dirac delta and its derivatives, which belong to the Laplace transform of distributions.
The initial value theorem refines the statement: if $f(t) \to c$ as $t \to 0^+$, then $sF(s) \to c$, so $F(s)$ behaves like $c/s$.

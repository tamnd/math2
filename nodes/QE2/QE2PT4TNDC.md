---
tag: QE2PT4TNDC
kind: statement
role: proposition
name: Scaling rule for the Laplace transform
msc: [44A10]
uses: [05XT5AVJBK]
about: [0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Statement

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$, and let $F$ be its [[Laplace transform|05XT5AVJBK]].
Let $c > 0$ be real, and let $s$ be a complex number such that the Laplace integral of $f$ converges at $s / c$.
Then the Laplace integral of $t \mapsto f(c t)$ converges at $s$, and
$$\mathcal{L}\{f(c t)\}(s) = \frac{1}{c} F\!\left(\frac{s}{c}\right).$$

## Remarks

The substitution $\tau = c t$ turns $\int_0^\infty f(c t) e^{-s t} \, dt$ into $\frac{1}{c} \int_0^\infty f(\tau) e^{-(s / c) \tau} \, d\tau$.
Example: from $\mathcal{L}\{\sin t\}(s) = 1 / (s^2 + 1)$ one gets $\mathcal{L}\{\sin \omega t\}(s) = \frac{1}{\omega} \cdot \frac{1}{(s / \omega)^2 + 1} = \frac{\omega}{s^2 + \omega^2}$ for $\omega > 0$.
The condition $c > 0$ is needed: for $c < 0$ the function $f(c t)$ uses values of $f$ at negative times.

## Explanations

### L1 human

Speeding up time by a factor $c$ stretches the transform by the same factor and scales its height by $1/c$.
Fast signals have transforms that are spread out in $s$.

### L2 human

The rule lets one derive a whole family of transforms from one transform, for example all $\sin \omega t$ from $\sin t$.
It also explains how the abscissa of convergence changes: it is multiplied by $c$.

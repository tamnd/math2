---
tag: 45P0QAMAFW
kind: definition
name: Wright omega function
msc: ["33E20"]
defines: 563ANQ3MY7
uses: [FW2JKAN14B]
sources:
  - url: https://en.wikipedia.org/wiki/Wright_omega_function
---

## Definition

Let $W_k$, for $k \in \Z$, be the branches of the [[Lambert W function|FW2JKAN14B]] over $\C$.
For $z \in \C$, let $K(z) = \ceil{\frac{\operatorname{Im} z - \pi}{2\pi}}$ be the unwinding number.
The *Wright omega function* is
$$\omega(z) = W_{K(z)}(e^z).$$

## Remarks

Example: for real $x$, $\operatorname{Im} x = 0$ and $K(x) = \ceil{-\tfrac12} = 0$, so $\omega(x) = W_0(e^x)$.
It is the unique real $y > 0$ with $y + \ln y = x$, since $y e^y = e^x$ is the same equation and $y \mapsto y + \ln y$ is a strictly increasing bijection from $(0, \infty)$ onto $\R$.
For instance $\omega(1) = 1$, and $\omega(0) = W_0(1) \approx 0.5671$, the omega constant.

Non-example: $W_0(e^z)$ is not $\omega(z)$ in general.
For $z = 4\pi i$, $K(z) = \ceil{3/2} = 2$, so $\omega(4\pi i) = W_2(1)$, which is not real, while $W_0(e^{4\pi i}) = W_0(1)$ is real.

The function $\omega$ is single-valued.
With the principal branch of the logarithm, $\omega(z) + \ln \omega(z) = z$ holds for every $z$ except possibly on the two half-lines $\set{t \pm i\pi : t \le -1}$.

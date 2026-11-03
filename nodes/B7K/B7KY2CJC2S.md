---
tag: B7KY2CJC2S
kind: definition
name: Transfer function
msc: [93C05, 93C80]
defines: 86JKV3TRFD
uses: [6J9MPVHSMF, 3X3SYVM7R5, NSR7N8A71M, 0V49JEZW06, 0XDK9CGYKJ, 5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer_function
---

## Definition

Let $H$ be a continuous-time [[linear time-invariant system|6J9MPVHSMF]] that is [[causal|NSR7N8A71M]], with [[impulse response|3X3SYVM7R5]] $h$, so that $h(t) = 0$ for $t < 0$.
Assume that $\int_0^\infty \abs{h(t)} e^{-\sigma t} \, dt < \infty$ for some real $\sigma$.
The *transfer function* of $H$ is the [[Laplace transform|0V49JEZW06]] of $h$:
$$G(s) = \int_0^\infty h(t) \, e^{-st} \, dt \quad \text{for } \operatorname{Re} s > \sigma.$$

## Remarks

If $u$ vanishes for $t < 0$ and has a Laplace transform $U$, then the output $y = Hu$ satisfies $Y(s) = G(s) U(s)$ where both sides are defined, by the convolution theorem.
Example: for $x' = Ax + Bu$, $y = Cx + Du$ with constant matrices and zero initial state, transforming gives $G(s) = C (sI - A)^{-1} B + D$.
This is a matrix of [[rational functions|0XDK9CGYKJ]] of $s$; with several inputs and outputs it is called the transfer matrix.
For $y' = -a y + u$ with real $a$, the impulse response is $h(t) = e^{-at}$ for $t \ge 0$, and $G(s) = 1/(s + a)$ for $\operatorname{Re} s > -a$.
Non-example: the system $(Hu)(t) = t \, u(t)$ has no transfer function, because it is not time-invariant, so there is no impulse response.
For discrete-time systems one uses the [[Z-transform|5FY0JQGHYZ]] instead: $G(z) = \sum_{n \ge 0} h[n] z^{-n}$.

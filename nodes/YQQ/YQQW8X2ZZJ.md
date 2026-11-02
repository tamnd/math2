---
tag: YQQW8X2ZZJ
kind: definition
name: Bessel polynomials
msc: [33C47, 33C10]
defines: M5NXATQ48S
uses: [1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_polynomials
---

## Definition

Let $n \ge 0$ be an integer.
The *Bessel polynomial* of degree $n$ is the [[polynomial|1G0B73WPX8]]
$$y_n(x) = \sum_{k=0}^{n} \frac{(n + k)!}{(n - k)! \, k!} \left( \frac{x}{2} \right)^k.$$
The *reverse Bessel polynomial* is $\theta_n(x) = x^n y_n(1/x)$.

## Remarks

Examples: $y_0 = 1$, $y_1 = 1 + x$ and $y_2 = 1 + 3x + 3x^2$.
Check for the top coefficient of $y_2$: $\frac{4!}{0! \, 2!} \cdot \frac14 = 3$.
Each $y_n$ solves $x^2 y'' + (2x + 2) y' - n(n + 1) y = 0$; for $y_1$ this reads $0 + (2x + 2) - 2(1 + x) = 0$.
Non-example: $1 + 2x$ has degree $1$ but is not a solution for $n = 1$, since $(2x + 2) \cdot 2 - 2(1 + 2x) = 2 \ne 0$.
For $x > 0$ they are linked to the modified Bessel function of the second kind: $y_n(x) = \sqrt{\frac{2}{\pi x}} \, e^{1/x} K_{n + 1/2}(1/x)$.

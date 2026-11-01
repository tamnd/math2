---
tag: BH5TK7DC2X
kind: definition
name: Caputo fractional derivative
msc: [26A33]
defines: 6VMGQYF8RW
uses: [JTKCZ44NN3, 0H5SYBSED9, 04TKTF8KDK]
sources:
  - url: https://en.wikipedia.org/wiki/Caputo_fractional_derivative
---

## Definition

Let $a < b$ be real numbers and let $\alpha > 0$ be a real number that is not an integer.
Let $n = \ceil{\alpha}$.
Let $f \colon [a, b] \to \R$ have $n - 1$ continuous derivatives such that $f^{(n-1)}$ is absolutely continuous, so that $f^{(n)}$ exists almost everywhere and is integrable.
The *Caputo fractional derivative* of order $\alpha$ of $f$ is
$${}^{C}D_a^\alpha f(x) = \frac{1}{\Gamma(n - \alpha)} \int_a^x (x - t)^{n - \alpha - 1} f^{(n)}(t) \, dt, \qquad a < x \le b,$$
that is, the [[Riemann–Liouville integral|JTKCZ44NN3]] $I_a^{n - \alpha}$ applied to the [[higher derivative|04TKTF8KDK]] $f^{(n)}$.
Here $\Gamma$ is the [[gamma function|0H5SYBSED9]].
For an integer $\alpha = n$, one sets ${}^{C}D_a^n f = f^{(n)}$.

## Remarks

Example: let $a = 0$, $\alpha = \tfrac{1}{2}$, so $n = 1$, and $f(x) = x$.
Then $f' = 1$ and ${}^{C}D_0^{1/2} f(x) = \frac{1}{\Gamma(1/2)} \int_0^x (x - t)^{-1/2} \, dt = \frac{2\sqrt{x}}{\sqrt{\pi}}$.
For a constant $f = c$, $f^{(n)} = 0$ and the Caputo derivative is $0$.
Non-example: the Riemann–Liouville derivative $\frac{d}{dx} I_0^{1/2} 1 = \frac{1}{\sqrt{\pi x}}$ is not $0$, so it does not agree with the Caputo derivative on constants.
In general, under the hypotheses above, the Caputo derivative equals the Riemann–Liouville derivative of $f(x) - \sum_{k=0}^{n-1} \frac{f^{(k)}(a)}{k!} (x - a)^k$.

## Explanations

### L1 human

The Caputo derivative takes an ordinary derivative of whole order first, and then smooths with a fractional integral.
This keeps the familiar rule that constants have derivative zero.

---
tag: 4V4AGE7XP4
kind: definition
name: Fractional calculus
msc: [26A33]
defines: T73XK15SA2
uses: [JTKCZ44NN3, 0H5SYBSED9, 04TKTF8KDK]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_calculus
---

## Definition

Let $a \in \R$ and let $f$ be a locally integrable real function on $[a, \infty)$.
For a real number $\alpha > 0$, the fractional integral of order $\alpha$ of $f$ is the [[Riemann–Liouville integral|JTKCZ44NN3]]
$$I_a^\alpha f(x) = \frac{1}{\Gamma(\alpha)} \int_a^x (x - t)^{\alpha - 1} f(t) \, dt, \qquad x > a,$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
For $\alpha > 0$ let $n = \ceil{\alpha}$.
The Riemann–Liouville fractional derivative of order $\alpha$ is
$$D_a^\alpha f(x) = \frac{d^n}{dx^n} \, I_a^{n - \alpha} f(x),$$
whenever the right side exists, with $I_a^0 f = f$.
*Fractional calculus* is the study of these operators and of their variants, for real or complex orders $\alpha$.

## Remarks

For a positive integer $\alpha = n$, $I_a^n f$ is the $n$-fold iterated integral of $f$ from $a$, and $D_a^n f$ is the ordinary [[higher derivative|04TKTF8KDK]] $f^{(n)}$.
Example: with $a = 0$ and $f(t) = 1$, $I_0^{1/2} f(x) = \frac{1}{\Gamma(1/2)} \int_0^x (x - t)^{-1/2} \, dt = \frac{2\sqrt{x}}{\sqrt{\pi}}$.
Non-example: for $\alpha = 0$ the integral formula is not defined, since $\Gamma(0)$ is not defined; the operator $I_a^0$ is set to be the identity by convention.
The fractional integrals satisfy $I_a^\alpha I_a^\beta = I_a^{\alpha + \beta}$ for $\alpha, \beta > 0$.
Other fractional derivatives, such as the [[Caputo derivative|6VMGQYF8RW]] and the [[Grünwald–Letnikov derivative|M9Z8VM4K1Z]], agree with $D_a^\alpha$ on suitable classes of functions.

## Explanations

### L1 human

The fractional integral replaces "integrate $n$ times" by a single weighted integral whose weight makes sense for any positive order.
A fractional derivative of order $\alpha$ is then obtained by integrating a little, to order $n - \alpha$, and differentiating a whole number $n$ of times.

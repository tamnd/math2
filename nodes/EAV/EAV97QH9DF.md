---
tag: EAV97QH9DF
kind: example
name: Bessel's equation
msc: [34B30, 33C10, 34M03]
illustrates: [H96HXG6CA0, W8ZWXC2HQS]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Example

Let $\nu \in \C$. *Bessel's equation* of order $\nu$ is
$$z^2 y'' + z y' + (z^2 - \nu^2)\, y = 0.$$
In normalised form, $p(z) = \frac{1}{z}$ and $q(z) = 1 - \frac{\nu^2}{z^2}$.
Then $z p(z) = 1$ and $z^2 q(z) = z^2 - \nu^2$ are analytic at $0$, so $0$ is a [[regular singular point|H96HXG6CA0]].
The indicial equation is $r (r - 1) + r - \nu^2 = r^2 - \nu^2 = 0$, with exponents $r = \pm \nu$.
If $\nu$ is not a negative integer, the [[Frobenius method|W8ZWXC2HQS]] with $r = \nu$ gives the recurrence $\left( (\nu + k)^2 - \nu^2 \right) a_k = - a_{k-2}$, that is, $k (k + 2 \nu)\, a_k = - a_{k-2}$, with $a_1 = 0$.
With $a_0 = \frac{1}{2^\nu \Gamma(\nu + 1)}$ it gives the Bessel function of the first kind
$$J_\nu(z) = \sum_{m \ge 0} \frac{(-1)^m}{m!\, \Gamma(m + \nu + 1)} \left( \frac{z}{2} \right)^{2m + \nu},$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
The series converges for all $z$, since the coefficients of the equation are analytic on $\C \setminus \set{0}$.
At $\infty$, the function $z^2 q(z) = z^2 - \nu^2$ is not bounded, so $\infty$ is an irregular singular point.

## Remarks

If $\nu \notin \Z$, then $J_\nu$ and $J_{-\nu}$ are linearly independent solutions.
If $\nu$ is an integer, then $J_{-\nu} = (-1)^\nu J_\nu$, and a second solution contains a logarithm, as Fuchs' theorem predicts.
For $\nu = \frac{1}{2}$, one gets $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}}\, \sin x$ for $x > 0$.
The equation arises from separating variables in the Laplace or wave equation in cylindrical coordinates.

## Explanations

### L1 human

Bessel's equation describes waves on a round drum and heat flow in a cylinder.
Its solutions near $0$ behave like the power $z^{\nu}$, and the Frobenius method finds them as series.
Far from $0$ they oscillate like a sine wave whose size decays like $\frac{1}{\sqrt{x}}$.

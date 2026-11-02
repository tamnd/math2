---
tag: PCE6XQTT6R
kind: statement
role: proposition
name: Bessel's integral
msc: [33C10]
uses: [CZCMRDWDYW]
about: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Statement

Let $n$ be an integer and let $J_n$ be the [[Bessel function of the first kind|CZCMRDWDYW]] of order $n$.
Then for every $z \in \C$,
$$J_n(z) = \frac{1}{\pi} \int_0^\pi \cos(n\tau - z \sin \tau)\, d\tau.$$

## Remarks

The generating function $\exp\left( \frac{z}{2} (t - t^{-1}) \right) = \sum_{k \in \Z} J_k(z)\, t^k$ with $t = e^{i\tau}$ gives $e^{iz \sin \tau} = \sum_{k} J_k(z)\, e^{ik\tau}$, the [[Jacobi–Anger expansion|KFHYQM8T7E]].
So $J_n(z)$ is the $n$-th Fourier coefficient $\frac{1}{2\pi} \int_{-\pi}^{\pi} e^{i(z \sin \tau - n\tau)}\, d\tau$.
Writing $e^{i(z \sin \tau - n\tau)} = \cos(n\tau - z\sin\tau) - i \sin(n\tau - z\sin\tau)$, the sine term is odd in $\tau$ and the cosine term is even, which gives the formula on $[0, \pi]$.
Example: for $n = 0$ and $z = 0$ the integral is $\frac{1}{\pi} \int_0^\pi 1\, d\tau = 1 = J_0(0)$.
The hypothesis that $n$ is an integer is needed: for non-integer $\nu$ the same integral defines the Anger function, which differs from $J_\nu$.
For $\Re z > 0$ and any $\nu$, Schläfli's extension reads $J_\nu(z) = \frac{1}{\pi} \int_0^\pi \cos(\nu\tau - z \sin\tau)\, d\tau - \frac{\sin(\nu\pi)}{\pi} \int_0^\infty e^{-z \sinh t - \nu t}\, dt$.

## Explanations

### L1 human

This formula writes a Bessel function as an average of a cosine over half a turn.
It was Bessel's own definition, coming from a problem in planetary motion.
It shows at once that $\abs{J_n(x)} \le 1$ for real $x$, since the integrand lies between $-1$ and $1$.

### L2 human

The integral turns many questions about $J_n$ into questions about an oscillatory integral.
Applying stationary phase to it gives the large-$x$ asymptotics of $J_n(x)$.
Differentiating under the integral sign checks Bessel's equation directly.
It is also the bridge between Bessel functions and Fourier series of $e^{iz\sin\tau}$, which is how they enter Kepler's equation and frequency modulation.

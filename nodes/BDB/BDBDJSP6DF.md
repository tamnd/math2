---
tag: BDBDJSP6DF
kind: statement
role: proposition
name: Integration operator as convolution with the unit step
msc: [44A40, 44A35]
uses: [FCKX8KFVGN, 09C4JP7Y0M]
about: [TD5XK5AHNV, FCKX8KFVGN]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Statement

Let $f$ be a locally integrable function on $[0, \infty)$.
Let $h$ be the constant function $h(t) = 1$ on $[0, \infty)$, the restriction of the [[Heaviside step function|09C4JP7Y0M]].
Write $f * g$ for the [[convolution on the half-line|FCKX8KFVGN]], $(f * g)(t) = \int_0^t f(\tau) \, g(t - \tau) \, d\tau$.
Then:

1. $(h * f)(t) = \int_0^t f(\tau) \, d\tau$ for all $t \ge 0$.
2. For every integer $n \ge 1$, the $n$-fold convolution power of $h$ is $h^{*n}(t) = \dfrac{t^{n-1}}{(n-1)!}$.
3. For every integer $n \ge 1$, $(h^{*n} * f)(t) = \displaystyle \int_0^t \frac{(t - \tau)^{n-1}}{(n-1)!} f(\tau) \, d\tau$, and this is the $n$-fold iterated integral of $f$ from $0$ to $t$.

## Remarks

Clause 1 is the definition of convolution with $h(t - \tau) = 1$ for $0 \le \tau \le t$.
Clause 2 follows by induction, since $\int_0^t \tau^{n-1}/(n-1)! \, d\tau = t^n / n!$.
Clause 3 follows from clauses 1 and 2 and the associativity of convolution; it is the Cauchy formula for repeated integration.
For example, with $f(t) = \cos t$, one gets $(h * f)(t) = \sin t$ and $(h * h * f)(t) = 1 - \cos t$.
In the [[Mikusiński operational calculus|TD5XK5AHNV]] this result lets one treat integration as multiplication by the element $h$ of a commutative ring.

## Explanations

### L1 human

Integrating a function from $0$ to $t$ is the same as convolving it with the function that is constantly $1$.
So the operation "integrate" becomes multiplication by a fixed object in a ring whose product is convolution.
Integrating twice is multiplication by $h * h$, which is the function $t$.

### L2 human

This is the starting point of Mikusiński's calculus.
The convolution ring of functions on $[0, \infty)$ has no zero divisors by the Titchmarsh convolution theorem, so it has a field of fractions.
In that field $h$ has an inverse $s$, which plays the role of differentiation.
Under the Laplace transform, $h$ corresponds to $1/s$, in line with the rule that the transform of $\int_0^t f$ is $F(s)/s$.

---
tag: Z22Y9N8EHN
kind: statement
role: proposition
name: Operator exponential and translation
msc: [44A40, 44A45]
uses: [82YAXZMMQ1, BDBDJSP6DF, 09C4JP7Y0M]
about: [82YAXZMMQ1, TD5XK5AHNV]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Statement

Let $\mathcal{M}$ be the [[Mikusiński field of operators|82YAXZMMQ1]], the field of fractions of the convolution ring of locally integrable functions on $[0, \infty)$.
Let $s$ be the inverse of the constant function $1$ in $\mathcal{M}$.
For $\lambda \ge 0$, let $h_\lambda(t) = H(t - \lambda)$ for $t \ge 0$, where $H$ is the [[Heaviside step function|09C4JP7Y0M]], and define the translation operator $e^{-\lambda s} = s \, h_\lambda$.
Then:

1. For every locally integrable $f$ on $[0, \infty)$, the product $e^{-\lambda s} f$ is the function $t \mapsto H(t - \lambda) f(t - \lambda)$.
2. $e^{-0 s} = 1$, and $e^{-\lambda s} e^{-\mu s} = e^{-(\lambda + \mu) s}$ for all $\lambda, \mu \ge 0$.

## Remarks

For $t \ge \lambda$, $(h_\lambda * f)(t) = \int_0^{t - \lambda} f(\tau) \, d\tau$, and for $t < \lambda$ it is $0$.
So $h_\lambda * f$ is the [[integral from zero|BDBDJSP6DF]] of the delayed function $f_\lambda(t) = H(t - \lambda) f(t - \lambda)$, that is, $h_\lambda f = h f_\lambda$.
Multiplying by $s = 1/h$ gives clause 1.
Clause 2 follows from clause 1, since a delay by $\mu$ followed by a delay by $\lambda$ is a delay by $\lambda + \mu$, and $\mathcal{M}$ has no zero divisors.
For example, $e^{-\lambda s} h = h_\lambda$: delaying the unit step $h$ by $\lambda$ gives the jump of size one at time $\lambda$.
The notation matches the Laplace transform, where a delay by $\lambda$ multiplies the transform by $e^{-\lambda s}$.

## Explanations

### L1 human

Shifting a signal later in time by $\lambda$ is, in the field of operators, multiplication by one fixed operator.
That operator behaves like an exponential: two shifts compose by adding their lengths.
This is why it is written $e^{-\lambda s}$.

### L2 human

The result explains Heaviside's formal rule that $e^{-\lambda p}$ acts as a delay, where $p$ is differentiation.
In Mikusiński's setting no power series in $s$ is needed: the operator is defined directly from the delayed step.
It lets one solve equations with delays and treat piecewise defined inputs, such as a switch that turns on at time $\lambda$.
The same rule for the Laplace transform is the time shift theorem.

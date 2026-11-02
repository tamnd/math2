---
tag: 4NFHBBNZBK
kind: definition
name: Integro-differential equation
msc: [45J05]
defines: YRKW2KX2CW
uses: [0NT64JV96A, 0W29TBTY12, DND8CBEVXT]
sources:
  - url: https://en.wikipedia.org/wiki/Integro-differential_equation
---

## Definition

Let $I = [t_0, t_0 + T]$ with $T > 0$, let $n \ge 1$, and let $f \colon I \times \R^n \to \R^n$ and $K \colon I \times I \times \R^n \to \R^n$ be continuous.
A (Volterra type) *integro-differential equation* is an equation
$$x'(t) = f(t, x(t)) + \int_{t_0}^{t} K(t, s, x(s)) \, ds, \quad t \in I,$$
for an unknown continuously differentiable $x \colon I \to \R^n$.
More generally, an integro-differential equation is any equation with the unknown both under a derivative and under an [[integral|0W29TBTY12]].
When the integral is over a fixed interval, the equation is of Fredholm type.

## Remarks

Example: $x'(t) = -\int_0^t x(s) \, ds$, $x(0) = 1$.
Differentiating gives $x'' = -x$ with $x(0) = 1$ and $x'(0) = 0$, so $x = \cos t$.
Check: $-\int_0^t \cos s \, ds = -\sin t = x'(t)$.

Non-example: $x'(t) = -x(t)$ contains no integral of the unknown, so it is an [[ordinary differential equation|0NT64JV96A]].
Also $x(t) = 1 + \int_0^t x(s) \, ds$ contains no derivative; it is a [[Volterra integral equation|DND8CBEVXT]].

Integrating the Volterra form from $t_0$ to $t$ turns the problem with $x(t_0) = x_0$ into a Volterra integral equation for $x$.
For a convolution kernel $K(t, s, x) = k(t - s) x$, the Laplace transform turns the linear equation into an algebraic one.

## Explanations

### L1 human

The rate of change is given partly by the present value and partly by a weighted sum of all past values.

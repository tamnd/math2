---
tag: 6ZQRVRD8KP
kind: definition
name: Volterra integro-differential equation
msc: [45J05, 45D05]
defines: 5126SDXYHF
uses: [YRKW2KX2CW, DND8CBEVXT, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Integro-differential_equation
---

## Definition

Let $t_0 \in \R$, $T > 0$, $I = [t_0, t_0 + T]$ and $n \ge 1$.
Let $f \colon I \times \R^n \to \R^n$ and $K \colon I \times I \times \R^n \to \R^n$ be continuous, and let $x_0 \in \R^n$.
A *Volterra integro-differential equation* with initial value $x_0$ is the problem of finding a continuously differentiable $x \colon I \to \R^n$ with
$$x'(t) = f\big(t, x(t)\big) + \int_{t_0}^{t} K\big(t, s, x(s)\big) \, ds \quad \text{for } t \in I, \qquad x(t_0) = x_0.$$
It is *linear* when $f(t, x) = A(t) x + b(t)$ and $K(t, s, x) = B(t, s) x$ for continuous matrix functions $A$, $B$ and a continuous $b$.
Equations with higher derivatives of $x$, or with derivatives of $x$ inside the integral, are included in the same name.

## Remarks

Example: $x'(t) = \int_0^t x(s) \, ds$, $x(0) = 1$, with $f = 0$ and $K(t, s, x) = x$.
Differentiating gives $x'' = x$ with $x(0) = 1$ and $x'(0) = 0$, so $x(t) = \cosh t$.
Check: $\int_0^t \cosh s \, ds = \sinh t = x'(t)$.

Non-example: $x'(t) = \int_0^1 x(s) \, ds$ for $t \in [0, 1]$ has an integral over the fixed interval $[0, 1]$, including future times, so it is an integro-differential equation of Fredholm type, not of Volterra type.

Integrating from $t_0$ to $t$ turns the problem into the [[Volterra integral equation|DND8CBEVXT]]
$$x(t) = x_0 + \int_{t_0}^{t} \left[f\big(s, x(s)\big) + \int_{t_0}^{s} K\big(s, r, x(r)\big) \, dr\right] ds.$$
If $f$ and $K$ are Lipschitz in their last variable, uniformly in the others, successive approximations converge on all of $I$ and give a unique solution.
This generalizes the [[initial value problem|0FXDW992DS]] for ordinary differential equations, which is the case $K = 0$.

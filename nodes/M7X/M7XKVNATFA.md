---
tag: M7XKVNATFA
kind: statement
role: proposition
name: Backward Euler method
msc: [65L04, 65L05, 65L20]
uses: [558XADG64M, 0FXDW992DS, 0AW1E6YTJY, 0VK6VEH345, T220HF0562]
about: [558XADG64M]
sources:
  - url: https://en.wikipedia.org/wiki/Backward_Euler_method
same_as:
  wikidata: Q2736820
  wikipedia: Backward Euler method
---

## Statement

Let $f \colon [t_0, T] \times \R^d \to \R^d$ be continuous and [[Lipschitz|0AW1E6YTJY]] in $y$ with constant $L$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
The *backward Euler method* with step $h > 0$ sets $t_{n+1} = t_n + h$ and defines $y_{n+1}$ by the implicit equation
$$y_{n+1} = y_n + h \, f(t_{n+1}, y_{n+1}).$$
Then:

1. if $hL < 1$, the equation has exactly one solution $y_{n+1}$ for each $y_n$;
2. if the exact solution $y$ is of class $C^3$, the [[local truncation error|T220HF0562]] is $y(t_{n+1}) - y(t_n) - h \, y'(t_{n+1}) = -\frac{h^2}{2} y''(t_n) + O(h^3)$, so the method has order $1$;
3. for the test equation $y' = \lambda y$ with $\lambda \in \C$, it gives $y_{n+1} = R(h\lambda) y_n$ with $R(z) = \frac{1}{1 - z}$, and $\abs{R(z)} < 1$ whenever $\operatorname{Re} z < 0$.

## Remarks

Clause 1: the map $z \mapsto y_n + h f(t_{n+1}, z)$ is a contraction with constant $hL < 1$, so the [[Banach fixed point theorem|0VK6VEH345]] gives a unique fixed point, which fixed-point iteration finds.
Clause 2 follows by Taylor expansion of $y(t_n)$ and $y'(t_{n+1})$ about $t_n$.
Clause 3: if $\operatorname{Re} z < 0$ then $\abs{1 - z} > 1$; so the numerical solution decays whenever the exact one does, for every step size, and the method is A-stable.
Example: for $y' = -1000 y$ and $h = 0.1$, the explicit Euler method multiplies by $1 - 100 = -99$ at each step and explodes, while backward Euler multiplies by $\frac{1}{101}$ and decays like the true solution.
For stiff problems $hL$ is large, and the equation is solved by Newton's method rather than by fixed-point iteration.
So the restriction $hL < 1$ of clause 1 is a feature of that proof, not of the method.

## Explanations

### L1 human

The ordinary Euler method uses the slope at the start of a step; the backward Euler method uses the slope at the end of the step.
Since that endpoint is not yet known, each step requires solving an equation.
The reward is stability: the method does not blow up on problems whose solutions decay very fast, even with large steps.

### L2 human

Backward Euler is the simplest implicit method and the prototype of methods for [[stiff equations|RR5FCG92PN]].
It is both the one-stage Radau IIA Runge–Kutta method and the first backward differentiation formula (BDF1).
Its stability function $R(z) = 1/(1-z)$ tends to $0$ as $z \to -\infty$, a property called L-stability, which damps fast transients strongly.
Its accuracy is only first order, so in practice higher-order implicit methods such as the BDF family or the [[Gauss–Legendre methods|D99FZQ2SQT]] are used, with backward Euler as their simplest relative.

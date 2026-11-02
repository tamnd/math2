---
tag: RJEK60G28F
kind: statement
role: proposition
name: Heun's method
msc: [65L06, 65L05]
uses: [7DBPJKYC6C, 0FXDW992DS, T220HF0562, 0JARTXX4XP, 03QHBVW4TT]
about: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Heun%27s_method
same_as:
  wikidata: Q1531998
  wikipedia: Heun's method
---

## Statement

Let $f \colon [t_0, T] \times \R^d \to \R^d$ be of class $C^2$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$ with exact solution $y$.
*Heun's method* with step $h > 0$ computes a predictor $\tilde y_{n+1} = y_n + h f(t_n, y_n)$ and then
$$y_{n+1} = y_n + \frac{h}{2}\Big( f(t_n, y_n) + f(t_{n+1}, \tilde y_{n+1}) \Big), \qquad t_{n+1} = t_n + h.$$
Its [[local truncation error|T220HF0562]] is $O(h^3)$, so it is a Runge–Kutta method of order $2$.

## Remarks

Proof idea: by [[Taylor's theorem|03QHBVW4TT]], $f\big(t + h, y + h f\big) = f + h(f_t + f_y f) + O(h^2)$ at $(t, y)$, so the increment is $h f + \frac{h^2}{2}(f_t + f_y f) + O(h^3)$, which matches the Taylor expansion of $y(t + h)$ up to $h^2$.
In Butcher form it has $c = (0, 1)$, $a_{21} = 1$ and $b = (\tfrac12, \tfrac12)$.
Example: for $y' = y$, $y(0) = 1$ and $h = 0.1$, one step gives $\tilde y_1 = 1.1$ and $y_1 = 1 + 0.05 (1 + 1.1) = 1.105$, against $e^{0.1} \approx 1.10517$; the [[Euler method|0JARTXX4XP]] gives $1.1$.
If $f$ does not depend on $y$, the method is the trapezoidal rule for $\int f(t)\,dt$.

## Explanations

### L1 human

Heun's method first takes a trial Euler step to guess where the solution goes.
It then measures the slope at the guessed endpoint, averages it with the slope at the start, and redoes the step with this average slope.
The averaging cancels most of the error of the plain Euler step.

### L2 human

Heun's method is also called the improved Euler method or the explicit trapezoidal method.
It is the simplest predictor–corrector scheme: an explicit Euler predictor followed by one correction with the trapezoidal rule.
Like the [[midpoint method|WHK8D383YT]], it is a two-stage explicit [[Runge–Kutta method|7DBPJKYC6C]] of order $2$.
The difference between its result and the Euler predictor gives a cheap estimate of the local error for step size control.

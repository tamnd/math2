---
tag: WHK8D383YT
kind: statement
role: proposition
name: Midpoint method
msc: [65L06, 65L05]
uses: [7DBPJKYC6C, 0FXDW992DS, T220HF0562, 03QHBVW4TT]
about: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Midpoint_method
same_as:
  wikidata: Q17103851
  wikipedia: Midpoint method
---

## Statement

Let $f \colon [t_0, T] \times \R^d \to \R^d$ be of class $C^2$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$ with exact solution $y$.
The *explicit midpoint method* with step $h > 0$ is
$$y_{n+1} = y_n + h \, f\Big(t_n + \frac{h}{2}, \; y_n + \frac{h}{2} f(t_n, y_n)\Big).$$
Its [[local truncation error|T220HF0562]] is $O(h^3)$, so it is a Runge–Kutta method of order $2$.

## Remarks

Proof idea: by [[Taylor's theorem|03QHBVW4TT]], $y(t + h) = y + h f + \frac{h^2}{2}(f_t + f_y f) + O(h^3)$, with $f$ and its partial derivatives taken at $(t, y(t))$.
Expanding the increment gives $h f\big(t + \frac h2, y + \frac h2 f\big) = h f + \frac{h^2}{2}(f_t + f_y f) + O(h^3)$, and the two expansions agree up to $h^2$.
In Butcher form it has $c = (0, \tfrac12)$, $a_{21} = \tfrac12$ and $b = (0, 1)$.
Example: for $y' = \lambda y$ it gives $y_{n+1} = \big(1 + z + \frac{z^2}{2}\big) y_n$ with $z = h\lambda$, the Taylor polynomial of $e^z$ of degree $2$.
The *implicit midpoint method* $y_{n+1} = y_n + h f\big(t_n + \frac h2, \frac{y_n + y_{n+1}}{2}\big)$ also has order $2$; it is the one-stage Gauss–Legendre method.

## Explanations

### L1 human

The Euler method follows the slope at the start of the step all the way to the end.
The midpoint method first uses that slope to walk half a step, measures the slope there, and then makes the whole step with this better slope.
This costs two slope evaluations per step but makes the error shrink like $h^2$ instead of $h$.

### L2 human

The explicit midpoint method is one of the simplest second-order [[Runge–Kutta methods|7DBPJKYC6C]], together with [[Heun's method|RJEK60G28F]].
Both satisfy the order conditions $\sum b_i = 1$ and $\sum b_i c_i = \frac12$, and they differ in the choice of the second stage.
The implicit midpoint method is symplectic and preserves quadratic invariants, which makes it useful for Hamiltonian systems.

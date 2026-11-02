---
tag: JJCQ0DG4Z9
kind: definition
name: Runge–Kutta methods
msc: [65L06, 65L05]
defines: 7DBPJKYC6C
uses: [0FXDW992DS, 0JARTXX4XP]
sources:
  - url: https://en.wikipedia.org/wiki/Runge–Kutta_methods
---

## Definition

Let $f \colon \R \times \R^n \to \R^n$, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
Let $s \ge 1$ be an integer and let $a_{ij}$, $b_i$, $c_i$ be real numbers for $i, j = 1, \ldots, s$.
The *$s$-stage Runge–Kutta method* with these coefficients and step size $h > 0$ computes approximations $y_k \approx y(t_k)$ at $t_k = t_0 + k h$ by
$$K_i = f\Big( t_k + c_i h, \; y_k + h \sum_{j=1}^{s} a_{ij} K_j \Big), \quad i = 1, \ldots, s, \qquad y_{k+1} = y_k + h \sum_{i=1}^{s} b_i K_i.$$
The method is *explicit* if $a_{ij} = 0$ for all $j \ge i$, and *implicit* otherwise.

## Remarks

The coefficients are written in the Butcher tableau with the $c_i$ in a column, the matrix $(a_{ij})$ beside it, and the $b_i$ as a bottom row.
Usually $c_i = \sum_j a_{ij}$, and the method is consistent, of order at least $1$, exactly when $\sum_i b_i = 1$.
Example: $s = 1$, $a_{11} = 0$, $b_1 = 1$, $c_1 = 0$ gives $y_{k+1} = y_k + h f(t_k, y_k)$, the [[Euler method|0JARTXX4XP]].
The classical method has $s = 4$, $c = (0, \tfrac12, \tfrac12, 1)$, $a_{21} = a_{32} = \tfrac12$, $a_{43} = 1$, the other $a_{ij} = 0$, and $b = (\tfrac16, \tfrac13, \tfrac13, \tfrac16)$; it has order $4$.
For $y' = \lambda y$ it gives $y_{k+1} = \left( 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24} \right) y_k$ with $z = h \lambda$, the Taylor polynomial of $e^z$ of degree $4$.
Non-example: the two-step formula $y_{k+2} = y_k + 2 h f(t_{k+1}, y_{k+1})$ is not a Runge–Kutta method, since $y_{k+2}$ depends on two earlier values and not only on $y_{k+1}$; it is a linear multistep method.

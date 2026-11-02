---
tag: Z45HQ5VNF4
kind: definition
name: Cubic Hermite spline
msc: [41A15, 65D07, 41A05]
defines: HCQWPAHYAT
uses: [9Z50M2WPTP, 84TJ8KQ926, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_Hermite_spline
---

## Definition

Let $x_0 < x_1 < \cdots < x_n$ be real nodes, and let $p_0, \dots, p_n$ and $m_0, \dots, m_n$ be real numbers.
Let $h_i = x_{i+1} - x_i$.
The *cubic Hermite spline* for these data is the function $s \colon [x_0, x_n] \to \R$ given on each $[x_i, x_{i+1}]$ by
$$s(x) = h_{00}(u)\, p_i + h_{10}(u)\, h_i m_i + h_{01}(u)\, p_{i+1} + h_{11}(u)\, h_i m_{i+1},$$
where $u = (x - x_i)/h_i$ and
$$h_{00}(u) = 2u^3 - 3u^2 + 1, \quad h_{10}(u) = u^3 - 2u^2 + u, \quad h_{01}(u) = -2u^3 + 3u^2, \quad h_{11}(u) = u^3 - u^2.$$

## Remarks

The piece on $[x_i, x_{i+1}]$ is the unique cubic with $s(x_i) = p_i$, $s'(x_i) = m_i$, $s(x_{i+1}) = p_{i+1}$ and $s'(x_{i+1}) = m_{i+1}$, that is, a [[Hermite interpolant|9Z50M2WPTP]].
Check: $h_{00}(0) = 1$, $h_{00}(1) = 0$, $h_{01}(1) = 1$, $h_{10}'(0) = 1$, $h_{11}'(1) = 1$, and the other values and slopes at $0$ and $1$ vanish.
So $s$ is a [[spline|84TJ8KQ926]] of class [[$C^1$|0VW90BBSJ4]], but in general not of class $C^2$.
Example: nodes $0, 1$ with $p = (0, 1)$ and $m = (0, 0)$ give $s(x) = 3x^2 - 2x^3$.
Non-example: the piecewise linear interpolant of the same values is not a cubic Hermite spline for these slopes, since its slope on $[0, 1]$ is $1$, not $0$.
When the slopes are not given, they are chosen from the values, for instance by finite differences (Catmull–Rom spline) or by monotonicity-preserving rules.

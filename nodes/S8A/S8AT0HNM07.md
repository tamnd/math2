---
tag: S8AT0HNM07
kind: definition
name: Riccati difference equation
msc: [39A20, 39A06]
defines: D4Q8VM7826
uses: [T8YDEASD1H]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_difference_equation
    locator: Riccati difference equation
---

## Definition

Let $a, b, c, d$ be real numbers with $c \ne 0$ and $ad - bc \ne 0$.
The *Riccati difference equation* with these coefficients is the [[rational difference equation|T8YDEASD1H]]
$$x_{n+1} = \frac{a x_n + b}{c x_n + d} \qquad (n \ge 0),$$
for real sequences $(x_n)_{n \ge 0}$ with $c x_n + d \ne 0$ for all $n$.

## Remarks

Example: $x_{n+1} = 1/(1 + x_n)$ has $a = 0$, $b = c = d = 1$, so $c \ne 0$ and $ad - bc = -1 \ne 0$.
Non-example: $x_{n+1} = (2 x_n + 1)/3$ has $c = 0$; it is an affine linear recurrence, not a Riccati equation.
The condition $ad - bc \ne 0$ excludes the degenerate case where the right side is a constant.
Linearization: if $(y_n)$ satisfies $y_{n+2} = (a + d)\, y_{n+1} - (ad - bc)\, y_n$ with all $y_n \ne 0$, then $x_n = (y_{n+1}/y_n - d)/c$ solves the equation.
To check, put $w_n = c x_n + d$; the equation becomes $w_{n+1} = (a + d) - (ad - bc)/w_n$, and $w_n = y_{n+1}/y_n$ turns this into the linear recurrence.

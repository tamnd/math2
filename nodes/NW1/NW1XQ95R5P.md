---
tag: NW1XQ95R5P
kind: statement
role: theorem
name: Inverse quadratic interpolation
msc: [65H05, 65D05]
uses: [237KR6FRCK, 9ZC177PVPC, YWZQC5E54B, 0J2WAR83WP]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_quadratic_interpolation
same_as:
  wikidata: Q3153554
  wikipedia: Inverse quadratic interpolation
---

## Statement

Let $f$ be a real function that is three times continuously differentiable on an open interval $I$, and let $r \in I$ satisfy $f(r) = 0$ and $f'(r) \ne 0$.
Given three points $x_{n-2}, x_{n-1}, x_n$ whose values $f_k = f(x_k)$ are pairwise distinct, *inverse quadratic interpolation* defines
$$x_{n+1} = \frac{f_{n-1} f_n \, x_{n-2}}{(f_{n-2} - f_{n-1})(f_{n-2} - f_n)} + \frac{f_{n-2} f_n \, x_{n-1}}{(f_{n-1} - f_{n-2})(f_{n-1} - f_n)} + \frac{f_{n-2} f_{n-1} \, x_n}{(f_n - f_{n-2})(f_n - f_{n-1})}.$$
Then there is $\delta > 0$ with the following property.
For all starting points $x_0, x_1, x_2$ within $\delta$ of $r$ for which the iteration is defined, the iterates [[converge|YWZQC5E54B]] to $r$ with order $q \approx 1.839$.
Here $q$ is the real root of $q^3 = q^2 + q + 1$.

## Remarks

The new point is the value at $y = 0$ of the [[Lagrange interpolation|237KR6FRCK]] polynomial of degree at most $2$ through the points $(f_k, x_k)$.
This polynomial approximates the [[inverse function|0J2WAR83WP]] of $f$ near $r$, so its value at $0$ approximates $r = f^{-1}(0)$.
The error analysis gives $e_{n+1} \approx C e_n e_{n-1} e_{n-2}$ for the errors $e_k = x_k - r$, which leads to the stated order.
Interpolating $x$ as a function of $y$ avoids solving a quadratic equation, unlike Muller's method.
The method breaks down when two of the values $f_k$ coincide, and it can diverge from poor starting points.
For this reason it is used inside safeguarded methods such as Brent's method.
With two points instead of three, the same idea gives the [[secant method|9ZC177PVPC]].

## Explanations

### L1 human

Swap the roles of $x$ and $y$: think of $x$ as a function of $y = f(x)$.
Fit a parabola in this swapped picture through three known points, and read off where it meets $y = 0$.
That reading is the next guess for the root.

### L2 human

The method needs no derivatives and only one new function value per step.
Its order is a little less than $2$ but better than the secant method's $1.618$.
It is fast but fragile, so libraries combine it with bisection to keep a bracket around the root.

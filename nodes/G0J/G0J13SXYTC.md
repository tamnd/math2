---
tag: G0J13SXYTC
kind: statement
role: theorem
name: Wirtinger's inequality for functions
msc: [26D10, 42A05]
uses: [089KWVYD69, 06SKCHDQT5, 0QM4TXT3DR]
about: [089KWVYD69]
sources:
  - url: https://en.wikipedia.org/wiki/Wirtinger%27s_inequality_for_functions
same_as:
  wikidata: Q947364
  wikipedia: Wirtinger's inequality for functions
---

## Statement

Let $f \colon \R \to \R$ be a [[continuously differentiable function|06SKCHDQT5]] that is [[periodic|089KWVYD69]] with period $2\pi$ and satisfies $\int_0^{2\pi} f(x) \, dx = 0$.
Then
$$\int_0^{2\pi} f(x)^2 \, dx \le \int_0^{2\pi} f'(x)^2 \, dx,$$
with equality if and only if $f(x) = \alpha \cos x + \beta \sin x$ for some real numbers $\alpha, \beta$.

## Remarks

Proof idea: expand $f$ in its Fourier series $\sum_k c_k e^{i k x}$.
The mean zero condition gives $c_0 = 0$, and $f'$ has coefficients $i k c_k$.
By [[Parseval's identity|047RFCNVSK]] the two sides are $2\pi \sum_{k \ne 0} \abs{c_k}^2$ and $2\pi \sum_{k \ne 0} k^2 \abs{c_k}^2$, and $k^2 \ge 1$ with equality only for $k = \pm 1$.

The mean zero condition is needed: the constant function $f = 1$ gives $2\pi \le 0$, which is false.

A related form holds on an interval with zero boundary values: if $f \colon [0, \pi] \to \R$ is continuously differentiable with $f(0) = f(\pi) = 0$, then $\int_0^\pi f^2 \le \int_0^\pi f'^2$.

## Explanations

### L1 human

A periodic function with average zero cannot be large without also changing fast.
Wirtinger's inequality makes this precise: the total square of the function is at most the total square of its slope.
The extreme case is a single sine wave of the longest possible period.

### L2 human

This is the simplest Poincaré-type inequality, and the constant $1$ is the smallest nonzero eigenvalue of $-d^2/dx^2$ on the circle of length $2\pi$.
It gives a short proof of the isoperimetric inequality in the plane, by applying it to the coordinates of a closed curve parametrized by arc length.

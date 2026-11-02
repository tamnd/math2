---
tag: WVD069C7QF
kind: statement
role: theorem
name: Cox–de Boor recursion
msc: [41A15, 65D07]
uses: [62AFX32JGT, N5ZHV4HWDC]
about: [62AFX32JGT]
sources:
  - url: https://en.wikipedia.org/wiki/B-spline
---

## Statement

Let $(t_j)$ be a nondecreasing sequence of real knots.
Let $i$ be an index and $k \ge 1$ an order.
The normalized [[B-spline|62AFX32JGT]] is
$$B_{i,k}(x) = (t_{i+k} - t_i)\, [t_i, \dots, t_{i+k}]\, (\cdot - x)_+^{k-1}.$$
Here $[t_i, \dots, t_{i+k}]$ is the [[divided difference|N5ZHV4HWDC]] in the first variable, $(u)_+^{k-1} = u^{k-1}$ for $u > 0$ and $0$ otherwise, also for $k = 1$.
Set $B_{i,k} = 0$ when $t_i = t_{i+k}$.
Then
$$B_{i,1}(x) = \begin{cases} 1 & \text{if } t_i \le x < t_{i+1}, \\ 0 & \text{otherwise,} \end{cases}$$
and for $k \ge 2$ and all real $x$,
$$B_{i,k}(x) = \frac{x - t_i}{t_{i+k-1} - t_i} B_{i,k-1}(x) + \frac{t_{i+k} - x}{t_{i+k} - t_{i+1}} B_{i+1,k-1}(x),$$
where a term whose denominator is $0$ is read as $0$.

## Remarks

The proof applies the Leibniz rule for divided differences to the product $(t - x)_+^{k-1} = (t - x) \cdot (t - x)_+^{k-2}$ and uses the recursive definition of divided differences.
Many texts take the recursion itself as the definition of B-splines, and then the divided difference formula becomes a theorem.
Example: with knots $0, 1, 2$, the recursion gives $B_{0,2}(x) = x$ on $[0, 1)$, $2 - x$ on $[1, 2)$ and $0$ elsewhere, the hat function.
The recursion shows at once that $B_{i,k}$ is nonnegative, vanishes outside $[t_i, t_{i+k})$, and is a piecewise polynomial of degree at most $k - 1$.
It is numerically stable, since for $x$ in the support both coefficients lie in $[0, 1]$.

## Explanations

### L1 human

B-splines of higher degree are built from those of lower degree.
Each one is a blend of two neighbours of one lower degree, with weights that grow or shrink linearly across the support.
Starting from step functions that are $1$ on one knot interval, one gets hat functions, then smooth quadratic bumps, then cubic bumps.

### L2 human

The recursion, found independently by Cox and by de Boor in 1972, is the standard way to evaluate B-splines and their derivatives.
Applying it to a whole spline gives [[de Boor's algorithm|5JHFB384BF]], which evaluates $\sum_j c_j B_{j,k}(x)$ by repeated convex combinations of the coefficients.
From it one also derives the derivative formula for B-splines and the partition of unity $\sum_j B_{j,k}(x) = 1$ on the basic interval.

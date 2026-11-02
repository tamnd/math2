---
tag: 8R4CVVV8WT
kind: definition
name: B-spline
msc: [41A15, 65D07, 65D17]
defines: 62AFX32JGT
uses: [84TJ8KQ926, NH739XXVXK]
sources:
  - url: https://en.wikipedia.org/wiki/B-spline
---

## Definition

Let $t_0 \le t_1 \le \cdots \le t_m$ be real numbers, called *knots*.
The *B-splines* $B_{i,p}$ of degree $p \ge 0$ for these knots are the functions $\R \to \R$ defined by recursion on $p$:

1. for $0 \le i \le m - 1$, $B_{i,0}(x) = 1$ if $t_i \le x < t_{i+1}$ and $B_{i,0}(x) = 0$ otherwise;
2. for $p \ge 1$ and $0 \le i \le m - p - 1$,
$$B_{i,p}(x) = \frac{x - t_i}{t_{i+p} - t_i} \, B_{i,p-1}(x) + \frac{t_{i+p+1} - x}{t_{i+p+1} - t_{i+1}} \, B_{i+1,p-1}(x),$$
where a term whose denominator is $0$ is taken to be $0$.

## Remarks

$B_{i,p}$ is a [[spline|84TJ8KQ926]] of degree $p$ with knots $t_i, \dots, t_{i+p+1}$; if $t_i < t_{i+p+1}$, it is positive on $(t_i, t_{i+p+1})$ and zero outside $[t_i, t_{i+p+1})$.
On $[t_p, t_{m-p})$ the B-splines of degree $p$ sum to $1$, so they form a [[partition of unity|NH739XXVXK]] there.
At a knot of multiplicity $r \le p$, the B-splines of degree $p$ have $p - r$ continuous derivatives.
An equivalent definition writes $B_{i,p}$ as $(t_{i+p+1} - t_i)$ times a divided difference of the truncated power $(\cdot - x)_+^p$ at $t_i, \dots, t_{i+p+1}$.

Example: knots $0, 1, 2$ and $p = 1$.
Then $B_{0,1}(x) = x \, B_{0,0}(x) + (2 - x) \, B_{1,0}(x)$, which is $x$ on $[0, 1)$, $2 - x$ on $[1, 2)$ and $0$ elsewhere: the hat function.

Non-example: let $g$ be $x$ on $[0, 1)$, $1$ on $[1, 2)$ and $0$ elsewhere.
It is piecewise linear on the same knots, but it is not $B_{0,1}$.
It differs from the hat function on $(1, 2)$, and it jumps at $2$.

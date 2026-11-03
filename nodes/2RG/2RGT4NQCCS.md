---
tag: 2RGT4NQCCS
kind: definition
name: Optimization problem
msc: [90C99, 90C30]
defines: NS0Q42Y3FX
uses: [0BSJ7RQ9BW, 0EPAT51DXQ, 1TTKMRW8PD, 5X1YMSR204, 0QF1MZ9FRG]
sources:
  - url: https://en.wikipedia.org/wiki/Optimization_problem
---

## Definition

An *optimization problem* (in minimization form) is given by a [[set|0BSJ7RQ9BW]] $X$, a subset $F \subseteq X$ and a [[function|0EPAT51DXQ]] $f \colon X \to \R$.
It is written
$$\text{minimize } f(x) \quad \text{subject to } x \in F.$$
The function $f$ is the *objective function* and $F$ is the [[feasible region|1TTKMRW8PD]].

1. A point $x^* \in F$ is an *optimal solution* (or *global minimizer*) if $f(x^*) \le f(x)$ for all $x \in F$.
2. The *optimal value* is the [[infimum|0QF1MZ9FRG]] $\inf \set{f(x) : x \in F}$ in $[-\infty, +\infty]$, with the convention $\inf \emptyset = +\infty$.
3. The problem is *infeasible* if $F = \emptyset$, and *unbounded* if its optimal value is $-\infty$.

A *maximization problem* "maximize $f(x)$ subject to $x \in F$" has the same optimal solutions as the minimization of $-f$ over $F$.

## Remarks

The optimal solutions are the points where $f$ restricted to $F$ attains its [[minimum|5X1YMSR204]].
Usually $F$ is described by [[constraints|X3663P90AE]], and the problem is written "minimize $f(x)$ subject to $g_i(x) \le 0$, $h_j(x) = 0$".

Example: minimize $f(x) = x^2 - 2x$ over $F = X = \R$.
Since $f(x) = (x - 1)^2 - 1 \ge -1 = f(1)$, the point $x^* = 1$ is the optimal solution and the optimal value is $-1$.

Non-example of an optimal solution: minimize $f(x) = x$ over $F = (0, 1]$.
The optimal value is $0$, but it is not attained, since every $x \in F$ has $f(x/2) < f(x)$ and $x/2 \in F$.
So this problem is feasible and bounded but has no optimal solution.

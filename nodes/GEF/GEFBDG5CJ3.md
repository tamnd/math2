---
tag: GEFBDG5CJ3
kind: statement
role: theorem
name: Steffensen's method
msc: [65H05, 65B99]
uses: [07EXVNF9VP, WF08BMN6Q6, YWZQC5E54B]
about: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Steffensen%27s_method
same_as:
  wikidata: Q7606635
  wikipedia: Steffensen's method
---

## Statement

Let $f$ be a real function that is twice continuously differentiable on an open interval $I$.
Let $r \in I$ be a simple zero of $f$, that is, $f(r) = 0$ and $f'(r) \ne 0$.
For $x$ with $f(x) \ne 0$, put
$$g(x) = \frac{f(x + f(x)) - f(x)}{f(x)}.$$
*Steffensen's method* is the iteration
$$x_{n+1} = x_n - \frac{f(x_n)}{g(x_n)},$$
stopped when $f(x_n) = 0$.
Then there is $\delta > 0$ such that for every $x_0$ with $\abs{x_0 - r} < \delta$ the iterates are defined and [[converge|YWZQC5E54B]] to $r$ quadratically.

## Remarks

The quantity $g(x)$ is a difference quotient of $f$ with step $h = f(x)$.
Near $r$ the step $f(x)$ is small, and $g(x) = f'(x) + O(f(x))$.
So the method behaves like [[Newton's method|07EXVNF9VP]], with an error in the slope of the same size as the current error, which keeps the order $2$.
Each step costs two evaluations of $f$ and no derivative.
The step is exactly [[Aitken's delta-squared process|WF08BMN6Q6]] applied to the points $x$, $\varphi(x)$, $\varphi(\varphi(x))$ of the fixed-point map $\varphi(x) = x + f(x)$.
The method needs $x_0$ close to $r$: when $f(x_0)$ is large, the point $x_0 + f(x_0)$ can be far away and the slope estimate is useless.

## Explanations

### L1 human

Newton's method needs the derivative.
Steffensen's method replaces it by the slope between $x$ and $x + f(x)$.
Near the root $f(x)$ is tiny, so this slope is very accurate, and the method is as fast as Newton's method.

### L2 human

It is the derivative-free counterpart of Newton's method, with the same quadratic order.
It also shows how convergence acceleration turns a linearly convergent fixed-point iteration into a quadratically convergent one.
Its basin of convergence is often smaller than that of Newton's method.

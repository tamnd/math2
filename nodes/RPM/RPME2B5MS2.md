---
tag: RPME2B5MS2
kind: statement
role: theorem
name: Halley's method
msc: [65H05]
uses: [07EXVNF9VP, YWZQC5E54B, 0F1WR9C83K]
about: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Halley%27s_method
same_as:
  wikidata: Q1476051
  wikipedia: Halley's method
---

## Statement

Let $f$ be a real function that is three times continuously differentiable on an open interval $I$.
Let $r \in I$ be a simple zero of $f$, that is, $f(r) = 0$ and $f'(r) \ne 0$.
*Halley's method* is the iteration
$$x_{n+1} = x_n - \frac{2 f(x_n) f'(x_n)}{2 f'(x_n)^2 - f(x_n) f''(x_n)}.$$
Then there is $\delta > 0$ such that for every $x_0$ with $\abs{x_0 - r} < \delta$ the iterates are defined and converge to $r$.
The [[convergence|YWZQC5E54B]] has order at least $3$:
$$\abs{x_{n+1} - r} \le C \abs{x_n - r}^3$$
for some constant $C$ and all $n$.

## Remarks

The step is [[Newton's method|07EXVNF9VP]] applied to $g = f / \sqrt{\abs{f'}}$.
At a simple zero, $g$ has the zero $r$ and satisfies $g''(r) = 0$, and Newton's method on such a function converges cubically.
The same formula can be written $x_{n+1} = x_n - \dfrac{f/f'}{1 - f f''/(2 f'^2)}$, evaluated at $x_n$.
Here $f'$ is the [[derivative|0F1WR9C83K]] of $f$.
For $f(x) = x^2 - a$ with $a > 0$, the method gives $x_{n+1} = x_n \dfrac{x_n^2 + 3a}{3x_n^2 + a}$, which roughly triples the number of correct digits of $\sqrt{a}$ per step near the root.
At a multiple zero the order of convergence drops to $1$.

## Explanations

### L1 human

Newton's method replaces the graph by a tangent line.
Halley's method also uses the second derivative, so it follows the bending of the graph.
Near a simple root, each step roughly triples the number of correct digits, against doubling for Newton's method.

### L2 human

Each step costs one evaluation of $f$, $f'$ and $f''$.
So it pays off when the second derivative is cheap, as for polynomials.
It is the case $d = 2$ of the Householder family of methods, whose case $d = 1$ is Newton's method.

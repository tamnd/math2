---
tag: 1YDR94WQMZ
kind: statement
role: theorem
name: Newton–Kantorovich theorem
msc: [65J15, 47J25]
uses: [06GZ956657, 06EH97V2A7, 07EXVNF9VP, 0AW1E6YTJY]
about: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Kantorovich_theorem
same_as:
  wikidata: Q2226698
  wikipedia: Kantorovich theorem
---

## Statement

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]], let $D \subseteq X$ be open, and let $F \colon D \to Y$ be [[Fréchet differentiable|06EH97V2A7]] with derivative $F'(x)$ at $x$.
Let $x_0 \in D$ be a point where $F'(x_0)$ is invertible with bounded inverse.
Assume that there are constants $\eta > 0$ and $L > 0$ such that:

1. $\norm{F'(x_0)^{-1} F(x_0)} \le \eta$;
2. $\norm{F'(x_0)^{-1} (F'(x) - F'(y))} \le L \norm{x - y}$ for all $x, y \in D$, a [[Lipschitz condition|0AW1E6YTJY]];
3. $h = L \eta \le \tfrac12$;
4. the closed ball $\bar B(x_0, t^*)$ lies in $D$, where $t^* = \dfrac{1 - \sqrt{1 - 2h}}{L}$.

Then the [[Newton iterates|07EXVNF9VP]] $x_{k+1} = x_k - F'(x_k)^{-1} F(x_k)$ are well defined, they lie in $\bar B(x_0, t^*)$, and they converge to a point $x^* \in \bar B(x_0, t^*)$ with $F(x^*) = 0$.

## Remarks

The proof compares the iterates with Newton's method for the real quadratic $p(t) = \tfrac{L}{2} t^2 - t + \eta$, started at $t_0 = 0$.
Those scalar iterates increase to the smallest root $t^*$ of $p$, and an induction shows $\norm{x_{k+1} - x_k} \le t_{k+1} - t_k$, so $(x_k)$ is a Cauchy sequence.
The quadratic $p$ has a real root exactly when $h \le \tfrac12$, which explains the condition on $h$.
If $h < \tfrac12$, the convergence is quadratic; if $h = \tfrac12$, it may be only linear.
Example: for $F(x) = x^2 - 2$ on $\R$ and $x_0 = 3/2$, one has $\eta = 1/12$ and $L = 2/3$ on $D = \R$, so $h = 1/18 \le 1/2$, and Newton's method converges to $\sqrt 2$.

## Explanations

### L1 human

Newton's method solves an equation by repeatedly replacing it with its linear approximation.
It can fail if the start is poor.
The Newton–Kantorovich theorem gives a test that uses only data at the starting point.
If the first Newton step is small compared with how fast the derivative can change, then the method converges.
The theorem also says in which ball the solution lies.

### L2 human

The theorem works in any Banach space, so it applies to nonlinear integral and differential equations, not only to systems in $\R^n$.
It is also an existence theorem: it proves that a solution exists near $x_0$ without knowing it in advance.
This is the basis of computer-assisted proofs, where $\eta$ and $L$ are bounded rigorously by interval arithmetic.
Compared with the Banach fixed point theorem, it needs a derivative but gives quadratic convergence when $h < \tfrac12$.

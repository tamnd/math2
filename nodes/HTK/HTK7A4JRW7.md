---
tag: HTK7A4JRW7
kind: statement
role: theorem
name: Crandall–Lions uniqueness theorem
msc: [49L25, 35D40, 35F21]
uses: [H1ERJ3T75T, 5TRXQKP7DY, 0M4JJT780X]
about: [H1ERJ3T75T, 5TRXQKP7DY]
sources:
  - url: https://en.wikipedia.org/wiki/Viscosity_solution
---

## Statement

Let $n \ge 1$, let $T > 0$, and let $H \colon \R^n \times \R^n \to \R$ be continuous, written $H(x, p)$.
Assume that there is a constant $C$ such that, for all $x, y, p, q \in \R^n$,
$$\abs{H(x, p) - H(x, q)} \le C \abs{p - q}, \qquad \abs{H(x, p) - H(y, p)} \le C \abs{x - y} (1 + \abs{p}).$$
Let $g \colon \R^n \to \R$ be bounded and [[uniformly continuous|0M4JJT780X]].
Consider the Cauchy problem for the [[Hamilton–Jacobi equation|5TRXQKP7DY]]
$$u_t + H(x, D_x u) = 0 \quad \text{in } \R^n \times (0, T), \qquad u(x, 0) = g(x) \quad \text{for } x \in \R^n.$$
Then this problem has at most one solution $u \colon \R^n \times [0, T] \to \R$ in the following sense.
The function $u$ is bounded and uniformly continuous, satisfies the initial condition, and is a [[viscosity solution|H1ERJ3T75T]] of the equation in $\R^n \times (0, T)$.

## Remarks

The theorem is a consequence of a comparison principle: if $u$ is a bounded uniformly continuous subsolution and $v$ a bounded uniformly continuous supersolution with $u(\cdot, 0) \le v(\cdot, 0)$, then $u \le v$.
The proof doubles the variables.
One maximises $u(x, t) - v(y, s) - \abs{x - y}^2 / \varepsilon - \abs{t - s}^2 / \varepsilon$ over pairs of points, after adding small extra terms that force a maximum to exist on the unbounded domain.
At the maximum point the two halves of the penalty serve as test functions for $u$ and for $v$, and the two inequalities of the definition are subtracted.
The Lipschitz hypotheses on $H$ make the error terms tend to $0$ with $\varepsilon$, which gives a contradiction if $u - v$ had a positive supremum.

Example: for $H(x, p) = \abs{p}$ the hypotheses hold with $C = 1$.
The unique bounded uniformly continuous viscosity solution is given by the Hopf–Lax formula $u(x, t) = \min_{\abs{y - x} \le t} g(y)$.

The viscosity sense is needed.
For $H(x, p) = \abs{p}$ and $g = 0$, both $u = 0$ and $w(x, t) = \min(0, \abs{x} - t)$ (with $n = 1$) are Lipschitz and satisfy the equation almost everywhere.
Only $u = 0$ is a viscosity solution: at a point $(0, t)$ the function $w - \varphi$ with $\varphi(x, s) = -s$ has a local minimum, while $\varphi_t + \abs{\varphi_x} = -1 < 0$.

## Explanations

### L1 human

Hamilton–Jacobi equations usually have no smooth solutions, and they have many solutions that hold only almost everywhere.
Viscosity solutions are a way to choose the right one.
This theorem says the choice is never ambiguous: given the initial data, there is only one viscosity solution.

### L2 human

Uniqueness is what makes viscosity solutions useful in control theory.
To show that a value function equals a given formula, it is enough to check that both are viscosity solutions of the same Hamilton–Jacobi–Bellman equation with the same data.
The same doubling-of-variables argument gives comparison for stationary equations such as $u + H(x, Du) = 0$, and, with more work, for second-order degenerate elliptic equations.
Existence comes separately, for instance from the value function of a control problem or from the vanishing viscosity method.

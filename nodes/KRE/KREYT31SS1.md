---
tag: KREYT31SS1
kind: statement
role: theorem
name: Viscosity solution of the Hamilton–Jacobi–Bellman equation
msc: [49L25, 49L12, 35F21]
uses: [K6G0DRQ3CP, SJP9HW82VX, H1ERJ3T75T, 0R6EWFKRCF]
about: [K6G0DRQ3CP, SJP9HW82VX, H1ERJ3T75T]
sources:
  - url: https://en.wikipedia.org/wiki/Viscosity_solution
---

## Statement

Let $U \subseteq \R^m$ be a nonempty [[compact set|0R6EWFKRCF]] and $T > 0$.
Let $f \colon [0, T] \times \R^n \times U \to \R^n$ and $L \colon [0, T] \times \R^n \times U \to \R$ be bounded and continuous.
Assume that both are Lipschitz in $x$, uniformly in $(t, u)$, and let $g \colon \R^n \to \R$ be bounded and Lipschitz.
Let $V$ be the [[value function|K6G0DRQ3CP]] of the problem of minimizing $\int_t^T L(s, y, u) \, ds + g(y(T))$ subject to $y' = f(s, y, u)$, $y(t) = x$.
Let $H(t, x, p) = \max_{u \in U} \big( -p \cdot f(t, x, u) - L(t, x, u) \big)$.
Then $V$ is bounded and Lipschitz on $[0, T] \times \R^n$, $V(T, \cdot) = g$, and $V$ is a [[viscosity solution|H1ERJ3T75T]] of the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]]
$$-V_t + H(t, x, \nabla_x V) = 0 \quad \text{in } (0, T) \times \R^n.$$
That is, for every $C^1$ function $\varphi$ on $(0, T) \times \R^n$ and every point $(t_0, x_0) \in (0, T) \times \R^n$:

1. if $V - \varphi$ has a local maximum at $(t_0, x_0)$, then $-\varphi_t(t_0, x_0) + H(t_0, x_0, \nabla_x \varphi(t_0, x_0)) \le 0$;
2. if $V - \varphi$ has a local minimum at $(t_0, x_0)$, then $-\varphi_t(t_0, x_0) + H(t_0, x_0, \nabla_x \varphi(t_0, x_0)) \ge 0$.

## Remarks

The proof uses the dynamic programming principle.
If $V - \varphi$ has a local maximum at $(t_0, x_0)$, use a constant control $u$ on $[t_0, t_0 + h]$: the principle gives $\varphi(t_0, x_0) - \varphi(t_0 + h, y(t_0 + h)) \le \int_{t_0}^{t_0 + h} L \, ds$.
Dividing by $h$ and letting $h \to 0$ gives $-\varphi_t - \nabla_x \varphi \cdot f(t_0, x_0, u) - L(t_0, x_0, u) \le 0$ for every $u \in U$, which is condition 1.
Condition 2 uses nearly optimal controls in the same way, with the compactness of $U$.
Example: for $f = u$, $U = [-1, 1]$, $L = 0$ and $g(x) = \abs{x}$, the value function $\max(\abs{x} - (T - t), 0)$ is not differentiable, yet it is a viscosity solution of $-V_t + \abs{V_x} = 0$.
Here $g$ is unbounded, but one checks the two conditions directly at the corners.
By the comparison principle of Crandall and Lions, $V$ is the only bounded uniformly continuous viscosity solution with $V(T, \cdot) = g$.
So the equation characterizes the value function even when no classical solution exists.

## Explanations

### L1 human

The optimal cost of a control problem should satisfy the Hamilton–Jacobi–Bellman equation, but it often has corners where derivatives do not exist.
This theorem says that it still satisfies the equation in the weak sense of viscosity solutions.
Together with uniqueness, it shows that the equation determines the optimal cost completely.

### L2 human

The theorem is the bridge between optimal control and the theory of viscosity solutions.
Smooth test functions $\varphi$ touching $V$ from above or below replace the missing derivatives of $V$.
Combined with the comparison principle, it gives convergence proofs for numerical schemes, which only need to be monotone, stable and consistent.
It also explains why the verification theorem for smooth solutions is not enough in general.

---
tag: T5BEKMG5W8
kind: statement
role: theorem
name: Verification theorem
msc: [49L20, 49L12, 49K15]
uses: [K6G0DRQ3CP, QPS8VSJGMJ, SJP9HW82VX, ZPDTVZQN5K, HR720TJZZR, KREYT31SS1]
about: [K6G0DRQ3CP, SJP9HW82VX]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi–Bellman_equation
---

## Statement

Let $U \subseteq \R^m$ be a nonempty compact set and $T > 0$.
Let $f \colon [0, T] \times \R^n \times U \to \R^n$ be continuous and Lipschitz in $x$ uniformly in $(t, u)$, and let $L$ and $g$ be continuous.
Let $V$ be the [[value function|K6G0DRQ3CP]] of the problem of minimizing $\int_t^T L(s, y, u) \, ds + g(y(T))$ subject to $y' = f(s, y, u)$, $y(t) = x$.
Let $W \colon [0, T] \times \R^n \to \R$ be continuous, of class $C^1$ on $(0, T) \times \R^n$, with $W(T, x) = g(x)$.
Assume that $W$ solves the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]]
$$W_t(t, x) + \min_{u \in U} \big( L(t, x, u) + \nabla_x W(t, x) \cdot f(t, x, u) \big) = 0 \quad \text{on } (0, T) \times \R^n.$$
Then:

1. $W(t, x) \le V(t, x)$ for all $(t, x) \in [0, T] \times \R^n$.
2. Let $u^*$ be a measurable control on $[t, T]$ with trajectory $y^*$ from $(t, x)$. Suppose that for almost every $s \in [t, T]$ the value $u^*(s)$ attains the minimum in the equation at $(s, y^*(s))$. Then $u^*$ is optimal from $(t, x)$, and $W(t, x) = V(t, x)$.

## Remarks

The proof is a chain rule computation.
For any control $u$ with trajectory $y$, the function $s \mapsto W(s, y(s))$ is absolutely continuous with derivative $W_t + \nabla_x W \cdot f(s, y, u) \ge -L(s, y, u)$ by the equation.
Integrating from $t$ to $T$ gives $g(y(T)) - W(t, x) \ge -\int_t^T L \, ds$, that is, $W(t, x) \le J(t, x; u)$.
For $u^*$ the inequality is an equality at almost every time, so $J(t, x; u^*) = W(t, x) \le V(t, x)$.
Example: for the [[linear-quadratic regulator|HR720TJZZR]], $W(t, x) = x^{T} P(t) x$ with $P$ the solution of the Riccati differential equation solves the equation with $U = \R^m$.
The minimum is attained at $u = -R^{-1} B^{T} P(t) x$, so this feedback is optimal; the proof adapts to the unbounded control set.
The smoothness of $W$ is essential: value functions are often not differentiable, and then one needs the theory of [[viscosity solutions|KREYT31SS1]].

## Explanations

### L1 human

Suppose someone hands you a candidate function for the optimal cost and a candidate control.
The verification theorem gives a test: if the function solves the Hamilton–Jacobi–Bellman equation and the control achieves the minimum in it, then the control is optimal.
It turns a guess into a proof of optimality.

### L2 human

The theorem is the sufficiency half of [[dynamic programming|QPS8VSJGMJ]].
It is the standard way to prove that a feedback law found by solving the HJB equation, for example the linear feedback of the linear-quadratic regulator, is truly optimal.
Pontryagin's maximum principle gives only necessary conditions, so the verification theorem complements it.
When the value function is not smooth, versions of the theorem use viscosity solutions or generalized gradients.

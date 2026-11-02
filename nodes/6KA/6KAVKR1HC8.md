---
tag: 6KAVKR1HC8
kind: definition
name: Stochastic optimal control
msc: ["93E20", 49L20]
defines: B24T6DQCDR
uses: [B219G9SHJA, 22735FGJV6, HNK1Y62G7V, 0WQNRCNY3M, 0QNVQ4VD9T, SJP9HW82VX]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_control
---

## Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, P)$ be a probability space with a [[filtration|HNK1Y62G7V]] that carries a $d$-dimensional [[Wiener process|22735FGJV6]] $W$.
Let $T > 0$ and let $U \subseteq \R^m$ be a nonempty closed set, the control set.
Let $b \colon \R^n \times U \to \R^n$ and $\sigma \colon \R^n \times U \to \R^{n \times d}$ be continuous.
Assume that they are [[Lipschitz|0QNVQ4VD9T]] in $x$ uniformly in $u$, and that $\abs{b(x, u)} + \abs{\sigma(x, u)} \le K (1 + \abs{x} + \abs{u})$ for a constant $K$.
Let $f \colon \R^n \times U \to \R$ and $g \colon \R^n \to \R$ be continuous with $\abs{f(x, u)} \le K (1 + \abs{x}^2 + \abs{u}^2)$ and $\abs{g(x)} \le K (1 + \abs{x}^2)$.

1. An *admissible control* is a progressively measurable process $u = (u_t)_{0 \le t \le T}$ with values in $U$ and $E \int_0^T \abs{u_t}^2 \, dt < \infty$.
2. For an admissible control $u$ and $x \in \R^n$, the *state* is the solution $X^u$ of the [[stochastic differential equation|B219G9SHJA]] $dX_t = b(X_t, u_t) \, dt + \sigma(X_t, u_t) \, dW_t$ with $X_0 = x$.
3. The *cost* of $u$ is $J(x; u) = E\left[ \int_0^T f(X^u_t, u_t) \, dt + g(X^u_T) \right]$, an [[expected value|0WQNRCNY3M]].

The *stochastic optimal control problem* is to find an admissible control $u^*$ with $J(x; u^*) = \inf_u J(x; u)$, the infimum over all admissible controls.
Such a $u^*$ is an *optimal control*, and $V(x) = \inf_u J(x; u)$ is the *value*.

## Remarks

Under these hypotheses the state equation has a unique strong solution and the cost is finite.
Starting the problem at time $t$ in state $x$ gives the value function $V(t, x)$.
When $V$ is smooth enough, it solves the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]]
$$V_t + \min_{u \in U} \left\{ b(x, u) \cdot \nabla_x V + \tfrac{1}{2} \tr\left( \sigma \sigma^T(x, u) D_x^2 V \right) + f(x, u) \right\} = 0, \qquad V(T, x) = g(x).$$
With $\sigma = 0$ the problem is a deterministic optimal control problem.

Example: $n = m = d = 1$, $U = \R$, $b(x, u) = u$, $\sigma = 1$, $f(x, u) = u^2 / 2$ and $g(x) = x^2 / 2$.
The function $V(t, x) = \dfrac{x^2}{2 (1 + T - t)} + \dfrac{1}{2} \ln(1 + T - t)$ satisfies $V(T, x) = x^2 / 2$.
The minimum over $u$ of $u V_x + u^2 / 2$ is $-\frac{1}{2} V_x^2$, attained at $u = -V_x$.
With $s = 1 + T - t$, one has $V_t = \frac{x^2}{2 s^2} - \frac{1}{2 s}$, $\frac{1}{2} V_x^2 = \frac{x^2}{2 s^2}$ and $\frac{1}{2} V_{xx} = \frac{1}{2 s}$, so the equation holds.
The optimal control is the feedback $u_t = -X_t / (1 + T - t)$.

Non-example: the process $u_t = W_T$ for all $t$ is not admissible, because it is not adapted: it uses the future of the noise.

## Explanations

### L1 human

The controller picks its action at each time using only what it has seen so far.
The noise makes the cost random, so one minimises its average.

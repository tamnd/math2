---
tag: SAH0W43RMW
kind: definition
name: Model predictive control
msc: [93B45, 49N35, 93C55]
defines: 15Z6BT9XYR
uses: [T3V6ZNAMDN, ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Model_predictive_control
---

## Definition

Let $f \colon \R^n \times \R^m \to \R^n$ define the discrete-time [[control system|ZPDTVZQN5K]] $x_{k+1} = f(x_k, u_k)$.
Let $\mathbb{X} \subseteq \R^n$, $\mathbb{U} \subseteq \R^m$ and $\mathbb{X}_f \subseteq \mathbb{X}$ be constraint sets.
Let $\ell \colon \R^n \times \R^m \to \R$ be a stage cost, let $V_f \colon \R^n \to \R$ be a terminal cost, and let $N \ge 1$ be the horizon.
For $x \in \R^n$, let $P_N(x)$ be the problem: minimise
$$\sum_{i=0}^{N-1} \ell(z_i, v_i) + V_f(z_N)$$
over $v_0, \dots, v_{N-1} \in \mathbb{U}$, subject to $z_0 = x$, $z_{i+1} = f(z_i, v_i)$, $z_i \in \mathbb{X}$ for $i < N$, and $z_N \in \mathbb{X}_f$.
Assume that $P_N(x)$ has a minimiser $(v_0^*(x), \dots, v_{N-1}^*(x))$ for each $x$ in a set $\mathcal{X}_N$, and fix a choice of it.
The *model predictive control law* is $\kappa_N(x) = v_0^*(x)$ for $x \in \mathcal{X}_N$.
*Model predictive control* operates the system in closed loop by $u_k = \kappa_N(x_k)$: at each time $k$ it solves $P_N(x_k)$ and applies only the first control.

## Remarks

The problem $P_N(x)$ is a finite-horizon [[optimal control|T3V6ZNAMDN]] problem, and the horizon moves forward with time, hence the name receding-horizon control.
Stability of the closed loop is not automatic.
Standard sufficient conditions ask for a terminal set $\mathbb{X}_f$ that is invariant under some local controller.
They also ask for a terminal cost $V_f$ that decreases along this controller by at least the stage cost.
Then the optimal value of $P_N$ is a Lyapunov function of the closed loop.

Example: $n = m = 1$, $f(x, u) = x + u$, no constraints, $\ell(x, u) = x^2 + u^2$, $N = 1$ and $V_f(z) = z^2$.
Then $P_1(x)$ minimises $x^2 + v^2 + (x + v)^2$, whose minimiser is $v = -x/2$.
So $\kappa_1(x) = -x/2$, and the closed loop $x_{k+1} = x_k / 2$ converges to $0$.

Non-example of a stabilising choice: in the same setting with $V_f = 0$, the problem minimises $x^2 + v^2$, so $\kappa_1(x) = 0$.
The closed loop is $x_{k+1} = x_k$, which does not converge to $0$, although each step is optimal for the short horizon.

## Explanations

### L1 human

At each time the controller plans the best moves over the next $N$ steps, applies the first one, observes the new state, and plans again.

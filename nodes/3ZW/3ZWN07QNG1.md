---
tag: 3ZWN07QNG1
kind: definition
name: Moving horizon estimation
msc: ["93E10", 93B45, 93C55]
defines: QJ59HPYQ9D
uses: [0BYTQ4X1HC, TQ7E9S194T]
sources:
  - url: https://en.wikipedia.org/wiki/Moving_horizon_estimation
---

## Definition

Consider a discrete-time system with state $x_k \in \R^n$, known input $u_k$ and measurement $y_k \in \R^p$:
$$x_{k+1} = f(x_k, u_k) + w_k, \qquad y_k = h(x_k) + v_k.$$
Here $w_k$ is an unknown process disturbance and $v_k$ is an unknown measurement error.
Fix a horizon length $N \ge 1$ and constraint sets $\mathbb{X} \subseteq \R^n$ and $\mathbb{W} \subseteq \R^n$.
Fix nonnegative stage costs $\ell_w$ and $\ell_v$, and an arrival cost $\Gamma_k \colon \R^n \to [0, \infty)$ for each $k$.
At a time $T \ge N$, the *moving horizon estimation* problem is to minimize
$$\Gamma_{T-N}(z_{T-N}) + \sum_{k=T-N}^{T-1} \ell_w(\omega_k) + \sum_{k=T-N}^{T} \ell_v\big(y_k - h(z_k)\big)$$
over $z_{T-N}, \dots, z_T \in \R^n$ and $\omega_{T-N}, \dots, \omega_{T-1} \in \R^n$, subject to:

1. $z_{k+1} = f(z_k, u_k) + \omega_k$ for $T-N \le k \le T-1$;
2. $z_k \in \mathbb{X}$ for $T-N \le k \le T$;
3. $\omega_k \in \mathbb{W}$ for $T-N \le k \le T-1$.

If $(z^*, \omega^*)$ is a minimizer, the moving horizon estimate of $x_T$ is $\hat{x}_T = z^*_T$.

## Remarks

The usual choice is quadratic: $\ell_w(\omega) = \omega^{T} Q^{-1} \omega$ and $\ell_v(e) = e^{T} R^{-1} e$ with positive definite $Q$ and $R$, so each step is a constrained [[least squares|0BYTQ4X1HC]] problem.
The arrival cost $\Gamma_{T-N}$ summarizes the data before the window, often as $(z - \bar{x})^{T} P^{-1} (z - \bar{x})$ with a prior estimate $\bar{x}$ and a positive definite matrix $P$ taken from a filter.
Example: take $f(x, u) = A x + B u$, $h(x) = C x$, no constraints and quadratic costs.
Take the arrival cost $(z - \bar{x})^{T} P^{-1} (z - \bar{x})$, where $\bar{x}$ and $P$ are the Kalman filter prediction of $x_{T-N}$ and its covariance, computed from the data before time $T - N$.
Then $\hat{x}_T$ equals the [[Kalman filter|DFM9YXF9AG]] estimate.
Indeed both come from the minimizer of the same quadratic function of the trajectory, which the Kalman recursion computes step by step.
Non-example: full information estimation uses all data from time $0$, so its window grows with $T$.
Its cost per step is not bounded, and it is not a moving horizon method.
Like any [[state observer|TQ7E9S194T]], the method yields an estimate of the current state from past inputs and outputs.

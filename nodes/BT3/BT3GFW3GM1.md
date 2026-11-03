---
tag: BT3GFW3GM1
kind: definition
name: Dual control theory
msc: ["93E20", "93E35", 93C41]
defines: 7R4X50J54S
uses: [B24T6DQCDR, 0TTDGTEFMN]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_control_theory
---

## Definition

Consider a discrete-time stochastic system on the horizon $k = 0, \dots, T$.
It has state $x_k$, control $u_k$, unknown parameter $\theta$, and measurement $y_k$:
$$x_{k+1} = f(x_k, u_k, \theta, w_k), \qquad y_k = h(x_k, v_k).$$
Here $x_0$, $\theta$, and the noises $w_k$ and $v_k$ are random with a known joint law.
The information available at time $k$ is $I_k = (y_0, \dots, y_k, u_0, \dots, u_{k-1})$.
An admissible policy is a sequence of measurable maps $\mu_k$ with $u_k = \mu_k(I_k)$.
The *dual control problem* is to find an admissible policy that minimizes
$$E\Big[\sum_{k=0}^{T-1} g(x_k, u_k) + g_T(x_T)\Big].$$
An optimal policy of this problem is a *dual control*.
A control $u_k$ has a *dual effect* when it can change the future uncertainty of the state, and not only its expected value.
That is, $u_k$ can change the conditional covariance of $(x_j, \theta)$ given $I_j$ for some $j > k$.

## Remarks

The problem is a partially observed [[stochastic optimal control|B24T6DQCDR]] problem.
Dynamic programming solves it over the hyperstate, the [[conditional|0TTDGTEFMN]] law of $(x_k, \theta)$ given $I_k$, which is in general infinite-dimensional.
The optimal control then balances the expected cost with the value of the information that the control will produce.
Example: $x_{k+1} = x_k + \theta u_k + w_k$ with $\theta$ unknown and $y_k = x_k$.
The input $u_k$ affects how well $\theta$ can be estimated from $y_{k+1} - y_k$, so the control has a dual effect.
For a quadratic cost, the optimal policy is in general not the certainty-equivalent one.
Non-example: the certainty-equivalence controller computes $u_k$ as the optimal control for known parameters, with the estimate of $\theta$ put in place of $\theta$.
It is admissible but ignores the effect of $u_k$ on future information, so it is in general not optimal.
In the linear-quadratic-Gaussian problem with known parameters, the control has no dual effect, and the [[separation principle|TMEKPXMC7V]] makes certainty equivalence optimal.

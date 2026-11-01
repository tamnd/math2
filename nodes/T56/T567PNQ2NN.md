---
tag: T567PNQ2NN
kind: definition
name: Doléans-Dade exponential
msc: [60H05, 60G44]
defines: 3D88622PBQ
uses: [4EJB6E2AZK, JA95NH206E, X4DHMZD5JA, 22735FGJV6, 2J1RVQB0CM, XC2YPC2BSW]
sources:
  - url: https://en.wikipedia.org/wiki/Dol%C3%A9ans-Dade_exponential
---

## Definition

Let $X$ be a real [[semimartingale|4EJB6E2AZK]] on a filtered probability space.
The *Doléans-Dade exponential* of $X$ is the unique semimartingale $Z = \mathcal{E}(X)$ such that, for all $t \ge 0$,
$$Z_t = 1 + \int_0^t Z_{s-} \, dX_s.$$
Here the integral is the stochastic integral of [[Itô calculus|JA95NH206E]].
The process $Z_{s-}$ is the left limit of $Z$ at $s$.

## Remarks

If $X$ is continuous, then $\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \tfrac12 [X]_t\right)$, where $[X]$ is the [[quadratic variation|X4DHMZD5JA]] of $X$.
In general, $\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \tfrac12 [X]^c_t\right) \prod_{0 < s \le t} (1 + \Delta X_s) e^{-\Delta X_s}$, where $[X]^c$ is the continuous part of $[X]$ and $\Delta X_s = X_s - X_{s-}$.
Example: let $B$ be a [[Brownian motion|22735FGJV6]] and $X = \sigma B$ with a constant $\sigma$.
Then $Z_t = \exp(\sigma B_t - \tfrac12 \sigma^2 t)$, and [[Itô's lemma|2J1RVQB0CM]] gives $dZ_t = \sigma Z_t \, dB_t = Z_t \, dX_t$.
Non-example: $W_t = \exp(\sigma B_t)$ fails the equation, since Itô's lemma gives $dW_t = W_t \, dX_t + \tfrac12 \sigma^2 W_t \, dt$.
If $X$ is a continuous [[local martingale|XC2YPC2BSW]], then $\mathcal{E}(X)$ is a positive local martingale and hence a supermartingale.
It is a true martingale under Novikov's condition $E\left[\exp\left(\tfrac12 [X]_\infty\right)\right] < \infty$.

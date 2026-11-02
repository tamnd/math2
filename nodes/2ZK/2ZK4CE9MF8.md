---
tag: 2ZK4CE9MF8
kind: statement
role: theorem
name: Wold's decomposition theorem
msc: [60G10, 62M10, 62M20]
uses: [DT0QXJE705, HM2HHE3J51, 0B8KZRT28M, PEB9DN0AHA]
about: [DT0QXJE705]
sources:
  - url: https://en.wikipedia.org/wiki/Wold%27s_theorem
same_as:
  wikidata: Q2588432
  wikipedia: Wold's theorem
---

## Statement

Let $(X_t)_{t \in \Z}$ be a real weakly [[stationary process|DT0QXJE705]] with mean $0$.
Let $L^2$ be the [[Hilbert space|HM2HHE3J51]] of square-integrable random variables.
For $s \in \Z$, let $H_s$ be the closed linear span of $\set{X_r : r \le s}$ in $L^2$.
Let $P_s$ be the [[orthogonal projection|0B8KZRT28M]] onto $H_s$.
Assume that the one-step prediction error variance $\sigma^2 = E[(X_t - P_{t-1} X_t)^2]$ is positive.
Then
$$X_t = \sum_{j=0}^{\infty} \psi_j \varepsilon_{t-j} + V_t \qquad \text{for all } t \in \Z,$$
where:

1. $\varepsilon_t = X_t - P_{t-1} X_t$, and $(\varepsilon_t)$ is a white noise with variance $\sigma^2$: mean $0$, variance $\sigma^2$, pairwise uncorrelated.
2. $\psi_0 = 1$, $\sum_{j \ge 0} \psi_j^2 < \infty$, and $\psi_j = E[X_t \varepsilon_{t-j}] / \sigma^2$.
3. $E[\varepsilon_s V_t] = 0$ for all $s, t \in \Z$.
4. $V_t$ lies in $\bigcap_{s \in \Z} H_s$, and $(V_t)$ is deterministic: $V_t = P_{s} V_t$ for all $s$, so it is predicted without error from its own remote past.

The sequences $(\psi_j)$, $(\varepsilon_t)$ and $(V_t)$ are uniquely determined by these conditions.

## Remarks

The idea is to split $H_t$ orthogonally into the innovations $\varepsilon_t, \varepsilon_{t-1}, \dots$, which are orthogonal to each other, and the remote past $\bigcap_s H_s$.
The first sum is the projection of $X_t$ onto the closed span of the innovations, with coefficients given by inner products.
The remainder $V_t$ is the projection onto the remote past.
The process is called purely nondeterministic when $V_t = 0$; then $X_t$ is a [[moving-average model|PEB9DN0AHA]] of infinite order.
Example: a causal AR($1$) process $X_t = \phi X_{t-1} + \varepsilon_t$ with $\abs{\phi} < 1$ has $\psi_j = \phi^j$ and $V_t = 0$.
Example of a deterministic process: let $A$ and $B$ be uncorrelated with mean $0$ and variance $1$, let $0 < \lambda < \pi$, and let $X_t = A \cos(\lambda t) + B \sin(\lambda t)$.
This process is weakly stationary, and any two consecutive values determine $A$ and $B$, so $X_t$ lies in every $H_s$ and $\sigma^2 = 0$; the whole process is its own deterministic part.
The coefficients $\psi_j$ need not be absolutely summable, and the shocks $\varepsilon_t$ are only uncorrelated, not independent in general.

## Explanations

### L1 human

Any stationary series can be split into two parts that do not interact.
One part is fully predictable from the distant past, like a fixed periodic wave.
The other part is built from a sequence of unpredictable surprises, each passed on to the future with fading weights.
So, as far as linear prediction goes, every stationary series looks like a moving average of white noise plus a predictable part.

### L2 human

The theorem justifies the use of linear models, such as ARMA models, for stationary series: they are finite-parameter approximations of the infinite moving average in the decomposition.
The innovations $\varepsilon_t$ are the one-step prediction errors, which is why residual checks in model fitting test them for whiteness.
The proof is pure Hilbert space geometry: only means and covariances enter, so the result says nothing about nonlinear dependence.
It was proved by Herman Wold in his 1938 thesis.

---
tag: 5QJTQ3S6ZP
kind: definition
name: Kalman–Bucy filter
msc: ["93E11", 60G35, 60H10]
defines: P9ECW9MXYX
uses: [B219G9SHJA, 22735FGJV6, 0XN3K7RSZY, 0TTDGTEFMN, 0VT2QK6X6Q, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
---

## Definition

Let $A$, $G$, $C$, $D$ be real matrices of sizes $n \times n$, $n \times q$, $p \times n$ and $p \times p$, with $D$ invertible.
Let $W$ and $V$ be independent standard [[Wiener processes|22735FGJV6]] in $\R^q$ and $\R^p$.
Let $X_0$ be [[Gaussian|0XN3K7RSZY]] with mean $m_0$ and covariance $P_0$, independent of $W$ and $V$.
The state $X_t \in \R^n$ and the observation $Z_t \in \R^p$, $t \ge 0$, solve the [[stochastic differential equations|B219G9SHJA]]
$$dX_t = A X_t\, dt + G\, dW_t, \qquad dZ_t = C X_t\, dt + D\, dV_t, \qquad Z_0 = 0.$$
Put $Q = G G^T$ and $R = D D^T$, which is [[positive definite|0KX66CZMBB]].
Let $P_t$ be the solution of the matrix [[Riccati equation|0VT2QK6X6Q]]
$$P_t' = A P_t + P_t A^T + Q - P_t C^T R^{-1} C P_t, \qquad P_0 \text{ given},$$
and put $K_t = P_t C^T R^{-1}$.
The *Kalman–Bucy filter* is the process $\hat X_t$ that solves
$$d\hat X_t = A \hat X_t\, dt + K_t \big(dZ_t - C \hat X_t\, dt\big), \qquad \hat X_0 = m_0.$$

## Remarks

Under these assumptions $\hat X_t = \mathbb{E}[X_t \mid Z_s, 0 \le s \le t]$, and $P_t$ is the covariance matrix of the error $X_t - \hat X_t$; the conditional distribution of $X_t$ is Gaussian with these parameters.
The Riccati equation has a unique solution on $[0, \infty)$, symmetric and positive semidefinite.
Example: for $n = p = 1$, $A = 0$, $G = 0$, $C = 1$, $D = 1$, the state is a constant $X_0$ observed in white noise.
Then $P_t' = -P_t^2$, so $P_t = P_0/(1 + P_0 t)$, and the error variance decays like $1/t$, as for an average of $t$ independent measurements.
The term $dZ_t - C \hat X_t\, dt$ is the innovation; it is the increment of a Wiener process with covariance $R$ with respect to the observation filtration.
If $(A, G)$ is stabilizable and $(C, A)$ is detectable, $P_t$ converges to the stabilizing solution of the algebraic Riccati equation, and the filter becomes time-invariant.

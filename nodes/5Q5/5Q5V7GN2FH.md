---
tag: 5Q5V7GN2FH
kind: definition
name: Kalman filter
msc: ["93E11", 60G35, 62M20]
defines: DFM9YXF9AG
uses: [0XN3K7RSZY, 0V7G6WMFK0, 0TTDGTEFMN, 0KX66CZMBB, D4Q8VM7826]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
---

## Definition

Let $n, p \ge 1$.
Let $F_k$ and $H_k$, $k \ge 1$, be known real matrices of sizes $n \times n$ and $p \times n$.
The states $x_k \in \R^n$ and the measurements $z_k \in \R^p$ are random vectors with
$$x_k = F_k x_{k-1} + w_k, \qquad z_k = H_k x_k + v_k \qquad (k \ge 1).$$
The initial state $x_0$ is [[Gaussian|0XN3K7RSZY]] with mean $\hat x_{0|0}$ and [[covariance matrix|0V7G6WMFK0]] $P_{0|0}$.
The noises $w_k$ and $v_k$ are Gaussian with mean $0$ and covariances $Q_k$ and $R_k$, with $R_k$ [[positive definite|0KX66CZMBB]].
The random vectors $x_0, w_1, v_1, w_2, v_2, \dots$ are independent.
The *Kalman filter* is the recursion that, for $k = 1, 2, \dots$, computes:

1. the prediction $\hat x_{k|k-1} = F_k \hat x_{k-1|k-1}$ and $P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k$;
2. the gain $K_k = P_{k|k-1} H_k^T \big(H_k P_{k|k-1} H_k^T + R_k\big)^{-1}$;
3. the update $\hat x_{k|k} = \hat x_{k|k-1} + K_k \big(z_k - H_k \hat x_{k|k-1}\big)$ and $P_{k|k} = (I - K_k H_k) P_{k|k-1}$.

## Remarks

Under these assumptions, the conditional distribution of $x_k$ given $z_1, \dots, z_k$ is Gaussian with mean $\hat x_{k|k}$ and covariance $P_{k|k}$, so $\hat x_{k|k}$ is the [[conditional expectation|0TTDGTEFMN]] $\mathbb{E}[x_k \mid z_1, \dots, z_k]$.
Likewise $\hat x_{k|k-1}$ and $P_{k|k-1}$ are the conditional mean and covariance of $x_k$ given $z_1, \dots, z_{k-1}$.
Without the Gaussian assumption, but with the same means and covariances, $\hat x_{k|k}$ is still the best estimate among those that are affine in $z_1, \dots, z_k$.
Example: let $n = p = 1$, $F_k = H_k = 1$, $Q_k = 0$, $R_k = r > 0$, $\hat x_{0|0} = 0$ and $P_{0|0} = q > 0$; this is a constant unknown observed with noise.
Then $1/P_{k|k} = 1/q + k/r$ and $\hat x_{k|k} = (z_1 + \cdots + z_k)/(k + r/q)$, as one checks by induction on $k$.
For a vague prior, $q \to \infty$, the estimate becomes the running average of the measurements.
The quantity $z_k - H_k \hat x_{k|k-1}$ is called the innovation.
The recursion for $P$ does not depend on the data and is a [[Riccati difference equation|D4Q8VM7826]].

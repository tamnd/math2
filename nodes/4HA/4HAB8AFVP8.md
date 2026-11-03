---
tag: 4HAB8AFVP8
kind: definition
name: Extended Kalman filter
msc: ["93E11", 60G35, 93C10]
defines: 3E6E4VQGFJ
uses: [DFM9YXF9AG, 047NDTEPCV, 0V7G6WMFK0, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_Kalman_filter
---

## Definition

Let $f \colon \R^n \to \R^n$ and $h \colon \R^n \to \R^p$ be continuously differentiable.
Let $w_k$ and $v_k$, $k \ge 1$, be independent noises with mean $0$ and [[covariance matrices|0V7G6WMFK0]] $Q_k$ and $R_k$, with $R_k$ [[positive definite|0KX66CZMBB]].
Consider the model
$$x_k = f(x_{k-1}) + w_k, \qquad z_k = h(x_k) + v_k \qquad (k \ge 1).$$
Let an initial estimate $\hat x_{0|0}$ and a symmetric positive semidefinite matrix $P_{0|0}$ be given.
The *extended Kalman filter* is the recursion that, for $k = 1, 2, \dots$, computes:

1. the prediction $\hat x_{k|k-1} = f(\hat x_{k-1|k-1})$ and $P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k$, where $F_k$ is the [[Jacobian matrix|047NDTEPCV]] of $f$ at $\hat x_{k-1|k-1}$;
2. the gain $K_k = P_{k|k-1} H_k^T \big(H_k P_{k|k-1} H_k^T + R_k\big)^{-1}$, where $H_k$ is the Jacobian matrix of $h$ at $\hat x_{k|k-1}$;
3. the update $\hat x_{k|k} = \hat x_{k|k-1} + K_k \big(z_k - h(\hat x_{k|k-1})\big)$ and $P_{k|k} = (I - K_k H_k) P_{k|k-1}$.

## Remarks

If $f$ and $h$ are linear, $f(x) = F x$ and $h(x) = H x$, then $F_k = F$, $H_k = H$, and the recursion is the [[Kalman filter|DFM9YXF9AG]].
In general $\hat x_{k|k}$ is only an approximation of the conditional mean, and $P_{k|k}$ is only an approximation of the error covariance.
Example: for $n = p = 1$, $f(x) = x$ and $h(x) = x^3$, the gain at step $k$ uses $H_k = 3 \hat x_{k|k-1}^2$.
Non-example of good behaviour: in this example, if $\hat x_{k|k-1} = 0$, then $H_k = 0$, so $K_k = 0$ and the measurement $z_k$ is ignored, even though it carries information about $x_k$ when $x_k \ne 0$.

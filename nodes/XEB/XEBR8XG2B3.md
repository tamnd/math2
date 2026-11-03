---
tag: XEBR8XG2B3
kind: definition
name: Four-dimensional variational assimilation
msc: [86A22, 49N45, 65K10]
defines: RW98W3R424
uses: [TKT0QAPWW8, T3V6ZNAMDN, 0R9NMSM1ZP, 047NDTEPCV]
sources:
  - url: https://en.wikipedia.org/wiki/Data_assimilation
---

## Definition

Let $t_0 < t_1 < \dots < t_N$ be the times of an assimilation window.
Let $M_{i} \colon \R^n \to \R^n$ be the model map from the state at time $t_{i-1}$ to the state at time $t_i$, and write $x_i = M_i(x_{i-1})$.
Let $x_b$ be a background estimate of the initial state $x_0$ with error covariance $B$.
At each time $t_i$ let $y_i \in \R^{m_i}$ be observations with observation operator $H_i$ and error covariance $R_i$, where $B$ and the $R_i$ are symmetric positive definite.
Consider the cost function
$$J(x_0) = \frac12 (x_0 - x_b)^T B^{-1} (x_0 - x_b) + \frac12 \sum_{i=0}^{N} \left(y_i - H_i(x_i)\right)^T R_i^{-1} \left(y_i - H_i(x_i)\right),$$
where the $x_i$ are given by the model equations $x_i = M_i(x_{i-1})$.
*Four-dimensional variational assimilation* (strong-constraint 4D-Var) is the method of [[data assimilation|TKT0QAPWW8]] that takes as analysis the minimiser $x_0$ of $J$.
The analysed trajectory is then $x_1, \dots, x_N$ computed from it.

## Remarks

Let $\mathbf{M}_i$ and $\mathbf{H}_i$ be the [[Jacobian matrices|047NDTEPCV]] of $M_i$ and $H_i$ along the trajectory, and $d_i = R_i^{-1}(y_i - H_i(x_i))$.
The gradient is
$$\nabla J(x_0) = B^{-1}(x_0 - x_b) - \sum_{i=0}^{N} \mathbf{M}_1^T \mathbf{M}_2^T \cdots \mathbf{M}_i^T \mathbf{H}_i^T d_i.$$
It is evaluated by one backward sweep $\lambda_N = \mathbf{H}_N^T d_N$, $\lambda_{i-1} = \mathbf{M}_i^T \lambda_i + \mathbf{H}_{i-1}^T d_{i-1}$, giving $\nabla J(x_0) = B^{-1}(x_0 - x_b) - \lambda_0$.
The transposed Jacobians define the adjoint model, the [[adjoint|0R9NMSM1ZP]] of the tangent linear model, and $J$ is then minimised by a gradient-based method.
This is a discrete [[optimal control|T3V6ZNAMDN]] problem with the initial state as the control.

Example: with $N = 0$ the window has one time and $J$ is the 3D-Var cost function of data assimilation.
If all $M_i$ and $H_i$ are linear and the errors are Gaussian, the 4D-Var analysis at $t_N$ equals the Kalman filter analysis at $t_N$ started from $x_b$ and $B$.

Non-example: weak-constraint 4D-Var, which adds model-error terms to $J$ and does not impose $x_i = M_i(x_{i-1})$ exactly, is a different method.

In practice the minimisation uses incremental formulations with simplified linearised models, and $B$ is modelled rather than known.

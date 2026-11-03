---
tag: HX0EMWJBNJ
kind: definition
name: Recursive least squares filter
msc: ["93E24", "93E12", 94A12]
defines: GJ21825GA8
uses: [H5CGZHBR58, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Recursive_least_squares_filter
---

## Definition

Let $\varphi_1, \varphi_2, \dots \in \R^n$ be regressor vectors and $d_1, d_2, \dots \in \R$ be desired outputs.
Fix a forgetting factor $\lambda \in (0, 1]$ and a regularization constant $\delta > 0$.
The *recursive least squares filter* is the sequence of weight vectors $w_k \in \R^n$ and matrices $P_k \in \R^{n \times n}$ given by $w_0 = 0$, $P_0 = \delta^{-1} I$ and, for $k \ge 1$,
$$g_k = \frac{P_{k-1} \varphi_k}{\lambda + \varphi_k^{T} P_{k-1} \varphi_k}, \qquad e_k = d_k - w_{k-1}^{T} \varphi_k,$$
$$w_k = w_{k-1} + g_k e_k, \qquad P_k = \lambda^{-1} \big(P_{k-1} - g_k \varphi_k^{T} P_{k-1}\big).$$
The vector $g_k$ is the gain and $e_k$ is the a priori error.

## Remarks

For every $k$, $P_k$ is [[positive definite|0KX66CZMBB]] and
$$P_k^{-1} = \lambda^k \delta I + \sum_{i=1}^{k} \lambda^{k-i} \varphi_i \varphi_i^{T},$$
by the Sherman–Morrison formula applied to $P_k^{-1} = \lambda P_{k-1}^{-1} + \varphi_k \varphi_k^{T}$.
Then $w_k$ is the unique minimizer of the regularized [[weighted least squares|H5CGZHBR58]] cost
$$J_k(w) = \lambda^k \delta \norm{w}^2 + \sum_{i=1}^{k} \lambda^{k-i} \big(d_i - w^{T} \varphi_i\big)^2.$$
Example: take $n = 1$, $\varphi_i = 1$ and $\lambda = 1$.
Then $P_k = 1/(\delta + k)$, $g_k = 1/(\delta + k)$, and $w_k = (d_1 + \cdots + d_k)/(\delta + k)$, which minimizes $J_k(w) = \delta w^2 + \sum_{i \le k} (d_i - w)^2$.
As $\delta \to 0$ this is the running mean.
Non-example: the [[least mean squares filter|17RASDZEBS]] $w_k = w_{k-1} + \mu e_k \varphi_k$ uses a fixed step $\mu$ in place of the gain $g_k$; its $w_k$ is in general not the minimizer of $J_k$.
The cost per step of RLS is of order $n^2$ operations, against order $n$ for least mean squares.
With $\lambda = 1$ and a suitable prior, RLS is the [[Kalman filter|DFM9YXF9AG]] for the constant state $w$ observed through $d_k = w^{T} \varphi_k + v_k$.

---
tag: TEWNXHRQ5H
kind: definition
name: Rauch–Tung–Striebel smoother
msc: ["93E14", "93E11", 62M20]
defines: AJCJB112YR
uses: [DFM9YXF9AG, 0TTDGTEFMN, 0V7G6WMFK0]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_filter
---

## Definition

Consider the linear Gaussian model $x_k = F_k x_{k-1} + w_k$, $z_k = H_k x_k + v_k$ for $1 \le k \le N$, with the assumptions of the [[Kalman filter|DFM9YXF9AG]].
Let $\hat x_{k|k}$, $P_{k|k}$, $\hat x_{k|k-1}$, $P_{k|k-1}$ be the quantities computed by the Kalman filter, and assume each $P_{k|k-1}$ is invertible.
The *Rauch–Tung–Striebel smoother* is the backward recursion that starts from $\hat x_{N|N}$ and $P_{N|N}$ and, for $k = N - 1, N - 2, \dots, 0$, computes
$$C_k = P_{k|k} F_{k+1}^T P_{k+1|k}^{-1},$$
$$\hat x_{k|N} = \hat x_{k|k} + C_k \big(\hat x_{k+1|N} - \hat x_{k+1|k}\big),$$
$$P_{k|N} = P_{k|k} + C_k \big(P_{k+1|N} - P_{k+1|k}\big) C_k^T.$$

## Remarks

Under the model assumptions, $\hat x_{k|N} = \mathbb{E}[x_k \mid z_1, \dots, z_N]$ and $P_{k|N}$ is the [[covariance matrix|0V7G6WMFK0]] of the error $x_k - \hat x_{k|N}$.
The proof uses that $x_k$ and $x_{k+1}$ are jointly Gaussian given $z_1, \dots, z_k$, and that, given $x_{k+1}$, the state $x_k$ is independent of the later measurements $z_{k+1}, \dots, z_N$.
Since conditioning on more data cannot increase the error covariance, $P_{k|N} \preceq P_{k|k}$.
Example: let $n = 1$, $F_k = 1$, $Q_k = 0$, so the state is a constant.
Then $P_{k+1|k} = P_{k|k}$, $C_k = 1$, and the recursion gives $\hat x_{k|N} = \hat x_{N|N}$ for all $k$: every past value of a constant is estimated with all the data.
Non-example: the filtered estimate $\hat x_{k|k}$ itself is not the smoothed estimate when $k < N$, because it ignores $z_{k+1}, \dots, z_N$.

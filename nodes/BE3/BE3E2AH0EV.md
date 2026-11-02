---
tag: BE3E2AH0EV
kind: definition
name: Parry measure
msc: [37B10, 37A35]
defines: 1C2TEAKJHJ
uses: [M7RPDE39FM, B232EZ1FMB, 62NS7PV1M9, ZEZPYJC06B, 0VGMEBVW1M]
sources:
  - url: https://en.wikipedia.org/wiki/Subshift_of_finite_type
---

## Definition

Let $A$ be a $k \times k$ matrix with entries in $\set{0, 1}$ that is [[irreducible|ZEZPYJC06B]].
Let $\Sigma_A = \set{x \in \set{1, \ldots, k}^{\Z} : A_{x_i x_{i+1}} = 1 \text{ for all } i}$ be its vertex shift, a [[subshift of finite type|M7RPDE39FM]], with shift map $\sigma$.
By the [[Perron–Frobenius theorem|62NS7PV1M9]], $A$ has a positive eigenvalue $\lambda$ of largest modulus, with eigenvectors $u, v$ with positive entries such that $u^T A = \lambda u^T$ and $A v = \lambda v$.
Normalise them so that $\sum_i u_i v_i = 1$.
Put $p_i = u_i v_i$ and $P_{ij} = A_{ij} v_j / (\lambda v_i)$.
The *Parry measure* is the [[probability measure|0VGMEBVW1M]] $\mu$ on $\Sigma_A$ such that, for all $n \in \Z$, $m \ge 0$ and states $i_0, \ldots, i_m$,
$$\mu\set{x : x_{n} = i_0, \ldots, x_{n+m} = i_m} = p_{i_0} P_{i_0 i_1} \cdots P_{i_{m-1} i_m}.$$

## Remarks

The matrix $P$ is stochastic and $p^T P = p^T$, so these values are consistent and $\mu$ is a $\sigma$-[[invariant measure|B232EZ1FMB]].
Its entropy is $\log \lambda$, which is the topological entropy of $\sigma$ on $\Sigma_A$, and it is the only invariant probability measure with this entropy.
Example: the golden mean shift has $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ and $\lambda = \varphi = (1 + \sqrt5)/2$.
Here $u = v = (\varphi, 1)$ up to scaling, since $\varphi + 1 = \varphi^2$.
After normalisation, $p_1 = \varphi^2/(\varphi^2 + 1)$ and $p_2 = 1/(\varphi^2 + 1)$, and $P_{11} = 1/\varphi$, $P_{12} = 1/\varphi^2$, $P_{21} = 1$, $P_{22} = 0$.
Each row of $P$ sums to $1$, because $1/\varphi + 1/\varphi^2 = 1$.
Non-example: on the same shift, the Markov measure with $P_{11} = P_{12} = 1/2$ is invariant for its stationary vector but is not the Parry measure, and its entropy is smaller than $\log \varphi$.

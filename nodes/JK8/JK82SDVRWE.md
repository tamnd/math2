---
tag: JK82SDVRWE
kind: definition
name: Balanced truncation
msc: [93B11, 93C05]
defines: H5H7RRQNX6
uses: [D54SM8Q12V, VCPQ0B99MA, 703MCKB5SZ, 9YEW705KHA, 3SNPPX5SAZ, QVREFP7BH7]
sources:
  - url: https://en.wikipedia.org/wiki/Model_order_reduction
---

## Definition

Let $(A, B, C, D)$ be a [[minimal realization|3SNPPX5SAZ]] of order $n$, with $A \in \R^{n \times n}$ whose eigenvalues all have negative real part.
Let $P$ and $Q$ be its [[controllability Gramian|703MCKB5SZ]] and [[observability Gramian|9YEW705KHA]], and let $\sigma_1 \ge \cdots \ge \sigma_n > 0$ be its [[Hankel singular values|VCPQ0B99MA]].

1. The realization is *balanced* if $P = Q = \Sigma$, where $\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_n)$.
2. Let the realization be balanced, and let $1 \le r < n$ with $\sigma_r > \sigma_{r+1}$. Partition
$$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_1 \\ B_2 \end{pmatrix}, \quad C = \begin{pmatrix} C_1 & C_2 \end{pmatrix},$$
with $A_{11} \in \R^{r \times r}$, $B_1 \in \R^{r \times m}$ and $C_1 \in \R^{p \times r}$.
3. The *balanced truncation of order $r$* is the system $(A_{11}, B_1, C_1, D)$.

Every such minimal realization can be balanced by a change of coordinates $x = T^{-1} \tilde{x}$.
The balanced truncation of a realization that is not balanced is that of its balanced form.

## Remarks

Under the hypotheses, $A_{11}$ has all eigenvalues in the open left half-plane, and the truncated system is again minimal and balanced.
Its transfer function $G_r$ satisfies the error bound
$$\norm{G - G_r}_{\infty} \le 2 (\sigma_{r+1} + \cdots + \sigma_n),$$
where each distinct value among $\sigma_{r+1}, \ldots, \sigma_n$ is counted once and $\norm{\cdot}_\infty$ is the [[H-infinity norm|QVREFP7BH7]].

Example: $A = \operatorname{diag}(-1, -2)$, $B = C = I_2$, $D = 0$ has $P = Q = \operatorname{diag}(1/2, 1/4)$, so it is balanced with $\sigma_1 = 1/2 > \sigma_2 = 1/4$.
Its truncation of order $1$ is $A_{11} = -1$, $B_1 = (1, 0)$, $C_1 = (1, 0)^T$.
The error $G - G_1 = \operatorname{diag}(0, 1/(s + 2))$ has H-infinity norm $1/2$, which equals the bound $2 \sigma_2$.

Non-example: the realization $A = -1$, $B = 2$, $C = 1/2$ of $G(s) = 1/(s + 1)$ has $P = 2$ and $Q = 1/8$, so it is not balanced; the coordinate change $\tilde{x} = x/2$ balances it to $A = -1$, $B = C = 1$, with $P = Q = 1/2$.

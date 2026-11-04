---
tag: ~dcbd4f03
kind: statement
role: theorem
name: Singular value decomposition and the four fundamental subspaces
msc: [15A18, 15A03]
uses: [000NPTMX6J, 0K2TX12X58, 0EWQEYRVA8, 03AJKXH1AV, 0PHDYNR24D, 0S9GGTR0EX]
about: [000NPTMX6J]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L1688
    locator: src/section7-4.xml:1688
---

## Statement

Let $A$ be a real $m \times n$ matrix with a [[singular value decomposition|000NPTMX6J]] $A = U \Sigma V^T$.
Here $U$ is $m \times m$ orthogonal with columns $u_1, \ldots, u_m$.
Also $V$ is $n \times n$ orthogonal with columns $v_1, \ldots, v_n$.
The [[singular values|0K2TX12X58]] on the diagonal of $\Sigma$ are in decreasing order.

Let $r$ be the number of nonzero singular values.
Then the following hold.

- The [[rank|0EWQEYRVA8]] of $A$ equals $r$.
- The vectors $u_1, \ldots, u_r$ are an [[orthonormal basis|0S9GGTR0EX]] of the [[column space|03AJKXH1AV]] of $A$.
- The vectors $u_{r+1}, \ldots, u_m$ are an orthonormal basis of the [[null space|0PHDYNR24D]] of $A^T$.
- The vectors $v_1, \ldots, v_r$ are an orthonormal basis of the column space of $A^T$, which is the row space of $A$.
- The vectors $v_{r+1}, \ldots, v_n$ are an orthonormal basis of the null space of $A$.

## Remarks

So an SVD gives orthonormal bases of all four fundamental subspaces of $A$ at once.

---
kind: statement
msc:
- 15A18
- 15A23
name: Reduced singular value decomposition
role: proposition
sources:
- locator: src/section7-4.xml:2021
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L2021
tag: ~2c6acf6e
uses:
- 03AJKXH1AV
- 0ZC9YTXZRY
- 0S9GGTR0EX
- 09VMDSRXWJ
about:
- 000NPTMX6J
---

## Statement

Let $A$ be a real $m \times n$ matrix of [[rank|0ZC9YTXZRY]] $r$, with [[singular values|09VMDSRXWJ]] $\sigma_1 \ge \cdots \ge \sigma_r > 0$ that are nonzero.
Then $A$ factors as
$$A = U_r \Sigma_r V_r^T.$$

In this factorization:

- $U_r$ is an $m \times r$ matrix. Its columns are an [[orthonormal basis|0S9GGTR0EX]] of the [[column space|03AJKXH1AV]] of $A$.
- $\Sigma_r$ is the $r \times r$ diagonal matrix with diagonal entries $\sigma_1, \dots, \sigma_r$. It is invertible, since these entries are nonzero.
- $V_r$ is an $n \times r$ matrix. Its columns are an orthonormal basis of the column space of $A^T$.

## Remarks

This is the full decomposition with the zero rows and columns removed. Only the $r$ directions on which $A$ acts nontrivially are kept.

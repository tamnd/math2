---
tag: Z182BABP6P
kind: proof
name: Proof that the determinant is the product of the eigenvalues by comparing constant terms
msc: [15A15, 15A18]
proves: 0C2F40MEBC
uses: [0T0X8GTYYS, 039HF58KQ5, 0125QVNCFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Eigenvalues and characteristic polynomial
---

## Proof

We compute $p_A(0)$ in two ways.

1. Let $A$ be an $n \times n$ matrix over $F$. The [[characteristic polynomial|039HF58KQ5]] is defined for $n \ge 1$, so $n \ge 1$. Assume that its characteristic polynomial is $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$ with $\lambda_i \in F$.
2. The [[evaluation homomorphism|0125QVNCFQ]] at $0$ preserves products. So $p_A(0) = (0 - \lambda_1) \cdots (0 - \lambda_n) = (-1)^n \lambda_1 \cdots \lambda_n$.
3. By the rule for the [[determinant as a coefficient|0T0X8GTYYS]], $p_A(0) = (-1)^n \det A$.
4. By steps 2 and 3, $(-1)^n \det A = (-1)^n \lambda_1 \cdots \lambda_n$.
5. Multiply both sides by $(-1)^n$, and use $(-1)^n (-1)^n = 1$. Then $\det A = \lambda_1 \lambda_2 \cdots \lambda_n$.

## Idea

The value of the characteristic polynomial at $0$ is $(-1)^n \det A$. From the factored form, the same value is $(-1)^n$ times the product of the roots. The signs cancel.

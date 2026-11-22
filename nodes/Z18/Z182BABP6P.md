---
tag: Z182BABP6P
kind: proof
name: Proof that the determinant is the product of the eigenvalues by comparing constant terms
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0C2F40MEBC
methods: [0NTF6DMVAP]
uses: [0T0X8GTYYS, 039HF58KQ5, 0125QVNCFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Eigenvalues and characteristic polynomial
---

## Proof

We compute the value $p_A(0)$ in two ways, once from the factored form and once from the determinant, and compare.

1. Let $A$ be an $n \times n$ matrix over $F$ with $n \ge 1$.
   By hypothesis its [[characteristic polynomial|039HF58KQ5]] is $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$ with all $\lambda_i \in F$.
2. The [[evaluation homomorphism|0125QVNCFQ]] at $0$ preserves products, so
$$p_A(0) = (0 - \lambda_1) \cdots (0 - \lambda_n) = (-1)^n \lambda_1 \cdots \lambda_n.$$
3. By the rule for the [[determinant as a coefficient|0T0X8GTYYS]], the constant term of $p_A$ is $p_A(0) = \det(-A) = (-1)^n \det A$.
4. Steps 2 and 3 give $(-1)^n \det A = (-1)^n \lambda_1 \cdots \lambda_n$.
5. Multiply both sides by $(-1)^n$ and use $(-1)^n (-1)^n = 1$.
   This gives $\det A = \lambda_1 \lambda_2 \cdots \lambda_n$.

## Idea

Put $t = 0$ in the characteristic polynomial.
From the definition $\det(tI - A)$ we get $\det(-A)$, which is $(-1)^n \det A$, since each of the $n$ rows carries a factor $-1$.
From the factored form we get $(-1)^n$ times the product of the roots.
The two signs are the same, so they cancel.
For example, $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has $p_A(t) = t^2 - 4t + 3 = (t - 1)(t - 3)$, and $p_A(0) = 3 = \det A = 1 \cdot 3$.

## Variants

A second proof uses [[triangularization|0363JMQ42Y]].
Since $p_A$ splits, $A = P U P^{-1}$ with $U$ upper triangular, and the diagonal of $U$ lists $\lambda_1, \dots, \lambda_n$.
Then the product rule and the [[determinant of a triangular matrix|0K1KKMFHYH]] give $\det A = \det P \det U \det P^{-1} = \det U = \prod_i \lambda_i$.
For a diagonalizable matrix, $A = P D P^{-1}$ with $D$ diagonal, and the same computation is shorter, but it covers only diagonalizable matrices.

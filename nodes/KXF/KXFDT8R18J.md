---
tag: KXFDT8R18J
kind: proof
name: Proof that the number of nonzero singular values is the rank
msc: [15A18, 15A03]
topics: [SS4EVPKT3A]
audience: ug1
proves: 6VXM1T8PG7
methods: [0NTF6DMVAP]
uses: [0AM050KCAW, 0DGZBQWZWN, 0HYC2RHD3M, 09DZ8CD1AK, AMFJCC9M7G, 0BVTDM872V, 0NMXDCNNKR, 0EWQEYRVA8, 0F0RPPJ2TT, 0PQ2GGY1QV, K33BQX70N0, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Based on the spectral theorem
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Proof

Here $\ip{x}{y} = y^* x$, where $^*$ is the [[conjugate transpose|0EX045E2BP]].

1. By [[the Gram matrix theorem|0AM050KCAW]], $A^* A$ is positive semidefinite. By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]] and the [[eigenvalue test|0HYC2RHD3M]], an orthonormal eigenbasis $v_1, \dots, v_n$ as in the statement exists, with all $\lambda_i \ge 0$.
2. For all $i, j$, $\ip{A v_i}{A v_j} = v_j^* A^* A v_i = \lambda_i v_j^* v_i = \lambda_i \ip{v_i}{v_j}$.
3. Since the $v_i$ are orthonormal, step 2 gives $\ip{A v_i}{A v_j} = 0$ for $i \ne j$, and $\norm{A v_i}^2 = \lambda_i = \sigma_i^2$. This proves part 1.
4. Since the $\lambda_i$ decrease, $\sigma_i > 0$ for $i \le r$ and $\sigma_i = 0$ for $i > r$. By step 3, $A v_i = 0$ for $i > r$, and $A v_i \ne 0$ for $i \le r$.
5. Let $x \in \C^n$. By [[coordinates in an orthonormal basis|09DZ8CD1AK]], $x = \sum_i c_i v_i$ with $c_i = \ip{x}{v_i}$. By step 4, $Ax = \sum_{i \le r} c_i A v_i$.
6. By step 5, every vector $Ax$ of the [[column space|0F0RPPJ2TT]] lies in the span of $A v_1, \dots, A v_r$. Each $A v_i$ lies in the column space, so the column space equals this span.
7. By steps 3 and 4, $A v_1, \dots, A v_r$ are nonzero and pairwise orthogonal. By the [[independence of orthogonal nonzero vectors|AMFJCC9M7G]], they are linearly independent. So they are an orthogonal basis of the column space.
8. If $Ax = 0$, then $\sum_{i \le r} c_i A v_i = 0$ by step 5, so $c_i = 0$ for $i \le r$ by step 7. So $x$ lies in the span of $v_{r+1}, \dots, v_n$. Conversely these vectors lie in the [[null space|0PQ2GGY1QV]] by step 4. This proves part 2.
9. By step 7, the column space has dimension $r$. The [[rank|0EWQEYRVA8]] of $A$ is this dimension, so $\rank A = r$. This proves part 3.
10. For $x$ as in step 5, the [[Pythagorean theorem|0BVTDM872V]] and step 3 give $\norm{Ax}^2 = \sum_i \abs{c_i}^2 \sigma_i^2$, and $\norm{x}^2 = \sum_i \abs{c_i}^2$.
11. If $\norm x = 1$, step 10 gives $\sigma_n^2 \le \norm{Ax}^2 \le \sigma_1^2$, since the $\abs{c_i}^2$ are nonnegative weights with sum $1$. The bounds are reached at $x = v_n$ and $x = v_1$, by step 3. This proves part 4.
12. Let $a_1, \dots, a_n$ be the columns of $A$. By the [[definition of the Frobenius norm|K33BQX70N0]], $\norm{A}_F^2 = \sum_j \norm{a_j}^2 = \sum_j a_j^* a_j$, which is the sum of the diagonal entries of $A^* A$.
13. The [[trace is the sum of the eigenvalues|0NMXDCNNKR]], so $\norm{A}_F^2 = \tr(A^* A) = \lambda_1 + \dots + \lambda_n = \sigma_1^2 + \dots + \sigma_n^2$. This proves part 5.
14. Let $\mu > 0$, and let $E$ and $E'$ be the eigenspaces of $A^* A$ and $A A^*$ for $\mu$. If $v \in E$, then $A A^* (Av) = A (\mu v) = \mu A v$, so $Av \in E'$.
15. If $v \in E$ and $Av = 0$, then $\mu v = A^* A v = 0$, so $v = 0$. So $v \mapsto Av$ is an injective linear map $E \to E'$, and $\dim E \le \dim E'$.
16. Step 15 with $A^*$ in place of $A$ gives $\dim E' \le \dim E$, since $(A^*)^* = A$. So $\dim E = \dim E'$. The multiplicity of an eigenvalue of a Hermitian matrix is the dimension of its eigenspace, by the spectral theorem. This proves part 6.

## Idea

The identity $\ip{A v_i}{A v_j} = \lambda_i \ip{v_i}{v_j}$ says that $A$ maps an orthonormal eigenbasis of $A^* A$ to orthogonal vectors of lengths $\sigma_i$.
The nonzero images are independent and span the column space, so their number is the rank.
Lengths and the trace give the norm statements.

## Variants

- Part 3 also follows from $\ker(A^* A) = \ker A$: if $A^* A x = 0$, then $\norm{Ax}^2 = x^* A^* A x = 0$. Then $\rank(A^* A) = \rank A$ by rank-nullity, and the rank of the Hermitian matrix $A^* A$ is the number of its nonzero eigenvalues.
- Part 4 is the case of the [[Rayleigh quotient|06WHP8SE98]] of $A^* A$: $\norm{Ax}^2 / \norm{x}^2 = x^* A^* A x / x^* x$.

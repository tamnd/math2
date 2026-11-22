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

We compute the inner products of the images $A v_i$, and then we expand every vector in the basis $v_1, \dots, v_n$.
Throughout, $\ip{x}{y} = y^* x$, where $^*$ is the [[conjugate transpose|0EX045E2BP]].

1. By [[the Gram matrix theorem|0AM050KCAW]], $A^* A$ is positive semidefinite. So the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]] and the [[eigenvalue test|0HYC2RHD3M]] give an orthonormal eigenbasis $v_1, \dots, v_n$ as in the statement, with all $\lambda_i \ge 0$.
2. For all $i$ and $j$, we move $A$ across the inner product and use $A^* A v_i = \lambda_i v_i$:
$$\ip{A v_i}{A v_j} = v_j^* A^* A v_i = \lambda_i \, v_j^* v_i = \lambda_i \ip{v_i}{v_j}.$$
3. The $v_i$ are orthonormal, so step 2 gives $\ip{A v_i}{A v_j} = 0$ for $i \ne j$ and $\norm{A v_i}^2 = \lambda_i = \sigma_i^2$. This proves part 1.
4. The $\lambda_i$ decrease, so $\sigma_i > 0$ for $i \le r$ and $\sigma_i = 0$ for $i > r$. By step 3, $A v_i \ne 0$ for $i \le r$ and $A v_i = 0$ for $i > r$.
5. Let $x \in \C^n$. By [[coordinates in an orthonormal basis|09DZ8CD1AK]], $x = \sum_i c_i v_i$ with $c_i = \ip{x}{v_i}$. Linearity and step 4 then give $Ax = \sum_{i \le r} c_i A v_i$.
6. By step 5, every vector $Ax$ of the [[column space|0F0RPPJ2TT]] lies in the span of $A v_1, \dots, A v_r$. Each $A v_i$ is itself in the column space, so the column space equals this span.
7. By steps 3 and 4, the vectors $A v_1, \dots, A v_r$ are nonzero and pairwise orthogonal. So they are linearly independent, by the [[independence of orthogonal nonzero vectors|AMFJCC9M7G]], and step 6 makes them an orthogonal basis of the column space.
8. Suppose $Ax = 0$. Then $\sum_{i \le r} c_i A v_i = 0$ by step 5, so $c_i = 0$ for $i \le r$ by step 7, and $x$ lies in the span of $v_{r+1}, \dots, v_n$.
9. These vectors lie in the [[null space|0PQ2GGY1QV]] by step 4, and they are orthonormal. With step 8, they are an orthonormal basis of the null space, which proves part 2.
10. By step 7, the column space has dimension $r$. The [[rank|0EWQEYRVA8]] of $A$ is this dimension, so $\rank A = r$, which proves part 3.
11. For $x$ as in step 5, the [[Pythagorean theorem|0BVTDM872V]] applied to the orthogonal vectors $c_i A v_i$ and to the orthonormal $v_i$ gives, with step 3,
$$\norm{Ax}^2 = \sum_i \abs{c_i}^2 \sigma_i^2, \qquad \norm{x}^2 = \sum_i \abs{c_i}^2.$$
12. Let $\norm x = 1$. The numbers $\abs{c_i}^2$ are nonnegative weights with sum $1$, so step 11 gives $\sigma_n^2 \le \norm{Ax}^2 \le \sigma_1^2$. Step 3 shows that $x = v_1$ and $x = v_n$ reach the two bounds, which proves part 4.
13. Let $a_1, \dots, a_n$ be the columns of $A$. By the [[definition of the Frobenius norm|K33BQX70N0]], $\norm{A}_F^2 = \sum_j \norm{a_j}^2 = \sum_j a_j^* a_j$, and $a_j^* a_j$ is the diagonal entry $(j, j)$ of $A^* A$.
14. So $\norm{A}_F^2 = \tr(A^* A)$. The [[trace is the sum of the eigenvalues|0NMXDCNNKR]], so $\norm{A}_F^2 = \lambda_1 + \dots + \lambda_n = \sigma_1^2 + \dots + \sigma_n^2$, which proves part 5.
15. Let $\mu > 0$, and let $E$ and $E'$ be the eigenspaces of $A^* A$ and of $A A^*$ for $\mu$. If $v \in E$, then $A A^* (Av) = A (A^* A v) = \mu \, Av$, so $Av \in E'$.
16. If $v \in E$ and $Av = 0$, then $\mu v = A^* A v = 0$, so $v = 0$ because $\mu \ne 0$. So $v \mapsto Av$ is an injective linear map from $E$ to $E'$, and $\dim E \le \dim E'$.
17. Step 16 with $A^*$ in place of $A$ gives $\dim E' \le \dim E$, because $(A^*)^* = A$. So $\dim E = \dim E'$.
18. For a Hermitian matrix the multiplicity of an eigenvalue is the dimension of its eigenspace, by the spectral theorem. So step 17 says that $A^* A$ and $A A^*$ have the same nonzero eigenvalues with the same multiplicities, and taking square roots proves part 6.

## Idea

The identity $\ip{A v_i}{A v_j} = \lambda_i \ip{v_i}{v_j}$ is the whole proof in one line.
It says that $A$ sends an orthonormal eigenbasis of $A^* A$ to orthogonal vectors of lengths $\sigma_i$.
The nonzero images are independent and span the column space, so their number is the rank.
Expanding a unit vector in the eigenbasis turns $\norm{Ax}^2$ into a weighted average of the $\sigma_i^2$, which gives the bounds, and the trace gives the Frobenius norm.

## Variants

Part 3 also follows from the equality of kernels $\ker(A^* A) = \ker A$.
If $A^* A x = 0$, then $\norm{Ax}^2 = x^* A^* A x = 0$, so $Ax = 0$, and the other inclusion holds for every matrix.
Rank-nullity then gives $\rank(A^* A) = \rank A$, and the rank of the Hermitian matrix $A^* A$ is the number of its nonzero eigenvalues.

Part 4 is the extreme case of the [[Rayleigh quotient|06WHP8SE98]] of $A^* A$, since $\norm{Ax}^2 / \norm{x}^2 = x^* A^* A x / x^* x$, and the Rayleigh quotient of a Hermitian matrix ranges between its smallest and largest eigenvalues.

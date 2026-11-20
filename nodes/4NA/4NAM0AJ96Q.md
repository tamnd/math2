---
tag: 4NAM0AJ96Q
kind: proof
name: Proof of the extreme values of the Rayleigh quotient
msc: ["15A18", "15A42"]
topics: [3YM9EK6VMB]
audience: ug1
proves: T7MFPSY009
uses: [06J4PXRG22, 09DZ8CD1AK, 0MB8HQW495]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Proof

We expand $v$ in an orthonormal eigenbasis, so that $R(v)$ becomes a weighted average of the eigenvalues.

1. By parts 1 and 3 of [[the real spectral theorem|06J4PXRG22]], $V$ has an orthonormal basis $u_1, \dots, u_n$ with $T u_j = \lambda_j u_j$. Order it so that $\lambda_1 \geq \dots \geq \lambda_n$.
2. Let $v \neq 0$, and let $c_j = \ip{v}{u_j}$. By [[coordinates in an orthonormal basis|09DZ8CD1AK]], $v = \sum_j c_j u_j$.
3. Then $T v = \sum_j \lambda_j c_j u_j$. Orthonormality gives $\ip{Tv}{v} = \sum_j \lambda_j \abs{c_j}^2$ and $\ip{v}{v} = \sum_j \abs{c_j}^2 > 0$.
4. So $R(v) = \sum_j \lambda_j \abs{c_j}^2 / \sum_j \abs{c_j}^2$. This is a weighted average of the $\lambda_j$ with the weights $\abs{c_j}^2 \geq 0$.
5. Part 1. We get $\lambda_1 \ip{v}{v} - \ip{Tv}{v} = \sum_j (\lambda_1 - \lambda_j) \abs{c_j}^2$. Each term is $\geq 0$, so $R(v) \leq \lambda_1$.
6. In the same way, $\ip{Tv}{v} - \lambda_n \ip{v}{v} = \sum_j (\lambda_j - \lambda_n) \abs{c_j}^2 \geq 0$. So $R(v) \geq \lambda_n$.
7. Part 2, "if". Let $T v = \lambda_1 v$ with $v \neq 0$. Then $\ip{Tv}{v} = \lambda_1 \ip{v}{v}$, so $R(v) = \lambda_1$.
8. Part 2, "only if". Let $R(v) = \lambda_1$. Then the sum in step 5 is $0$. All its terms are $\geq 0$, so each term is $0$.
9. So $c_j = 0$ whenever $\lambda_j < \lambda_1$. Then $v$ is a combination of the $u_j$ with $\lambda_j = \lambda_1$, and $T v = \lambda_1 v$. As $v \neq 0$, $v$ is an eigenvector for $\lambda_1$.
10. The claims for $\lambda_n$ follow in the same way from step 6.
11. Part 3. By part 1, $R \leq \lambda_1$ everywhere. By step 7, $R(u_1) = \lambda_1$. So $\lambda_1$ is the maximum. In the same way, $R(u_n) = \lambda_n$ is the minimum.
12. For a Hermitian matrix $A$, the map $x \mapsto Ax$ is [[self-adjoint|0MB8HQW495]] for $\ip{x}{y} = y^* x$, and $R_A(x) = \ip{Ax}{x} / \ip{x}{x}$. So the matrix form follows.

## Idea

In an orthonormal eigenbasis, the Rayleigh quotient is a weighted average of the eigenvalues, with the weights $\abs{c_j}^2$.
An average lies between the smallest and the largest value.
It equals the largest value only if all the weight sits on the largest value.

## Variants

- One can avoid the spectral theorem for part 3 by part 2 of [[the theorem on real eigenvalues|0C4NT4GT3X]]. That part shows directly that the maximum on the unit sphere exists and is an eigenvalue.
- Lagrange multipliers give the same result. At a maximizer of $\ip{Tv}{v}$ on $\ip{v}{v} = 1$, the gradients are parallel, so $Tv = \lambda v$.

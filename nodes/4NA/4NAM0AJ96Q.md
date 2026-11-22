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

We expand $v$ in an orthonormal eigenbasis, so that $R(v)$ becomes a weighted average of the eigenvalues, and then we read off the bounds.

1. By [[the real spectral theorem|06J4PXRG22]], in its real form (part 1) or its complex form (part 3), $V$ has an orthonormal basis $u_1, \dots, u_n$ with $T u_j = \lambda_j u_j$. We number it so that $\lambda_1 \geq \dots \geq \lambda_n$.
2. Let $v \neq 0$ and $c_j = \ip{v}{u_j}$. By [[coordinates in an orthonormal basis|09DZ8CD1AK]], $v = \sum_j c_j u_j$, and so $Tv = \sum_j \lambda_j c_j u_j$.
3. Orthonormality makes every cross term $\ip{u_j}{u_k}$ with $j \ne k$ vanish, so
$$\ip{Tv}{v} = \sum_j \lambda_j \abs{c_j}^2, \qquad \ip{v}{v} = \sum_j \abs{c_j}^2 > 0.$$
4. Part 1, upper bound. Step 3 gives
$$\lambda_1 \ip{v}{v} - \ip{Tv}{v} = \sum_j (\lambda_1 - \lambda_j) \abs{c_j}^2.$$
Each term is a product of two numbers that are at least $0$, so the sum is at least $0$, and dividing by $\ip{v}{v} > 0$ gives $R(v) \leq \lambda_1$.
5. Part 1, lower bound. In the same way, $\ip{Tv}{v} - \lambda_n \ip{v}{v} = \sum_j (\lambda_j - \lambda_n) \abs{c_j}^2 \geq 0$, so $R(v) \geq \lambda_n$.
6. Part 2, "if". Let $Tv = \lambda_1 v$ with $v \neq 0$. Then $\ip{Tv}{v} = \lambda_1 \ip{v}{v}$, so $R(v) = \lambda_1$.
7. Part 2, "only if". Let $R(v) = \lambda_1$. Then the sum in step 4 is $0$, and a sum of terms that are at least $0$ is $0$ only when each term is $0$.
8. So $c_j = 0$ whenever $\lambda_j < \lambda_1$. Then $v$ is a combination of the $u_j$ with $\lambda_j = \lambda_1$, and so $Tv = \lambda_1 v$. Since $v \neq 0$, it is an eigenvector for $\lambda_1$.
9. The claims for $\lambda_n$ follow in the same way from step 5.
10. Part 3. By part 1, $R(v) \le \lambda_1$ for every $v$, and by step 6, $R(u_1) = \lambda_1$. So $\lambda_1$ is the maximum of $R$, and in the same way $R(u_n) = \lambda_n$ is the minimum.
11. For a Hermitian matrix $A$, the map $x \mapsto Ax$ is [[self-adjoint|0MB8HQW495]] for the standard inner product $\ip{x}{y} = y^* x$, and $R_A(x) = \ip{Ax}{x} / \ip{x}{x}$. So the matrix form follows from the operator form, and the real symmetric case is the same with $\mathbb{R}$ in place of $\mathbb{C}$.

## Idea

In an orthonormal eigenbasis, the Rayleigh quotient is an average of the eigenvalues, with the weights $\abs{c_j}^2$.
An average lies between the smallest and the largest value it averages.
It equals the largest value only when all the weight sits on that value, which means that $v$ lies in the top eigenspace.

## Variants

Part 3 also follows without the spectral theorem from part 2 of [[the theorem on real eigenvalues|0C4NT4GT3X]].
That result shows by compactness that $\ip{Tv}{v}$ has a maximum on the unit sphere and that every maximum point is an eigenvector.
This maximum is an eigenvalue, and it is at least every eigenvalue $\lambda$, because a unit eigenvector for $\lambda$ gives the value $\lambda$.
So the maximum is $\lambda_1$.

Lagrange multipliers give the same result.
At a maximum point of $\ip{Tv}{v}$ under the constraint $\ip{v}{v} = 1$, the two gradients are parallel, and this says $Tv = \lambda v$ for some real $\lambda$.

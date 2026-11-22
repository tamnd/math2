---
tag: GHGBEV51GZ
kind: proof
name: Variational proof of the real spectral theorem
msc: ["47B15", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 06J4PXRG22
uses: [0VGSYBWHV2, 0MB8HQW495, 0B5H4208Z9, 0FWJ0VW561, 0C4NT4GT3X, 079D68S3AW, 0E2NYPVSP9, 0JWM6GJNQW, 096V7H13H9, 0DBTE6HVBD, 0N28QN4CYA, 0QRBVFJ50X]
methods: [MD3MRG90W4, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
---

## Proof

We find the eigenvectors one after another as points where $q(v) = \ip{Tv}{v}$ is largest on smaller and smaller unit spheres.
Steps 1 to 8 prove the direction "only if" of part 1 together with part 3, and steps 9 to 11 prove the rest.

1. Setting. Let $V$ be an inner product space of dimension $n \geq 1$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to V$ be [[self-adjoint|0MB8HQW495]]. For $V = \{0\}$ the empty basis works, so this case is enough.
2. The construction. We build orthonormal vectors $u_1, \dots, u_n$ and real numbers $\lambda_1, \dots, \lambda_n$ with $T u_j = \lambda_j u_j$, one at a time. Let $1 \leq k \leq n$, and assume that $u_1, \dots, u_{k-1}$ are already built.
3. The space $W_k$. Let $W_k$ be the [[orthogonal complement|079D68S3AW]] of the span of $u_1, \dots, u_{k-1}$, so $W_1 = V$. The vectors $u_1, \dots, u_{k-1}$ are orthonormal, hence [[linearly independent|0JWM6GJNQW]], so their span has dimension $k - 1$. By the [[dimension formula for the complement|0E2NYPVSP9]], $\dim W_k = n - k + 1 \geq 1$.
4. $W_k$ is invariant. Let $w \in W_k$ and $j < k$. Self-adjointness gives
$$\ip{Tw}{u_j} = \ip{w}{T u_j} = \overline{\lambda_j} \ip{w}{u_j} = 0,$$
so $Tw \in W_k$.
5. The restriction $S_k$ of $T$ to $W_k$ is therefore an operator on $W_k$. It is self-adjoint for the restricted inner product, because $\ip{S_k w}{w'} = \ip{Tw}{w'} = \ip{w}{Tw'} = \ip{w}{S_k w'}$ for $w, w' \in W_k$.
6. The maximum. The unit sphere of $W_k$ is compact and $q$ is continuous and real-valued on it, since $q(v) = \ip{Tv}{v}$ is real for self-adjoint $T$. By the [[theorem on real eigenvalues|0C4NT4GT3X]] applied to $S_k$, the maximum $\lambda_k$ of $q$ on this sphere is attained at some $u_k$, and $S_k u_k = \lambda_k u_k$.
7. So $T u_k = \lambda_k u_k$ with $\lambda_k = q(u_k)$ real. The unit vector $u_k$ lies in $W_k$, so it is orthogonal to $u_1, \dots, u_{k-1}$, and the family $u_1, \dots, u_k$ is orthonormal.
8. The basis. After $n$ steps, $u_1, \dots, u_n$ are $n$ orthonormal [[eigenvectors|0B5H4208Z9]] of $T$. They are linearly independent, so they form a [[basis|096V7H13H9]] of $V$, and this is an [[orthonormal basis|0FWJ0VW561]] of eigenvectors with real eigenvalues.
9. The order of the eigenvalues. $W_{k+1}$ is a subspace of $W_k$, so its unit sphere is a subset of the unit sphere of $W_k$. A maximum over a smaller set is not larger, so $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$.
10. Direction "if" of part 1. Let $V$ be real with an orthonormal eigenbasis. The matrix $D$ of $T$ in this basis is real and diagonal. By the [[matrix of the adjoint|0DBTE6HVBD]], $T^*$ has the matrix $D^{\mathsf{T}} = D$ in the same basis, so $T^* = T$.
11. Part 2. For a real [[symmetric|0N28QN4CYA]] matrix $A$, the map $x \mapsto Ax$ is self-adjoint on $\mathbb{R}^n$ with $\ip{x}{y} = y^{\mathsf{T}} x$, because $y^{\mathsf{T}} A x = (Ay)^{\mathsf{T}} x$. The orthonormal eigenvectors of step 8 are the columns of an [[orthogonal matrix|0QRBVFJ50X]] $Q$, column by column $AQ = QD$, and so $A = Q D Q^{\mathsf{T}}$. Conversely, $(Q D Q^{\mathsf{T}})^{\mathsf{T}} = Q D Q^{\mathsf{T}}$.

## Idea

Think of $q(v) = \ip{Tv}{v}$ as a height function on the unit sphere.
Its highest point is an eigenvector, and the height there is the largest eigenvalue.
Now cut the sphere with the hyperplane orthogonal to that eigenvector.
That hyperplane is invariant under $T$, so the highest point on the smaller sphere is the next eigenvector, and its height is the next eigenvalue.
Repeating the cut $n$ times gives the whole orthonormal eigenbasis, with the eigenvalues in decreasing order.

## Variants

The proof gives more than the theorem.
The first maximum $\lambda_1$ is taken over the whole unit sphere, so it is the largest eigenvalue, and in the same way a minimum gives the smallest one.
These are the [[extreme values of the Rayleigh quotient|T7MFPSY009]], and the [[Courant-Fischer min-max theorem|CJK2HS2508]] describes every $\lambda_k$ as a min-max of $q$ over subspaces.

The eigenvector equation of step 6 can also come from Lagrange multipliers.
For a real space, a maximizer of $q(v)$ under the condition $\ip{v}{v} = 1$ has $\nabla q = 2Tv$ parallel to $\nabla \ip{v}{v} = 2v$, so $Tv = \lambda v$ for the multiplier $\lambda$.

The [[proof by induction|A81KPS16D7]] uses only one maximum, and then applies the induction hypothesis to the orthogonal complement.

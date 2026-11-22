---
tag: RK1QVMYW7H
kind: statement
role: theorem
name: An endomorphism is cyclic if and only if its minimal and characteristic polynomials are equal
aliases: [cyclic-iff-minimal-equals-characteristic, nonderogatory-criterion]
msc: ["15A21", "15A18"]
topics: [GEBYZKYV3D]
audience: ug2
about: [42MMQBTP0M, 03NDVCSHSB, 0VSSPAFM2C]
uses: [42MMQBTP0M, 03NDVCSHSB, 0J5EMJRRFM, 5VYBJYPYMW, QPE5Y86Y8V]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: Similarity to companion matrix
---

## Statement

A linear map has a cyclic vector exactly when its minimal polynomial is as long as it can be, that is, when it equals the characteristic polynomial.
Let $V$ be a vector space of finite dimension $n \ge 1$ over a field $F$, and let $T \colon V \to V$ be linear.
Let $m_T$ be its [[minimal polynomial|03NDVCSHSB]] and $\chi_T$ its [[characteristic polynomial|0J5EMJRRFM]].
Then $T$ is [[cyclic|42MMQBTP0M]], that is, $V = Z(v; T)$ for some $v \in V$, if and only if $m_T = \chi_T$.
In this case, for each cyclic vector $v$, the matrix of $T$ in the basis $v, Tv, \dots, T^{n-1} v$ is the companion matrix $C(\chi_T)$.

## Remarks

### Why the full equality is needed

The condition is $m_T = \chi_T$, and having the same roots is not enough.
The matrices $I_2$ and $J_2(1) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have the single root $1$ in both polynomials.
For $J_2(1)$ we get $m = \chi = (x - 1)^2$, and it is cyclic with cyclic vector $e_2$.
For $I_2$ we get $m = x - 1$ but $\chi = (x - 1)^2$, and [[no vector is cyclic|M135QJH5NQ]].
Finite dimension is needed so that $\chi_T$ exists at all.

### What it gives you

The test needs no search for a vector.
Compute $m_T$ and compare it with $\chi_T$; by the [[Cayley-Hamilton theorem|0F765KFC2J]] $m_T$ always divides $\chi_T$, so only the degree must be checked.

Distinct roots give a quick sufficient condition.
If $\chi_T$ has $n$ distinct roots in $F$, then each root is also a root of $m_T$, so $m_T$ has degree $n$ and equals $\chi_T$, and $T$ is cyclic.
A [[Jordan block|07PH4RX0X5]] $J_n(\lambda)$ shows that the condition is not necessary: it has $m = \chi = (x - \lambda)^n$, one root, and still it is cyclic.

The theorem also says that a matrix $A$ is cyclic exactly when it is similar to the [[companion matrix|0ZCWPNZTQ3]] $C(\chi_A)$.
So two cyclic matrices are similar if and only if they have the same characteristic polynomial.

### The general picture

The [[cyclic decomposition theorem|R3Z20J19BR]] writes $V$ as a sum of $r$ cyclic subspaces with annihilators $d_1 \mid d_2 \mid \cdots \mid d_r$.
Then $\chi_T = d_1 \cdots d_r$ and $m_T = d_r$.
The theorem is the case $r = 1$, and $r$ is the least number of vectors that generate $V$ under $T$.
Over an algebraically closed field, $T$ is cyclic if and only if each eigenvalue has exactly one Jordan block, that is, geometric multiplicity $1$.

## Explanations

### L1 human

The characteristic polynomial of a map on an $n$-dimensional space always has degree $n$.
The minimal polynomial can be shorter.
The theorem says that the two are equal exactly when one vector, pushed again and again by the map, reaches every direction of the space.
For the map that doubles the second coordinate of a point in the plane, both polynomials are $(x - 1)(x - 2)$, and the point $(1, 1)$ does the job.

### L2 human

Here is a typical use: decide whether
$$A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$
over $\mathbb{Q}$ is cyclic, and find a cyclic vector.
The matrix is upper triangular, so $\chi_A = (x - 2)^2 (x - 3)$.
The only shorter candidate for $m_A$ with both roots is $(x - 2)(x - 3)$, and it fails, because the $(1, 2)$ entry of $(A - 2I)(A - 3I)$ is $1 \cdot (-1) = -1$.
So $m_A = \chi_A$, and $A$ is cyclic.

To find a cyclic vector, try $v = e_2 + e_3$.
Then
$$Av = (1, 2, 3), \qquad A^2 v = (4, 4, 9), \qquad \det \begin{pmatrix} 0 & 1 & 4 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \end{pmatrix} = -1 \ne 0,$$
so $v, Av, A^2 v$ is a basis.
Watch out: $\operatorname{diag}(2, 2, 3)$ has the same characteristic polynomial, but $m = (x - 2)(x - 3)$, so it is not cyclic.

### L3 human

For the $F[x]$-module $V_T$, the theorem says that $V_T$ is cyclic if and only if $\dim_F F[x]/(m_T) = \dim_F V$.
Indeed a cyclic module is $F[x]/(m_T)$, and in general $V_T$ contains a copy of $F[x]/(m_T)$ by the [[lemma on a vector of maximal annihilator|QPE5Y86Y8V]].
Over an algebraically closed field the cyclic matrices are the regular elements of the Lie algebra $\mathfrak{gl}_n$, those whose centralizer has the least possible dimension $n$, as the [[theorem on centralizers|GXZGWZSJ2J]] explains.

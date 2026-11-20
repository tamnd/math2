---
tag: 1YGY396SAS
kind: example
name: A Jordan chain of length 3
msc: ["15A18", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
instance_of: [01H6QKWGDH, 0AJ035ZTZE]
not_instance_of:
  - target: 07SQCNV233
    note: the only eigenvalue is 2 and its eigenspace is the line spanned by e1, so there is no basis of eigenvectors
illustrates: [PHZ684KGWS]
uses: [0SAAHC36J9, 07PNDWA7CE, 0AYEPBQMAW, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Jordan chains
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Example

Let $F$ be a field and let
$$J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$
over $F$, the Jordan block of size $3$ for the eigenvalue $2$.
Let $N = J - 2I$.

1. $J$ is upper triangular, so its [[characteristic polynomial|0VSSPAFM2C]] is $(t - 2)^3$, and $2$ is the only eigenvalue.
2. $N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$, so $N e_1 = 0$, $N e_2 = e_1$ and $N e_3 = e_2$.
3. $N^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ and $N^3 = 0$.
4. So $\ker N = F e_1$, $\ker N^2 = \operatorname{span}(e_1, e_2)$ and $\ker N^3 = F^3$.
5. The vector $e_3$ is a [[generalized eigenvector|0SAAHC36J9]] for $2$ of rank $3$, since $N^2 e_3 = e_1 \ne 0$ and $N^3 e_3 = 0$.
6. Its Jordan chain is $e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$ under $N$. The last nonzero vector $e_1$ is an [[eigenvector|0B5H4208Z9]].
7. The [[generalized eigenspace|07PNDWA7CE]] $V_2 = \ker N^3$ is all of $F^3$. Its dimension $3$ equals the algebraic multiplicity of $2$.
8. The [[eigenspace|0AYEPBQMAW]] $\ker N$ has dimension $1$. So $J$ is not diagonalizable.

## Remarks

The kernels $\ker N^k$ grow by exactly one dimension at each step until $k = 3$, and then they stay equal to $F^3$.
This agrees with the [[dimension of the generalized eigenspace|PHZ684KGWS]]: the chain of kernels stops at a power $k \le 3$.
A vector $v = (a, b, c)$ has rank $3$ if $c \ne 0$, rank $2$ if $c = 0$ and $b \ne 0$, and rank $1$ if $b = c = 0$ and $a \ne 0$.
In the basis $(e_1, e_2, e_3)$, which is the chain read from the eigenvector, the matrix is $J$ itself.
In the reversed basis $(e_3, e_2, e_1)$, the matrix is the lower triangular transpose $J^{\mathsf{T}}$.

## Explanations

### L1 human

The matrix $J - 2I$ moves each basis vector one place down the list: $e_3$ goes to $e_2$, $e_2$ goes to $e_1$, and $e_1$ goes to zero.
So $e_3$ needs three steps to reach zero.
Such a list of vectors is a Jordan chain.
Only the last vector of the chain is a true eigenvector.

### L2 human

Find the rank of $v = (5, -1, 0)$.

1. $N v = (-1, 0, 0)$, by step 2, since $N(a, b, c) = (b, c, 0)$.
2. $N v \ne 0$, so the rank is at least $2$.
3. $N^2 v = N(-1, 0, 0) = 0$, so the rank is $2$.

The typical use is to read the rank from the last nonzero coordinate in the basis of the chain.
The trap is to read it from the first coordinate: $(5, -1, 0)$ has rank $2$, not $1$.

### L3 human

The chain $e_3, e_2, e_1$ makes $F^3$ a cyclic module over $F[t]$, isomorphic to $F[t]/(t - 2)^3$, with $t$ acting as $J$.
Every generalized eigenspace over an algebraically closed field is a direct sum of such cyclic pieces, which is the [[Jordan normal form|085HQ5G5TE]].

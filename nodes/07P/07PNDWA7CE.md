---
tag: 07PNDWA7CE
kind: definition
name: Generalized eigenspace
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
defines: 0AJ035ZTZE
uses: [0SAAHC36J9]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Definition

The generalized eigenspace of $\lambda$ is the set of vectors that some power of $T - \lambda \id_V$ sends to zero.
Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]], and let $\lambda \in F$.
The *generalized eigenspace* of $T$ for $\lambda$ is
$$V_\lambda = \{ v \in V : (T - \lambda \id_V)^k (v) = 0 \text{ for some } k \ge 1 \} = \bigcup_{k \ge 1} \ker (T - \lambda \id_V)^k.$$
Its nonzero elements are the [[generalized eigenvectors|0SAAHC36J9]] of $T$ for $\lambda$.

## Notation

Other notations are $V^\lambda$, $G(\lambda, T)$ and $K_\lambda$.
In Mathlib, this subspace is `Module.End.maxGenEigenspace`, the union of the subspaces `Module.End.genEigenspace` for all $k$.

## Remarks

The definition is a union of kernels, and a union of subspaces is usually not a subspace.
Here it is one, because the kernels increase: if $(T - \lambda)^k v = 0$, then $(T - \lambda)^{k+1} v = 0$ too.
So two vectors of $V_\lambda$ lie in one common kernel, and their sum lies there as well.
The exponent $k$ is allowed to depend on the vector, and in finite dimension one exponent works for all of them.

The space $V_\lambda$ is $T$-[[invariant|0ACX5QT8TE]], since $T$ commutes with $(T - \lambda \id_V)^k$.
It contains the [[eigenspace|0AYEPBQMAW]] $E_\lambda = \ker (T - \lambda \id_V)$, which is the case $k = 1$.
If $\dim V = n$ is finite, then $V_\lambda = \ker (T - \lambda \id_V)^n$, and its dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$, by the [[dimension of the generalized eigenspace|PHZ684KGWS]].

For a small example, let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\lambda = 0$.
Then $\ker N = F e_1$ and $N^2 = 0$, so $V_0 = F^2$.
For a case where the space is zero, take $\lambda = 1$: the matrix $N - I$ is invertible, so $V_1 = 0$.
The concept page [[generalized eigenspace|0AJ035ZTZE]] gives more examples.

## Explanations

### L1 human

The generalized eigenspace is a larger version of the eigenspace.
It contains the vectors that become zero after we apply $T - \lambda \id$ several times.
Over the complex numbers these spaces always fill the whole space, even when the eigenspaces do not.

### L2 human

Let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ over $\R$ and $\lambda = 0$.

1. The kernel of $N$ is $\R e_1$, since $N(x, y) = (y, 0)$.
2. The square is $N^2 = 0$, so $\ker N^k = \R^2$ for all $k \ge 2$.
3. So $V_0 = \R^2$, while the eigenspace is $\R e_1$.

The typical use is to take $k = n$, which is always enough in dimension $n$.
Watch out: the choice $k = 1$ gives only the eigenspace.

### L3 human

The same definition works for a module over a commutative ring $R$ and $\lambda \in R$.
In infinite dimension, the union can be strictly larger than each kernel, as for the derivative on $\R[x]$ with $\lambda = 0$.

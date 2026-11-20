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

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]], and let $\lambda \in F$.
The *generalized eigenspace* of $T$ for $\lambda$ is
$$V_\lambda = \{v \in V : (T - \lambda \id_V)^k (v) = 0 \text{ for some } k \ge 1\} = \bigcup_{k \ge 1} \ker (T - \lambda \id_V)^k.$$
Its nonzero elements are the [[generalized eigenvectors|0SAAHC36J9]] of $T$ for $\lambda$.

## Notation

Other notations are $V^\lambda$, $G(\lambda, T)$ and $K_\lambda$.
In Mathlib, this subspace is `Module.End.maxGenEigenspace`, the union of the subspaces `Module.End.genEigenspace` for all $k$.

## Remarks

The kernels $\ker (T - \lambda \id_V)^k$ increase with $k$, so their union is a subspace.
It is $T$-[[invariant|0ACX5QT8TE]], since $T$ commutes with $(T - \lambda \id_V)^k$.
It contains the [[eigenspace|0AYEPBQMAW]] $E_\lambda = \ker (T - \lambda \id_V)$.
If $\dim V = n$ is finite, then $V_\lambda = \ker (T - \lambda \id_V)^n$, and its dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$, by the [[dimension of the generalized eigenspace|PHZ684KGWS]].

## Explanations

### L1 human

The generalized eigenspace is a larger version of the eigenspace.
It contains the vectors that become zero after we apply $T - \lambda \id$ several times.
These spaces always fill the space over $\C$, even when the eigenspaces do not.

### L2 human

Let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\lambda = 0$.

1. $\ker N = \R e_1$.
2. $N^2 = 0$, so $\ker N^2 = \R^2$, and $\ker N^k = \R^2$ for all $k \ge 2$.
3. So $V_0 = \R^2$, while the eigenspace is $\R e_1$.

The typical use is to take $k = n$, which is always enough in dimension $n$.
The trap is to take $k = 1$, which only gives the eigenspace.

### L3 human

The same definition works for a module over a commutative ring $R$ and $\lambda \in R$.
In infinite dimension, the union can be strictly larger than each kernel, as for the derivative on $\R[x]$ with $\lambda = 0$.

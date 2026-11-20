---
tag: 0SAAHC36J9
kind: definition
name: Generalized eigenvector
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
defines: 01H6QKWGDH
uses: [0B5H4208Z9, 0BNEXSKNRV]
formal:
  - system: lean4
    library: mathlib
    decl: Module.End.genEigenspace
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]], and let $\lambda \in F$.
A *generalized eigenvector* of $T$ for $\lambda$ is a vector $v \in V$ with $v \ne 0$ and
$$(T - \lambda \id_V)^k (v) = 0$$
for some integer $k \ge 1$.
The least such $k$ is the *rank* of the generalized eigenvector.
Here $(T - \lambda \id_V)^k$ is the [[polynomial $(t - \lambda)^k$ evaluated at $T$|0BNEXSKNRV]].

## Notation

The set $\ker (T - \lambda \id_V)^k$ consists of $0$ and the generalized eigenvectors of rank at most $k$.
The union of these kernels over all $k$ is the [[generalized eigenspace|07PNDWA7CE]] $V_\lambda$.
The Mathlib declaration `Module.End.genEigenspace` gives the subspaces $\ker (T - \lambda \id_V)^k$, indexed by $k$, and not the vectors themselves.
So the match is a variant.

## Remarks

The generalized eigenvectors of rank $1$ are the [[eigenvectors|0B5H4208Z9]].
If a generalized eigenvector $v$ of rank $k$ for $\lambda$ exists, then $(T - \lambda \id_V)^{k-1} v$ is an eigenvector, so $\lambda$ is an eigenvalue.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the vector $e_2$ is a generalized eigenvector for $1$ of rank $2$, and it is not an eigenvector.

## Explanations

### L1 human

Some matrices do not have enough eigenvectors to make a basis.
Generalized eigenvectors fill the gap.
They reach zero after several applications of $T - \lambda \id$, and not always after one.
They are the building blocks of the Jordan normal form.

### L2 human

Let $J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ and $\lambda = 2$.

1. $N = J - 2I$ sends $e_1 \mapsto 0$, $e_2 \mapsto e_1$ and $e_3 \mapsto e_2$.
2. So $N e_1 = 0$, and $e_1$ has rank $1$.
3. $N e_2 = e_1 \ne 0$ and $N^2 e_2 = 0$, so $e_2$ has rank $2$.
4. $N^2 e_3 = e_1 \ne 0$ and $N^3 e_3 = 0$, so $e_3$ has rank $3$.

The typical use is to build a basis of Jordan chains.
The trap is to test only $k = 1$, which finds the eigenvector $e_1$ and misses $e_2$ and $e_3$.

### L3 human

The definition makes sense for a module over any commutative ring, with $\lambda$ in the ring.
In Mathlib, the subspaces $\ker (T - \lambda)^k$ form a monotone family `Module.End.genEigenspace`, and their union is the maximal generalized eigenspace.
For a representation of a nilpotent Lie algebra, the same idea gives generalized weight vectors.

---
tag: 0AYEPBQMAW
kind: definition
name: Eigenspace
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
defines: 0G0RFPG8HR
uses: [0B5H4208Z9, 02YFME3RGW]
formal:
  - system: lean4
    library: mathlib
    decl: Module.End.eigenspace
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an endomorphism, and let $\lambda \in F$.
The *eigenspace* of $T$ for $\lambda$ is
$$E_\lambda = \ker(T - \lambda \id_V) = \{v \in V : T(v) = \lambda v\}.$$

## Notation

Other symbols are $E_\lambda(T)$, $V_\lambda$ and $E(\lambda, T)$.
Mathlib writes `Module.End.eigenspace T λ`, and defines it for every $\lambda$, also when $\lambda$ is not an eigenvalue.

## Remarks

The eigenspace is a subspace of $V$; it is the [[kernel|0S23E6YE83]] of a linear map.
Its nonzero elements are the [[eigenvectors|0N6960W0BV]] of $T$ for $\lambda$.
$E_\lambda \ne 0$ if and only if $\lambda$ is an eigenvalue of $T$.
The dimension of $E_\lambda$ is the [[geometric multiplicity|099TWVJ909]] of $\lambda$.

## Explanations

### L1 human

The eigenspace collects all the vectors that the map stretches by the same factor $\lambda$, with the zero vector.
These vectors form a subspace, for example a line or a plane.
On this subspace, the map acts as multiplication by $\lambda$.

### L2 human

We compute $E_2$ for $A = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ and for $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

1. $A - 2I = 0$, so $E_2(A) = F^2$, of dimension $2$.
2. $B - 2I$ has the rows $(0, 1)$ and $(0, 0)$, so $(B - 2I)v = 0$ means $v_2 = 0$.
3. So $E_2(B)$ is the line spanned by $(1, 0)^{\mathsf{T}}$, of dimension $1$.
4. Check: $B (1, 0)^{\mathsf{T}} = (2, 0)^{\mathsf{T}}$.

The typical use is to compare these dimensions with the algebraic multiplicity, here $2$ for both matrices.
A trap: $A$ and $B$ have the same eigenvalues, but their eigenspaces have different dimensions.

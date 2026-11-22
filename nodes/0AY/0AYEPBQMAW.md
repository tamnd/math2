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

The eigenspace for a scalar $\lambda$ is the set of all vectors that a linear map multiplies by $\lambda$.
Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an endomorphism, and let $\lambda \in F$.
The *eigenspace* of $T$ for $\lambda$ is
$$E_\lambda = \ker(T - \lambda \id_V) = \{ v \in V : T(v) = \lambda v \}.$$

## Notation

Other symbols are $E_\lambda(T)$, $V_\lambda$ and $E(\lambda, T)$.
Mathlib writes `Module.End.eigenspace T λ`, and it defines this space for every $\lambda$, also when $\lambda$ is not an eigenvalue.

## Remarks

The two descriptions of $E_\lambda$ agree, because $(T - \lambda \id_V)(v) = T(v) - \lambda v$ is zero exactly when $T(v) = \lambda v$.
The kernel description shows at once that $E_\lambda$ is a subspace of $V$, since the [[kernel|0S23E6YE83]] of a linear map is a subspace.
The set description shows what the vectors do.

The definition does not ask $\lambda$ to be an eigenvalue.
When it is one, the nonzero elements of $E_\lambda$ are exactly the [[eigenvectors|0N6960W0BV]] of $T$ for $\lambda$.
When it is not, $E_\lambda = 0$; for example, $\operatorname{diag}(1, 2)$ has $E_5 = 0$, because $(1 - 5)v_1 = 0$ and $(2 - 5)v_2 = 0$ force $v = 0$.
The dimension of $E_\lambda$ is the [[geometric multiplicity|099TWVJ909]] of $\lambda$, and the [[concept of an eigenspace|0G0RFPG8HR]] shows how to compute it.

## Explanations

### L1 human

The eigenspace collects all the vectors that the map stretches by the same factor $\lambda$, together with the zero vector.
These vectors form a flat space through the origin, for example a line or a plane.
On this space, the map acts as multiplication by $\lambda$.

### L2 human

We compute $E_2$ for $A = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ and for $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

1. $A - 2I = 0$, so every vector is in the kernel, and $E_2(A) = F^2$ has dimension $2$.
2. $B - 2I$ has the rows $(0, 1)$ and $(0, 0)$, so $(B - 2I)v = 0$ means $v_2 = 0$.
3. So $E_2(B)$ is the line spanned by $(1, 0)$, of dimension $1$.
4. Check: $B(1, 0) = (2, 0) = 2(1, 0)$.

Both matrices have the characteristic polynomial $(t - 2)^2$, so $2$ is a double root for each of them.
Watch out: the same eigenvalue with the same multiplicity as a root can still give eigenspaces of different dimensions.

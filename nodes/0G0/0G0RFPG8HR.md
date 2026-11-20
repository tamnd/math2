---
tag: 0G0RFPG8HR
kind: concept
name: Eigenspace
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
specializes: [0ACX5QT8TE]
uses: [0BQAA2BK3Q, 0N6960W0BV, 0S23E6YE83, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780321982384
---

## Summary

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $\lambda \in F$.
The eigenspace of $T$ for $\lambda$ is the subspace $E_\lambda = \ker(T - \lambda \id_V) = \{v \in V : T(v) = \lambda v\}$.
Its nonzero vectors are the [[eigenvectors|0N6960W0BV]] of $T$ for $\lambda$.
So $E_\lambda \ne 0$ exactly when $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$.
It is an [[invariant subspace|0ACX5QT8TE]] on which $T$ acts as multiplication by $\lambda$.

## Motivation

The eigenvectors for one eigenvalue are not a subspace, because they exclude $0$.
Adding $0$ gives a subspace, the [[kernel|0S23E6YE83]] of $T - \lambda \id_V$.
Its dimension counts the independent directions that $T$ stretches by $\lambda$.
This dimension, the [[geometric multiplicity|099TWVJ909]], decides whether $T$ can be diagonalised.

## Notation

The formal definition is the [[definition of an eigenspace|0AYEPBQMAW]].
Common symbols are $E_\lambda$, $E_\lambda(T)$, $V_\lambda$ and $E(\lambda, T)$, the last one in Axler.
Mathlib writes `Module.End.eigenspace T λ`.

## Remarks

### Examples

- [[The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] has the plane $x + y + z = 0$ as eigenspace for $3$ and the line through $(1, 1, 1)$ as eigenspace for $6$.
- [[The derivative on smooth functions|1SKH5XJ5RB]] has the line spanned by $e^{\lambda x}$ as eigenspace for $\lambda$.
- [[Projections, reflections and shears of the plane|HJ117SV1AN]]: a reflection has a line of fixed vectors and a line of flipped vectors.
- The eigenspace of $\id_V$ for $1$ is all of $V$, and the eigenspace of the zero map for $0$ is all of $V$.

### Non-examples

- [[The union of two eigenspaces is not a subspace|7WYEAWSYNZ]].
- For a scalar $\lambda$ that is not an eigenvalue, $E_\lambda = 0$. Some authors do not call this zero space an eigenspace.

### Basic properties

- $E_\lambda$ is a subspace, because it is the kernel of the linear map $T - \lambda \id_V$.
- $T(E_\lambda) \subseteq E_\lambda$, and $T$ restricted to $E_\lambda$ is $\lambda \id_{E_\lambda}$.
- For distinct scalars $\lambda_1, \dots, \lambda_k$, the sum $E_{\lambda_1} + \dots + E_{\lambda_k}$ is direct, by the theorem that [[eigenvectors for distinct eigenvalues are linearly independent|0HNMFG8F8K]].
- So, for $\dim V = n$, the dimensions of the eigenspaces add up to at most $n$.
- $T$ is [[diagonalisable|07SQCNV233]] exactly when $V$ is the direct sum of its eigenspaces.
- In finite dimension, $\dim E_\lambda = \dim V - \operatorname{rank}(T - \lambda \id_V)$, by [[rank-nullity|0W4FSW1TVB]].
- If $S$ commutes with $T$, then $S(E_\lambda) \subseteq E_\lambda$.

### History

Lagrange saw that the principal axes of a rotating rigid body are the eigenvectors of the inertia matrix.
Cauchy used this work to classify quadric surfaces, and he generalized it to arbitrary dimensions.

### Common errors

- Forgetting the zero vector. The eigenspace contains $0$; the set of eigenvectors does not.
- Taking the union of eigenspaces instead of their sum.
- Confusing the eigenspace with the generalised eigenspace $\ker(T - \lambda \id_V)^n$. They differ when $\lambda$ is defective, as for the shear.

## Explanations

### L1 human

For one stretch factor $\lambda$, collect all vectors that the map stretches by exactly $\lambda$.
Add the zero vector.
The result is a line, a plane or a bigger flat space through the origin.
This space is the eigenspace for $\lambda$.
On it, the map is just "multiply by $\lambda$".

### L2 human

We compute the eigenspace of $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$ for $\lambda = 3$.

1. $A - 3I$ has three equal rows $(1, 1, 1)$.
2. So $(A - 3I)v = 0$ means $v_1 + v_2 + v_3 = 0$.
3. A basis of the solutions is $(1, -1, 0)^{\mathsf{T}}$ and $(1, 0, -1)^{\mathsf{T}}$, so $\dim E_3 = 2$.
4. Check: $A (1, -1, 0)^{\mathsf{T}} = (3, -3, 0)^{\mathsf{T}}$ and $A (1, 0, -1)^{\mathsf{T}} = (3, 0, -3)^{\mathsf{T}}$.

The typical use is to find a basis of each eigenspace and to join these bases into an eigenbasis.
A trap: a basis of $E_\lambda$ comes from the null space of $A - \lambda I$, not from the column space.

### L3 human

The eigenspace $E_\lambda$ is the largest subspace on which $T$ acts as the scalar $\lambda$.
For a commuting family of endomorphisms, each eigenspace of one member is invariant under the others, which leads to simultaneous diagonalisation.
In the module language, $E_\lambda$ is the submodule of $V$ killed by $x - \lambda$ in $F[x]$.
For self-adjoint operators on inner product spaces, distinct eigenspaces are orthogonal.

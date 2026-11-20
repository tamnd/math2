---
tag: 0AJ035ZTZE
kind: concept
name: Generalized eigenspace
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
specializes: [0ACX5QT8TE]
uses: [01H6QKWGDH, 0G0RFPG8HR, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
  - book: isbn:9780134860244
    locator: Section 7.1
---

## Summary

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space over a field $F$, and let $\lambda \in F$.
The [[generalized eigenspace|07PNDWA7CE]] $V_\lambda$ is the set of vectors $v$ with $(T - \lambda \id_V)^k v = 0$ for some $k \ge 1$.
Its nonzero elements are the [[generalized eigenvectors|01H6QKWGDH]] for $\lambda$.
In dimension $n$, $V_\lambda = \ker (T - \lambda \id_V)^n$, it is a $T$-[[invariant subspace|0ACX5QT8TE]], and its dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.

## Motivation

The [[eigenspace|0G0RFPG8HR]] of $\lambda$ can be smaller than the algebraic multiplicity, and then the eigenspaces do not fill $V$.
The generalized eigenspaces always have the right size.
Over $\C$, $V$ is the direct sum of the generalized eigenspaces, by the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
This reduces the study of $T$ to maps with a single eigenvalue, and leads to the [[Jordan normal form|085HQ5G5TE]].

## Notation

Common notations are $V_\lambda$, $V^\lambda$, $G(\lambda, T)$ in Axler, and $K_\lambda$ in Friedberg, Insel and Spence.
In Mathlib, `Module.End.maxGenEigenspace` is the union of the subspaces $\ker (T - \lambda)^k$.
The subspaces themselves, indexed by $k$, are `Module.End.genEigenspace`.

## Remarks

### Examples

- For the [[Jordan block of size 3|1YGY396SAS]] with eigenvalue $2$, $V_2 = F^3$, while the eigenspace is the line $F e_1$.
- For the [[3 × 3 matrix with eigenvalues 1, 2, 2|18WSA33PKA]], $V_2$ is the plane $z = 0$ and $V_1$ is the line spanned by $(1, 1, -1)$.
- For [[the matrix with p = (t − 2)²|6918MS1QRN]], $V_2 = \R^2$, while the eigenspace is a line.
- For a [[diagonalizable|07SQCNV233]] map, each $V_\lambda$ is the eigenspace $E_\lambda$, since $T - \lambda$ is invertible on the sum of the other eigenspaces.
- For the [[derivative on cubic polynomials|7DGJWWZ8DW]], $V_0$ is the whole space.

### Non-examples

- For the [[sum of two eigenvectors|EWGV69Z2VZ]] $(1, 1)$ of $\operatorname{diag}(1, 2)$, the vector lies in no generalized eigenspace. So the union of the $V_\lambda$ is not a subspace.
- The kernel $\ker (T - \lambda)$ alone is not the generalized eigenspace when $T$ has a nontrivial Jordan block for $\lambda$, as for the [[shear|SBDF8APDF7]].
- For the rotation by a right angle over $\R$, every real $\lambda$ has $V_\lambda = 0$.

### Basic properties

- $E_\lambda \subseteq V_\lambda$, and $V_\lambda \ne 0$ exactly when $\lambda$ is an eigenvalue.
- $V_\lambda$ is invariant under $T$ and under every map that commutes with $T$, since it is the kernel of a polynomial in $T$.
- In dimension $n$, $\dim V_\lambda$ equals the algebraic multiplicity of $\lambda$, by the [[dimension of the generalized eigenspace|PHZ684KGWS]].
- On $V_\lambda$, $T - \lambda$ is [[nilpotent|063D5Z2C70]], and $T$ has the single eigenvalue $\lambda$.
- Generalized eigenspaces for distinct $\lambda$ form a direct sum, by the [[kernels lemma|ACBNK1VFVG]].

### History

Generalized eigenspaces are the pieces of the space on which Jordan's normal form has blocks with a single eigenvalue.
The name and the notation $G(\lambda, T)$ are used in Axler, Chapter 8, where they replace determinants in the proof of the Jordan form.

### Common errors

- Using $\ker (T - \lambda)$ instead of $\ker (T - \lambda)^n$. This gives the eigenspace, which can be too small.
- Expecting $\dim V_\lambda$ to equal the geometric multiplicity. It equals the algebraic multiplicity.
- Thinking that the stable power is always $n$. The kernels stop growing at a power at most the algebraic multiplicity, and often earlier.

## Explanations

### L1 human

The eigenspace collects the vectors that $T$ only stretches by $\lambda$.
The generalized eigenspace also collects the vectors that $T - \lambda$ sends to zero after a few steps.
It is a bigger space that always has the size predicted by the characteristic polynomial.
Over the complex numbers, these spaces fill the whole space.

### L2 human

Let $J = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix}$ and $\lambda = 4$.

1. $J - 4I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, so the eigenspace is $\R e_1$.
2. $(J - 4I)^2 = 0$, so $V_4 = \R^2$.
3. $p_J = (t - 4)^2$, so the algebraic multiplicity is $2 = \dim V_4$.

The typical use is to split $V$ into the $V_\lambda$ and study each piece, where $T$ has one eigenvalue.
The trap is to compute $V_\lambda$ as the eigenspace and then find that the pieces do not fill $V$.

### L3 human

$V_\lambda$ is the $(t - \lambda)$-primary component of $V$ viewed as an $F[t]$-module, with $t$ acting as $T$.
For a nilpotent Lie algebra acting on a finite-dimensional module, the generalized weight spaces play the same role.
In infinite dimension, $V_\lambda$ is still an invariant subspace, but $V$ need not be the sum of the $V_\lambda$.

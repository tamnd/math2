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

The generalized eigenspace of $\lambda$ is the eigenspace made large enough.
It always has the size that the characteristic polynomial predicts, even when the ordinary eigenspace is too small.
Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space over a field $F$, and let $\lambda \in F$.
The [[generalized eigenspace|07PNDWA7CE]] of $T$ for $\lambda$ is
$$V_\lambda = \{ v \in V : (T - \lambda \id_V)^k v = 0 \text{ for some } k \ge 1 \}.$$
Its nonzero elements are the [[generalized eigenvectors|01H6QKWGDH]] for $\lambda$.
When $\dim V = n$ is finite, $V_\lambda = \ker (T - \lambda \id_V)^n$, it is a $T$-[[invariant subspace|0ACX5QT8TE]], and its dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.

## Motivation

A map is diagonalizable when its eigenspaces fill $V$.
Often they do not, because the [[eigenspace|0G0RFPG8HR]] of $\lambda$ has a smaller dimension than the algebraic multiplicity.
The generalized eigenspaces never have that defect.
When the characteristic polynomial splits, for example over $\C$, the [[decomposition into generalized eigenspaces|0Z3GDY89T5]] gives
$$V = V_{\lambda_1} \oplus \dots \oplus V_{\lambda_k}.$$

This splitting reduces the study of $T$ to maps with a single eigenvalue.
On each piece, $T$ is $\lambda$ times the identity plus a nilpotent map, and the [[Jordan normal form|085HQ5G5TE]] of the next sub-area describes that nilpotent map.
Powers $T^m$ and exponentials $e^{tT}$, which appear in recurrences and in linear differential equations, are computed piece by piece in the same way.

## Notation

Books write $V_\lambda$, $V^\lambda$, $G(\lambda, T)$ (Axler) or $K_\lambda$ (Friedberg, Insel and Spence).
In Mathlib, `Module.End.maxGenEigenspace` is the union of the kernels $\ker (T - \lambda)^k$, and the single kernels are `Module.End.genEigenspace`.
Watch out for $V_\lambda$: some books use the same symbol for the ordinary eigenspace, so check the definition before you use a formula.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$ over $\R$, which is [[the example with p = (t − 2)²|6918MS1QRN]].
The trace is $4$ and the determinant is $4$, so $p_A = t^2 - 4t + 4 = (t - 2)^2$.
Subtract $2I$ and square:
$$A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}, \qquad (A - 2I)^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
The eigenspace $\ker(A - 2I)$ is the line spanned by $(1, -1)$, but $V_2 = \ker (A - 2I)^2$ is all of $\R^2$.
So $\dim V_2 = 2$ matches the multiplicity of the root $2$, while the eigenspace has dimension $1$.

### More examples

For the [[Jordan block of size 3|1YGY396SAS]] with eigenvalue $2$, the generalized eigenspace $V_2$ is $F^3$, while the eigenspace is the line $F e_1$.
For the [[3 × 3 matrix with eigenvalues 1, 2, 2|18WSA33PKA]], $V_2$ is the plane $z = 0$ and $V_1$ is the line spanned by $(1, 1, -1)$.
For the [[derivative on real cubic polynomials|7DGJWWZ8DW]], $V_0$ is the whole space, since the fourth derivative of a cubic is $0$.

For a [[diagonalizable|07SQCNV233]] map, each $V_\lambda$ equals the eigenspace $E_\lambda$.
The reason is that $T - \lambda$ acts on each other eigenspace $E_\mu$ as the nonzero scalar $\mu - \lambda$, so a power of it sends no nonzero vector of their sum to $0$.

### What it is not

The union of all the $V_\lambda$ is not a subspace.
For $\operatorname{diag}(1, 2)$, the [[sum of two eigenvectors|EWGV69Z2VZ]] $(1, 1)$ lies in neither $V_1$ nor $V_2$.
The kernel $\ker(T - \lambda)$ alone is not the generalized eigenspace when $T$ has too few eigenvectors, as for the [[shear|SBDF8APDF7]], where $\ker(S - I)$ is a line and $V_1 = F^2$.
For the rotation of $\R^2$ by a right angle, every real $\lambda$ has $V_\lambda = 0$, because there is no real eigenvalue.

### The rules you can use

The eigenspace lies inside the generalized eigenspace, since $k = 1$ is allowed, and $V_\lambda \ne 0$ exactly when $\lambda$ is an eigenvalue.
The space $V_\lambda$ is a kernel of a polynomial in $T$, so it is invariant under $T$ and under every map that commutes with $T$.
In dimension $n$, the [[dimension of the generalized eigenspace|PHZ684KGWS]] shows that $\dim V_\lambda$ equals the algebraic multiplicity of $\lambda$.
On $V_\lambda$ the map $T - \lambda$ is [[nilpotent|063D5Z2C70]], so $\lambda$ is the only eigenvalue of $T$ there.
Generalized eigenspaces for distinct scalars form a direct sum, by the [[kernels lemma|ACBNK1VFVG]].

### Watch out

The first trap is to compute $\ker(T - \lambda)$ and call it the generalized eigenspace.
For the matrix $A$ above that gives a line, and then the pieces do not fill $\R^2$.
The correct move is to take powers until the dimension reaches the algebraic multiplicity.

The second trap is to expect $\dim V_\lambda$ to equal the geometric multiplicity.
It equals the algebraic multiplicity, and the two differ for $A$.

### Try it

First, find $V_3$ for $B = \begin{pmatrix} 3 & 0 \\ 5 & 3 \end{pmatrix}$.
Here $B - 3I = \begin{pmatrix} 0 & 0 \\ 5 & 0 \end{pmatrix}$ squares to $0$, so $V_3 = \R^2$, while the eigenspace is the line $\R e_2$.

Second, find $V_1$ for $C = \operatorname{diag}(1, 1, 4)$.
The map $C - I = \operatorname{diag}(0, 0, 3)$ has every power equal to $\operatorname{diag}(0, 0, 3^k)$, so $V_1 = \operatorname{span}(e_1, e_2)$, which is the eigenspace.

## Explanations

### L1 human

The eigenspace collects the vectors that $T$ only stretches by $\lambda$.
The generalized eigenspace also collects the vectors that $T - \lambda$ sends to zero after a few steps.
For the matrix $J = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix}$, only the horizontal line is stretched by $4$, but every vector reaches zero when we apply $J - 4I$ to it twice.
So the generalized eigenspace is the whole plane, which matches the double root $4$.

### L2 human

Let $J = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix}$ and $\lambda = 4$.
Subtract $4I$ and square:
$$J - 4I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad (J - 4I)^2 = 0.$$
The eigenspace is $\ker(J - 4I) = \R e_1$, and the generalized eigenspace is $\ker(J - 4I)^2 = \R^2$.
Check: $p_J = (t - 4)^2$, so the algebraic multiplicity is $2 = \dim V_4$.

Now compute $J^m$ with this knowledge.
Write $J = 4I + N$ with $N = J - 4I$, and note that $4I$ and $N$ commute and $N^2 = 0$.
The binomial formula stops after two terms:
$$J^m = 4^m I + m \, 4^{m-1} N = \begin{pmatrix} 4^m & m \, 4^{m-1} \\ 0 & 4^m \end{pmatrix}.$$
This is the typical use: on a generalized eigenspace, $T$ is a scalar plus a nilpotent map, and powers become finite sums.

### L3 human

Make $V$ a module over $F[t]$, with $t$ acting as $T$.
Then $V_\lambda$ is the $(t - \lambda)$-primary component of this module.
When the characteristic polynomial does not split, the [[primary decomposition theorem|49ZHBMYKVE]] uses the kernels of powers of the irreducible factors instead.
In infinite dimension, $V_\lambda$ is still an invariant subspace, but $V$ need not be the sum of the $V_\lambda$.
For a commuting family of maps, or a nilpotent Lie algebra acting on a module over $\C$, the same idea gives generalized weight spaces.

---
tag: 01H6QKWGDH
kind: concept
name: Generalized eigenvector
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
uses: [0N6960W0BV, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
  - book: isbn:9780134860244
    locator: Section 7.1
same_as:
  wikidata: Q970767
  wikipedia: Generalized eigenvector
---

## Summary

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $\lambda \in F$.
A [[generalized eigenvector|0SAAHC36J9]] of $T$ for $\lambda$ is a vector $v \ne 0$ with $(T - \lambda \id_V)^k v = 0$ for some integer $k \ge 1$; the least such $k$ is its rank.
The generalized eigenvectors of rank $1$ are the [[eigenvectors|0N6960W0BV]].
Generalized eigenvectors fill the gap left by a matrix that has too few eigenvectors: over $\C$, every finite-dimensional space has a basis of them.

## Motivation

The [[shear|~58e14c85]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has only one line of eigenvectors, so it is not [[diagonalizable|07SQCNV233]].
The vector $e_2$ is not an eigenvector, but $(S - I) e_2 = e_1$ is one, so $(S - I)^2 e_2 = 0$.
Allowing higher powers of $T - \lambda$ recovers enough vectors to make a basis, and this leads to the [[Jordan normal form|085HQ5G5TE]].

## Notation

We write $N_\lambda = T - \lambda \id_V$.
A Jordan chain of length $k$ is a list $v, N_\lambda v, \dots, N_\lambda^{k-1} v$ with $N_\lambda^{k-1} v \ne 0$ and $N_\lambda^k v = 0$.
Some books order the chain the other way, starting from the eigenvector $N_\lambda^{k-1} v$.
The rank is also called the height, the order or the grade.
In Mathlib, the generalized eigenvectors of rank at most $k$, together with $0$, form `Module.End.genEigenspace`.

## Remarks

### Examples

- For the shear, $e_2$ is a generalized eigenvector for $1$ of rank $2$, since $(S - I) e_2 = e_1 \ne 0$ and $(S - I)^2 = 0$.
- For the [[Jordan block of size 3|~6530bcca]], $e_3$ has rank $3$, and its chain is $e_3, e_2, e_1$.
- For the [[derivative on cubic polynomials|~6463dbd0]], every nonzero polynomial is a generalized eigenvector for $0$. The rank of a polynomial of degree $d$ is $d + 1$.
- For the [[3 × 3 matrix with a repeated eigenvalue|~47d94525]], $(0, 1, 0)$ is a generalized eigenvector for $2$ of rank $2$.
- For the [[matrix with the single eigenvalue 2|~b3d99dba]], every nonzero vector of $\R^2$ is a generalized eigenvector for $2$.

### Non-examples

- The [[vector (1, 1) for diag(1, 2)|~19a26702]] is not a generalized eigenvector for any scalar: it has components in two eigenspaces.
- The zero vector is never a generalized eigenvector, by definition.
- For the rotation by a right angle over $\R$, no real $\lambda$ has a generalized eigenvector, since $\lambda$ would be an eigenvalue.

### Basic properties

- If $v$ has rank $k$ for $\lambda$, then $N_\lambda^{k-1} v$ is an eigenvector for $\lambda$. So $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]].
- The vectors of a Jordan chain are linearly independent. Apply $N_\lambda^{k-1}$ to a relation $\sum_j c_j N_\lambda^j v = 0$ to get $c_0 = 0$, and repeat with lower powers.
- In dimension $n$, every generalized eigenvector has rank at most $n$. This follows from the chain independence, and also from the [[dimension of the generalized eigenspace|~b8d53cf6]].
- Generalized eigenvectors for distinct eigenvalues are linearly independent, by the [[kernels lemma|~4b2aa8fd]], since $(t - \lambda)^k$ and $(t - \mu)^l$ are coprime.
- The generalized eigenvectors for $\lambda$, together with $0$, form the [[generalized eigenspace|0AJ035ZTZE]].

### History

Generalized eigenvectors appear implicitly in the normal form of Jordan, whose 1870 treatise reduced matrices over finite fields to blocks.
The name "generalized eigenvector" is standard in modern textbooks, for example in Axler, Chapter 8.

### Common errors

- Thinking that a generalized eigenvector is an eigenvector of $T^k$. It is a vector killed by $(T - \lambda)^k$, which is different unless $\lambda = 0$.
- Forgetting to fix $\lambda$. A vector can be a generalized eigenvector for one scalar only, but a sum of generalized eigenvectors for different scalars is in general not one.
- Taking $k$ larger than needed as the rank. The rank is the least $k$, and it is at most the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.

## Explanations

### L1 human

An eigenvector is a direction that a matrix only stretches.
Some matrices, like the shear, have too few such directions.
A generalized eigenvector is a direction that becomes an eigenvector after we remove the stretching once or several times.
These extra directions are enough to describe every matrix over the complex numbers.

### L2 human

Find the generalized eigenvectors of $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ for $2$.

1. $N = A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and $N^2 = 0$.
2. So every nonzero $v \in \R^2$ satisfies $N^2 v = 0$, and it is a generalized eigenvector.
3. $N(x, y) = (y, 0)$. So $v$ has rank $1$ if $y = 0$, and rank $2$ if $y \ne 0$.
4. The chain of $e_2$ is $e_2, e_1$, and in the basis $(e_1, e_2)$ the matrix is already the Jordan block $A$.

The typical use is to complete a set of eigenvectors to a basis in which the matrix has Jordan form.
The trap is to stop at $k = 1$: then only the line $\R e_1$ appears, and the second basis vector is missing.

### L3 human

The generalized eigenvectors for $\lambda$ are the nonzero elements of the $(t - \lambda)$-primary part of $V$ as an $F[t]$-module.
In infinite dimension, the rank can be unbounded, as for the derivative on all polynomials.
For a Lie algebra acting on a module, generalized weight vectors play the same role, and they give the generalized weight spaces of Fitting's decomposition.

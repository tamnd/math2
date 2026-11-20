---
tag: 0E3MV6E6MG
kind: concept
name: Polynomial of an endomorphism
aliases: [polynomials-in-an-endomorphism, matrix-polynomial]
msc: ["15A04", "15A54"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [0PTF1PTJK0, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_polynomial
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780135367971
same_as:
  wikidata: Q6787887
  wikipedia: Matrix polynomial
---

## Summary

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0PTF1PTJK0]].
For a polynomial $p(x) = c_0 + c_1 x + \cdots + c_d x^d$ in $F[x]$, the endomorphism $p(T)$ is $c_0 I + c_1 T + \cdots + c_d T^d$.
The map $p \mapsto p(T)$ from the [[polynomial ring|0Q9EZS90GY]] $F[x]$ to $\End_F(V)$ is a homomorphism of $F$-algebras, called evaluation at $T$.
Its image $F[T]$ is a commutative subalgebra of $\End_F(V)$.
The eigenvalues of $p(T)$ are the values $p(\lambda)$ at the eigenvalues $\lambda$ of $T$, over an algebraically closed field.

## Motivation

Polynomials in $T$ are the simplest maps built from $T$ alone.
They commute with $T$, and they preserve every eigenspace and every invariant subspace of $T$.
The [[minimal polynomial|03NDVCSHSB]] and the [[Cayley-Hamilton theorem|0F765KFC2J]] are statements about the polynomials $p$ with $p(T) = 0$.
Functions of a matrix such as $e^A$ are limits of polynomials in $A$.

## Notation

The formal definition is the [[definition of the value of a polynomial at an endomorphism|0BNEXSKNRV]].
Mathlib writes `Polynomial.aeval T p` for $p(T)$.
The constant term $c_0$ becomes $c_0 I$, never the scalar $c_0$.
For a square matrix $A$, $p(A) = c_0 I_n + c_1 A + \cdots + c_d A^d$.

## Remarks

### Examples

- [[A polynomial in a symmetric 2 by 2 matrix|SPNE23C2MM]]: for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $p(x) = x^2 - 4x$, $p(A) = -3I$.
- [[Polynomials in a projection|F5TTF31NR5]]: if $P^2 = P$, then $p(P) = p(0)(I - P) + p(1)P$.
- For a diagonal matrix $D = \operatorname{diag}(d_1, \dots, d_n)$, $p(D) = \operatorname{diag}(p(d_1), \dots, p(d_n))$.
- For $A = SDS^{-1}$, $p(A) = S\, p(D)\, S^{-1}$, because $(SDS^{-1})^k = SD^kS^{-1}$.

### Non-examples

- [[The entrywise square is not a polynomial in the matrix|P50X3T3Y9V]]: it does not commute with the matrix.
- $p(A)$ is not obtained by applying $p$ to each entry of $A$. For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $p(x) = x^2$, $p(A) = 0$, while the entrywise square is $A$.

### Basic properties

- $(p + q)(T) = p(T) + q(T)$, $(cp)(T) = c\,p(T)$, $(pq)(T) = p(T)q(T)$ and $1(T) = I$.
- So $p(T)q(T) = q(T)p(T)$, and $F[T]$ is commutative.
- If $T v = \lambda v$, then $p(T)v = p(\lambda)v$. So each eigenvector of $T$ is an eigenvector of $p(T)$.
- The theorem on the [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]] gives $\sigma(p(T)) = p(\sigma(T))$ over an algebraically closed field, and $\sigma(T^{-1}) = \{1/\lambda : \lambda \in \sigma(T)\}$.
- If $V$ is finite-dimensional, then $F[T]$ has dimension equal to the degree of the minimal polynomial, by the theorem on [[annihilating polynomials|AH34SFJ8SF]].
- Every subspace that is invariant under $T$ is invariant under $p(T)$. In particular $\ker p(T)$ and $\operatorname{im} p(T)$ are invariant under $T$.

### History

Cayley stated the Cayley-Hamilton theorem $p_A(A) = 0$ in 1858.
Frobenius gave the first general proof in 1878.

### Common errors

- Writing the constant term as $c_0$ instead of $c_0 I$, which gives a sum of a matrix and a scalar.
- Expanding $(A + B)^2$ as $A^2 + 2AB + B^2$ when $A$ and $B$ do not commute. This is valid inside $F[T]$, but not for two arbitrary matrices.
- Assuming that $p(A) = 0$ forces $A$ to be a scalar root of $p$. For $p(x) = x^2$, the nonzero matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ satisfies $p(A) = 0$.

## Explanations

### L1 human

Matrices can be added, scaled and multiplied, so a matrix can be put into a polynomial.
The constant term becomes a multiple of the identity matrix.
For example, if $p(x) = x^2 - 3x + 2$, then $p(A) = A^2 - 3A + 2I$.
If $v$ is an eigenvector of $A$ for $\lambda$, then $p(A)$ multiplies $v$ by the number $p(\lambda)$.

### L2 human

We compute $p(A)$ for $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ and $p(x) = x^2 - 3x + 2$.

1. $A^2 = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix}$, because the $(1,2)$ entry is $1 \cdot 2 + 2 \cdot 3 = 8$.
2. $p(A) = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix} - \begin{pmatrix} 3 & 6 \\ 0 & 9 \end{pmatrix} + \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 2 \end{pmatrix}$.
3. The eigenvalues of $A$ are $1$ and $3$, and $p(1) = 0$ and $p(3) = 2$. The diagonal of the triangular matrix $p(A)$ shows the same values.
4. The eigenvector $e_1$ for $1$ gives $p(A)e_1 = 0 = p(1)e_1$.

The typical use is to reduce a question about $p(A)$ to a question about the numbers $p(\lambda)$.
A trap: $p(A)$ is not the matrix of the values $p(a_{ij})$.

### L3 human

Evaluation at $T$ makes $V$ into a module over $F[x]$, with $x \cdot v = Tv$.
Invariant subspaces of $T$ are the submodules, and the kernel of evaluation is the annihilator ideal of the module.
The structure theorem for finitely generated modules over a principal ideal domain then gives the rational and Jordan canonical forms.

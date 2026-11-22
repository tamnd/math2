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

Linear maps of a space to itself can be added, scaled and composed, so we can substitute such a map into a polynomial.
The result is a new linear map built from $T$ alone, and it acts on each eigenvector of $T$ by the polynomial evaluated at the eigenvalue.

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0PTF1PTJK0]].
For $p(x) = c_0 + c_1 x + \dots + c_d x^d$ in the [[polynomial ring|0Q9EZS90GY]] $F[x]$, the endomorphism $p(T)$ is
$$p(T) = c_0 I + c_1 T + c_2 T^2 + \dots + c_d T^d,$$
where $I$ is the identity map and $T^k$ is $T$ composed with itself $k$ times.
The map $p \mapsto p(T)$ from $F[x]$ to $\operatorname{End}_F(V)$ is a homomorphism of $F$-algebras, called *evaluation at $T$*.
Its image $F[T]$ is a commutative subalgebra of $\operatorname{End}_F(V)$.

## Motivation

Polynomials in $T$ are the simplest maps that we can make out of $T$ and nothing else.
They commute with $T$, and they keep every eigenspace and every invariant subspace of $T$.
So they are the natural tools for cutting $V$ into pieces on which $T$ is simple.
The kernels $\ker (T - \lambda I)^k$ that lead to the Jordan form in a later sub-area are kernels of polynomials in $T$.

The main questions of the next pages are about the polynomials that make $T$ zero.
An [[annihilating polynomial|0PBN8VEKY8]] is a $p$ with $p(T) = 0$, the [[minimal polynomial|03NDVCSHSB]] is the smallest one, and the [[Cayley-Hamilton theorem|0F765KFC2J]] says that the characteristic polynomial is one of them.
Outside linear algebra, functions of a matrix such as $e^A$, used to solve systems of linear differential equations, are limits of polynomials in $A$.

## Notation

The formal statement is the [[definition of the value of a polynomial at an endomorphism|0BNEXSKNRV]].
For a square matrix $A$ we write $p(A) = c_0 I_n + c_1 A + \dots + c_d A^d$ in the same way.
Mathlib writes `Polynomial.aeval T p` for $p(T)$.
Watch the constant term: it becomes the map $c_0 I$, never the scalar $c_0$, since a matrix plus a number has no meaning.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ and $p(x) = x^2 - 3x + 2$.
First square the matrix; the corner entry is $1 \cdot 2 + 2 \cdot 3 = 8$:
$$A^2 = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix}.$$
Then combine, with the constant $2$ turned into $2I$:
$$p(A) = \begin{pmatrix} 1 & 8 \\ 0 & 9 \end{pmatrix} - \begin{pmatrix} 3 & 6 \\ 0 & 9 \end{pmatrix} + \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 2 \end{pmatrix}.$$
The eigenvalues of $A$ are $1$ and $3$, and $p(1) = 0$, $p(3) = 9 - 9 + 2 = 2$.
These are exactly the diagonal entries of the triangular matrix $p(A)$.

### Why eigenvectors behave so well

If $Tv = \lambda v$, then $T^2 v = T(\lambda v) = \lambda^2 v$, and by induction $T^k v = \lambda^k v$.
Adding up the terms gives
$$p(T)v = c_0 v + c_1 \lambda v + \dots + c_d \lambda^d v = p(\lambda)\, v.$$
So every eigenvector of $T$ is an eigenvector of $p(T)$, for the eigenvalue $p(\lambda)$.
The theorem on the [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]] adds the converse over an algebraically closed field: the eigenvalues of $p(T)$ are exactly the numbers $p(\lambda)$.
It also gives the eigenvalues $1/\lambda$ of $T^{-1}$ when $T$ is invertible.
In [[a polynomial in a symmetric 2 by 2 matrix|SPNE23C2MM]], the polynomial $x^2 - 4x$ sends both eigenvalues $1$ and $3$ of $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ to $-3$, and so $p(A) = -3I$.

### The rules you can use

Evaluation respects the algebra: $(p + q)(T) = p(T) + q(T)$, $(cp)(T) = c\,p(T)$, $(pq)(T) = p(T)q(T)$ and $1(T) = I$.
The product rule holds because $T^j T^k = T^{j+k}$ and composition distributes over sums.
Since $pq = qp$, it follows that $p(T)q(T) = q(T)p(T)$, so $F[T]$ is commutative.
Every subspace that $T$ maps into itself, $p(T)$ maps into itself too, and $\ker p(T)$ and $\operatorname{im} p(T)$ are invariant under $T$.
For a diagonal matrix, $p(\operatorname{diag}(d_1, \dots, d_n)) = \operatorname{diag}(p(d_1), \dots, p(d_n))$, and for $A = SDS^{-1}$ we get $p(A) = S\,p(D)\,S^{-1}$, because $(SDS^{-1})^k = SD^kS^{-1}$.
If $\dim V$ is finite, then $\dim F[T]$ equals the degree of the minimal polynomial, by the theorem that the [[ideal of annihilating polynomials is nonzero and principal|AH34SFJ8SF]].
For a projection $P$ with $P^2 = P$, every polynomial collapses to $p(P) = p(0)(I - P) + p(1)P$, as [[polynomials in a projection of the plane|F5TTF31NR5]] shows.

### What it is not

A polynomial in $A$ is not the matrix of the values $p(a_{ij})$.
For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $p(x) = x^2$, the matrix product gives $A^2 = 0$, while squaring each entry gives back $A$.
In the same way, [[the entrywise square is not a polynomial in the matrix|P50X3T3Y9V]]: for $\begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}$ it does not even commute with the matrix, and every polynomial in the matrix does.

### Watch out

The rules of ordinary algebra hold inside $F[T]$ because its elements commute, but not for two arbitrary maps.
With $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ we get $(A + B)^2 = I$, while $A^2 + 2AB + B^2 = 2AB = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$.
A second trap is to think that $p(A) = 0$ forces $A$ to be a scalar root of $p$.
The same nonzero $A$ satisfies $A^2 = 0$, although the only root of $x^2$ is $0$.

### History

Cayley's memoir on the theory of matrices of 1858 already substituted a matrix into its own characteristic polynomial and stated that the result is zero.
Frobenius gave a general proof of that statement in 1878.

### Try it

First, compute $p(A)$ for $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $p(x) = x^2 - x - 1$.
Since $A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, we get $A^2 - A - I = 0$, so this $p$ kills $A$.

Second, $Tv = 2v$ with $v \ne 0$; find $(T^3 - 4T + I)v$.
It is $(8 - 8 + 1)v = v$.

## Explanations

### L1 human

Matrices can be added, scaled and multiplied, so you can put a matrix into a polynomial.
The only change is that the constant term becomes a multiple of the identity matrix.
For example, $p(x) = x^2 - 3x + 2$ gives $p(A) = A^2 - 3A + 2I$.
If $v$ is a direction that $A$ stretches by $3$, then $p(A)$ stretches $v$ by $p(3) = 2$.
So the polynomial acts on each special direction just as it acts on the stretch factor.

### L2 human

Here is a typical use: find $A^{10}$ times $v = (1, 1)^{\mathsf{T}}$ for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ without computing $A^{10}$.
The vector $v$ is an eigenvector: $Av = (3, 3)^{\mathsf{T}} = 3v$.
So for $p(x) = x^{10}$ the rule $p(A)v = p(3)v$ gives
$$A^{10} v = 3^{10} v = 59049\, (1, 1)^{\mathsf{T}}.$$
For a vector that is not an eigenvector, such as $e_1 = \tfrac{1}{2}(1, 1)^{\mathsf{T}} + \tfrac{1}{2}(1, -1)^{\mathsf{T}}$, split it first into eigenvectors; since $A(1, -1)^{\mathsf{T}} = (1, -1)^{\mathsf{T}}$,
$$A^{10} e_1 = \tfrac{1}{2} \cdot 3^{10} (1, 1)^{\mathsf{T}} + \tfrac{1}{2} (1, -1)^{\mathsf{T}} = (29525, 29524)^{\mathsf{T}}.$$
Check: the entries must add up to $3^{10} = 59049$, and $29525 + 29524 = 59049$.
Watch out: the shortcut needs the vector split into eigenvectors first, because $p(A)$ acts on each eigenvector with a different factor.

### L3 human

Evaluation at $T$ makes $V$ into a module over $F[x]$, with $x \cdot v = Tv$.
The invariant subspaces of $T$ are the submodules, and the kernel of evaluation is the annihilator ideal of the module, generated by the minimal polynomial.
The structure theorem for finitely generated modules over a principal ideal domain then gives the rational and Jordan canonical forms of the later sub-area on canonical forms.
In analysis, the same substitution extends from polynomials to power series and to holomorphic functions, the holomorphic functional calculus.

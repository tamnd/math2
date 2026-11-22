---
tag: 0XPX5NC67E
kind: concept
name: Spectrum of a matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [0BQAA2BK3Q, 0JXZKX526R, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_of_a_matrix
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Spectral_theory
    locator: Mathematical background
  - url: https://www.math.brown.edu/streil/papers/LADW/LADW.html
    locator: Chapter 4
same_as:
  wikidata: Q3490774
  wikipedia: Spectrum of a matrix
inventory: [9F89D494GH]
---

## Summary

The spectrum of a square matrix is the set of all its eigenvalues.
It is one object that records every stretch factor of the matrix at once, and many questions about the matrix are answered by looking at it.
Let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] over a field $F$.
The *spectrum* of $A$ is the set $\sigma(A)$ of its [[eigenvalues|0BQAA2BK3Q]] in $F$, that is,
$$\sigma(A) = \{ \lambda \in F : A - \lambda I_n \text{ is not invertible} \}.$$
It has at most $n$ elements, and over an algebraically closed field such as $\mathbb{C}$ it is nonempty when $n \ge 1$.
The [[formal definition|04EHB7YDQS]] gives the details.

## Motivation

Many properties of a matrix depend only on its eigenvalues, so it helps to have one name for the whole set.
A matrix is [[invertible|0EB9N0S33C]] exactly when $0$ is not in its spectrum.
The powers $A^k$ tend to the zero matrix exactly when every complex eigenvalue has absolute value less than $1$, which matters for iterative methods and Markov chains.
The solutions of the differential equation $x' = Ax$ all tend to $0$ exactly when every eigenvalue has negative real part, which is the test for stability in engineering.

The name comes from operator theory, where the [[spectrum of an operator|XXXSST2DR5]] on an infinite-dimensional space can contain points that are not eigenvalues.
For matrices the two notions agree, and the sub-area on [[the spectral theorems|3YM9EK6VMB]] describes the spectra of symmetric and normal matrices.

## Notation

Books write $\sigma(A)$, $\operatorname{spec}(A)$ or $\Lambda(A)$.
Some authors mean by the spectrum the list of eigenvalues with their algebraic multiplicities, a multiset of size $n$ over $\mathbb{C}$.
For example, $I_2$ has the spectrum $\{1\}$ as a set and the list $1, 1$ as a multiset, so check which meaning a book uses.
In Mathlib the set is `spectrum F A`, defined for every element $A$ of an $F$-algebra.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{R}$.
The scalars $\lambda$ with $A - \lambda I$ singular are the roots of
$$\det(tI - A) = (t - 2)^2 - 1 = (t - 1)(t - 3),$$
so $\sigma(A) = \{1, 3\}$, as [[the symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]] shows in full.
For a triangular matrix the spectrum can be read off the diagonal.
For example, $\begin{pmatrix} 1 & 5 & 7 \\ 0 & 1 & 2 \\ 0 & 0 & 4 \end{pmatrix}$ has the spectrum $\{1, 4\}$ as a set, and $1, 1, 4$ as a list with multiplicities.

### The field matters

The spectrum consists of the roots of the [[characteristic polynomial|0VSSPAFM2C]] that lie in $F$.
The matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has the characteristic polynomial $t^2 + 1$.
Over $\mathbb{R}$ it has no root, so the spectrum is empty.
Over $\mathbb{C}$ the spectrum is $\{i, -i\}$, and over $\mathbb{F}_5$ it is $\{2, 3\}$, because $2^2 + 1$ and $3^2 + 1$ are multiples of $5$.
[[The spectrum depends on the field|B7C9Y27YA3]] checks each case with eigenvectors.

### More examples

A [[diagonal matrix|044JNC7ZAA]] or an [[upper triangular matrix|0N4XY7Z3NN]] has the set of its diagonal entries as its spectrum.
A [[nilpotent matrix|07BSPZPSMF]] of size $n \ge 1$ has the spectrum $\{0\}$, because $A^k = 0$ and $Av = \lambda v$ give $\lambda^k v = 0$, so $\lambda = 0$.
A projection, with $P^2 = P$, has its spectrum inside $\{0, 1\}$ for the same kind of reason.

### The rules you can use

The spectrum is the set of roots in $F$ of $\det(tI - A)$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
So $|\sigma(A)| \le n$, and similar matrices have the same spectrum.
Transposing does not change it, $\sigma(A^{\mathsf{T}}) = \sigma(A)$, because $\det(tI - A^{\mathsf{T}}) = \det\big((tI - A)^{\mathsf{T}}\big) = \det(tI - A)$.
When $A$ is invertible, $\sigma(A^{-1}) = \{ \lambda^{-1} : \lambda \in \sigma(A) \}$.
For a polynomial $p$, the inclusion $p(\sigma(A)) \subseteq \sigma(p(A))$ holds, with equality over an algebraically closed field, by the theorem on [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]].
For matrices $A$ of size $m \times n$ and $B$ of size $n \times m$, the products $AB$ and $BA$ have the same nonzero eigenvalues, by the theorem on the [[eigenvalues of AB and BA|MCXV71BY74]].

### What it is not

The spectrum is not the set of diagonal entries, unless the matrix is triangular.
The swap matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the diagonal entries $0, 0$ and the spectrum $\{1, -1\}$, as [[the diagonal entries of a non-triangular matrix|FT8XA974H9]] shows.
The spectrum is not the set of singular values either.
For $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, the matrix $N^{\mathsf{T}} N = \operatorname{diag}(0, 1)$ gives the singular values $0$ and $1$, while $\sigma(N) = \{0\}$.

### Watch out

The spectrum of a sum is not the sum of the spectra.
Take $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, so that $\sigma(A) = \sigma(B) = \{0\}$.
Their sum is the swap matrix, with $\sigma(A + B) = \{1, -1\}$, which is not $\{0 + 0\}$.
The same pair shows that products fail too: $AB = \operatorname{diag}(1, 0)$ has the spectrum $\{0, 1\}$.

### History

Hilbert introduced the name "spectral theory" in his early work on what are now called Hilbert spaces.
Later, quantum mechanics showed that the spectra of operators explain the lines of atomic spectra, so the name turned out to fit physics by luck.

### Try it

First, find the spectrum of $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$.
The matrix is triangular with diagonal $3, 3$, so the spectrum is $\{3\}$, and $3$ is a double root.

Second, find the real and the complex spectrum of $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.
The characteristic polynomial is $(t - 1)^2 + 1$, which is positive on $\mathbb{R}$, so the real spectrum is empty and the complex spectrum is $\{1 + i, 1 - i\}$.

## Explanations

### L1 human

A square matrix can have several special stretch factors, its eigenvalues.
The spectrum is the set of all of them, like a list of the notes a string can play.
A $2 \times 2$ matrix has at most two, and a $3 \times 3$ matrix at most three.
For the diagonal matrix with entries $5$ and $7$, the spectrum is $\{5, 7\}$.

### L2 human

Here is a typical use: does the iteration $x_{k+1} = A x_k$ with $A = \begin{pmatrix} 0.5 & 0.2 \\ 0.2 & 0.5 \end{pmatrix}$ tend to $0$ from every start?
The characteristic polynomial is
$$\det(tI - A) = (t - 0.5)^2 - 0.04 = (t - 0.3)(t - 0.7),$$
so $\sigma(A) = \{0.3, 0.7\}$.
Check: the trace is $1 = 0.3 + 0.7$ and the determinant is $0.25 - 0.04 = 0.21 = 0.3 \cdot 0.7$.
Both eigenvalues have absolute value less than $1$, so $A^k x_0 \to 0$ for every $x_0$.
This shows the typical use: one look at the spectrum decides invertibility, stability or convergence.
Watch out: the entries of $A$ alone do not decide this, since $\begin{pmatrix} 0.5 & 0.6 \\ 0.6 & 0.5 \end{pmatrix}$ has the eigenvalue $1.1$ and its powers grow.

### L3 human

For an element $a$ of a unital algebra over $F$, the spectrum is the set of $\lambda$ with $a - \lambda$ not a unit.
For matrices this is the set of eigenvalues, because a square matrix is a unit exactly when it is injective.
For bounded operators on Banach spaces the [[spectrum of an operator|XXXSST2DR5]] can contain points that are not eigenvalues, and it is a nonempty compact subset of $\mathbb{C}$.
The [[spectral radius|3PR407YKHN]] $\max \{ |\lambda| : \lambda \in \sigma(A) \}$ and the [[spectral mapping theorem|Q71WX8HFYT]] belong to that general theory.

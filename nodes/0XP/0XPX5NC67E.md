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

Let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] over a field $F$.
The spectrum of $A$ is the set $\sigma(A)$ of its [[eigenvalues|0BQAA2BK3Q]] in $F$.
Equivalently, it is the set of $\lambda \in F$ with $A - \lambda I_n$ not [[invertible|0EB9N0S33C]].
It has at most $n$ elements, and over an algebraically closed field it is nonempty when $n \ge 1$.

## Motivation

The eigenvalues of a matrix decide much of its behaviour.
The powers $A^k$ tend to zero when every eigenvalue in $\C$ has absolute value less than $1$.
The solutions of $x' = Ax$ are stable when every eigenvalue has negative real part.
So it is useful to have one name for the whole set of eigenvalues.

## Notation

The formal definition is the [[definition of the spectrum of a matrix|04EHB7YDQS]].
Common symbols are $\sigma(A)$, $\operatorname{spec}(A)$ and $\Lambda(A)$.
Some authors mean the list of eigenvalues with algebraic multiplicities, a multiset of size $n$ over $\C$.
Mathlib writes `spectrum F A`, for an element $A$ of an $F$-algebra.

## Remarks

### Examples

- [[The symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]] has spectrum $\{1, 3\}$.
- [[The spectrum depends on the field|B7C9Y27YA3]]: one integer matrix has empty spectrum over $\R$, spectrum $\{i, -i\}$ over $\C$, and spectrum $\{2, 3\}$ over $\mathbb{F}_5$.
- The spectrum of a [[diagonal matrix|044JNC7ZAA]] or of an [[upper triangular matrix|0N4XY7Z3NN]] is the set of its diagonal entries.
- A [[nilpotent matrix|07BSPZPSMF]] of size $n \ge 1$ has spectrum $\{0\}$.

### Non-examples

- [[The diagonal entries of a non-triangular matrix|FT8XA974H9]]: the matrix with rows $(0, 1)$ and $(1, 0)$ has diagonal entries $0, 0$ and spectrum $\{1, -1\}$.
- The set of singular values is in general not the spectrum. For the matrix with rows $(0, 1)$ and $(0, 0)$, the singular values are $1$ and $0$, and the spectrum is $\{0\}$.

### Basic properties

- $\sigma(A)$ is the set of roots in $F$ of the [[characteristic polynomial|0VSSPAFM2C]], by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
- So $|\sigma(A)| \le n$, and similar matrices have the same spectrum.
- $\sigma(A^{\mathsf{T}}) = \sigma(A)$, because $\det(tI - A^{\mathsf{T}}) = \det(tI - A)$.
- $A$ is invertible if and only if $0 \notin \sigma(A)$. Then $\sigma(A^{-1}) = \{\lambda^{-1} : \lambda \in \sigma(A)\}$.
- For a polynomial $p$, $p(\sigma(A)) \subseteq \sigma(p(A))$, with equality over an algebraically closed field, by the theorem on [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]].
- $\sigma(AB) \setminus \{0\} = \sigma(BA) \setminus \{0\}$, by the theorem on the [[eigenvalues of AB and BA|MCXV71BY74]].

### History

Hilbert introduced the name "spectral theory" in his first formulation of Hilbert space theory.
Later, quantum mechanics showed that spectral theory explains features of atomic spectra, and this match of names was a fortunate accident.

### Common errors

- Reading the spectrum off the diagonal of a matrix that is not triangular.
- Forgetting that the spectrum depends on the field. A real matrix can have an empty real spectrum.
- Mixing the set and the multiset. The matrix $I_2$ has spectrum $\{1\}$ as a set, and the list $1, 1$ with multiplicities.

## Explanations

### L1 human

A square matrix can have several special stretch factors, its eigenvalues.
The spectrum is the set of all of them.
For a $2 \times 2$ matrix, it has at most two numbers.
For the diagonal matrix with entries $5$ and $7$, the spectrum is $\{5, 7\}$.

### L2 human

We find the spectrum of $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ over $\R$.

1. $\det(tI - A) = (t - 1)^2 - 4 = t^2 - 2t - 3 = (t - 3)(t + 1)$.
2. So $\sigma(A) = \{3, -1\}$.
3. Check: $A (1, 1)^{\mathsf{T}} = (3, 3)^{\mathsf{T}}$ and $A (1, -1)^{\mathsf{T}} = (-1, 1)^{\mathsf{T}} = -1 \cdot (1, -1)^{\mathsf{T}}$.
4. Second check: the sum $3 + (-1) = 2$ is the trace, and the product $-3$ is $\det A = 1 - 4$.

The typical use is to test invertibility, stability or convergence from the set $\sigma(A)$.
A trap: the spectrum of $A + B$ is in general not $\sigma(A) + \sigma(B)$.

### L3 human

For an element $a$ of a unital algebra over $F$, the spectrum is the set of $\lambda$ with $a - \lambda$ not a unit.
For matrices, this is the set of eigenvalues, because a square matrix is a unit exactly when it is injective.
For bounded operators on Banach spaces, the [[spectrum of an operator|XXXSST2DR5]] can contain points that are not eigenvalues.
The [[spectral radius|3PR407YKHN]] and the [[spectral mapping theorem|Q71WX8HFYT]] belong to that general theory.

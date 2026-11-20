---
tag: 0VSSPAFM2C
kind: concept
name: Characteristic polynomial
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
uses: [00KDZRW4C0, 0JXZKX526R, 0Q9EZS90GY, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9780134860244
  - book: isbn:9780135367971
same_as:
  wikidata: Q849705
  wikipedia: Characteristic polynomial
---

## Summary

Let $A$ be an $n \times n$ matrix over a commutative ring $K$, with $n \ge 1$.
The characteristic polynomial of $A$ is $p_A(t) = \det(t I_n - A)$, a [[determinant|00KDZRW4C0]] of a matrix with entries in the [[polynomial ring|0Q9EZS90GY]] $K[t]$.
It is monic of degree $n$, and over a field its roots are the [[eigenvalues|0BQAA2BK3Q]] of $A$.
Its coefficients are, up to sign, the sums of the principal minors of $A$, from the trace to the determinant.

## Motivation

The scalar $\lambda$ is an eigenvalue of $A$ exactly when $\det(\lambda I - A) = 0$.
Replacing $\lambda$ by a variable $t$ turns this condition into one polynomial equation.
So the search for eigenvalues becomes the search for roots of one polynomial of degree $n$.
The polynomial also carries more information: the multiplicities of its roots, the trace, the determinant, and by the [[Cayley-Hamilton theorem|0F765KFC2J]] a polynomial relation among the powers of $A$.

## Notation

The formal definition is the [[definition of the characteristic polynomial|039HF58KQ5]].
Common symbols are $p_A$, $\chi_A$, $c_A$ and $P_A$.
This encyclopedia and Mathlib use $\det(t I - A)$, which is monic.
Many textbooks, for example Lay and Strang, use $\det(A - t I) = (-1)^n \det(t I - A)$.
The two conventions agree for even $n$ and differ by the sign for odd $n$; see the [[non-example on this sign|~f7f14dfc]].
Mathlib writes `Matrix.charpoly A`, and `LinearMap.charpoly f` for an endomorphism.
For an endomorphism of a finite-dimensional space, the [[characteristic polynomial of an endomorphism|0J5EMJRRFM]] is $p_A$ for any matrix $A$ of the map.

## Remarks

### Examples

- [[The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere|~29b91e21]] has $p_A(t) = t^3 - 12t^2 + 45t - 54 = (t - 3)^2 (t - 6)$.
- [[A real matrix with complex eigenvalues|~8162274d]] has $p_A(t) = t^2 - 2t + 5$, with the roots $1 \pm 2i$.
- [[A rotation of the plane|~805e3c17]] by the angle $\theta$ has $p(t) = t^2 - 2\cos\theta \, t + 1$.
- For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $p_A(t) = t^2 - (a + d) t + (ad - bc)$.
- The [[companion matrix|0ZCWPNZTQ3]] of a monic polynomial $f$ has characteristic polynomial $f$. So every monic polynomial of degree $n \ge 1$ is a characteristic polynomial.

### Non-examples

- [[The polynomial det(A - tI) for a 3 by 3 matrix|~f7f14dfc]] has leading coefficient $-1$, so it is not $p_A$.
- The polynomial $\prod_i (t - a_{ii})$ of the diagonal entries is $p_A$ only for triangular matrices.

### Basic properties

- $p_A$ is monic of degree $n$. The coefficient of $t^{n-1}$ is $-\operatorname{tr} A$, and the constant term is $(-1)^n \det A$, by the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
- Similar matrices have the same characteristic polynomial, by the theorem that the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
- $p_{A^{\mathsf{T}}} = p_A$, because a matrix and its transpose have the same determinant.
- Over a field, the roots of $p_A$ are the eigenvalues of $A$, by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
- $p_{AB} = p_{BA}$ for square $A$ and $B$, by the theorem on the [[eigenvalues of AB and BA|~4971526f]].
- For a block upper triangular matrix, $p_A$ is the product of the characteristic polynomials of the diagonal blocks, by the theorem on the [[characteristic polynomial of an endomorphism|~756cfc1f]].
- $p_A(A) = 0$, by the [[Cayley-Hamilton theorem|0F765KFC2J]].

### History

Cauchy introduced the term "racine caractéristique", characteristic root, for what is now called an eigenvalue.
The name "characteristic equation" keeps his term.
Cayley stated in 1858 that a matrix satisfies its own characteristic equation.

### Common errors

- Mixing the two sign conventions. For odd $n$, $\det(A - tI) = -p_A(t)$.
- Computing $\det(A) - t$ or $\det(A - t)$ with $t$ subtracted from every entry.
- Substituting $t = A$ into $\det(tI - A)$ to "prove" Cayley-Hamilton. This gives a scalar $\det(0) = 0$, not the matrix $p_A(A)$; see the remarks on the [[Cayley-Hamilton theorem|0F765KFC2J]].
- Thinking that $p_A$ determines $A$ up to similarity. The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ have the same $p_A = (t - 1)^2$ and are not similar.

## Explanations

### L1 human

To find the eigenvalues of a square matrix, we look for numbers $\lambda$ that make $\lambda I - A$ singular.
The determinant tests singularity.
If we write a letter $t$ in place of $\lambda$, then $\det(tI - A)$ is a polynomial in $t$.
This polynomial is the characteristic polynomial.
Its roots are the eigenvalues.

### L2 human

We compute $p_A$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ in two ways.

1. Directly: $\det \begin{pmatrix} t - 1 & -2 \\ -3 & t - 4 \end{pmatrix} = (t - 1)(t - 4) - 6 = t^2 - 5t - 2$.
2. By the formula $t^2 - (\operatorname{tr} A) t + \det A$: $\operatorname{tr} A = 5$ and $\det A = 4 - 6 = -2$, so $p_A(t) = t^2 - 5t - 2$.
3. The roots are $\frac{5 \pm \sqrt{33}}{2}$, so $A$ has two real eigenvalues.

The typical use is to find eigenvalues, their algebraic multiplicities, and the trace and determinant at once.
A trap: for $n \ge 5$ the roots of $p_A$ have in general no formula in radicals, so eigenvalues are computed numerically, not from $p_A$.

### L3 human

For an endomorphism $T$ of a free module of rank $n$ over a commutative ring, the characteristic polynomial is $\det(t - T)$ on $K[t] \otimes_K V$.
It is the product of the invariant factors of the $K[t]$-module $V$, when $K$ is a field; see [[modules over a principal ideal domain|WKJXXX0DYG]].
When $p_A$ splits, its coefficients are, up to sign, the [[elementary symmetric polynomials|0X5QVCF06N]] of the eigenvalues.
The [[minimal polynomial in field theory|0VX9EP2GS8]] of an algebraic element $\alpha$ divides the characteristic polynomial of multiplication by $\alpha$.

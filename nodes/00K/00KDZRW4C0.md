---
tag: 00KDZRW4C0
kind: concept
name: Determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0K6CH0MT0F, 0CP7YY6NAG, 06DW9BAWB1, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Definitions
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Four, Determinants
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
same_as:
  wikidata: Q178546
  wikipedia: Determinant
---

## Summary

Let $K$ be a [[commutative ring|0310REJJY8]] and let $n \ge 1$.
The *determinant* is the unique function $\det \colon M_n(K) \to K$ on [[square matrices|0CP7YY6NAG]] that is multilinear in the columns, is zero when two columns are equal, and has value $1$ on the [[identity matrix|06DW9BAWB1]] $I_n$.
In other words, it is the unique [[alternating multilinear map|0K6CH0MT0F]] of the columns with $\det I_n = 1$; the same function is the unique such map of the rows.
It is given by the [[Leibniz formula|016PE4VZ8Q]] $\det A = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$.
The determinant matters because it tests invertibility, measures the change of volume under a linear map, and gives the characteristic polynomial.

## Motivation

A system of $n$ linear equations in $n$ unknowns has exactly one solution for each right side if and only if one number built from the coefficients is not zero.
For $n = 2$ this number is $ad - bc$.
The search for this number for all $n$ led to the determinant.
A second motivation is geometric: the signed volume of the parallelotope spanned by $n$ vectors of $\mathbb{R}^n$ is linear in each vector, zero for two equal vectors, and $1$ for the unit cube.
These are exactly the defining properties.

## Notation

The determinant of $A = (a_{ij})$ is written $\det A$, $\det(A)$ or $\abs{A}$, and the matrix is often written with vertical bars:
$$\det A = \begin{vmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{vmatrix}.$$
The bars $\abs{A}$ must not be read as an absolute value; a determinant can be negative.
In Lean's Mathlib the function is `Matrix.det`, defined by the Leibniz sum.

## Remarks

### Examples

- For $n = 1$, $\det(a) = a$. For $n = 2$, $\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$, by the [[2 × 2 formula|0ZN2J42SK7]].
- A $3 \times 3$ determinant, computed by the Leibniz formula, by a Laplace expansion and by row reduction, with the same value $6$; see the [[worked example|7YSM0NJQX1]].
- A rotation of the plane has determinant $1$, and a reflection has determinant $-1$; see the [[example on rotations and reflections|D3F3XAZA0M]].
- A diagonal matrix has determinant equal to the product of its diagonal entries, by the [[triangular rule|0K1KKMFHYH]].
- The [[permutation matrix|08SP3DF8NB]] of $\sigma$ has determinant $\sgn(\sigma)$, by the [[effect of row operations|09YB3WQG38]].

### Non-examples

- The [[permanent|X9B1XETBPF]] $\sum_\sigma a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ is multilinear with value $1$ on $I_n$, but it is not alternating; see the [[non-example|K9T8BNTZ2G]].
- The [[trace|0XC1RDBY7A]] is linear in the matrix and has $\operatorname{tr} I_n = n$, so for $n \ge 2$ it is neither multilinear in the columns nor normalized.
- A non-square matrix has no determinant.
- The function $A \mapsto \det A + \det B_0$ for a fixed nonzero $B_0$ is not the determinant, because the determinant is not additive; see the [[counterexample on sums|D5VBC7621G]].

### Basic properties

- Three definitions agree: the axiomatic one, the [[Leibniz formula|016PE4VZ8Q]] and the recursive [[Laplace expansion|0C08BQ3M05]]; see the [[equivalence theorem|W3JN0WPZ10]].
- It is [[multilinear in the rows|0PPG793642]], and it is zero for [[equal rows, a zero row or dependent rows|0K4VQB7HWR]].
- [[Row operations|09YB3WQG38]] change it in a known way, and the [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of the diagonal.
- $\det A^{\mathsf{T}} = \det A$, by the [[transpose rule|0ZZQ2E1MTE]], and $\det(AB) = \det A \det B$, by [[multiplicativity|04CPJ6AF00]].
- Over a field, $A$ is invertible if and only if $\det A \neq 0$, by the [[invertibility criterion|FBSAPTP1PR]]. Over a commutative ring, the condition is that $\det A$ is a unit, by the [[ring version|03Q7RE2HXR]].

### History

Determinants originated in the work of Seki in Japan in 1683 and of Leibniz in 1693.
Cramer stated his rule, without proof, in 1750.
Vandermonde first recognized determinants as independent functions in 1771.
Cauchy used the word "determinant" in its present sense in his paper of 30 November 1812, and he proved the multiplication theorem there.

### Common errors

- Assuming $\det(A + B) = \det A + \det B$; this is false in general.
- Writing $\det(cA) = c \det A$; the correct rule is $\det(cA) = c^n \det A$ for $n \times n$ matrices.
- Using the rule of Sarrus for $4 \times 4$ matrices; it gives wrong values.

## Explanations

### L1 human

The determinant turns a square table of numbers into one number.
For a $2 \times 2$ table with rows $a, b$ and $c, d$, the number is $ad - bc$.
The table describes a way to stretch the plane, and the determinant says how much areas grow.
A determinant of $3$ means that areas triple, and a negative determinant means that the picture is also flipped.
A determinant of $0$ means that the plane is squashed onto a line, and then the stretching cannot be undone.

### L2 human

We compute $\det A$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ in two ways.

1. By the $2 \times 2$ formula, $\det A = 1 \cdot 4 - 2 \cdot 3 = -2$.
2. By row reduction: subtract $3$ times row $1$ from row $2$. This gives $\begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}$ and does not change the determinant.
3. The new matrix is triangular, so its determinant is $1 \cdot (-2) = -2$.
4. Since $-2 \neq 0$, the matrix is invertible.

The typical use is the test of invertibility, and the computation of eigenvalues as roots of $\det(A - \lambda I)$.
A trap: the determinant is not linear in the matrix, so $\det(2A) = 4 \det A = -8$ here, not $-4$.

### L3 human

For a free module $V$ of rank $n$, the top exterior power $\Lambda^n V$ is free of rank $1$, and an endomorphism $T$ acts on it by multiplication with a scalar; this scalar is the [[determinant of the endomorphism|0X0HQYSZ0K]].
So $\det$ is a natural group homomorphism $\mathrm{GL}_n(K) \to K^\times$, its kernel is $\mathrm{SL}_n(K)$, and it commutes with ring homomorphisms $K \to K'$.
The same object appears as the Jacobian determinant in the change of variables formula, as the Wronskian in differential equations, and as the norm in field extensions.

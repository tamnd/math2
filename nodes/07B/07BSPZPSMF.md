---
tag: 07BSPZPSMF
kind: concept
name: Nilpotent matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Characterization
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
same_as:
  wikidata: Q650670
  wikipedia: Nilpotent matrix
inventory: [HSZH6NG7SR]
---

## Summary

A nilpotent matrix is a [[square matrix|0JXZKX526R]] $N$ with $N^k = 0$ for some integer $k \ge 1$.
The least such $k$ is the *index* of $N$; the [[formal definition|0419GJC84P]] states both.
[[Strictly upper triangular matrices|~0f948644]] are nilpotent, and over a field every nilpotent matrix is similar to one of them.
If $N$ is nilpotent, then $I - N$ is invertible with inverse $I + N + \cdots + N^{k-1}$, by the [[geometric series for nilpotent matrices|~9c73b141]].

## Motivation

Nilpotent matrices show that the matrix ring has zero divisors of a strong kind: $N \neq 0$ but $N^k = 0$.
They are the "infinitely small" part of a matrix.
Over $\mathbb{C}$, every matrix is $D + N$ with $D$ diagonalizable, $N$ nilpotent and $DN = ND$, by the [[Jordan–Chevalley decomposition|011K11VPJN]].
For nilpotent $N$, the exponential $e^{N} = I + N + \cdots + N^{k-1}/(k-1)!$ is a finite sum, which makes linear systems of differential equations solvable by hand.

## Notation

- In Mathlib, the predicate is `IsNilpotent N`, defined for elements of any monoid with zero.
- The index is also called the *degree* or the *order of nilpotency*.

## Remarks

### Examples

- [[A nilpotent 2 × 2 matrix with no zero entries|~1cfd4aa0]].
- [[A strictly upper triangular 3 × 3 matrix and its powers|~9021d76b]].
- [[The matrix E₁₂, a nonzero matrix with zero square|~47ca595b]].
- The zero matrix is nilpotent of index $1$.

### Non-examples

- [[Two matrices that look nilpotent but are not|~fe703052]]: an upper triangular matrix with $1$ on the diagonal, and a matrix with zero diagonal and nonzero square.
- An [[invertible matrix|0EB9N0S33C]] is never nilpotent, because $N^k = 0$ would give $I = (N^{-1})^k N^k = 0$.

### Basic properties

Let $N$ be a nilpotent $n \times n$ matrix with $N^k = 0$.

- $I - N$ and $I + N$ are invertible, with $(I - N)^{-1} = I + N + \cdots + N^{k-1}$, by [[this theorem|~9c73b141]].
- $cN$ is nilpotent for each scalar $c$, and $P^{-1} N P$ is nilpotent for each invertible $P$.
- If $M$ is nilpotent and $MN = NM$, then $M + N$ and $MN$ are nilpotent, by the [[binomial theorem for commuting matrices|~af4d44e0]].
- Over a field, the index of $N$ is at most $n$, so $N^n = 0$. The proof uses the kernels $\ker N \subsetneq \ker N^2 \subsetneq \cdots$ or the [[characteristic polynomial|0VSSPAFM2C]], which belong to later topics.
- Over a field, the only eigenvalue of $N$ is $0$. So the [[trace|0XC1RDBY7A]] of $N$ is $0$, by the theorem that the [[trace is the sum of the eigenvalues|0NMXDCNNKR]].
- The sum of two nilpotent matrices that do not commute need not be nilpotent: $E_{12} + E_{21}$ has square $I$.

### Common errors

- Taking a zero diagonal as enough for nilpotency.
- Taking "no nonzero real eigenvalue" as enough. The rotation by a quarter turn has no real eigenvalue, and it is not nilpotent. The right test is that the characteristic polynomial is $x^n$.

## Explanations

### L1 human

A nilpotent matrix becomes the zero matrix after we multiply it by itself enough times.
A shift that moves each coordinate one step down, and drops the last one, is an example.
After $n$ shifts nothing is left.

### L2 human

As a map, a nilpotent $N$ pushes every vector towards $0$ in finitely many steps.
The chain $V \supseteq N V \supseteq N^2 V \supseteq \cdots$ must reach $0$.
In a suitable basis, this makes $N$ strictly upper triangular.

### L3 human

The nilpotent elements of a commutative ring form an ideal, the nilradical; in $M_n(F)$ they do not, because $E_{12} + E_{21}$ is not nilpotent.
Over a field, the nilpotent $n \times n$ matrices form a closed algebraic set, the nilpotent cone, defined by the vanishing of the coefficients of the characteristic polynomial.

---
tag: FBSAPTP1PR
kind: statement
role: theorem
name: Invertible iff the determinant is nonzero
aliases: [a-square-matrix-is-invertible-iff-its-determinant-is-nonzero]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0EB9N0S33C, 0C3CFHDN6R, 0QA8CHH8MG, 0CRMGPAH83]
sources:
  - locator: ap-linear-algebra.tex:6604
    url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L6604
  - locator: ch-systems.tex:1083
    url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L1083
  - locator: src/section3-4.xml:766
    url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-4.xml#L766
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Invertibility
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Statement

Let $F$ be a [[field|0QA8CHH8MG]] and let $A$ be an $n \times n$ matrix over $F$.
The following conditions are equivalent.

1. $A$ is [[invertible|0EB9N0S33C]].
2. $\det A \neq 0$, where $\det$ is the [[determinant|0C3CFHDN6R]].
3. The columns of $A$ are [[linearly independent|0CRMGPAH83]].
4. The rows of $A$ are linearly independent.

In particular, the system $Ax = 0$ has a nonzero solution if and only if $\det A = 0$.

## Remarks

### Why each hypothesis is needed

$F$ must be a field.
Over $\mathbb{Z}$, the $1 \times 1$ matrix $(2)$ has $\det = 2 \neq 0$ and independent columns, but it has no inverse over $\mathbb{Z}$.
Over a commutative ring the correct condition is that $\det A$ is a unit; see the [[criterion over commutative rings|03Q7RE2HXR]].
$A$ must be square, since $\det$ is defined only for square matrices.

### Consequences

- A homogeneous system of $n$ equations in $n$ unknowns has a nonzero solution exactly when its determinant is $0$.
- $\lambda$ is an eigenvalue of $A$ if and only if $\det(A - \lambda I) = 0$; this is the starting point of the [[characteristic polynomial|0VSSPAFM2C]].
- $n$ vectors in $F^n$ form a basis if and only if the matrix with these columns has nonzero determinant.
- The set of singular real $n \times n$ matrices is the zero set of a polynomial, so it is closed and has measure zero.

### Converse

The statement is already an equivalence.
A one-sided version also holds: if $AB = I_n$ for square $A$ and $B$ over $F$, then $\det A \neq 0$, so $A$ is invertible and $B = A^{-1}$.

### Generalizations

The [[rank by minors|HVHQ50TJB1]] refines condition 2: the rank of any matrix is the largest size of a nonzero minor.
Over a commutative ring, $A$ is invertible if and only if $\det A$ is a unit, by the [[adjugate|0ENVM493VK]].

## History

A determinant was first a property of a system of linear equations.
It determines whether the system has a unique solution, which happens exactly when the determinant is nonzero.

## Explanations

### L1 human

A square table of numbers can be undone exactly when its determinant is not $0$.
A determinant $0$ means that the columns lie in a smaller space, so some information is lost.
For example, $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has determinant $0$, and its second column is twice the first.

### L2 human

For which $t$ is $A = \begin{pmatrix} 1 & t \\ t & 4 \end{pmatrix}$ invertible over $\mathbb{R}$?

1. $\det A = 4 - t^2$.
2. So $\det A = 0$ exactly for $t = 2$ and $t = -2$.
3. For $t = 2$, the columns $(1, 2)$ and $(2, 4)$ are dependent, which confirms the test.
4. For every other real $t$, $A$ is invertible.

The typical use is to decide invertibility without computing an inverse.
A trap: over $\mathbb{Z}$ or another ring, a nonzero determinant is not enough.

### L3 human

Condition 2 says that $\mathrm{GL}_n$ is the open subscheme of $M_n$ where $\det$ does not vanish, that is, $\mathrm{GL}_n = \operatorname{Spec} \mathbb{Z}[x_{ij}, 1/\det]$.
Over $\mathbb{R}$ or $\mathbb{C}$ this shows that $\mathrm{GL}_n$ is open and dense in $M_n$, which supports many density arguments.

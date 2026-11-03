---
tag: JT0KWAC6P0
kind: statement
role: theorem
name: Ackermann's formula
msc: [93B55, 93C05]
uses: [SCY6X79XVP, AWDQ3ES2S3, 9NSCZ2KBEB, 0VSSPAFM2C, 0F765KFC2J, 0EB9N0S33C]
about: [AWDQ3ES2S3]
sources:
  - url: https://en.wikipedia.org/wiki/Ackermann%27s_formula
same_as:
  wikidata: Q42417197
  wikipedia: Ackermann's formula
---

## Statement

Let $A \in \R^{n \times n}$ and $b \in \R^{n}$, and assume that the controllability matrix $\mathcal{C} = (b, Ab, \ldots, A^{n-1} b)$ is [[invertible|0EB9N0S33C]].
Let $p(s) = s^n + a_{n-1} s^{n-1} + \cdots + a_1 s + a_0$ be a monic polynomial with real coefficients, and let $e_n^T = (0, \ldots, 0, 1) \in \R^{1 \times n}$.
Then the row vector
$$k = e_n^T\, \mathcal{C}^{-1}\, p(A)$$
is the unique $k \in \R^{1 \times n}$ such that the [[characteristic polynomial|0VSSPAFM2C]] of $A - bk$ is $p$.

## Remarks

Existence and uniqueness of $k$ come from the [[pole placement theorem|SCY6X79XVP]] for a single input.
For the formula, put $A_c = A - bk$; by the [[Cayley–Hamilton theorem|0F765KFC2J]], $p(A_c) = 0$.
Expanding the powers $A_c^j = (A - bk)^j$ and collecting terms gives $p(A) = \mathcal{C} M$ for a matrix $M$ whose last row is $k$.
Multiplying on the left by $e_n^T \mathcal{C}^{-1}$ gives the formula.

Example: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $b = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ and $p(s) = (s + 1)^2 = s^2 + 2s + 1$, one has $\mathcal{C} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \mathcal{C}^{-1}$ and $p(A) = A^2 + 2A + I = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
So $e_2^T \mathcal{C}^{-1} = (1, 0)$ and $k = (1, 2)$.
Indeed $A - bk = \begin{pmatrix} 0 & 1 \\ -1 & -2 \end{pmatrix}$ has characteristic polynomial $s^2 + 2s + 1$.

Without invertibility of $\mathcal{C}$ the formula has no meaning, and some polynomials $p$ cannot be reached at all.

## Explanations

### L1 human

The pole placement theorem says that a single-input controllable system can be given any closed-loop characteristic polynomial by state feedback.
Ackermann's formula computes the feedback gain directly: evaluate the desired polynomial at the matrix $A$, and take the last row of the inverse of the controllability matrix times it.
No change of coordinates is needed.

### L2 human

The formula is convenient for hand computation and for symbolic work with small systems.
It is the single-input case of [[full state feedback|AWDQ3ES2S3]] design; for several inputs the gain is not unique and other methods are used.
Numerically it is not recommended for large $n$, because the controllability matrix is often badly conditioned.
By duality, the same formula applied to $(A^T, C^T)$ gives the gain of a Luenberger observer for a single output.

---
tag: MDZDEFE53C
kind: statement
role: theorem
name: Sherman-Morrison-Woodbury formula
msc: ["15A09", "65F05"]
topics: [P8J6QR66TJ]
audience: ug2
about: [0EB9N0S33C]
uses: [0EB9N0S33C, 0TWTS88TWN, 076JGP6R3T, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Woodbury_matrix_identity
  - url: https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
---

## Statement

When an invertible matrix is changed by a matrix of low rank, the new inverse is the old inverse minus a correction that needs only one small inversion.
Let $F$ be a [[field|0QA8CHH8MG]], and let $A$ be an [[invertible|0EB9N0S33C]] $n \times n$ matrix over $F$.
Let $U$ be $n \times k$, let $C$ be an invertible $k \times k$ matrix and let $V$ be $k \times n$.
Put $K = C^{-1} + V A^{-1} U$, a $k \times k$ matrix.

1. (Woodbury.) $A + UCV$ is invertible if and only if $K$ is invertible. In that case
$$(A + UCV)^{-1} = A^{-1} - A^{-1} U K^{-1} V A^{-1}.$$
2. (Sherman-Morrison, the case $k = 1$ and $C = (1)$.) For column vectors $u, v \in F^n$, the matrix $A + uv^{\mathsf{T}}$ is invertible if and only if $1 + v^{\mathsf{T}} A^{-1} u \ne 0$. In that case
$$(A + uv^{\mathsf{T}})^{-1} = A^{-1} - \frac{A^{-1} u v^{\mathsf{T}} A^{-1}}{1 + v^{\mathsf{T}} A^{-1} u}.$$

## Remarks

### The theorem at work

Take $A = I_2$, $u = (1, 0)^{\mathsf{T}}$ and $v = (0, 1)^{\mathsf{T}}$, so that $A + uv^{\mathsf{T}} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
The denominator is $1 + v^{\mathsf{T}} u = 1 + 0 = 1$, and part 2 gives
$$(I_2 + uv^{\mathsf{T}})^{-1} = I_2 - uv^{\mathsf{T}} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}.$$
Check: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 + 1 \\ 0 & 1 \end{pmatrix} = I_2$.
The [[worked $3 \times 3$ example|RNZ6YSRZWP]] has the denominator $3/2$.

### Why the hypotheses are needed

$A$ must be invertible, because the formula uses $A^{-1}$, although a rank one update of a singular matrix can be invertible: $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + e_2 e_2^{\mathsf{T}} = I_2$.
The condition on $K$ cannot be dropped.
For $A = I_2$, $u = e_1$ and $v = -e_1$, we get $1 + v^{\mathsf{T}} u = 0$, and $A + uv^{\mathsf{T}} = \operatorname{diag}(0, 1)$ is singular.
$C$ must be invertible for $K$ to be defined; without this, one can use the form $(A + UCV)^{-1} = A^{-1} - A^{-1} U (I_k + C V A^{-1} U)^{-1} C V A^{-1}$.

### What it gives you

If $A^{-1}$ is known, the inverse after a change of rank $k$ costs one $k \times k$ inversion and $O(n^2 k)$ further operations, with no new $n \times n$ inversion.
Solutions can be updated in the same way: if $Ay = b$ and $Az = u$ are solved, then the solution of $(A + uv^{\mathsf{T}}) x = b$ is
$$x = y - \frac{v^{\mathsf{T}} y}{1 + v^{\mathsf{T}} z}\, z.$$
The formula is used in the [[recursive least squares filter|HX0EMWJBNJ]] and in [[Broyden's method|GYNYT7KTC3]], where a rank one update is made at each step.
The [[matrix determinant lemma|0BC3Q6K92H]] is the companion result, $\det(A + uv^{\mathsf{T}}) = (1 + v^{\mathsf{T}} A^{-1} u) \det A$.

### Converse and generalizations

The formula is symmetric: if $W = (A + UCV)^{-1}$ exists, then $K^{-1} = C - CVWUC$, and this gives the "only if" direction of part 1.
The identity holds in any ring for units $A$, $C$ and $K$, with the same proof by multiplication.
It is the upper left block of the [[block inverse formula|5QTK7JWXF3]] for $\begin{pmatrix} A & U \\ V & -C^{-1} \end{pmatrix}$, computed in two ways.

## History

Sherman and Morrison published the rank one formula in 1949 and 1950.
Woodbury gave the rank $k$ form in a report of 1950.

## Explanations

### L1 human

If you already know the inverse of $A$ and you change $A$ a little, you do not need to invert again from scratch.
The formula corrects the old inverse with a small term.
For a change of rank one, the correction needs only one division by a number.

### L2 human

Compute $z = A^{-1}u$ and $w^{\mathsf{T}} = v^{\mathsf{T}}A^{-1}$ first, then the number $1 + v^{\mathsf{T}} z$.
If that number is $0$, stop: the new matrix is singular.
Otherwise subtract the outer product $z w^{\mathsf{T}}$, divided by that number, from $A^{-1}$.
A trap: the correction is $A^{-1} u v^{\mathsf{T}} A^{-1}$, not $u v^{\mathsf{T}}$; the factors $A^{-1}$ on both sides are easy to forget when $A \ne I_n$.

### L3 human

The proof by multiplication is purely algebraic, so the formula is an identity in any ring.
It is the matrix form of the ring identity $(1 + ab)^{-1} = 1 - a(1 + ba)^{-1} b$.
In statistics and Kalman filtering it gives the update of a covariance matrix after new data.

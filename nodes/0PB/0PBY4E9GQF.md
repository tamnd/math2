---
tag: 0PBY4E9GQF
kind: concept
name: Skew-symmetric matrix
aliases: [antisymmetric-matrix]
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0JXZKX526R]
uses: [0JXZKX526R, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Properties
same_as:
  wikidata: Q526790
  wikipedia: Skew-symmetric matrix
inventory: [2FP1241FAJ]
---

## Summary

A skew-symmetric matrix is a square matrix that changes sign when you flip it across its main diagonal.
Skew-symmetric matrices describe the cross product with a fixed vector, small rotations, and the part of a matrix that a quadratic form cannot see.
Exactly, a [[square matrix|0JXZKX526R]] $A$ is skew-symmetric when its [[transpose|09DXWYRD43]] is its negative,
$$A^{\mathsf{T}} = -A, \qquad \text{that is,} \qquad a_{ji} = -a_{ij} \text{ for all } i, j.$$
The [[formal definition|03RNVFDEAN]] states this rule.
Outside characteristic $2$ the diagonal of a skew-symmetric matrix is $0$, and every square matrix is the sum of a [[symmetric|0VR671PHE5]] and a skew-symmetric matrix in exactly one way.

## Motivation

For a fixed vector $v \in \mathbb{R}^3$, the map $w \mapsto v \times w$ is linear, and its matrix is skew-symmetric, as in [[the cross product example|92G2HF4JT8]].
The vector $v \times w$ is always perpendicular to $w$, and skew-symmetry is the matrix form of this fact: $w \cdot (Aw) = 0$ for every real skew-symmetric $A$.

The same fact makes skew-symmetric matrices the infinitesimal rotations.
If $x(t)$ moves by $x' = Ax$ with $A$ real and skew-symmetric, then $\frac{d}{dt} (x \cdot x) = 2\, x \cdot (Ax) = 0$, so the length of $x$ stays constant.
Equivalently, $e^{tA}$ is orthogonal for every $t$, since $(e^{tA})^{\mathsf{T}} = e^{tA^{\mathsf{T}}} = e^{-tA}$ is its inverse.

## Notation

The condition is written $A^{\mathsf{T}} = -A$, or with other notations for the transpose $A^t = -A$, ${}^t\!A = -A$ or $A' = -A$.
Other names are *antisymmetric* and *skew*.
Some books write $\operatorname{Skew}_n(F)$ for the skew-symmetric $n \times n$ matrices over $F$, and $\mathfrak{so}_n(F)$ or $\mathfrak{so}(n)$ when they are viewed as a Lie algebra.
In Mathlib the condition is written `Aᵀ = -A`, for a matrix whose rows and columns are indexed by the same finite type, not necessarily $\{1, \dots, n\}$.

## Remarks

### Three skew-symmetric matrices

The matrix $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric, and so is the zero matrix.
For $v = (1, 2, 3)$, the cross product matrix
$$[v]_\times = \begin{pmatrix} 0 & -3 & 2 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{pmatrix}$$
is skew-symmetric, since each entry is the negative of its mirror entry.
For any square $A$, the matrix $A - A^{\mathsf{T}}$ is skew-symmetric, since its transpose is $A^{\mathsf{T}} - A$; for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ it is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

### What is not skew-symmetric

The real matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has zero diagonal but is not skew-symmetric, since its mirror entries are equal rather than opposite; see [[this example|8YRP1P4XRX]].
The real matrix $\begin{pmatrix} 1 & 1 \\ -1 & 0 \end{pmatrix}$ is not skew-symmetric either, because $a_{11} = 1$ but $-a_{11} = -1$.
A matrix that is not square is never skew-symmetric, since $A^{\mathsf{T}}$ and $-A$ have different sizes.

### Properties

Let $A$ and $B$ be skew-symmetric $n \times n$ matrices over a commutative ring $R$.
Then $A + B$ and $cA$ for $c \in R$ are skew-symmetric, and so is the commutator $AB - BA$, since its transpose is $B^{\mathsf{T}} A^{\mathsf{T}} - A^{\mathsf{T}} B^{\mathsf{T}} = BA - AB$ by the [[transpose of a product|09GK5PS824]].
The square $A^2$ is symmetric, since $(A^2)^{\mathsf{T}} = (-A)^2 = A^2$.

Each diagonal entry satisfies $a_{ii} = -a_{ii}$, that is, $2 a_{ii} = 0$.
So the diagonal is $0$ whenever $2$ is not a zero divisor in $R$, for example over $\mathbb{R}$, $\mathbb{Z}$ or any field of characteristic not $2$.
Over such a field the skew-symmetric matrices form a subspace of dimension $n(n-1)/2$, since the entries above the diagonal are free and fix all others.

When $n$ is odd and $\operatorname{char} F \neq 2$, the [[determinant|00KDZRW4C0]] is $0$: by the [[determinant of the transpose|0ZZQ2E1MTE]], $\det A = \det A^{\mathsf{T}} = \det(-A) = (-1)^n \det A = -\det A$.
For instance, $\det [v]_\times = 0$, which matches $[v]_\times v = v \times v = 0$.

### Splitting a matrix

When $2$ is invertible, every square matrix is $A = S + K$ with $S = \frac12 (A + A^{\mathsf{T}})$ symmetric and $K = \frac12 (A - A^{\mathsf{T}})$ skew-symmetric, and this pair is unique, by [[this theorem|K284W6D15Z]].
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, [[the 2 × 2 example|T4EGXYA8H3]] gives $S = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}$ and $K = \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}$.

### Watch out

The zero diagonal is not automatic in characteristic $2$.
There $-1 = 1$, so skew-symmetric means the same as symmetric, and the identity matrix over $\mathbb{F}_2$ is skew-symmetric with diagonal $(1, \dots, 1)$.

A zero diagonal is also not enough: the entries off the diagonal must be negatives of each other, and $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ fails this over $\mathbb{R}$.

### History

The name Pfaffian, for the polynomial in the entries whose square is the determinant of a skew-symmetric matrix of even order, was introduced by Cayley in 1852 after Johann Friedrich Pfaff.
For $n = 2$, $\det \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a^2$, and the Pfaffian is $a$.

### Try it

First, find all real skew-symmetric $2 \times 2$ matrices.
The diagonal must be $0$ and $a_{21} = -a_{12}$, so they are the matrices $\begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}$ with $a \in \mathbb{R}$, a space of dimension $1 = 2 \cdot 1/2$.

Second, check that $x \cdot (Ax) = 0$ for $A = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ and $x = (3, 5)$.
$Ax = (10, -6)$, so $x \cdot (Ax) = 30 - 30 = 0$.

## Explanations

### L1 human

In a skew-symmetric matrix, the number in row $i$, column $j$ is the negative of the number in row $j$, column $i$.
Over the real numbers this forces zeros on the diagonal, because the only number equal to its own negative is $0$.
So $\begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix}$ is skew-symmetric, and $\begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}$ is not.

### L2 human

Here is a typical use: for a real skew-symmetric $A$, the vector $Ax$ is always perpendicular to $x$.
Move $A$ across the dot product: $x \cdot (Ax) = (A^{\mathsf{T}} x) \cdot x = -(Ax) \cdot x$, so this number equals its own negative and is $0$.
For the cross product matrix $[v]_\times$ with $v = (1, 2, 3)$ and $x = (0, 1, 1)$, we get $[v]_\times x = (-1, -1, 1)$ and $x \cdot (-1, -1, 1) = 0$.
This is why the motion $x' = Ax$ keeps lengths fixed and describes a rotation.

### L3 human

The skew-symmetric matrices form the Lie algebra $\mathfrak{so}_n$ of the orthogonal group $O_n$, with the commutator as bracket: the tangent condition at $I$ to $Q^{\mathsf{T}} Q = I$ is $A^{\mathsf{T}} + A = 0$.
A bilinear form is alternating, meaning $\beta(x, x) = 0$ for all $x$, exactly when its matrix satisfies $A^{\mathsf{T}} = -A$ and has zero diagonal; in characteristic $2$ the second condition does not follow from the first.
Over a field, a nondegenerate alternating form exists only in even dimension, which matches the vanishing of $\det A$ for odd $n$.

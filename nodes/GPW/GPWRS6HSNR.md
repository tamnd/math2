---
tag: GPWRS6HSNR
kind: definition
name: Special orthogonal group
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
defines: 6WBVP2PB1Y
uses: [0QRBVFJ50X, 0C3CFHDN6R]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.specialOrthogonalGroup
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
  - book: isbn:9780134860244
    locator: Section 6.11
---

## Definition

The special orthogonal group is the group of real orthogonal matrices that keep orientation.
Let $n \ge 1$.
The *special orthogonal group* is the set
$$SO(n) = \{ Q \in M_n(\R) : Q^{\mathsf{T}} Q = I_n \text{ and } \det Q = 1 \}$$
of real [[orthogonal matrices|0QRBVFJ50X]] with [[determinant|0C3CFHDN6R]] $1$, with matrix multiplication as the group operation.
An element of $SO(n)$ is a *rotation* of $\R^n$.
For a real inner product space $V$ of finite dimension, $SO(V)$ is the group of linear isometries of $V$ with determinant $1$.

## Notation

Books write $SO(n)$, $SO_n(\R)$ or $SO(n, \R)$.
Mathlib writes `Matrix.specialOrthogonalGroup n ℝ` for a finite index type `n`, and its elements are the elements of `Matrix.orthogonalGroup n ℝ` with determinant $1$.

## Remarks

The definition has two conditions, and each one does its own job.
The condition $Q^{\mathsf{T}} Q = I_n$ says that $Q$ keeps lengths and angles.
The condition $\det Q = 1$ removes the mirror images, which have determinant $-1$.

The set is a group because both conditions survive products and inverses.
Orthogonal matrices form the group $O(n)$, and the product rule gives $\det(PQ) = \det P \det Q = 1$ and $\det(Q^{-1}) = (\det Q)^{-1} = 1$.

For an example, the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ satisfies both conditions.
The swap $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ satisfies the first condition but fails the second, since its determinant is $0 \cdot 0 - 1 \cdot 1 = -1$.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ satisfies the second condition but fails the first.
The [[concept page|6WBVP2PB1Y]] gives more examples and the structure of the group.

## Explanations

### L1 human

A rotation matrix is an orthogonal matrix that does not make mirror images.
The determinant tells the two kinds apart.
It is $1$ for rotations and $-1$ for mirror images.

### L2 human

Here is the check for the quarter turn $Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
First the orthogonality:
$$Q^{\mathsf{T}} Q = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
Then the determinant: $\det Q = 0 \cdot 0 - (-1) \cdot 1 = 1$.
So $Q \in SO(2)$, and it is the rotation $R(\pi/2)$.
Watch out: the two conditions are independent, and you must check both, as the swap and the shear above show.

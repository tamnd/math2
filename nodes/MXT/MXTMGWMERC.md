---
tag: MXTMGWMERC
kind: example
name: The upper and lower triangular matrices form conjugate subgroups of GL2(R)
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0H11ZPX4ND]
not_instance_of:
  - target: 0CB0DX5BVV
    note: the upper triangular subgroup has a conjugate that is the lower triangular subgroup, which is a different subgroup
uses: [0FCHE902D7, 0X1JXT47GA, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy of subgroups and general subsets
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Definitions
---

## Example

Let $G = \mathrm{GL}_2(\mathbb{R})$ be the [[general linear group|0FCHE902D7]] of invertible real $2 \times 2$ matrices.
Let $B_+$ be the set of upper triangular matrices in $G$, and $B_-$ the set of lower triangular matrices in $G$:
$$B_+ = \left\{ \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} : ad \ne 0 \right\}, \qquad B_- = \left\{ \begin{pmatrix} a & 0 \\ c & d \end{pmatrix} : ad \ne 0 \right\}.$$
Let $w = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
We show that $wB_+w^{-1} = B_-$, so $B_+$ and $B_-$ are [[conjugate subgroups|0H11ZPX4ND]], and $B_+$ is not [[normal|0CB0DX5BVV]].

1. A triangular matrix has [[determinant|00KDZRW4C0]] $ad$. So the condition $ad \ne 0$ says that the matrix is invertible.
2. $B_+$ contains $I$. A product of two upper triangular matrices is upper triangular: the lower left entry of the product is $0 \cdot a' + d \cdot 0 = 0$.
3. The inverse of $\begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$ is $\frac{1}{ad}\begin{pmatrix} d & -b \\ 0 & a \end{pmatrix}$, which is upper triangular. So $B_+$ is a [[subgroup|0X1JXT47GA]] of $G$.
4. $w^2 = I$, so $w^{-1} = w$.
5. Let $M = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \in B_+$. Left multiplication by $w$ swaps the rows, and right multiplication by $w$ swaps the columns.
6. So $wMw^{-1} = wMw = \begin{pmatrix} d & 0 \\ b & a \end{pmatrix}$, which is in $B_-$. Thus $wB_+w^{-1} \subseteq B_-$.
7. Each element $\begin{pmatrix} a & 0 \\ c & d \end{pmatrix}$ of $B_-$ is $wMw^{-1}$ for $M = \begin{pmatrix} d & c \\ 0 & a \end{pmatrix} \in B_+$, by step 6. So $wB_+w^{-1} = B_-$.
8. $B_-$ is the conjugate of the subgroup $B_+$, so $B_-$ is also a subgroup, and $B_+$ and $B_-$ are conjugate.
9. The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is in $B_+$ but not in $B_-$. So $B_+ \ne B_-$.
10. So $B_+$ has a conjugate that is different from $B_+$, and $B_+$ is not normal in $G$.

## Remarks

The conjugation by $w$ is a change of basis that swaps the two basis vectors $e_1$ and $e_2$.
The group $B_+$ is the set of invertible matrices that send the line $\mathbb{R}e_1$ to itself.
The group $B_-$ is the set of invertible matrices that send the line $\mathbb{R}e_2$ to itself.
Conjugation by $w$ swaps the two lines, so it swaps the two groups.
In general, the conjugates of $B_+$ are the stabilisers of the lines through the origin in $\mathbb{R}^2$.
There is one such line for each direction, so $B_+$ has infinitely many conjugates.

## Explanations

### L1 human

An upper triangular matrix keeps the horizontal axis in its place.
A lower triangular matrix keeps the vertical axis in its place.
If we swap the names of the two axes, the first kind of matrix becomes the second kind.
So the two groups are the same group seen from two points of view.
They are conjugate, but they are not equal, so the first group is not normal.

### L2 human

This example shows the most common way to prove that a subgroup is not normal.
Find one element $g$ and one element $h$ of the subgroup with $ghg^{-1}$ outside the subgroup.
Here $g = w$ and $h = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ give $ghg^{-1} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \notin B_+$.
A common error is to test only diagonal matrices $g$.
A diagonal matrix conjugates $B_+$ into $B_+$, so it gives no information.
The test must use an element that moves the subgroup.

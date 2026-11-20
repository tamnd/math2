---
tag: DER31Q8FCM
kind: example
name: The general linear group of 2 × 2 real matrices is not abelian
msc: ["20G15", "15A09"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0FCHE902D7]
uses: [0FCHE902D7, 032Q9FB8MT, 0P506SPZP2]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ in $\mathrm{GL}_2(\mathbb{R})$.

1. Both are in the [[general linear group|0FCHE902D7]]: $\det A = 1$ and $\det B = 1$, and $A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, $B^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$.
2. $AB = \begin{pmatrix} 1 + 1 & 0 + 1 \\ 0 + 1 & 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
3. $BA = \begin{pmatrix} 1 + 0 & 1 + 0 \\ 1 + 0 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
4. The $(1, 1)$ entries differ, so $AB \ne BA$, and $\mathrm{GL}_2(\mathbb{R})$ is not abelian.
5. For $n \ge 2$, the block matrices $\begin{pmatrix} A & 0 \\ 0 & I_{n-2} \end{pmatrix}$ and $\begin{pmatrix} B & 0 \\ 0 & I_{n-2} \end{pmatrix}$ do not commute in the same way, since block multiplication gives $\begin{pmatrix} AB & 0 \\ 0 & I_{n-2} \end{pmatrix}$ and $\begin{pmatrix} BA & 0 \\ 0 & I_{n-2} \end{pmatrix}$.

## Remarks

The example uses only entries $0$ and $1$, so it works over each field and also over $\mathbb{Z}$.
Over $\mathbb{Z}/2$ it gives two non-commuting elements of the group of order $6$.
The same matrices show the [[noncommutativity of matrix multiplication|0P506SPZP2]] in the ring $M_2$.
For $n = 1$, the group $\mathrm{GL}_1(F) = F^{\times}$ is abelian, so the condition $n \ge 2$ is needed.

## Explanations

### L1 human

The matrix $A$ slides the plane sideways and $B$ slides it upward.
Doing first the sideways slide and then the upward slide is not the same as the other order.
So the order of two invertible matrices matters.

### L2 human

The point is that a group of matrices need not be commutative.
A trap: some pairs do commute, for example two diagonal matrices, so one pair that commutes proves nothing.

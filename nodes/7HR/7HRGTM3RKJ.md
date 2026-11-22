---
tag: 7HRGTM3RKJ
kind: example
name: A symmetric map of the plane in a non-standard basis
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0YQSGNYE3K]
illustrates: [8B63KHW6D5]
uses: [0YYMY95FWS, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Eigenbasis and diagonal matrix
---

## Example

A well chosen basis can turn the matrix of a map into a diagonal matrix.
Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the linear map $T(x, y) = (2x + y, x + 2y)$.
In the standard basis $E = (e_1, e_2)$ we have $T(e_1) = (2, 1)$ and $T(e_2) = (1, 2)$, so the [[matrix|0YYMY95FWS]] is
$$[T]_E = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.$$
Now take the basis $B = (b_1, b_2)$ with $b_1 = (1, 1)$ and $b_2 = (1, -1)$, and compute $[T]_B$.

1. The first basis vector goes to $T(b_1) = (2 + 1, 1 + 2) = (3, 3)$, which is $3 b_1 + 0 b_2$, so column 1 of $[T]_B$ is $(3, 0)$.
2. The second goes to $T(b_2) = (2 - 1, 1 - 2) = (1, -1)$, which is $0 b_1 + 1 b_2$, so column 2 is $(0, 1)$.
3. Together these columns give
$$[T]_B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}.$$

Now we check the [[coordinate formula|8B63KHW6D5]] $[T(v)]_B = [T]_B [v]_B$ on $v = (5, 1)$.

4. The [[coordinates|0BMVBHTWV2]] $[v]_B = (a, b)$ satisfy $a b_1 + b b_2 = (a + b, a - b) = (5, 1)$, so $a + b = 5$ and $a - b = 1$, which give $a = 3$ and $b = 2$.
5. The matrix gives
$$[T]_B \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 9 \\ 2 \end{pmatrix}.$$
6. Directly, $T(5, 1) = (10 + 1, 5 + 2) = (11, 7)$, and its coordinates solve $a + b = 11$ and $a - b = 7$, so $a = 9$ and $b = 2$.
7. Steps 5 and 6 agree, as the formula says.

## Remarks

The diagonal matrix tells the geometry of $T$ at a glance.
The map stretches the line through $(1, 1)$ by the factor $3$, and it fixes each point of the line through $(1, -1)$.
In the standard basis the same facts are hidden in the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.

The two matrices of $T$ are [[similar|0E89HQATM8]], since they belong to one map in two bases.
So they share their trace and determinant: $2 + 2 = 3 + 1 = 4$ and $4 - 1 = 3 \cdot 1 = 3$.
If we swap the order of $b_1$ and $b_2$, the matrix becomes $\begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$, with the diagonal entries in the other order.
If we replace $b_2$ by $(1, 0)$, the matrix is no longer diagonal, because $T(1, 0) = (2, 1)$ is not a multiple of $(1, 0)$.

## Explanations

### L1 human

A good basis can make the matrix of a map much simpler.
This map pulls the plane out along the diagonal line through $(1, 1)$, to three times the length, and leaves the other diagonal line alone.
In the basis made of the two diagonal directions, the matrix has only the numbers $3$ and $1$ on its diagonal and zeros elsewhere.

### L2 human

The matrix in the basis $B$ needs the $B$-coordinates of $T(b_1)$ and $T(b_2)$, not their standard coordinates.
Here they are easy to find, because $T(b_1)$ and $T(b_2)$ are multiples of $b_1$ and $b_2$: the vectors of $B$ are eigenvectors of $T$.
The check in steps 4 to 7 uses $B$-coordinates on both sides of the formula.
Watch out: if you multiply $[T]_B$ by the standard coordinates $(5, 1)$ of $v$, you get $(15, 1)$, which is neither $T(v)$ nor its $B$-coordinates.

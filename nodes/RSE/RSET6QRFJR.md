---
tag: RSET6QRFJR
kind: example
name: Writing the images as rows does not give the matrix of a linear map
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0YQSGNYE3K
    note: the array with rows (1, 0) and (2, 3) sends (0, 1) to (0, 3), but T(0, 1) = (2, 3)
uses: [0YYMY95FWS, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Finding the matrix of a transformation
---

## Example

Let $T \colon \R^2 \to \R^2$ be $T(x, y) = (x + 2y,\ 3y)$, and use the standard basis $(e_1, e_2)$ on both sides.

1. $T(e_1) = (1, 0)$ and $T(e_2) = (2, 3)$.
2. With the images as columns, the [[matrix|0YYMY95FWS]] is $M = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
3. With the images as rows, the array is $N = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}$. This is the [[transpose|0W809K6AW0]] $M^\top$.
4. Take $v = (0, 1)$. Then $T(v) = (2, 3)$, and $Mv = (2, 3)$.
5. But $Nv = (0, 3) \ne (2, 3)$. So $N$ is not the matrix of $T$.

For a map between spaces of different dimension, the error shows at once.
Let $S \colon \R^2 \to \R^3$ be $S(x, y) = (x,\ x + y,\ 2y)$.

6. $S(e_1) = (1, 1, 0)$ and $S(e_2) = (0, 1, 2)$. The matrix of $S$ is the $3 \times 2$ matrix with these columns.
7. The array with these rows is $2 \times 3$. Its product with a vector of $\R^2$ is not defined.

## Remarks

- The array of step 3 is the matrix of $T$ in a convention where vectors are rows and act from the left, $v \mapsto vN$.
- The array $N$ is the matrix of the [[dual map|0AZ5ARP287]] in the dual bases. So it carries the same information, but it is not the matrix of $T$.

## Explanations

### L1 human

The images of the basis vectors go in the columns, not in the rows.
If they go in the rows, the product with a coordinate vector gives a wrong answer.

### L2 human

The test of step 5 is quick: multiply by a unit vector and compare with the image of the basis vector.
For square matrices the wrong array still has the right size, so the error does not show by size.
For maps between spaces of different dimension the sizes do not fit, as in step 7.

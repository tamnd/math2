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

The images of the basis vectors belong in the columns of the matrix, and putting them in the rows gives an array that computes the wrong map.
Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ be $T(x, y) = (x + 2y, 3y)$, with the standard basis $(e_1, e_2)$ on both sides.

1. The basis vectors go to $T(e_1) = (1, 0)$ and $T(e_2) = (2, 3)$.
2. With these images as columns, the [[matrix|0YYMY95FWS]] of $T$ is $M = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
3. With the images as rows, we get the array $N = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}$, which is the [[transpose|0W809K6AW0]] $M^{\mathsf{T}}$.
4. Take $v = (0, 1)$, so $T(v) = (2, 3)$, and the matrix agrees:
$$M \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}.$$
5. The array of rows does not agree:
$$N \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 3 \end{pmatrix} \ne \begin{pmatrix} 2 \\ 3 \end{pmatrix}.$$
So $N$ is not the matrix of $T$.

For a map between spaces of different dimensions, the error shows in the sizes.
Let $S \colon \mathbb{R}^2 \to \mathbb{R}^3$ be $S(x, y) = (x, x + y, 2y)$.

6. The basis vectors go to $S(e_1) = (1, 1, 0)$ and $S(e_2) = (0, 1, 2)$, and the matrix of $S$ is the $3 \times 2$ matrix with these columns.
7. The array with these rows is $2 \times 3$, and its product with a column of $\mathbb{R}^2$ is not defined, since a row of length $3$ cannot meet a column of length $2$.

## Remarks

The example shows the quickest test of a matrix: multiply it by a unit vector $e_j$ and compare the result with $T(e_j)$.
The product $M e_j$ is column $j$ of $M$, so the test checks exactly that the columns are the images.

The array $N$ is not useless.
In books that write vectors as rows and let matrices act from the right, $v \mapsto vN$, it is the matrix of $T$: for $v = (0, 1)$ the row $vN$ is the second row $(2, 3)$.
It is also the matrix of the [[dual map|0AZ5ARP287]] of $T$ in the dual bases.
So $N$ carries the same information as $M$, but in our convention of columns it describes a different map.
The two arrays agree only when $M$ is symmetric, for example for $T(x, y) = (x + 2y, 2x + 3y)$.

## Explanations

### L1 human

The images of the basis vectors go in the columns, not in the rows.
If they go in the rows, the product with a coordinate vector gives a wrong answer.
Here the second basis vector should go to $(2, 3)$, but the array of rows sends it to $(0, 3)$.

### L2 human

For a square matrix the wrong array still has the right size, so the mistake does not show by size and only a test catches it.
The test of step 5 takes one line: multiply by a unit vector and compare with the image of the basis vector.
For maps between spaces of different dimensions the sizes do not fit, as in step 7, so there the mistake shows at once.
Watch out: a symmetric example, such as a reflection in a diagonal line, passes the test with either array, so test with a map whose matrix is not symmetric.

---
tag: KWN1RM45D5
kind: example
name: Matrix of the derivative from quadratic to linear polynomials
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0YQSGNYE3K]
illustrates: [8B63KHW6D5]
uses: [0YYMY95FWS, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Finding the matrix of a transformation
  - book: isbn:9780134860244
    locator: Section 2.2
---

## Example

Differentiation of polynomials becomes the multiplication of a small matrix by a column of coefficients.
Let $P_k$ be the space of real polynomials of degree at most $k$, and let $D \colon P_2 \to P_1$ be the derivative, $D(p) = p'$.
Take the bases $B = (1, x, x^2)$ of $P_2$ and $C = (1, x)$ of $P_1$.
We build the [[matrix of D|0YYMY95FWS]] one column at a time.

1. The first basis vector goes to $D(1) = 0 = 0 \cdot 1 + 0 \cdot x$, so column 1 is $(0, 0)$.
2. The second goes to $D(x) = 1 = 1 \cdot 1 + 0 \cdot x$, so column 2 is $(1, 0)$.
3. The third goes to $D(x^2) = 2x = 0 \cdot 1 + 2 \cdot x$, so column 3 is $(0, 2)$.
4. Together the columns give the $2 \times 3$ matrix
$$[D]_{C,B} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$

Now we test the [[coordinate formula|8B63KHW6D5]] on $p = 3 + 5x - 4x^2$.

5. The [[coordinate vector|0BMVBHTWV2]] of $p$ is $[p]_B = (3, 5, -4)$.
6. Multiply the matrix by it:
$$\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 5 \\ -4 \end{pmatrix} = \begin{pmatrix} 0 \cdot 3 + 1 \cdot 5 + 0 \cdot (-4) \\ 0 \cdot 3 + 0 \cdot 5 + 2 \cdot (-4) \end{pmatrix} = \begin{pmatrix} 5 \\ -8 \end{pmatrix}.$$
7. Directly, $p' = 5 - 8x$, so $[p']_C = (5, -8)$, which agrees with step 6.

## Remarks

The shape of the matrix comes from the dimensions.
It has $2$ rows because $\dim P_1 = 2$, and $3$ columns because $\dim P_2 = 3$.
Its first column is zero because the constants lie in the kernel of $D$, and its rank is $2$ because every linear polynomial is a derivative.

The matrix depends on the order of the bases.
With the order $C = (x, 1)$ the two rows change places, and the matrix is $\begin{pmatrix} 0 & 0 & 2 \\ 0 & 1 & 0 \end{pmatrix}$.
If we view $D$ as a map $P_2 \to P_2$ with the basis $B$ on both sides, a zero row appears at the bottom, since no derivative of a quadratic has an $x^2$ term:
$$[D]_B = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}.$$

## Explanations

### L1 human

Differentiate each basis polynomial and write the coefficients of the answer as a column.
For example, $x^2$ has derivative $2x = 0 \cdot 1 + 2 \cdot x$, so its column is $(0, 2)$.
Multiplying the matrix by the coefficients of any quadratic $p$ then gives the coefficients of $p'$.

### L2 human

The example shows that a matrix can describe a map between spaces whose vectors are not lists of numbers.
The bases $B$ and $C$ turn each polynomial into a column, and steps 5 to 7 check the formula $[D(p)]_C = [D]_{C,B}[p]_B$ on one polynomial.
The same method gives the matrix of any linear operation on polynomials, such as $p \mapsto x p'$ or $p \mapsto p(x + 1)$.
Watch out: the coefficient list of $p$ must follow the order of the basis, so with $B = (x^2, x, 1)$ the same $p$ has coordinates $(-4, 5, 3)$, and the columns of the matrix are reordered too.

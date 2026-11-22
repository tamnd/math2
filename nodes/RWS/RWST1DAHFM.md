---
tag: RWST1DAHFM
kind: example
name: A linear map out of R² ⊕ R built from its pieces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0S7W6EG32V]
illustrates: [N04WS31KXB]
uses: [02WZB422CE, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Universal property
---

## Example

Let $V_1 = \R^2$ and $V_2 = \R$, and form the [[external direct sum|02WZB422CE]] $\R^2 \oplus \R$, whose vectors are pairs $((x, y), t)$.
Take the [[linear maps|0RJF668P1T]] $f_1 \colon \R^2 \to \R$, $f_1(x, y) = x + y$, and $f_2 \colon \R \to \R$, $f_2(t) = 2t$.
We build the map that the [[universal property|N04WS31KXB]] gives and check each of its claims.

1. The formula of the property adds the values of the two pieces:
$$f((x, y), t) = f_1(x, y) + f_2(t) = x + y + 2t.$$
2. The map $f$ is linear, since $x + y + 2t$ is a linear expression in the entries $x$, $y$ and $t$.
3. On the first summand, $f(\iota_1(x, y)) = f((x, y), 0) = x + y = f_1(x, y)$.
4. On the second summand, $f(\iota_2(t)) = f((0, 0), t) = 2t = f_2(t)$.
5. For uniqueness, let $g$ be linear with the same two restrictions.
   Since $((x, y), t) = ((x, y), 0) + ((0, 0), t)$, linearity gives $g((x, y), t) = f_1(x, y) + f_2(t)$.
   So $g = f$.

If we identify $\R^2 \oplus \R$ with $\R^3$, then $f$ has the $1 \times 3$ matrix $\begin{pmatrix} 1 & 1 & 2 \end{pmatrix}$, which is the block row made of the matrix $\begin{pmatrix} 1 & 1 \end{pmatrix}$ of $f_1$ and the matrix $\begin{pmatrix} 2 \end{pmatrix}$ of $f_2$.

## Remarks

The example shows that a map out of a direct sum is designed one piece at a time, with no condition linking the pieces.
Changing $f_2$ to $f_2(t) = -5t$ changes only the last entry of the matrix, which becomes $\begin{pmatrix} 1 & 1 & -5 \end{pmatrix}$.

The pieces do not tell us the kernel of $f$ piece by piece.
The kernel of $f$ is the plane $x + y + 2t = 0$, of dimension $2$.
The kernels of the pieces give only the line of vectors $((x, -x), 0)$, of dimension $1$.
For instance, $((1, 1), -1)$ lies in $\ker f$, since $1 + 1 - 2 = 0$, but its part $(1, 1)$ is not in $\ker f_1$ and its part $-1$ is not in $\ker f_2$.

## Explanations

### L1 human

A map on the pairs is built by applying one map to each part and adding the results.
The first map adds the two coordinates of the plane vector, and the second map doubles the number.
So the pair $((1, 2), 3)$ goes to $3 + 6 = 9$.

### L2 human

We compute the value at $((1, 2), 3)$ in two ways.
With the pieces:
$$f_1(1, 2) + f_2(3) = 3 + 6 = 9.$$
With the matrix:
$$\begin{pmatrix} 1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 1 + 2 + 6 = 9.$$
The two answers agree, as the block form of the matrix predicts.
Watch out: the order of the blocks in the matrix follows the order of the summands, so $\R \oplus \R^2$ would give the row $\begin{pmatrix} 2 & 1 & 1 \end{pmatrix}$ instead.

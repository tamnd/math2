---
tag: YMRSMANN2E
kind: example
name: The dual basis of a non-standard basis of the plane
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [0ZD2CF6ZS0]
uses: [0W6M3PSD08, 0TWTS88TWN, 04CYQHN6MC, SXWX10HSB6]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Example

Let $V = \R^2$ with the basis $b_1 = (1, 1)$ and $b_2 = (1, 2)$.
We find the [[dual basis|0W6M3PSD08]] $b_1^*, b_2^*$ by inverting a matrix.

1. Put $b_1$ and $b_2$ as the columns of $P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$. Then $\det P = 1 \cdot 2 - 1 \cdot 1 = 1 \ne 0$, so $P$ is [[invertible|0TWTS88TWN]] and $b_1, b_2$ is a basis.
2. The inverse of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is $\frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. So $P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$.
3. Check: $P^{-1} P = \begin{pmatrix} 2 - 1 & 2 - 2 \\ -1 + 1 & -1 + 2 \end{pmatrix} = I$.
4. Entry $(i, j)$ of $P^{-1} P$ is row $i$ of $P^{-1}$ applied to $b_j$. So row $i$ of $P^{-1}$ is a form that is $1$ at $b_i$ and $0$ at the other basis vector.
5. Hence $b_1^*(x, y) = 2x - y$ and $b_2^*(x, y) = -x + y$.
6. Direct check: $b_1^*(1, 1) = 1$, $b_1^*(1, 2) = 0$, $b_2^*(1, 1) = 0$ and $b_2^*(1, 2) = 1$.
7. Use for [[coordinates|04CYQHN6MC]]: for $v = (3, 5)$, we get $b_1^*(v) = 6 - 5 = 1$ and $b_2^*(v) = -3 + 5 = 2$.
8. Check: $1 \cdot (1, 1) + 2 \cdot (1, 2) = (3, 5) = v$.
9. Expansion of a form: let $f(x, y) = x$. Then $f(b_1) = 1$ and $f(b_2) = 1$, so $f = b_1^* + b_2^*$. Indeed $(2x - y) + (-x + y) = x$.

## Remarks

- The form $b_1^* = 2x - y$ is not the row $(1, 1)$ of the vector $b_1$. Identifying a vector with "its" form depends on the basis.
- With the standard basis, the map $e_i \mapsto e_i^*$ sends $(1, 1) = e_1 + e_2$ to the form $x + y$. With the basis $b_1, b_2$, the map $b_i \mapsto b_i^*$ sends $(1, 1) = b_1$ to $2x - y$. So the two "natural looking" isomorphisms $\R^2 \to (\R^2)^*$ differ.
- Here $(P^{-1})^{\mathsf{T}} = P^{-1}$, and the columns of $(P^{-1})^{\mathsf{T}}$ give the coordinates of $b_k^*$ in $e_1^*, e_2^*$, as the [[change of dual basis lemma|SXWX10HSB6]] says.
- Replacing $b_2 = (1, 2)$ by $(1, 0)$ changes $b_1^*$ to the form $y$, although $b_1$ stays the same.

## Explanations

### L1 human

The basis vectors $(1, 1)$ and $(1, 2)$ describe each point of the plane by two numbers.
The rule $2x - y$ gives the first number, and the rule $-x + y$ gives the second.
For the point $(3, 5)$, these rules give $1$ and $2$, and indeed $(3, 5) = 1 \cdot (1, 1) + 2 \cdot (1, 2)$.

### L2 human

The method works in every dimension.

1. Put the basis vectors as the columns of a matrix $P$.
2. Invert $P$.
3. Read the dual basis forms from the rows of $P^{-1}$.

The typical use is to compute coordinates in a new basis, since the coordinate column of $v$ is $P^{-1} v$.
A trap: reading the dual forms from the columns of $P^{-1}$ instead of the rows gives wrong forms when $P^{-1}$ is not symmetric.

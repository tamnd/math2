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
We find the [[dual basis|0W6M3PSD08]] $b_1^*, b_2^*$ by inverting one matrix, and then we use it.

1. Put $b_1$ and $b_2$ as the columns of a matrix:
$$P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det P = 1 \cdot 2 - 1 \cdot 1 = 1.$$
Since $\det P \ne 0$, the matrix is [[invertible|0TWTS88TWN]] and $b_1, b_2$ is a basis.
2. Invert with the rule for $2 \times 2$ matrices: swap the diagonal entries, negate the other two, and divide by $\det P = 1$.
$$P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}.$$
3. Check the inverse:
$$P^{-1} P = \begin{pmatrix} 2 - 1 & 2 - 2 \\ -1 + 1 & -1 + 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
4. Entry $(i, j)$ of $P^{-1} P$ is row $i$ of $P^{-1}$ applied to $b_j$. So row $i$ of $P^{-1}$ is a form that gives $1$ at $b_i$ and $0$ at the other basis vector.
5. Read off the rows: $b_1^*(x, y) = 2x - y$ and $b_2^*(x, y) = -x + y$.
6. Check directly: $b_1^*(1, 1) = 1$, $b_1^*(1, 2) = 0$, $b_2^*(1, 1) = 0$ and $b_2^*(1, 2) = 1$.

Now we use the dual basis to find [[coordinates|04CYQHN6MC]].
For $v = (3, 5)$, the two forms give
$$b_1^*(v) = 6 - 5 = 1, \qquad b_2^*(v) = -3 + 5 = 2.$$
Check: $1 \cdot (1, 1) + 2 \cdot (1, 2) = (3, 5) = v$.

We can also expand a form.
Let $f(x, y) = x$.
Then $f(b_1) = 1$ and $f(b_2) = 1$, so $f = b_1^* + b_2^*$.
Check: $(2x - y) + (-x + y) = x$.

## Remarks

The example shows that the dual form of a vector depends on the other basis vectors.
The form $b_1^* = 2x - y$ is not the row $(1, 1)$ of the vector $b_1$, which would be the form $x + y$.
If we keep $b_1 = (1, 1)$ and replace $b_2$ by $(1, 0)$, then $b_1^*$ becomes the form $y$, although $b_1$ has not changed.

It also shows that the isomorphism $b_i \mapsto b_i^*$ depends on the basis.
With the standard basis, $e_i \mapsto e_i^*$ sends $(1, 1) = e_1 + e_2$ to the form $x + y$.
With the basis $b_1, b_2$, the map $b_i \mapsto b_i^*$ sends $(1, 1) = b_1$ to $2x - y$.

Here $P^{-1}$ is symmetric, so $(P^{-1})^{\mathsf{T}} = P^{-1}$.
Its columns give the coordinates of $b_1^*$ and $b_2^*$ in $e_1^*, e_2^*$, as the [[change of dual basis lemma|SXWX10HSB6]] says.

## Explanations

### L1 human

The vectors $(1, 1)$ and $(1, 2)$ describe each point of the plane by two numbers, the amounts of each vector that we need.
The rule $2x - y$ gives the first amount, and the rule $-x + y$ gives the second.
For the point $(3, 5)$ these rules give $1$ and $2$, and indeed $(3, 5) = 1 \cdot (1, 1) + 2 \cdot (1, 2)$.

### L2 human

The method works in every dimension: put the basis vectors as the columns of $P$, invert $P$, and read the dual forms from the rows of $P^{-1}$.
For the basis $(1, 0), (1, 1)$ we get
$$P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix},$$
so the dual forms are $x - y$ and $y$.
The typical use is to compute coordinates in a new basis, since the coordinate column of $v$ is $P^{-1} v$.
Watch out: here $P^{-1}$ is not symmetric, and reading its columns instead of its rows gives the forms $x$ and $-x + y$, which are wrong since $x$ gives $1$ at $(1, 1)$.

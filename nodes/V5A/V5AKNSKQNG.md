---
tag: V5AKNSKQNG
kind: example
name: The quadratic form x² + xy and its symmetric matrix
msc: ["15A63"]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR, 0HYFWKKY3C]
uses: [0HZNE5QZDJ, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Associated symmetric matrix
---

## Example

Let $Q(x, y) = x^2 + xy$ on $\mathbb{R}^2$.
We check that $Q$ is a [[quadratic form|0HZNE5QZDJ]], compute its polar form, and find its symmetric matrix.

1. Scaling. Each term picks up $a^2$, so $Q(ax, ay) = a^2 x^2 + a^2 xy = a^2 Q(x, y)$ for all $a \in \mathbb{R}$.
2. Polar form. For $u = (x, y)$ and $v = (x', y')$, expand and cancel:
$$Q(u + v) - Q(u) - Q(v) = (x + x')^2 + (x + x')(y + y') - x^2 - xy - x'^2 - x'y' = 2xx' + xy' + x'y.$$
3. Bilinearity. The result $b_Q(u, v) = 2xx' + xy' + x'y$ is linear in $u$ for fixed $v$ and linear in $v$ for fixed $u$. So $Q$ is a quadratic form.
4. The symmetric bilinear form. Since $2$ is invertible in $\mathbb{R}$, the associated form is $B = \tfrac{1}{2} b_Q$, that is, $B(u, v) = xx' + \tfrac{1}{2} xy' + \tfrac{1}{2} x'y$.
5. The matrix. Its entries are $B(e_1, e_1) = 1$, $B(e_1, e_2) = B(e_2, e_1) = \tfrac{1}{2}$ and $B(e_2, e_2) = 0$:
$$A = \begin{pmatrix} 1 & \tfrac{1}{2} \\ \tfrac{1}{2} & 0 \end{pmatrix}.$$
6. Check. Multiply out: $\begin{pmatrix} x & y \end{pmatrix} A \begin{pmatrix} x \\ y \end{pmatrix} = x^2 + \tfrac{1}{2} xy + \tfrac{1}{2} yx + 0 \cdot y^2 = x^2 + xy$.
7. Uniqueness. The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ also gives $x^2 + xy$, but it is not [[symmetric|0N28QN4CYA]]. Among symmetric matrices, $A$ is the only one.

## Remarks

The example shows the convention that confuses many readers: the coefficient of a cross term $x_i x_j$ is split into two equal halves $a_{ij} = a_{ji}$.
So a form with integer coefficients can have a symmetric matrix with entries $\tfrac{1}{2}$.
For $x^2 + c\,xy$ the off-diagonal entry is $c/2$, and it is an integer exactly when $c$ is even.

The matrix also tells you the type of the form.
Its determinant is $1 \cdot 0 - \tfrac{1}{4} = -\tfrac{1}{4} < 0$, so the form is [[indefinite|01RBSSGMY5]].
Check with values: $Q(1, 0) = 1 > 0$ and $Q(1, -2) = 1 - 2 = -1 < 0$.

## Explanations

### L1 human

The expression $x^2 + xy$ has one square term and one mixed term.
To write it with a symmetric table of numbers, put half of the mixed coefficient in each of the two places off the diagonal.
So the table has $1$ and $0$ on the diagonal and $\tfrac{1}{2}$ twice off the diagonal.

### L2 human

The general rule for a form in two variables is
$$ax^2 + bxy + cy^2 = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} a & b/2 \\ b/2 & c \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
With $a = 1$, $b = 1$ and $c = 0$ this gives the matrix of step 5.
Watch out: the determinant of this matrix is $ac - b^2/4 = -\tfrac{1}{4}(b^2 - 4ac)$, not $ac - b^2$.
So the sign of the determinant is the opposite of the sign of $b^2 - 4ac$, and you get wrong answers from $ac - b^2$; for $x^2 + xy + y^2$ it gives $1 - 1 = 0$, while the correct value $\tfrac{3}{4}$ is positive.

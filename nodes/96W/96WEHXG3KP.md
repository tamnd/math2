---
tag: 96WEHXG3KP
kind: example
name: The discriminant of the binary form x² + xy + y²
msc: ["11E04", "11E16"]
topics: [6TSCEW8QMK]
audience: ug2
instance_of: [MZFRXECCMC]
uses: [MZFRXECCMC, VN9AG8JKYT, SBDSYA037Q]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_quadratic_form
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

Let $Q(x, y) = x^2 + xy + y^2$ over $\mathbb{Q}$.
We compute its [[discriminant|MZFRXECCMC]] in the convention of quadratic forms over fields, and we compare it with the number-theory discriminant $b^2 - 4ac$.

1. The matrix. By [[the correspondence theorem|VN9AG8JKYT]], the cross term $xy$ is split evenly between the two off-diagonal entries, so
$$A = \begin{pmatrix} 1 & \tfrac12 \\ \tfrac12 & 1 \end{pmatrix}.$$
Check: $x^{\mathsf{T}} A x = x^2 + \tfrac12 xy + \tfrac12 yx + y^2 = x^2 + xy + y^2$.
2. The determinant. We get $\det A = 1 \cdot 1 - \tfrac12 \cdot \tfrac12 = \tfrac34$.
3. The square class. Since $\tfrac34 = 3 \cdot \left( \tfrac12 \right)^2$, the discriminant of $Q$ is the class of $3$ in $\mathbb{Q}^\times / \mathbb{Q}^{\times 2}$.
4. The number-theory discriminant. The [[binary form|SBDSYA037Q]] $a x^2 + b xy + c y^2$ has discriminant $b^2 - 4ac$, and here $a = b = c = 1$, so $b^2 - 4ac = 1 - 4 = -3$.
5. The relation. The general identity $\det A = ac - b^2/4 = -\tfrac14 (b^2 - 4ac)$ gives $-4 \det A = b^2 - 4ac$. Here $-4 \cdot \tfrac34 = -3$, as it should be.
6. A diagonal form. Completing the square gives
$$Q = \left( x + \frac{y}{2} \right)^2 + 3 \left( \frac{y}{2} \right)^2,$$
so with $X = x + y/2$ and $Y = y/2$ the form is $X^2 + 3Y^2$. Its determinant is $3$, the same class as in step 3.

## Remarks

### Two conventions, one form

The two answers $3$ and $-3$ are not a contradiction.
They differ by the factor $-4 = -1 \cdot 2^2$, so modulo squares they differ exactly by the sign $-1$.
Over $\mathbb{R}$ the form is positive definite, and the field convention shows this as $\det A > 0$, while the number-theory convention shows it as $b^2 - 4ac < 0$.
For a real binary form, $b^2 - 4ac < 0$ means definite, $b^2 - 4ac > 0$ means indefinite, and $b^2 - 4ac = 0$ means degenerate.
Over $\mathbb{Q}$, an indefinite form factors into rational linear factors exactly when $b^2 - 4ac$ is the square of a rational number.

### What changes with the coefficient

For $x^2 + bxy + y^2$ the matrix has off-diagonal entries $b/2$, and $\det A = 1 - b^2/4$.
With $b = 2$ we get $(x + y)^2$ and $\det A = 0$, a degenerate form.
With $b = 3$ we get $\det A = -\tfrac54$, in the class of $-5$, and the form is indefinite.

## Explanations

### L1 human

The form $x^2 + xy + y^2$ has a cross term $xy$.
In its matrix this term is shared by two entries, so each of them is $\tfrac12$.
The determinant of the matrix is $1 - \tfrac14 = \tfrac34$.
Books on number theory use the number $b^2 - 4ac = 1 - 4 = -3$ instead, which is $-4$ times the determinant.

### L2 human

Here is the typical use: before you compare discriminants from two books, check which convention each book uses.
A book on binary forms lists $x^2 + xy + y^2$ with discriminant $-3$.
A book on quadratic forms over fields gives the class of $\tfrac34$, which is the class of $3$.
To translate, multiply by $-4$, or, modulo squares, change the sign.
Watch out: if you write the matrix of $x^2 + xy + y^2$ with entries $1$ in place of $\tfrac12$, you get $\det \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 0$ and the wrong conclusion that the form is degenerate.

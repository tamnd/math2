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

Let $Q(x, y) = x^2 + xy + y^2$ over $\Q$.

1. By [[the correspondence theorem|VN9AG8JKYT]], its symmetric matrix is $A = \begin{pmatrix} 1 & \frac12 \\ \frac12 & 1 \end{pmatrix}$.
2. $\det A = 1 - \frac14 = \frac34$.
3. $\frac34 = 3 \cdot \left( \frac12 \right)^2$, so the [[discriminant|MZFRXECCMC]] of $Q$ is the square class of $3$.
4. In number theory, the [[binary form|SBDSYA037Q]] $a x^2 + b x y + c y^2$ has discriminant $b^2 - 4ac$. Here $a = b = c = 1$, so $b^2 - 4ac = -3$.
5. Check of the relation between the conventions: $-4 \det A = -4 \cdot \frac34 = -3 = b^2 - 4ac$.
6. Completing the square: $Q = \left( x + \frac y2 \right)^2 + 3 \left( \frac y2 \right)^2$. So $Q$ is equivalent to $X^2 + 3Y^2$, whose determinant is $3$, in agreement with step 3.

## Remarks

The two conventions differ by the factor $-4 = -1 \cdot 2^2$.
So modulo squares they differ by the sign $-1$: the class of $3$ against the class of $-3$.
Over $\R$, $\det A > 0$ and the form is positive definite, while $b^2 - 4ac < 0$.
In the convention $b^2 - 4ac$, a negative number means a definite binary form.
A positive non-square means an indefinite form that does not factor over $\Q$.

## Explanations

### L1 human

The form $x^2 + xy + y^2$ has a cross term $xy$, so its matrix has the entries $\frac12$.
The determinant is $\frac34$.
Number theorists use $b^2 - 4ac = -3$ instead, which is $-4$ times the determinant.

### L2 human

A trap: before you compare discriminants from two books, check which convention each book uses.
The number $-3$ in a book on binary forms is the class $3$ in a book on quadratic forms over fields.

---
tag: HS1DY318PY
kind: example
name: A form with positive coefficients that is not positive definite
msc: [15A63]
topics: [6TSCEW8QMK]
audience: ug1
not_instance_of:
  - target: 0RP20HFYM3
    note: all coefficients are positive, but the form takes the value -2 at (3, -2)
uses: [00QN1N6MNT, 0WKEF78PMV]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Example

Let $Q(x, y) = 2x^2 + 6xy + 4y^2$ on $\mathbb{R}^2$.
Its symmetric matrix is $A = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$, with half of the coefficient $6$ in each off-diagonal place.
Every coefficient of $Q$ and every entry of $A$ is positive, and yet $Q$ is not [[positive definite|00QN1N6MNT]].

1. Evaluate at $(3, -2)$: $Q(3, -2) = 2 \cdot 9 + 6 \cdot 3 \cdot (-2) + 4 \cdot 4 = 18 - 36 + 16 = -2$.
   A negative value at a nonzero vector breaks the definition.
2. The minors test agrees: the first minor is $2 > 0$, but $\det A = 8 - 9 = -1 < 0$, so [[Sylvester's criterion|0WKEF78PMV]] fails.
3. The form factors as $Q = 2(x + y)(x + 2y)$.
   Check: $2(x^2 + 3xy + 2y^2) = 2x^2 + 6xy + 4y^2$.
   So $Q$ is $0$ on the lines $y = -x$ and $y = -\tfrac{1}{2} x$, and negative between them, where the two factors have opposite signs.
4. The eigenvalues solve $t^2 - 6t - 1 = 0$, since $\operatorname{tr} A = 6$ and $\det A = -1$.
   They are $3 \pm \sqrt{10}$, about $6.16$ and $-0.16$.
   One is negative, so $Q$ is indefinite.

## Remarks

The value $Q(1, -1) = 2 - 6 + 4 = 0$ shows the failure at a smaller point, on the line $y = -x$ of step 3.
For a binary form $ax^2 + bxy + cy^2$ with $a > 0$, positive definiteness needs $b^2 < 4ac$.
Here $b^2 = 36$ and $4ac = 32$, so the cross term is too large.
If the cross coefficient $6$ were $5$, the determinant would be $8 - \tfrac{25}{4} = \tfrac{7}{4} > 0$, and the form would be positive definite.

## Explanations

### L1 human

Every number in the form is positive, so it is tempting to say that the form is always positive.
But the term $6xy$ is negative when $x$ and $y$ have opposite signs.
At $(3, -2)$ that term is $-36$, and it beats the other two terms, $18$ and $16$.

### L2 human

The lesson is that the signs of the entries do not decide definiteness, in either direction.
The matrix $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ has negative entries and is positive definite, with eigenvalues $3$ and $1$.
Always use a real test: the leading minors, the eigenvalues, or a completion of squares.

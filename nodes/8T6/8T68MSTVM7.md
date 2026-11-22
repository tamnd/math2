---
tag: 8T68MSTVM7
kind: example
name: A positive definite Hermitian form on the complex plane
msc: ["15A63", "11E39"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [48P4A1CX85, 0NB0AWGJBW]
illustrates: [AXH4S084MR]
uses: [0W44K2VNBD, AXH4S084MR, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Hermitian form
---

## Example

On $\mathbb{C}^2$, with the second slot conjugate-linear, let $h(x, y) = x^{\mathsf{T}} M \bar y$ with
$$M = \begin{pmatrix} 1 & i \\ -i & 2 \end{pmatrix}, \qquad h(x, y) = x_1 \bar y_1 + i x_1 \bar y_2 - i x_2 \bar y_1 + 2 x_2 \bar y_2.$$
We show that $h$ is Hermitian and positive definite, so that it is an inner product on $\mathbb{C}^2$.

1. Conjugate and transpose: $M^* = \begin{pmatrix} 1 & \overline{-i} \\ \bar i & 2 \end{pmatrix} = \begin{pmatrix} 1 & i \\ -i & 2 \end{pmatrix} = M$. By the [[characterization of Hermitian forms|AXH4S084MR]], $h$ is Hermitian.
2. Let $x = (1, i)$, so $\bar x = (1, -i)$. Multiply $M$ by $\bar x$:
$$M \bar x = \begin{pmatrix} 1 + i \cdot (-i) \\ -i + 2 \cdot (-i) \end{pmatrix} = \begin{pmatrix} 2 \\ -3i \end{pmatrix}.$$
3. Then $h(x, x) = 1 \cdot 2 + i \cdot (-3i) = 2 + 3 = 5$, a real number.
4. Let $y = (0, 1)$. Then $M \bar y = (i, 2)$, and $h(x, y) = 1 \cdot i + i \cdot 2 = 3i$.
5. In the other order, $h(y, x) = y^{\mathsf{T}} M \bar x = -3i$, the second entry of step 2. This is $\overline{3i}$, as the Hermitian condition requires.
6. For a general $v = (v_1, v_2)$, complete the square on the terms with $v_1$:
$$h(v, v) = \lvert v_1 \rvert^2 + i v_1 \bar v_2 - i v_2 \bar v_1 + 2 \lvert v_2 \rvert^2 = \lvert v_1 - i v_2 \rvert^2 + \lvert v_2 \rvert^2.$$
7. Check step 6 by expanding the square, using $(-i)(i) = 1$:
$$\lvert v_1 - i v_2 \rvert^2 = (v_1 - i v_2)(\bar v_1 + i \bar v_2) = \lvert v_1 \rvert^2 + i v_1 \bar v_2 - i v_2 \bar v_1 + \lvert v_2 \rvert^2.$$
8. So $h(v, v) \ge 0$, and $h(v, v) = 0$ forces $v_2 = 0$ and then $v_1 = i v_2 = 0$. Hence $h$ is positive definite, and it is a complex inner product.

## Remarks

Step 6 is the Hermitian version of completing the square, with $\lvert \cdot \rvert^2$ in place of squares.
For $x = (1, i)$ it gives $\lvert 1 - i \cdot i \rvert^2 + \lvert i \rvert^2 = 4 + 1 = 5$, the value of step 3.

The leading principal minors of $M$ give a second test.
They are $1$ and $\det M = 1 \cdot 2 - i \cdot (-i) = 2 - 1 = 1$, both positive, so [[Sylvester's criterion|0WKEF78PMV]] confirms positive definiteness.

The off-diagonal entries are not real, but they are conjugates of each other, as in every [[Hermitian matrix|0EKZCX4K3P]].
What happens if we change the corner entries to $2i$ and $-2i$?
Then $\det M = 2 - 4 = -2 < 0$, and the same completion of squares gives $\lvert v_1 - 2i v_2 \rvert^2 - 2 \lvert v_2 \rvert^2$, so the form is Hermitian but no longer positive definite.

## Explanations

### L1 human

This form has complex numbers off the diagonal, but it is still Hermitian, because those two numbers are conjugates.
Its value on each nonzero vector is a positive real number, for example $5$ on the vector $(1, i)$.
So it measures lengths, and it is an inner product on $\mathbb{C}^2$, different from the standard one.

### L2 human

The test of a Hermitian form for positivity takes three steps.

1. Check that $M^* = M$.
2. Complete the squares: write $h(v, v)$ as a sum of terms $c \lvert \ell(v) \rvert^2$, where the $\ell$ are linear forms and the $c$ are real.
3. The form is positive definite when every $c$ is positive and the $\ell$ are linearly independent.

For the form above, step 2 gives $c = 1$ twice, with $\ell_1(v) = v_1 - i v_2$ and $\ell_2(v) = v_2$, which are independent.
The typical use is to build a new inner product on $\mathbb{C}^n$ from a matrix.
Watch out: the value $h(x, y) = 3i$ of step 4 is not real, and this is fine, since only the diagonal values $h(v, v)$ must be real.

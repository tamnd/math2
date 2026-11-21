---
tag: THMQA9AQZK
kind: example
name: For a complex vector x, x*x is the squared length
msc: ["15A99", "15A63"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0DXKE10PHF]
uses: [0EX045E2BP, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
---

## Example

We compute the [[conjugate transpose|0EX045E2BP]] of two vectors of $\mathbb{C}^2$ and the products that give lengths and inner products.
Let
$$x = \begin{pmatrix} 1 \\ i \end{pmatrix}, \qquad y = \begin{pmatrix} 3 + 4i \\ 2 \end{pmatrix}.$$

1. Conjugate each entry and write the column as a row: $x^* = \begin{pmatrix} 1 & -i \end{pmatrix}$ and $y^* = \begin{pmatrix} 3 - 4i & 2 \end{pmatrix}$.
2. Multiply the row $x^*$ by the column $x$:
$$x^* x = 1 \cdot 1 + (-i) \cdot i = 1 + 1 = 2.$$
Check: $|1|^2 + |i|^2 = 1 + 1 = 2$.
3. Do the same for $y$:
$$y^* y = (3 - 4i)(3 + 4i) + 2 \cdot 2 = (9 + 16) + 4 = 29.$$
Check: $|3 + 4i|^2 + |2|^2 = 25 + 4 = 29$.
4. In general, $x^* x = \sum_k \overline{x_k}\, x_k = \sum_k |x_k|^2$. Each term is a real number at least $0$, so the sum is real and nonnegative, and it is $0$ only when every $x_k = 0$.
5. Now mix the two vectors:
$$x^* y = 1 \cdot (3 + 4i) + (-i) \cdot 2 = 3 + 2i, \qquad y^* x = (3 - 4i) \cdot 1 + 2 \cdot i = 3 - 2i.$$
So $y^* x = \overline{x^* y}$.

## Remarks

Steps 2 to 4 show why the conjugate is there: it turns each product $\overline{x_k} x_k$ into a squared absolute value, so the length of $x$ is $\sqrt{x^* x} = \sqrt{2}$.
Step 5 shows the price: the complex inner product $\langle x, y \rangle = y^* x$ is conjugate-symmetric, $\langle y, x \rangle = \overline{\langle x, y \rangle}$, and not symmetric.
Some books put the conjugate on the other factor and define $\langle x, y \rangle = x^* y$, so read the convention first.
If you drop the conjugate, the length test fails, as [[the isotropic vector example|5AG0M5GR5T]] shows for the same $x$.
For real vectors the conjugates do nothing, and $x^* y$ is the dot product.

## Explanations

### L1 human

The size of a complex number $a + bi$ is found from $a^2 + b^2$, and you get that number by multiplying $a + bi$ by $a - bi$.
The conjugate transpose does this for every entry of a vector at once.
So multiplying the conjugate transpose of a vector by the vector gives the square of its length.
For $(3 + 4i, 2)$ this is $25 + 4 = 29$.

### L2 human

To find the angle-like quantity between two complex vectors, you compute $y^* x$ and compare it with the lengths.
Here $|y^* x| = |3 - 2i| = \sqrt{13}$, and the lengths are $\sqrt{2}$ and $\sqrt{29}$.
The Cauchy-Schwarz inequality says $|y^* x| \le \|x\| \, \|y\|$, and indeed $13 \le 2 \cdot 29 = 58$.
Watch out: $y^* x$ is a complex number, so you compare its absolute value, not the number itself, with the product of the lengths.

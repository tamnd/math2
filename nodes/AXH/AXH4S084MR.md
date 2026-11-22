---
tag: AXH4S084MR
kind: statement
role: proposition
name: Characterization of Hermitian forms
msc: ["15A63", "11E39"]
topics: [DYAK7YMK7B]
audience: ug1
about: [48P4A1CX85]
uses: [0W44K2VNBD, 8NJ7XY6F1S, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Hermitian form
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Statement

A sesquilinear form is fixed by its values $h(v, v)$, and it is Hermitian exactly when all these values are real.
Let $V$ be a vector space over $\mathbb{C}$, and let $h$ be a [[sesquilinear form|0W44K2VNBD]] on $V$, linear in the first slot and conjugate-linear in the second.

1. (Polarization.) For all $x, y \in V$,
$$4\, h(x, y) = \sum_{k = 0}^{3} i^k\, h(x + i^k y, x + i^k y).$$
2. The form $h$ is [[Hermitian|8NJ7XY6F1S]] if and only if $h(v, v) \in \mathbb{R}$ for every $v \in V$.
3. Let $V$ have finite dimension, with a basis $(e_1, \dots, e_n)$ and the matrix $M_{ij} = h(e_i, e_j)$. Then $h$ is Hermitian if and only if $M^* = M$, that is, $M$ is a [[Hermitian matrix|0EKZCX4K3P]].
4. In particular, if $h$ is Hermitian, then its matrices in all bases are Hermitian, and their determinants are real.

The [[proof|REG3P39586]] uses polarization to recover $h$ from its values on the diagonal.

## Remarks

### What it gives you

Part 3 turns the Hermitian condition into a finite check on the entries of a matrix.
For $M = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ the conjugate transpose is $\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix} \ne M$, so the form is not Hermitian.
Part 2 then promises a vector with a value that is not real, and $v = (1, 1)$ is one:
$$h(v, v) = 1 + i + i + 1 = 2 + 2i.$$

Part 2 also shortens the definition of a complex [[inner product|0NB0AWGJBW]].
A sesquilinear form with $h(v, v) > 0$ for all $v \ne 0$ has real diagonal values, so it is automatically Hermitian.

Part 1 has a consequence with no analogue for bilinear forms: a sesquilinear form with $h(v, v) = 0$ for all $v$ is the zero form.
The determinant form $x_1 y_2 - x_2 y_1$ on $\mathbb{R}^2$ shows the contrast, since it is bilinear, nonzero, and zero on every pair $(v, v)$.
Part 1 also splits every sesquilinear form as $h = h_1 + i h_2$ with Hermitian forms
$$h_1(x, y) = \tfrac12 \bigl(h(x, y) + \overline{h(y, x)}\bigr), \qquad h_2(x, y) = \tfrac{1}{2i} \bigl(h(x, y) - \overline{h(y, x)}\bigr).$$

### Why each hypothesis is needed

Sesquilinearity is needed in part 2.
A bilinear form $B$ on a complex space with all values $B(v, v)$ real has $B(v, v) = 0$ for all $v$.
The reason is that $B(cv, cv) = c^2 B(v, v)$, and with $c^2 = i$ this number is real only when $B(v, v) = 0$.
So the bilinear forms with real diagonal values are the alternating ones, such as $x_1 y_2 - x_2 y_1$, and they are not symmetric in general.

The complex field is needed as well.
Over $\mathbb{R}$, the form $B(x, y) = x_1 y_1 - x_1 y_2 + x_2 y_1$ has only real values, and $B(v, v) = v_1^2$ is the same as for the symmetric form $x_1 y_1$.
Yet $B(e_1, e_2) = -1$ and $B(e_2, e_1) = 1$, so the values $B(v, v)$ do not detect symmetry over $\mathbb{R}$.

Part 3 needs a basis, so it needs finite dimension, but parts 1 and 2 hold in every complex vector space.

### The converse

Parts 2 and 3 are equivalences, so their converses hold.
Part 3 also shows that one basis suffices.
If the matrix in one basis is Hermitian, then $h$ is Hermitian, and so its matrices in all other bases are Hermitian too.

### Generalizations

For a linear operator $T$ on a finite-dimensional complex inner product space, apply part 2 to $h(x, y) = \langle Tx, y \rangle$.
It says that $T$ is [[self-adjoint|0NEGN5CRSC]] exactly when $\langle Tv, v \rangle$ is real for every $v$.
In the language of the [[numerical range|XWXZ0DGW3Z]], $T$ is self-adjoint exactly when its numerical range lies in $\mathbb{R}$.
For a bilinear form over a field with $1 + 1 \ne 0$, the values $B(v, v)$ fix only the symmetric part $B(x, y) + B(y, x) = B(x + y, x + y) - B(x, x) - B(y, y)$.

## Explanations

### L1 human

A Hermitian form always gives real numbers when a vector is paired with itself.
The statement says that the converse holds too.
If a sesquilinear form gives a real number for every vector paired with itself, then it is Hermitian.
In coordinates, the test is that the matrix equals its conjugate transpose: mirror the entries across the diagonal and conjugate them.

### L2 human

Here is a typical use: which numbers $a$ and $b$ make the form with matrix $M = \begin{pmatrix} a & 2 + i \\ b & 1 \end{pmatrix}$ Hermitian?
By part 3 we need $M^* = M$.
The diagonal gives $\bar a = a$, so $a$ is real, and the corners give $b = \overline{2 + i} = 2 - i$.
For $a = 0$ and $v = (1, 1)$, check part 2:
$$h(v, v) = 0 + (2 + i) + (2 - i) + 1 = 5,$$
which is real, as it must be.
With $b = 2 + i$ in place of $2 - i$, the same vector gives $0 + (2 + i) + (2 + i) + 1 = 5 + 2i$.
Watch out: a complex symmetric matrix, $M^{\mathsf{T}} = M$, gives a Hermitian form only when its entries are real.

### L3 human

Part 1 says that a sesquilinear form is fixed by its Hermitian quadratic form $v \mapsto h(v, v)$.
Over $\mathbb{R}$ a bilinear form is fixed by its quadratic form only up to its alternating part, so the complex case is stronger.
The reason is the extra scalars: the four multipliers $1, i, -1, -i$ in the polarization identity separate $h(x, y)$ from $h(y, x)$, while over $\mathbb{R}$ only $\pm 1$ are available.

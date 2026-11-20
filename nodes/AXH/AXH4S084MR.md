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

Let $V$ be a vector space over $\C$, and let $h$ be a [[sesquilinear form|0W44K2VNBD]] on $V$, linear in the first slot.

1. (Polarization.) For all $x, y \in V$, $4\,h(x, y) = \sum_{k = 0}^{3} i^k\,h(x + i^k y, x + i^k y)$.
2. $h$ is [[Hermitian|8NJ7XY6F1S]] if and only if $h(v, v) \in \R$ for every $v \in V$.
3. Let $V$ have finite dimension, with a basis $(e_1, \dots, e_n)$ and the matrix $M_{ij} = h(e_i, e_j)$. Then $h$ is Hermitian if and only if $M^* = M$, that is, $M$ is a [[Hermitian matrix|0EKZCX4K3P]].
4. In particular, the matrices of a Hermitian form in all bases are Hermitian, and their determinants are real.

The [[proof|REG3P39586]] uses polarization to recover $h$ from its values on the diagonal.

## Remarks

### Why each hypothesis is needed

- Sesquilinearity is needed in part 2. The bilinear form $B(x, y) = x_1 y_1 - x_1 y_2 + x_2 y_1$ on $\R^2$ has real values everywhere but is not symmetric. Over $\C$, a bilinear form with real values on the diagonal has $B(v, v) = 0$ for all $v$, since $B(cv, cv) = c^2 B(v, v)$ and $c^2 = i$ for some $c$.
- The field must be $\C$, or another field with a conjugation. Over $\R$, a real-valued "sesquilinear" form is bilinear, and the values $B(v, v)$ do not detect symmetry, as the example above shows.

### Consequences

- A complex inner product is the same as a sesquilinear form with $h(v, v) > 0$ for all $v \neq 0$. The Hermitian condition follows from part 2.
- A form $h$ with $h(v, v) = 0$ for all $v$ is zero, by part 1. This is false for bilinear forms: the determinant form on $\R^2$ is nonzero but alternating.
- Each sesquilinear form is $h_1 + i h_2$ with Hermitian $h_1, h_2$, given by $h_1(x, y) = \frac12 \bigl(h(x, y) + \overline{h(y, x)}\bigr)$ and $h_2(x, y) = \frac{1}{2i} \bigl(h(x, y) - \overline{h(y, x)}\bigr)$.

### Converse

Parts 2 and 3 are equivalences, so their converses hold.
Part 3 shows that one basis suffices: if the matrix in one basis is Hermitian, then $h$ is Hermitian, and so are its matrices in all bases.

### Generalizations

For an operator $T$ on a complex inner product space, part 2 gives: $T$ is self-adjoint exactly when $\langle Tv, v \rangle$ is real for every $v$.

## Explanations

### L1 human

A Hermitian form always gives real numbers on the diagonal.
The statement says that the converse holds too: a sesquilinear form with real values on the diagonal is Hermitian.
In coordinates, the test is that the matrix equals its conjugate transpose.

### L2 human

We test $h(x, y) = x^T M \bar y$ on $\C^2$ with $M = \begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$.

1. $M^* = \begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix} \neq M$, so by part 3 $h$ is not Hermitian.
2. By part 2, some $v$ must give a value that is not real. Try $v = (1, 1)$: $h(v, v) = 1 + i + i + 1 = 2 + 2i$.
3. Indeed $2 + 2i \notin \R$.

The typical use is part 3, since it is a finite check of the matrix entries.
A trap: a complex symmetric matrix, $M^T = M$, does not give a Hermitian form unless its entries are real; this $M$ is symmetric.

### L3 human

Part 1 says that a sesquilinear form is fixed by its Hermitian quadratic form $v \mapsto h(v, v)$.
In operator theory this gives the numerical range: $T$ is self-adjoint exactly when its numerical range lies in $\R$.
For bilinear forms, the analogous statement needs $\operatorname{char} F \neq 2$ and gives only the symmetric part.

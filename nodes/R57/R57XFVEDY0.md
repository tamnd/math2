---
tag: R57XFVEDY0
kind: example
name: The classes of nondegenerate binary quadratic forms over F₃
msc: ["11E04", 11T99]
topics: [6TSCEW8QMK]
audience: grad
instance_of: [0RBQS1JJCR]
illustrates: [2HBR7137AD]
uses: [2HBR7137AD, VN9AG8JKYT, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

Let $F = \F_3 = \set{0, 1, 2}$, where $2 = -1$.
The nonzero squares are $1^2 = 1$ and $2^2 = 4 = 1$, so $1$ is the only nonzero square, and $2$ is not a square.
By [[the correspondence theorem|VN9AG8JKYT]], a binary quadratic form over $\F_3$ is a symmetric matrix $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$.

1. There are $3^3 = 27$ symmetric $2 \times 2$ matrices over $\F_3$.
2. The determinant $ac - b^2$ is $0$ for $9$ of them, by a direct count. So $18$ are nondegenerate.
3. Form I: $x^2 + y^2$, with matrix $I$ and determinant $1$, a square.
4. Form H: $2xy$, with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and determinant $-1 = 2$, a nonsquare.
5. By part 5 of [[the finite field theorem|2HBR7137AD]], every nondegenerate form is equivalent to exactly one of I and H. The square class of its determinant decides which one.
6. Form H is isotropic: $2xy = 0$ at $(1, 0)$. With $x = s + t$ and $y = s - t$, $2xy = 2s^2 - 2t^2 = t^2 - s^2$, since $2 = -1$. So H is equivalent to $x^2 - y^2$.
7. Form I is not isotropic: its values at nonzero vectors are $1$ at $(1, 0)$, $(0, 1)$, $(2, 0)$, $(0, 2)$, and $2$ at $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$.
8. Step 7 shows again that I and H are not equivalent, since equivalence keeps isotropy.
9. Example of part 4 of the theorem: $\langle 2, 2 \rangle = 2x^2 + 2y^2$ has determinant $4 = 1$, so it is equivalent to I. Explicitly, $v_1 = (1, 1)$ and $v_2 = (1, 2)$ give $Q(v_1) = 4 = 1$, $Q(v_2) = 10 = 1$ and $B(v_1, v_2) = 2 + 4 = 6 = 0$.

## Remarks

The group $GL_2(\F_3)$ has $(9 - 1)(9 - 3) = 48$ elements, and it acts on the $18$ nondegenerate matrices by $A \mapsto P^T A P$.
A direct count gives two orbits.
The class of I has $6$ matrices, with determinant $1$, and the class of H has $12$, with determinant $2$.
The class of I is $\set{\pm I, \pm \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \pm \begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}}$, with signs taken modulo $3$.
Over $\F_5$, where $-1 = 4$ is a square, the roles change: $x^2 + y^2$ is isotropic, at $(1, 2)$, and it is equivalent to $2xy$.
The two classes have $60$ and $40$ of the $100$ nondegenerate matrices.

## Explanations

### L1 human

Over $\F_3$ there are only two kinds of nondegenerate forms in two variables.
One kind, like $x^2 + y^2$, is never zero except at $(0, 0)$.
The other kind, like $2xy$, is zero on a line.
The determinant tells which kind: $1$ for the first and $2$ for the second.

### L2 human

To classify a binary form over $\F_q$ with $q$ odd, compute $ac - b^2$, and test whether it is a square.
A trap: over $\F_3$ the form $x^2 + y^2$ is anisotropic, but over $\F_5$ it is isotropic; the answer depends on whether $-1$ is a square.

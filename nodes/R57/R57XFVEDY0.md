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

Over the field $\mathbb{F}_3 = \{ 0, 1, 2 \}$, where $2 = -1$, the nondegenerate [[quadratic forms|0RBQS1JJCR]] in two variables fall into exactly two classes, represented by $x^2 + y^2$ and $2xy$.
Since $3$ is odd, [[the correspondence theorem|VN9AG8JKYT]] lets us describe a binary form by its symmetric matrix $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, which stands for $a x^2 + 2b xy + c y^2$.
We check the claim in steps.

1. The squares. We have $1^2 = 1$ and $2^2 = 4 = 1$, so $1$ is the only nonzero square and $2$ is a nonsquare.
2. The count of matrices. Each of $a$, $b$, $c$ has $3$ choices, so there are $3^3 = 27$ symmetric matrices.
3. The degenerate ones. The determinant $ac - b^2$ is $0$ in $5$ cases with $b = 0$, namely when $a = 0$ or $c = 0$. It is also $0$ in $2$ cases for each $b \ne 0$, namely $a = c = 1$ and $a = c = 2$. That makes $5 + 2 + 2 = 9$, so $27 - 9 = 18$ matrices are nondegenerate.
4. The first representative. The form $x^2 + y^2$ has matrix $I$ and determinant $1$, a square.
5. The second representative. The form $2xy$ has matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and determinant $-1 = 2$, a nonsquare.
6. The classification. By part 5 of [[the finite field theorem|2HBR7137AD]], every nondegenerate binary form over $\mathbb{F}_3$ is equivalent to exactly one of the two, and the square class of its determinant decides which.
7. The second form is isotropic, since $2xy = 0$ at $(1, 0)$. The substitution $x = s + t$, $y = s - t$ gives $2xy = 2s^2 - 2t^2 = t^2 - s^2$, because $2 = -1$. So $2xy$ is equivalent to $x^2 - y^2$.
8. The first form is not isotropic. At the eight nonzero vectors it takes the value $1$ at $(1, 0)$, $(2, 0)$, $(0, 1)$, $(0, 2)$, and the value $2$ at $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$.
9. A second proof of step 6. An equivalence carries zeros to zeros, so step 7 and step 8 show again that the two forms are not equivalent.
10. A use of part 4 of the theorem. The form $2x^2 + 2y^2$ has determinant $4 = 1$, so it is equivalent to $x^2 + y^2$. Explicitly, $v_1 = (1, 1)$ and $v_2 = (1, 2)$ give $Q(v_1) = 4 = 1$, $Q(v_2) = 2 + 8 = 10 = 1$ and $B(v_1, v_2) = 2 \cdot 1 \cdot 1 + 2 \cdot 1 \cdot 2 = 6 = 0$.

## Remarks

### The two orbits

The group $GL_2(\mathbb{F}_3)$ has $(9 - 1)(9 - 3) = 48$ elements, and it acts on the $18$ nondegenerate matrices by $A \mapsto P^{\mathsf{T}} A P$.
The theorem says that there are two orbits, and the determinant tells them apart.
Count the matrices with determinant $1$: with $b = 0$ we need $ac = 1$, which gives $2$ cases, and with $b = \pm 1$ we need $ac = 2$, which gives $2$ cases each.
So the class of $x^2 + y^2$ has $6$ matrices:
$$I, \quad 2I, \quad \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \quad \begin{pmatrix} 2 & 2 \\ 2 & 1 \end{pmatrix}, \quad \begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}, \quad \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.$$
Check: the third one has determinant $2 - 1 = 1$, and the fourth has $2 - 4 = -2 = 1$.
The class of $2xy$ has the other $18 - 6 = 12$ matrices.

### What changes over the field with five elements

Over $\mathbb{F}_5$ the number $-1 = 4 = 2^2$ is a square, and the roles of the forms change.
Now $x^2 + y^2$ is isotropic, since $1^2 + 2^2 = 5 = 0$, and it is equivalent to $2xy$, because both determinants $1$ and $-1 = 4$ are squares.
The anisotropic class is now represented by $x^2 + 2y^2$, with the nonsquare determinant $2$.
Of the $125$ symmetric matrices, $25$ are degenerate, and the two classes have $60$ and $40$ of the other $100$.
So the question "is $x^2 + y^2$ isotropic?" has the answer "exactly when $-1$ is a square", that is, when $q \equiv 1 \pmod 4$.

## Explanations

### L1 human

Over the field with three elements there are only two kinds of nondegenerate forms in two variables.
One kind, like $x^2 + y^2$, is never zero except at $(0, 0)$.
The other kind, like $2xy$, is zero along a whole line, for example at every point $(x, 0)$.
The determinant tells you the kind: $1$ for the first and $2$ for the second.

### L2 human

Here is a typical use: classify $Q = x^2 + xy + y^2$ over $\mathbb{F}_3$.
In $\mathbb{F}_3$ we have $\tfrac12 = 2$, because $2 \cdot 2 = 4 = 1$.
So the cross term $xy$ gives off-diagonal entries $\tfrac12 = 2$, and the matrix is
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}, \qquad \det A = 1 - 4 = -3 = 0.$$
So $Q$ is degenerate, and the classification of nondegenerate forms does not apply to it.
Check: $Q = (x + 2y)^2 = x^2 + 4xy + 4y^2 = x^2 + xy + y^2$ in $\mathbb{F}_3$, a single square of rank $1$.
Watch out: the same polynomial is nondegenerate over $\mathbb{Q}$, so a form can change type when you reduce it modulo a prime.

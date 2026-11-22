---
tag: RZMEYX1YJT
kind: example
name: A degenerate symmetric bilinear form on the rational 3-space and its radical
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [0AXZNE5XNH]
not_instance_of:
  - target: 01NHFZF2SK
    note: the matrix has determinant 0, and the nonzero vector (1, 1, -1) is orthogonal to every vector
illustrates: [3ND2FNJ38Y]
uses: [0P24YW565F, 0KAN330PAH, 3ND2FNJ38Y, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
---

## Example

On $\mathbb{Q}^3$ let $B(x, y) = x^{\mathsf{T}} A y$ with
$$A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix}.$$
The matrix is symmetric, so $B$ is [[symmetric|0744CN4MDA]], and its left and right radicals are the same subspace, the radical $\operatorname{rad} B$.
We show that $B$ is degenerate, find its radical, and split it off.

1. The third row of $A$ is the sum of the first two rows:
$$(1, 1, 2) + (1, 2, 3) = (2, 3, 5).$$
So the rows are dependent and $\det A = 0$, and by the [[criteria for nondegeneracy|3ND2FNJ38Y]] the form is degenerate.
2. The first two rows are not proportional, so $\operatorname{rank} A = 2$, and the radical has dimension $3 - 2 = 1$.
3. The radical is the null space of $A$. Subtract row $1$ from row $2$ and drop row $3$, which depends on the others:
$$x_1 + x_2 + 2x_3 = 0, \qquad x_2 + x_3 = 0.$$
4. Put $x_3 = -1$. Then $x_2 = 1$ and $x_1 = -1 + 2 = 1$, so the radical is the line spanned by $r = (1, 1, -1)$.
Check:
$$A r = (1 + 1 - 2,\ 1 + 2 - 3,\ 2 + 3 - 5) = (0, 0, 0).$$
5. So $B(y, r) = y^{\mathsf{T}} A r = 0$ for every $y$, and by symmetry $B(r, y) = 0$ too, although $r \ne 0$.
6. On the plane $U = \operatorname{span}(e_1, e_2)$ the form has the matrix $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, with determinant $2 - 1 = 1 \ne 0$, so $B$ restricted to $U$ is nondegenerate.
7. The vector $r$ has third coordinate $-1 \ne 0$, so $r \notin U$, and $U \cap \operatorname{rad} B = 0$. Since $2 + 1 = 3$, we get $\mathbb{Q}^3 = U \oplus \operatorname{rad} B$.

## Remarks

The example shows the general shape of a degenerate form in finite dimension: a nondegenerate part on a complement, plus a radical that the form cannot see.
The rank $2$ is the dimension of the quotient $\mathbb{Q}^3 / \operatorname{rad} B$, and step 6 gives the matrix of the induced nondegenerate form on the quotient, in the basis of the classes of $e_1$ and $e_2$.

Over $\mathbb{R}$ the same matrix is positive semidefinite.
Write $v = u + t r$ with $u \in U$; then $B(v, v) = B(u, u)$, and the matrix of step 6 is positive definite, since its leading minors are $1$ and $1$.
So for this form $B(v, v) = 0$ happens only on the radical.
That is special to semidefinite forms: the form $x_1 y_1 - x_2 y_2$ has $B(v, v) = 0$ for $v = (1, 1)$, but its radical is $0$.

What changes if we change one entry?
If the entry $5$ in place $(3, 3)$ becomes $6$, the matrix stays symmetric, but the third row is no longer the sum of the first two.
The determinant grows by the minor $\det \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = 1$, so it becomes $1$, and the form becomes nondegenerate.

## Explanations

### L1 human

This form looks harmless, but one direction is invisible to it.
The arrow $(1, 1, -1)$ gives the value $0$ with every arrow.
We find it by solving the equations that the table of the form gives.
On the plane of the first two coordinate arrows, the form sees everything.

### L2 human

Here is the general recipe to find the radical of a form $x^{\mathsf{T}} A y$, used on the matrix above.

1. Test $\det A$, or compute $\operatorname{rank} A$; here $\det A = 0$ and the rank is $2$.
2. Solve $A y = 0$ for the right radical and $A^{\mathsf{T}} x = 0$ for the left radical; for a symmetric $A$ the two systems are the same.
3. Check each solution by multiplying by $A$, as in step 4.

The typical use is to remove the radical and to work with the nondegenerate form on a complement or on the quotient.
Watch out: the diagonal values $B(e_1, e_1) = 1$, $B(e_2, e_2) = 2$ and $B(e_3, e_3) = 5$ are all nonzero, and still the form is degenerate; only the determinant or the radical decides.

---
tag: ~eadb0c41
kind: example
name: Completing squares in a quadratic form in three variables
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR]
illustrates: [0Z3FEWZ8HA]
uses: [0Z3FEWZ8HA, XNCV97HTZ8, ~00a7a300]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

Let $Q(x, y, z) = x^2 + 4xy + 2xz + 5y^2 + 8yz + 2z^2$ on $\R^3$.
We [[diagonalize|0Z3FEWZ8HA]] it by [[completing squares|XNCV97HTZ8]].

1. The terms with $x$ are $x^2 + 4xy + 2xz = (x + 2y + z)^2 - (2y + z)^2$.
2. Since $(2y + z)^2 = 4y^2 + 4yz + z^2$, we get $Q = (x + 2y + z)^2 + y^2 + 4yz + z^2$.
3. The terms with $y$ that are left are $y^2 + 4yz = (y + 2z)^2 - 4z^2$.
4. So $Q = (x + 2y + z)^2 + (y + 2z)^2 - 3z^2$.
5. Put $u = x + 2y + z$, $v = y + 2z$, $w = z$. Then $Q = u^2 + v^2 - 3w^2$.
6. The change is invertible: back substitution gives $z = w$, $y = v - 2w$ and $x = u - 2v + 3w$.
7. Check at three vectors. At $(1, 0, 0)$: $Q = 1$, and $(u, v, w) = (1, 0, 0)$ gives $1$.
8. At $(0, 1, 0)$: $Q = 5$, and $(u, v, w) = (2, 1, 0)$ gives $4 + 1 = 5$.
9. At $(0, 0, 1)$: $Q = 2$, and $(u, v, w) = (1, 2, 1)$ gives $1 + 4 - 3 = 2$.

In matrices: by [[the correspondence theorem|~00a7a300]], the symmetric matrix of $Q$ is
$$A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 4 \\ 1 & 4 & 2 \end{pmatrix}.$$
Step 6 says $x = P (u, v, w)^T$ with
$$P = \begin{pmatrix} 1 & -2 & 3 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}, \qquad P^T A P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -3 \end{pmatrix}.$$
The columns of $P$ are the new basis vectors $(1, 0, 0)$, $(-2, 1, 0)$ and $(3, -2, 1)$.

## Remarks

The diagonal form has two positive and one negative coefficient, so the [[signature|07EZA80NEH]] of $Q$ is $(2, 1, 0)$.
As a check, $\det A = -3$ and $\det(P^T A P) = -3$, since $\det P = 1$.
The diagonal entries $1, 1, -3$ are not the eigenvalues of $A$.
The eigenvalues are the roots of $\lambda^3 - 8\lambda^2 - 4\lambda + 3$; there are two positive roots and one negative root, as [[Sylvester's law|0WFED3K3DQ]] predicts.

## Explanations

### L1 human

We remove the cross terms one variable at a time.
First we put all terms with $x$ in one square, then all terms with $y$ that are left.
At the end only a multiple of $z^2$ is left.

### L2 human

The typical use is to find the signature of a form without computing eigenvalues.
Here the result $u^2 + v^2 - 3w^2$ shows that $Q$ is indefinite: $Q > 0$ at $(1, 0, 0)$, and $Q = -3$ at the vector with $(u, v, w) = (0, 0, 1)$, which is $(3, -2, 1)$.
Check: $Q(3, -2, 1) = 9 - 24 + 6 + 20 - 16 + 2 = -3$.
A trap: write the new variables as functions of the old ones, and invert to get the new basis.
The rows of the first matrix are not the basis vectors.

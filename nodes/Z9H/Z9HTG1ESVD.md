---
tag: Z9HTG1ESVD
kind: example
name: The inertia of a 3 × 3 symmetric matrix computed in two ways
msc: [15A63, 15A18]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [07EZA80NEH]
illustrates: [0WFED3K3DQ]
uses: [0KQZYGEJTF, 0WFED3K3DQ, 0Z3FEWZ8HA, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia
    locator: Statement in terms of eigenvalues
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 0 \end{pmatrix}, \qquad Q(x, y, z) = x^2 + 2xy + 2xz + 4yz.$$
$A$ is the symmetric matrix of $Q$: each cross coefficient is split into two equal off-diagonal entries.
We find the [[signature|0KQZYGEJTF]] $(p, q, r)$ of $Q$ first from the eigenvalues of $A$, and then by completing squares.

1. $A (1, 1, 1)^{\mathsf{T}} = (3, 3, 3)^{\mathsf{T}}$, so $3$ is an eigenvalue with [[eigenvector|0B5H4208Z9]] $(1, 1, 1)$.
2. $A (0, 1, -1)^{\mathsf{T}} = (0, -2, 2)^{\mathsf{T}}$, so $-2$ is an eigenvalue with eigenvector $(0, 1, -1)$.
3. $A (-2, 1, 1)^{\mathsf{T}} = (0, 0, 0)^{\mathsf{T}}$, so $0$ is an eigenvalue with eigenvector $(-2, 1, 1)$.
4. A $3 \times 3$ matrix has at most three distinct eigenvalues, so $3$, $-2$ and $0$ are all of them.
   Check: their sum is $1 = \operatorname{tr} A$, and their product is $0 = \det A$.
5. One positive, one negative and one zero eigenvalue give the signature $(1, 1, 1)$.
6. Now complete squares.
   All terms with $x$ fit in one square, since $(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2xz + 2yz$.
7. What is left is $Q - (x + y + z)^2 = -y^2 - z^2 + 2yz = -(y - z)^2$.
8. With $u = x + y + z$, $v = y - z$ and $w = z$, we get $Q = u^2 - v^2 + 0 \cdot w^2$.
9. Back substitution gives $z = w$, $y = v + w$ and $x = u - v - 2w$.
   So $P^{\mathsf{T}} A P = \operatorname{diag}(1, -1, 0)$ for
   $$P = \begin{pmatrix} 1 & -1 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix},$$
   whose columns are the new basis vectors.
10. Check on the columns: $Q(1, 0, 0) = 1$, $Q(-1, 1, 0) = 1 - 2 = -1$ and $Q(-2, 1, 1) = 4 - 4 - 4 + 4 = 0$.
11. One plus sign, one minus sign and one zero coefficient give the signature $(1, 1, 1)$ again.

## Remarks

In an orthonormal basis of eigenvectors the form is $3u'^2 - 2v'^2 + 0 \cdot w'^2$, and by completing squares it is $u^2 - v^2 + 0 \cdot w^2$.
The coefficients differ, but the signs agree, as [[Sylvester's law of inertia|0WFED3K3DQ]] predicts.
The rank is $p + q = 2$, which agrees with $\det A = 0$ and with the [[diagonalization|0Z3FEWZ8HA]] having one zero coefficient.

The third column of $P$ is $(-2, 1, 1)$, the eigenvector for $0$.
This is no accident: both computations find the radical of the form, the line of vectors $v$ with $Av = 0$.

Watch out: the diagonal entries $1, -1, 0$ of $P^{\mathsf{T}} A P$ are not eigenvalues of $A$.
Only their signs agree with the eigenvalues $3, -2, 0$.
The diagonal of $A$ itself, $1, 0, 0$, shows neither the eigenvalues nor the signs.

Try it: find the signature of $x^2 + 2xy + 2xz + 2yz$.
Here $(x + y + z)^2$ leaves $-y^2 - z^2$, so $Q = u^2 - y^2 - z^2$ and the signature is $(1, 2, 0)$.

## Explanations

### L1 human

The eigenvalue method needs the roots of a polynomial of degree $3$, which can be hard to find.
Here we guessed three eigenvectors and checked them.
Completing squares needs only addition and multiplication.
Both methods give one positive sign, one negative sign and one zero.

### L2 human

By hand, completing squares is faster, and it works for every symmetric matrix.
On a computer, eigenvalues are better, because the algorithms are stable.
The eigenvalue method also gives more: the eigenvalues fix the form up to an orthogonal change of basis, while completing squares fixes it only up to a general change of basis.

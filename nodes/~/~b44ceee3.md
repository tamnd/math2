---
tag: ~b44ceee3
kind: example
name: A symplectic basis for a nondegenerate alternating 4 x 4 matrix
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [0DGDS5XY84, 01NHFZF2SK, PQ7JJY0VPH]
illustrates: [~a52a9f11]
uses: [~a52a9f11, 05Q4JD6XEH, 0SPYAGE7T0, M0JEPXXWQM]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
---

## Example

On $\Q^4$ let $B(x, y) = x^T A y$ with
$$A = \begin{pmatrix} 0 & 1 & 2 & 3 \\ -1 & 0 & 4 & 5 \\ -2 & -4 & 0 & 6 \\ -3 & -5 & -6 & 0 \end{pmatrix}.$$
$A^T = -A$ and the diagonal is zero, so $B$ is alternating.
We follow the [[proof of the classification|~a52a9f11]].

1. $B(e_1, e_2) = a_{12} = 1$. So we take $u_1 = e_1$ and $v_1 = e_2$, and $H = \operatorname{span}(e_1, e_2)$.
2. The [[orthogonal complement|05Q4JD6XEH]] $H^\perp$ is the set of $x$ with $B(e_1, x) = 0$ and $B(e_2, x) = 0$, that is, with (row $1$ of $A$) $\cdot\, x = 0$ and (row $2$ of $A$) $\cdot\, x = 0$.
3. These equations are $x_2 + 2x_3 + 3x_4 = 0$ and $-x_1 + 4x_3 + 5x_4 = 0$.
4. With $(x_3, x_4) = (1, 0)$ we get $w_3 = (4, -2, 1, 0)$. With $(x_3, x_4) = (0, 1)$ we get $w_4 = (5, -3, 0, 1)$.
5. $A w_4 = (0 - 3 + 0 + 3, -5 + 0 + 0 + 5, -10 + 12 + 0 + 6, -15 + 15 + 0 + 0) = (0, 0, 8, 0)$.
6. So $B(w_3, w_4) = w_3^T A w_4 = 1 \cdot 8 = 8$. Put $u_2 = w_3$ and $v_2 = \frac18 w_4$, so $B(u_2, v_2) = 1$.
7. Let $P$ have the columns $e_1, e_2, w_3, \frac18 w_4$. By steps 1 to 6 and skew-symmetry, $P^T A P = J \oplus J$ with $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
8. A check of one entry: $B(e_1, w_3) = 0 \cdot 4 + 1 \cdot (-2) + 2 \cdot 1 + 3 \cdot 0 = 0$.
9. $P$ is upper triangular with diagonal $1, 1, 1, \frac18$, so $\det P = \frac18$.
10. By the [[change of basis rule|0SPYAGE7T0]], $1 = \det(J \oplus J) = (\det P)^2 \det A$, so $\det A = 64 = 8^2$.

## Remarks

The value $8$ in step 6 is the Pfaffian of $A$, computed in [[the example on the Pfaffian of this matrix|M0JEPXXWQM]]: $a_{12} a_{34} - a_{13} a_{24} + a_{14} a_{23} = 6 - 10 + 12 = 8$.
This is no accident: $\operatorname{pf}(P^T A P) = \det P \cdot \operatorname{pf}(A)$, and $\operatorname{pf}(J \oplus J) = 1$, so $\operatorname{pf}(A) = 8$.
The form is nondegenerate, since $\det A = 64 \neq 0$, so $(\Q^4, B)$ is a symplectic vector space.
In the order $(u_1, u_2, v_1, v_2)$ the matrix becomes $\begin{pmatrix} 0 & I_2 \\ -I_2 & 0 \end{pmatrix}$.

## Explanations

### L1 human

We start from an alternating $4 \times 4$ matrix with many entries.
We find two pairs of vectors such that each pair gives $1$ and different pairs give $0$.
In the basis of these four vectors, the matrix has only the entries $1$ and $-1$ in two small blocks.

### L2 human

The recipe for a symplectic basis is the following.

1. Find $u, z$ with $B(u, z) \neq 0$, and scale $z$ to $v$ with $B(u, v) = 1$.
2. Solve $B(u, x) = B(v, x) = 0$ to get $H^\perp$.
3. Repeat on $H^\perp$.

The typical use is to bring an alternating matrix to standard form and to read off its rank.
A trap: the vectors $w_3, w_4$ of step 4 are orthogonal to $H$, but $B(w_3, w_4) = 8$, so $w_4$ must be scaled by $\frac18$ before the pair is symplectic.

---
tag: V3AVVJV8HC
kind: example
name: Witt decomposition of x1 y1 + x2 y2 - x3 y3
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
instance_of: [0AXZNE5XNH, 01NHFZF2SK, MZHFGPV1YT]
illustrates: [BPMRSPB6GD]
uses: [BPMRSPB6GD, SN50886T80, 1X5PZSK44P, 0SPYAGE7T0]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's decomposition theorem
---

## Example

On $\mathbb{Q}^3$ let $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$, the [[symmetric bilinear form|0AXZNE5XNH]] with matrix $A = \operatorname{diag}(1, 1, -1)$.
Since $\det A = -1 \neq 0$, the form is [[nondegenerate|01NHFZF2SK]].
We compute its [[Witt decomposition|BPMRSPB6GD]].

1. An isotropic vector. The vector $u = e_1 + e_3 = (1, 0, 1)$ has $B(u, u) = 1 - 1 = 0$, so $u$ is [[isotropic|MZHFGPV1YT]].
2. A vector that sees it. The vector $z = e_1$ has $B(u, z) = 1$ and $B(z, z) = 1$.
3. The partner. As in the [[hyperbolic plane statement|SN50886T80]], put
$$v = z - \frac{B(z, z)}{2} u = (1, 0, 0) - \tfrac{1}{2}(1, 0, 1) = \left( \tfrac{1}{2}, 0, -\tfrac{1}{2} \right).$$
4. The hyperbolic pair. We get $B(v, v) = \tfrac{1}{4} - \tfrac{1}{4} = 0$ and $B(u, v) = \tfrac{1}{2} + \tfrac{1}{2} = 1$. So $(u, v)$ is a hyperbolic pair, and $H = \operatorname{span}(u, v)$ is the [[hyperbolic plane|1X5PZSK44P]] $x_2 = 0$.
5. The complement. $H^\perp$ is the set of $x$ with $B(u, x) = x_1 - x_3 = 0$ and $B(v, x) = \tfrac{1}{2} x_1 + \tfrac{1}{2} x_3 = 0$. These give $x_1 = x_3 = 0$, so $H^\perp = \operatorname{span}(e_2)$.
6. The anisotropic part. Since $B(e_2, e_2) = 1 \neq 0$, the line $H^\perp$ is anisotropic.
7. The result. $\mathbb{Q}^3 = H \perp \operatorname{span}(e_2)$, with Witt index $m = 1$ and anisotropic part $\langle 1 \rangle$, the line with the form $xy$.
8. The matrix. Let $P$ have the columns $u, v, e_2$. The entries of $P^{\mathsf{T}} A P$ are the values of $B$ on pairs of these columns, so the [[change of basis rule|0SPYAGE7T0]] gives
$$P = \begin{pmatrix} 1 & \tfrac{1}{2} & 0 \\ 0 & 0 & 1 \\ 1 & -\tfrac{1}{2} & 0 \end{pmatrix}, \qquad P^{\mathsf{T}} A P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check: expanding along the last column gives $\det P = -1 \cdot (1 \cdot (-\tfrac{1}{2}) - \tfrac{1}{2} \cdot 1) = 1$, and $\det(P^{\mathsf{T}} A P) = -1 = (\det P)^2 \det A$.
9. The index. The line $\operatorname{span}(u)$ is a maximal totally isotropic subspace. No plane is totally isotropic, since a totally isotropic $W$ has $2 \dim W \leq 3$.

## Remarks

The decomposition is not unique as a set of subspaces.
The isotropic vector $u' = e_2 + e_3$ gives the hyperbolic plane $H' = \operatorname{span}(e_2, e_3)$ with $H'^\perp = \operatorname{span}(e_1)$.
So $H' \neq H$, but both anisotropic parts are $\langle 1 \rangle$, as the uniqueness part of the theorem says.

The anisotropic part $\langle 1 \rangle$ cannot be replaced by $\langle -1 \rangle$.
The form $H \perp \langle -1 \rangle$ has determinant $(-1)(-1) = 1$, while $A$ has determinant $-1$, and the determinant up to nonzero squares is an invariant of congruence.
Over $\mathbb{R}$ the answer is the same: the form has $2$ positive and $1$ negative square, and the Witt index is $\min(2, 1) = 1$.
If you change the sign of the second term, to $x_1 y_1 - x_2 y_2 - x_3 y_3$, the decomposition becomes $H \perp \langle -1 \rangle$, still with index $1$.

## Explanations

### L1 human

The form $x_1^2 + x_2^2 - x_3^2$ is zero on a whole cone of vectors, such as $(1, 0, 1)$ and $(3, 4, 5)$.
One such vector and a suitable partner span a hyperbolic plane.
What remains is the line of $e_2$, where the form is $x_2^2$ and only $0$ gives zero.
So this form is one hyperbolic plane plus one anisotropic line.

### L2 human

You can test the new coordinates on the isotropic vector $x = (3, 4, 5)$, since $9 + 16 - 25 = 0$.
Write $x = a u + b v + c e_2 = \left( a + \tfrac{b}{2}, c, a - \tfrac{b}{2} \right)$.
Then $c = 4$, $a + \tfrac{b}{2} = 3$ and $a - \tfrac{b}{2} = 5$, so $a = 4$ and $b = -2$.
In the new basis the form is $B(x, x) = 2ab + c^2$, which gives
$$2 \cdot 4 \cdot (-2) + 4^2 = -16 + 16 = 0,$$
in agreement with the old coordinates.
Watch out: $(u, v)$ is not an orthogonal basis of $H$, so $B(x, x)$ is $2ab + c^2$, not $a^2 + b^2 + c^2$.

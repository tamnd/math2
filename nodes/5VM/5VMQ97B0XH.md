---
tag: 5VMQ97B0XH
kind: example
name: The isotropic vectors of the sum of three squares over the field with three elements
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
instance_of: [MZHFGPV1YT]
uses: [0744CN4MDA, 05Q4JD6XEH]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Field theory
---

## Example

On $V = \mathbb{F}_3^3$ let $B$ be the dot product, the [[symmetric bilinear form|0744CN4MDA]]
$$B(x, y) = x_1 y_1 + x_2 y_2 + x_3 y_3.$$
Its matrix is the identity, which has determinant $1$, so $B$ is nondegenerate.
We find every [[isotropic vector|MZHFGPV1YT]] and every totally isotropic subspace.
All arithmetic is modulo $3$.

1. The squares in $\mathbb{F}_3 = \{0, 1, 2\}$ are $0^2 = 0$, $1^2 = 1$ and $2^2 = 4 = 1$. So $v_i^2$ is $0$ when $v_i = 0$, and $1$ otherwise.
2. So $B(v, v) = v_1^2 + v_2^2 + v_3^2$ is the number $k$ of nonzero coordinates of $v$, read modulo $3$.
3. The number $k$ is $0$, $1$, $2$ or $3$, and it is $0$ modulo $3$ exactly when $k = 0$ or $k = 3$. The case $k = 0$ is the zero vector.
4. So the isotropic vectors are the vectors with all three coordinates nonzero. Each coordinate is $1$ or $2$, so there are $2^3 = 8$ of them.
5. A vector and its negative span the same line, so the $8$ vectors lie on $4$ lines through $0$, spanned by $(1, 1, 1)$, $(1, 1, 2)$, $(1, 2, 1)$ and $(2, 1, 1)$. Check: $(1, 1, 2)$ gives $1 + 1 + 4 = 6 = 0$.
6. Each of these lines is totally isotropic, since $B(su, tu) = st\, B(u, u) = 0$.
7. No plane is totally isotropic. Since $B$ is nondegenerate, a totally isotropic subspace $W$ has $2 \dim W \leq 3$, by the bound from the [[orthogonal complement|05Q4JD6XEH]], so $\dim W \leq 1$.
8. For a direct check, two of the lines pair to a nonzero value: $B((1, 1, 1), (1, 1, 2)) = 1 + 1 + 2 = 4 = 1$.

So the largest totally isotropic subspaces are the $4$ isotropic lines, and the Witt index of the form is $1$.

## Remarks

The example shows that isotropy depends on the field.
Over $\mathbb{Q}$ or $\mathbb{R}$ the same formula is anisotropic, because a sum of three real squares is $0$ only at $0$.
Over $\mathbb{F}_3$ the relation $1 + 1 + 1 = 0$ produces isotropic vectors.
This is a case of a general rule: by the Chevalley-Warning theorem, every symmetric form over a finite field in three or more variables is isotropic.

Compare it with two squares over the same field.
The form $x_1 y_1 + x_2 y_2$ on $\mathbb{F}_3^2$ has [[no isotropic vector|DH7M9YDXSS]], since a vector with $k = 1$ or $k = 2$ nonzero coordinates gives $1$ or $2$.
The third coordinate is what makes $k = 3$ possible.

The isotropic vector $u = (1, 1, 1)$ lies in a hyperbolic plane.
Take $z = (1, 0, 0)$, so $B(u, z) = 1$ and $B(z, z) = 1$, and correct $z$ by a multiple of $u$, using $\tfrac{1}{2} = 2$ in $\mathbb{F}_3$:
$$v = z - \tfrac{1}{2} B(z, z)\, u = (1, 0, 0) - 2(1, 1, 1) = (2, 1, 1).$$
Check: $B(v, v) = 4 + 1 + 1 = 6 = 0$ and $B(u, v) = 2 + 1 + 1 = 4 = 1$.
So $(u, v)$ is a hyperbolic pair.

## Explanations

### L1 human

In the field with three elements, $1 + 1 + 1 = 0$.
So the vector $(1, 1, 1)$ has dot product $0$ with itself, although it is not the zero vector.
The same happens for every vector whose three entries are all nonzero, and there are exactly eight such vectors.
Over the real numbers, the same dot product has no such vector.

### L2 human

The method used above works for any diagonal form $\sum_i a_i x_i y_i$ over a small finite field of odd order.
First list the squares of the field.
Then find the choices of squares $s_i$ with $\sum_i a_i s_i = 0$.
Last, count the vectors that give these squares: a coordinate with $s_i = 0$ has one choice, and a coordinate with $s_i \neq 0$ has two square roots.
For the form here, the only choice with not all $s_i$ zero is $s_1 = s_2 = s_3 = 1$, which gives $2 \cdot 2 \cdot 2 = 8$ vectors.
Watch out: reduce every square in the field, so $2^2 = 1$ in $\mathbb{F}_3$, not $4$.

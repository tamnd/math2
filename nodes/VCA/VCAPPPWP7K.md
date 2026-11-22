---
tag: VCAPPPWP7K
kind: proof
name: Proof that each isotropic vector lies in a hyperbolic plane
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
proves: SN50886T80
methods: [01XM7JEKHY, 0WCP0PVET6]
uses: [0KAN330PAH, 3ND2FNJ38Y, 0744CN4MDA, 08ZQAKBKHF, SX9CD5NEPD, M2JH84VEY9, 0P24YW565F, 0WGAXEK99E]
sources:
  - url: https://en.wikipedia.org/wiki/Isotropic_quadratic_form
    locator: Hyperbolic plane
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

We use nondegeneracy to find a vector $z$ with $B(u, z) = 1$, correct $z$ in the symmetric case, and then split the plane off with the dimension statement for orthogonal complements.
Let $u \in V$ with $u \neq 0$ and $B(u, u) = 0$.

The first vector.

1. The form $B$ is [[nondegenerate|0KAN330PAH]] and $u \neq 0$, so $u$ is not in the left radical. Hence there is $z' \in V$ with $c = B(u, z') \neq 0$.
2. Put $z = c^{-1} z'$. Linearity in the second slot gives $B(u, z) = c^{-1} c = 1$.

Part 1, for a [[symmetric|0744CN4MDA]] form $B$ with $1 + 1 \neq 0$ in $F$.

3. Since $2$ is invertible in $F$, we may define $v = z - a u$ with $a = \tfrac{1}{2} B(z, z)$.
4. Linearity in the second slot and $B(u, u) = 0$ give $B(u, v) = B(u, z) - a B(u, u) = 1$.
5. Bilinearity gives $B(v, v) = B(z, z) - a B(z, u) - a B(u, z) + a^2 B(u, u)$.
6. By symmetry $B(z, u) = B(u, z) = 1$, and $B(u, u) = 0$. So $B(v, v) = B(z, z) - 2a = 0$.

Part 2, for an [[alternating|08ZQAKBKHF]] form $B$.

7. Put $v = z$. Then $B(u, v) = 1$ by step 2.
8. Every vector $w$ has $B(w, w) = 0$, by the definition of an alternating form. So $B(v, v) = 0$, and this holds for every $v$ with $B(u, v) = 1$.

Part 3.

9. Suppose that $u$ and $v$ are linearly dependent. Since $u \neq 0$, we have $v = c u$ for some $c \in F$.
10. Then $B(u, v) = c B(u, u) = 0$, which contradicts $B(u, v) = 1$. So $u$ and $v$ are linearly independent, and $H = \operatorname{span}(u, v)$ has dimension $2$.
11. In case 1, symmetry gives $B(v, u) = B(u, v) = 1$.
12. In case 2, the form is skew-symmetric by the [[relation between alternating and skew-symmetric forms|SX9CD5NEPD]], so $B(v, u) = -B(u, v) = -1$.
13. Together with $B(u, u) = B(v, v) = 0$, the [[matrix of $B$|0P24YW565F]] on $H$ in the basis $(u, v)$ is $\begin{pmatrix} 0 & 1 \\ \pm 1 & 0 \end{pmatrix}$.

Part 4.

14. The matrix of step 13 has determinant $\mp 1 \neq 0$. So the restriction of $B$ to $H$ is nondegenerate, by the [[criteria for nondegeneracy|3ND2FNJ38Y]].
15. By part 3 of the [[dimension statement for orthogonal complements|M2JH84VEY9]], a subspace on which $B$ is nondegenerate satisfies $V = H \oplus H^\perp$.
16. To show that $B$ is nondegenerate on $H^\perp$, let $x \in H^\perp$ with $B(x, y) = 0$ for all $y \in H^\perp$.
17. For $h \in H$ we have $B(h, x) = 0$, since $x \in H^\perp$. The form is symmetric or skew-symmetric, so $B(x, h) = \pm B(h, x) = 0$.
18. So the linear form $B(x, \cdot)$ is zero on $H$ and on $H^\perp$. By linearity it is zero on $H + H^\perp = V$.
19. So $x$ is in the left radical of $B$, and $x = 0$ by nondegeneracy. Hence $B$ is nondegenerate on $H^\perp$.

The final claim.

20. Let $V$ be a nondegenerate symmetric plane with an isotropic vector $u$, and let $1 + 1 \neq 0$. Parts 1 and 3 give a subspace $H \subseteq V$ of dimension $2$ with a hyperbolic pair.
21. Since $\dim H = 2 = \dim V$, we get $H = V$, because a [[subspace of full dimension is the whole space|0WGAXEK99E]]. So $V$ is a hyperbolic plane.
22. Conversely, a hyperbolic plane contains the isotropic vector $u$ of a hyperbolic pair.

This proves all four parts and the final claim.

## Idea

Nondegeneracy hands us a vector $z$ that pairs to $1$ with $u$.
For an alternating form, $z$ already pairs to $0$ with itself, so it is the partner.
For a symmetric form, $z$ may have $B(z, z) \neq 0$, and we subtract $\tfrac{1}{2} B(z, z)\, u$.
This changes $B(z, z)$ by $-2 \cdot \tfrac{1}{2} B(z, z)$ and leaves $B(u, z)$ alone, because $u$ is isotropic.
The division by $2$ is the one place where $1 + 1 \neq 0$ is used.
The plane then splits off because its matrix is invertible.

## Variants

When $1 + 1 \neq 0$, one can first diagonalize the form on $\operatorname{span}(u, z)$ as $\operatorname{diag}(a, b)$.
That plane is nondegenerate and isotropic, so $-b/a$ is a square, say $t^2$, and the vectors $t e_1 \pm e_2$ in the diagonal basis span the two isotropic lines.
Scaling one vector on each line so that they pair to $1$ gives the hyperbolic pair.
This route needs the diagonalization of symmetric forms, while the proof above needs only one subtraction.

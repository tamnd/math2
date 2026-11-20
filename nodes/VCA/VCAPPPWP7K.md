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

Let $u$ be isotropic, so $u \neq 0$ and $B(u, u) = 0$.

1. $B$ is [[nondegenerate|0KAN330PAH]] and $u \neq 0$, so $u$ is not in the left radical. So there is $z'$ with $B(u, z') \neq 0$.
2. Put $z = z' / B(u, z')$. Then $B(u, z) = 1$, by linearity in the second slot.

Part 1.
Let $B$ be [[symmetric|0744CN4MDA]] and $\operatorname{char} F \neq 2$.

3. Since $2 \neq 0$ in $F$, we can put $v = z - \frac{B(z, z)}{2} u$.
4. Linearity in the second slot and $B(u, u) = 0$ give $B(u, v) = B(u, z) - \frac{B(z, z)}{2} B(u, u) = 1$.
5. Bilinearity gives $B(v, v) = B(z, z) - \frac{B(z, z)}{2} \bigl(B(u, z) + B(z, u)\bigr) + \frac{B(z, z)^2}{4} B(u, u)$.
6. By symmetry $B(z, u) = B(u, z) = 1$, and $B(u, u) = 0$. So $B(v, v) = B(z, z) - B(z, z) = 0$.

Part 2.
Let $B$ be [[alternating|08ZQAKBKHF]].

7. Put $v = z$. Then $B(u, v) = 1$ by step 2.
8. For every $v$, $B(v, v) = 0$, by the definition of an alternating form.

Part 3.

9. Suppose that $u$ and $v$ are linearly dependent. Since $u \neq 0$, $v = c u$ for some $c \in F$.
10. Then $B(u, v) = c B(u, u) = 0$, which contradicts $B(u, v) = 1$. So $u$ and $v$ are independent, and $H = \operatorname{span}(u, v)$ has dimension $2$.
11. In case 1, $B(v, u) = B(u, v) = 1$ by symmetry.
12. In case 2, $B$ is skew-symmetric by the [[relation of alternating and skew-symmetric forms|SX9CD5NEPD]], so $B(v, u) = -1$.
13. With $B(u, u) = B(v, v) = 0$, the [[matrix of $B$|0P24YW565F]] on $H$ in the basis $(u, v)$ is $\begin{pmatrix} 0 & 1 \\ \pm 1 & 0 \end{pmatrix}$.

Part 4.

14. The matrix of step 13 has determinant $\mp 1 \neq 0$. By the [[criteria for nondegeneracy|3ND2FNJ38Y]], $B$ is nondegenerate on $H$.
15. By part 3 of the [[dimension statement for orthogonal complements|M2JH84VEY9]], $V = H \oplus H^\perp$.
16. Let $x \in H^\perp$ with $B(x, y) = 0$ for all $y \in H^\perp$.
17. For $h \in H$, $B(h, x) = 0$ since $x \in H^\perp$. Since $B$ is symmetric or skew-symmetric, $B(x, h) = \pm B(h, x) = 0$.
18. So $B(x, \cdot)$ is zero on $H$ and on $H^\perp$. By linearity it is zero on $H + H^\perp = V$.
19. So $x$ is in the left radical of $B$, and $x = 0$ by nondegeneracy. Hence $B$ is nondegenerate on $H^\perp$.

The final claim.

20. Let $V$ be a nondegenerate symmetric plane with an isotropic vector $u$, and $\operatorname{char} F \neq 2$. Parts 1 and 3 give a plane $H \subseteq V$ with a hyperbolic pair.
21. $\dim H = 2 = \dim V$, so $H = V$, since a [[subspace of full dimension is the whole space|0WGAXEK99E]]. So $V$ is a hyperbolic plane.
22. Conversely, a hyperbolic plane contains the isotropic vector $u$ of a hyperbolic pair.

This proves all parts.

## Idea

Nondegeneracy gives a vector $z$ with $B(u, z) = 1$.
For an alternating form, $z$ is already a partner.
For a symmetric form, $z$ may have $B(z, z) \neq 0$, and we subtract the multiple $\frac{B(z, z)}{2} u$, which changes $B(z, z)$ but not $B(u, z)$.
The plane then splits off by the dimension statement for orthogonal complements.

## Variants

When $\operatorname{char} F \neq 2$, one can diagonalize the symmetric form on $\operatorname{span}(u, z)$ as $\operatorname{diag}(a, b)$ and use that $-ab$ is a square, because the plane is isotropic.
This gives the hyperbolic pair from the two isotropic lines of the plane, but needs the diagonalization of quadratic forms.

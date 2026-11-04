---
tag: 7NV628FRZZ
kind: proof
name: Proof that the constructible numbers form the smallest subfield of the complex numbers closed under square roots
msc: [12F05]
proves: 0PN9WMRWT7
uses: [0FMN2MN7TM, 0DAECMZVRT, 07QY5RPFBR, 0FRSR10DWF, 0BJV24C4SY, 00KRCVE7CK, 0KW2X0TFBX, 0ZB7J071WQ, 068BZBXE0C, 0KYZXYDGQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Constructible_number
    locator: Equivalence of algebraic and geometric definitions
---

## Proof

Let $\mathcal{C}$ be the set of the [[constructible numbers|0FMN2MN7TM]]. A [[straightedge and compass|0DAECMZVRT]] step draws the line through two distinct points already obtained, or the circle centred at one obtained point through another. It then adds a common point of two distinct drawn lines or circles. Points constructed from points of $\mathcal{C}$ lie in $\mathcal{C}$, since the two sequences of steps can be joined.

Part 1: basic constructions.

1. Let $a \in \mathcal{C}$ with $a \neq 0$. The line through $0$ and $a$ is $\set{ta : t \in \R}$. The circle centred $0$ through $a$ meets it at $-a$, and the circle centred $a$ through $0$ meets it at $2a$. So $-a, 2a \in \mathcal{C}$.
2. Let $a, b \in \mathcal{C}$ with $a \neq b$, and let $m = (a+b)/2$. The points $u, v = m \pm \tfrac{\sqrt 3}{2} i (b - a)$ satisfy $\abs{u - a} = \abs{u - b} = \abs{b - a}$, and the same holds for $v$.
3. So $u$ and $v$ lie on the circle centred $a$ through $b$ and on the circle centred $b$ through $a$. Hence $u, v \in \mathcal{C}$.
4. The line through $u$ and $v$ is $\set{m + t i (b - a) : t \in \R}$. It meets the line through $a$ and $b$ only at $m$. So the midpoint $m$ lies in $\mathcal{C}$.
5. Let $a, b \in \mathcal{C}$. If $a = b$, then $a + b = 2a \in \mathcal{C}$ by step 1, or $a + b = 0$. If $a \neq b$, then $a + b = 2m$ with $m \in \mathcal{C}$ by step 4, so $a + b \in \mathcal{C}$.
6. By steps 1 and 5, $\mathcal{C}$ contains $0$ and $1$ and is closed under addition and negation.
7. The circle centred $0$ through $1$ gives $-1 \in \mathcal{C}$. For $a = -1$ and $b = 1$, step 2 gives $u, v = \pm \sqrt 3 \, i$, so the imaginary axis can be drawn. It meets the circle centred $0$ through $1$ at $i$, so $i \in \mathcal{C}$.
8. Let $z \in \mathcal{C}$ not be real. Its [[conjugate|0BJV24C4SY]] satisfies $\abs{\bar z} = \abs{z}$ and $\abs{\bar z - 1} = \abs{z - 1}$, by the [[modulus of the conjugate|00KRCVE7CK]]. So $\bar z$ lies on the circles centred $0$ and $1$ through $z$, and $\bar z \in \mathcal{C}$.
9. Let $z = x + iy \in \mathcal{C}$ with $x, y$ real. If $z$ is not real, then $x$ is the midpoint of $z$ and $\bar z$, and $iy$ is the midpoint of $0$ and $z - \bar z$. So $x, iy \in \mathcal{C}$. If $z$ is real, then $x = z$ and $iy = 0$.
10. Let $y \neq 0$ be real. If $y \in \mathcal{C}$, the circle centred $0$ through $y$ meets the imaginary axis at $iy$. If $iy \in \mathcal{C}$, the circle centred $0$ through $iy$ meets the real axis at $y$. So $y \in \mathcal{C}$ if and only if $iy \in \mathcal{C}$.
11. By steps 9 and 10 and the sum $x + iy$ of step 5: $z \in \mathcal{C}$ if and only if $\operatorname{Re} z \in \mathcal{C}$ and $\operatorname{Im} z \in \mathcal{C}$.
12. Let $x, y$ be nonzero reals in $\mathcal{C}$. The point $x + iy - 1$ lies in $\mathcal{C}$, so we can draw the line $\set{x + t(iy - 1) : t \in \R}$ through $x$ parallel to the line through $1$ and $iy$.
13. This line meets the imaginary axis where $x - t = 0$, at the point $ixy$. So $ixy \in \mathcal{C}$, and $xy \in \mathcal{C}$ by step 10. If $x = 0$ or $y = 0$, then $xy = 0 \in \mathcal{C}$.
14. The line $\set{i + t(1 - iy) : t \in \R}$ through $i$ and $i + 1 - iy$ meets the real axis where $1 - ty = 0$, at $1/y$. So $1/y \in \mathcal{C}$.
15. Let $z = x + iy$ and $w = u + iv$ be in $\mathcal{C}$, with $x, y, u, v$ real. Then $zw = (xu - yv) + i(xv + yu)$, so $zw \in \mathcal{C}$ by steps 6, 11 and 13.
16. If $z \neq 0$, then $r = x^2 + y^2 > 0$ lies in $\mathcal{C}$, and $1/z = x/r - i y/r$. So $1/z \in \mathcal{C}$ by steps 11, 13 and 14.
17. By steps 6, 15 and 16, $\mathcal{C}$ is a [[subfield|07QY5RPFBR]] of the [[field $\C$|0FRSR10DWF]].
18. Let $r > 0$ be real in $\mathcal{C}$. The midpoint $c = (r - 1)/2$ of $-1$ and $r$ is in $\mathcal{C}$. The circle centred $c$ through $r$ has radius $(r+1)/2$.
19. A point $iy$ with $y$ real lies on this circle if and only if $c^2 + y^2 = (r+1)^2/4$, that is, $y^2 = r$. With $y = \sqrt r$ from the [[real square root|068BZBXE0C]], $i \sqrt r \in \mathcal{C}$, so $\sqrt r \in \mathcal{C}$.
20. Let $z \in \mathcal{C}$ with $z \neq 0$. By steps 8 and 17, [[$z \bar z = \abs{z}^2$|0ZB7J071WQ]] lies in $\mathcal{C}$, so the [[modulus|0KW2X0TFBX]] $\rho = \abs{z}$ lies in $\mathcal{C}$ by step 19. Let $w = z / \rho$, so $\abs{w} = 1$ and $\bar w = 1/w$.
21. If $w = -1$, then $(i \sqrt \rho)^2 = -\rho = z$, and $i \sqrt \rho \in \mathcal{C}$.
22. If $w \neq -1$, let $s = \sqrt \rho \, (w + 1)/\abs{w + 1}$, which lies in $\mathcal{C}$ by steps 17, 19 and 20. Then $s^2 = \rho (w+1)^2 / ((w+1)(\bar w + 1)) = \rho (w + 1)/(\bar w + 1)$.
23. Since $\bar w + 1 = (1 + w)/w$, this gives $s^2 = \rho w = z$. So $z$ has a square root in $\mathcal{C}$. Its negative, the other square root, is in $\mathcal{C}$ too. For $z = 0$ the only square root is $0$.
24. So $\mathcal{C}$ is a subfield of $\C$ that contains every square root of each of its elements.

Part 2: minimality.

25. Let $M$ be the intersection of all subfields of $\C$ that contain every square root of each of their elements. Then $M$ is a subfield of $\C$ with the same property.
26. Conjugation preserves sums and products, and it is its own inverse. So $\bar M = \set{\bar z : z \in M}$ is a subfield of $\C$. If $s^2 = \bar z$ with $z \in M$, then $\bar s^2 = z$, so $\bar s \in M$ and $s \in \bar M$.
27. So $\bar M$ has the same property, and $M \subseteq \bar M$. Conjugating gives $\bar M \subseteq M$. So $M$ is closed under conjugation.
28. The number $i$ is a square root of $-1 \in M$, so $i \in M$. For $z \in M$, then $\operatorname{Re} z = (z + \bar z)/2$ and $\operatorname{Im} z = (z - \bar z)/(2i)$ lie in $M$. Let $M_\R = M \cap \R$.
29. Every real $r \ge 0$ in $M_\R$ has $\sqrt r \in M_\R$. A line through two points of $M$ has an equation $\alpha x + \beta y = \gamma$ with $\alpha, \beta, \gamma \in M_\R$, not both $\alpha, \beta$ zero. Here $z = x + iy$. For the points $a_1 + i a_2$ and $b_1 + i b_2$, take $\alpha = b_2 - a_2$, $\beta = a_1 - b_1$ and $\gamma = \alpha a_1 + \beta a_2$.
30. A circle centred at $c_1 + i c_2 \in M$ through a point of $M$ has an equation $x^2 + y^2 + \delta x + \epsilon y + \eta = 0$ with $\delta = -2c_1$, $\epsilon = -2c_2$ and $\eta \in M_\R$.
31. Two distinct lines that meet have a nonzero determinant $\alpha \beta' - \alpha' \beta$. By Cramer's rule, the common point has coordinates in $M_\R$.
32. For a line and a circle, say $\beta \neq 0$; otherwise swap the roles of $x$ and $y$. Substituting $y = (\gamma - \alpha x)/\beta$ gives $A x^2 + B x + C = 0$ with $A = 1 + \alpha^2/\beta^2 \neq 0$ and $B, C \in M_\R$.
33. A real solution $x$ needs $D = B^2 - 4AC \ge 0$, and then [[$x = (-B \pm \sqrt D)/(2A)$|0KYZXYDGQZ]]. So $x \in M_\R$, and $y \in M_\R$.
34. For two distinct circles, subtracting their equations gives $(\delta - \delta')x + (\epsilon - \epsilon')y + (\eta - \eta') = 0$. If $\delta = \delta'$ and $\epsilon = \epsilon'$, the circles are concentric and distinct, so they have no common point.
35. Otherwise, the common points are the common points of the first circle with this line. They lie in $M$ by step 33.
36. So each step of a construction adds a point $x + iy$ with $x, y \in M_\R$, which lies in $M$ since $i \in M$. As $0, 1 \in M$, induction on the number of steps gives $\mathcal{C} \subseteq M$.
37. Every subfield $K$ of $\C$ closed under square roots contains $M$, so $\mathcal{C} \subseteq K$. With step 24, $\mathcal{C}$ is the smallest subfield of $\C$ closed under square roots.

## Idea

Midpoints, parallels and similar triangles give sums, products and quotients, and a circle on a diameter of length $1 + r$ gives $\sqrt r$. A complex square root needs only a real square root and the bisector direction $w + 1$. Conversely, the common points of lines and circles solve linear or quadratic equations, so each step needs only field operations and one square root.

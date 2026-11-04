---
tag: W2HR1B92VJ
kind: proof
name: Proof that Möbius transformations map circles and lines to circles and lines
msc: [30C35]
proves: 0SXDHQM2MH
uses: [0B346DDAM5, 0CDMXGPSES, 045DN06F3S, 0BMYPJBJH4, 0KW2X0TFBX, 0BJV24C4SY]
sources:
  - url: https://en.wikipedia.org/wiki/Generalised_circle
    locator: Extended complex plane
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_transformation
    locator: Preservation of angles and generalized circles
---

## Proof

We write the map as a composition of simple maps and check each simple map.
For $z \in \C$, $\bar z$ is the [[complex conjugate|0BJV24C4SY]] and $\abs{z}$ is the [[modulus|0KW2X0TFBX]], so $z \bar z = \abs{z}^2$.
Generalized circles live in the [[Riemann sphere|0CDMXGPSES]] $\widehat{\C} = \C \cup \set{\infty}$.

*Equations of generalized circles.*

1. Call a triple $(A, B, D)$ admissible if $A, D \in \R$, $B \in \C$ and $\abs{B}^2 > AD$. Let $Z(A, B, D)$ be the set of $z \in \C$ with $A z \bar z + B z + \bar B \bar z + D = 0$.
2. Let $\Gamma(A, B, D) = Z(A, B, D)$ if $A \ne 0$, and $\Gamma(A, B, D) = Z(A, B, D) \cup \set{\infty}$ if $A = 0$. We show that the generalized circles are exactly the sets $\Gamma(A, B, D)$ with $(A, B, D)$ admissible.
3. Let $C$ be a [[circle|045DN06F3S]] with centre $c$ and radius $r > 0$. Expanding $\abs{z - c}^2 = r^2$ gives $z \bar z - \bar c z - c \bar z + \abs{c}^2 - r^2 = 0$. So $C = \Gamma(1, -\bar c, \abs{c}^2 - r^2)$, and $\abs{-\bar c}^2 - (\abs{c}^2 - r^2) = r^2 > 0$.
4. Let $L = \set{p + t v : t \in \R}$ be a [[line|0BMYPJBJH4]], with $p \in \C$ and $v \in \C \setminus \set{0}$. A point $z$ lies on $L$ exactly when $(z - p)/v$ is real.
5. Since $(z - p)/v = \bar v (z - p)/\abs{v}^2$, this holds exactly when $\bar v (z - p) - v(\bar z - \bar p) = 0$. Multiply by $i$ and put $B = i \bar v$, so $\bar B = -iv$. The condition becomes $B z + \bar B \bar z + D = 0$ with $D = -(Bp + \bar B \bar p)$.
6. Here $D = -2 \operatorname{Re}(Bp)$ is real and $\abs{B}^2 = \abs{v}^2 > 0$. So $L \cup \set{\infty} = \Gamma(0, B, D)$ with $(0, B, D)$ admissible.
7. Conversely, let $(A, B, D)$ be admissible with $A \ne 0$. Put $c = -\bar B / A$. Dividing the equation by $A$ and using $\abs{z - c}^2 = z \bar z + (B/A) z + (\bar B/A) \bar z + \abs{B}^2/A^2$, the equation becomes $\abs{z - c}^2 = (\abs{B}^2 - AD)/A^2$.
8. The right side of step 7 is positive. So $\Gamma(A, B, D)$ is the circle with centre $c$ and radius $\sqrt{\abs{B}^2 - AD}/\abs{A}$.
9. Let $(0, B, D)$ be admissible, so $B \ne 0$. Put $v = i \bar B$, so $v \ne 0$ and $B = i \bar v$. Put $p = -D \bar B / (2 \abs{B}^2)$, so $B p = -D/2$ and $D = -(Bp + \bar B \bar p)$.
10. By steps 4 and 5, read backwards with these $v$ and $p$, the set $Z(0, B, D)$ is the line $\set{p + tv : t \in \R}$. So $\Gamma(0, B, D)$ is a line together with $\infty$.
11. Steps 3, 6, 8 and 10 prove the claim of step 2.

*Affine maps.*

12. Let $g(z) = \alpha z + \beta$ for $z \in \C$, with $\alpha \ne 0$, and $g(\infty) = \infty$. Then $g$ is a bijection of $\widehat{\C}$, with inverse $w \mapsto (w - \beta)/\alpha$ on $\C$.
13. Let $C$ be the circle with centre $c$ and radius $r$. For $z \in \C$, $\abs{g(z) - g(c)} = \abs{\alpha} \abs{z - c}$. So $w \in \C$ satisfies $\abs{w - g(c)} = \abs{\alpha} r$ exactly when $g^{-1}(w) \in C$.
14. By steps 12 and 13, $g(C)$ is the circle with centre $g(c)$ and radius $\abs{\alpha} r > 0$.
15. Let $L = \set{p + tv : t \in \R}$ with $v \ne 0$. Then $g(p + tv) = g(p) + t \alpha v$ and $\alpha v \ne 0$. With $g(\infty) = \infty$, the image $g(L \cup \set{\infty})$ is the line through $g(p)$ with direction $\alpha v$, together with $\infty$.
16. So $g$ maps each generalized circle to a generalized circle.

*The inversion.*

17. Let $J(z) = 1/z$ for $z \in \C \setminus \set{0}$, $J(0) = \infty$ and $J(\infty) = 0$. Then $J$ is a bijection of $\widehat{\C}$ and $J \circ J$ is the identity.
18. Let $C = \Gamma(A, B, D)$ with $(A, B, D)$ admissible, as in step 11. Then $(D, \bar B, A)$ is admissible, since $\abs{\bar B}^2 = \abs{B}^2 > DA$. Let $C' = \Gamma(D, \bar B, A)$, a generalized circle by step 11.
19. Let $z, w \in \C \setminus \set{0}$ with $w = 1/z$. Multiplying $A z \bar z + B z + \bar B \bar z + D = 0$ by $w \bar w \ne 0$ gives $A + B \bar w + \bar B w + D w \bar w = 0$. This is the equation of $Z(D, \bar B, A)$.
20. Since $w \bar w \ne 0$, the two equations of step 19 are equivalent. So $J$ maps $C \setminus \set{0, \infty}$ onto $C' \setminus \set{0, \infty}$.
21. Putting $z = 0$ in the equation shows $0 \in C$ exactly when $D = 0$. By step 2, $\infty \in C'$ exactly when $D = 0$. So $0 \in C$ exactly when $J(0) = \infty \in C'$.
22. By step 2, $\infty \in C$ exactly when $A = 0$. Putting $w = 0$ in the equation of $C'$ shows $0 \in C'$ exactly when $A = 0$. So $\infty \in C$ exactly when $J(\infty) = 0 \in C'$.
23. By steps 20, 21 and 22, $J(C) = C'$. So $J$ maps each generalized circle to a generalized circle.

*Decomposition.*

24. Let $f(z) = \frac{az + b}{cz + d}$ be a [[Möbius transformation|0B346DDAM5]], with $ad - bc \ne 0$.
25. If $c = 0$, then $ad \ne 0$, so $d \ne 0$. Then $f(z) = (a/d) z + b/d$ on $\C$ and $f(\infty) = \infty$, with $a/d \ne 0$. So $f$ is a map $g$ as in step 12.
26. Let $c \ne 0$. Put $g_1(z) = cz + d$ and $g_2(w) = a/c + k w$ with $k = (bc - ad)/c \ne 0$, both extended by $\infty \mapsto \infty$.
27. For $z \in \C$ with $cz + d \ne 0$: $g_2(J(g_1(z))) = \frac{a}{c} + \frac{bc - ad}{c(cz + d)} = \frac{a(cz + d) + bc - ad}{c(cz + d)} = \frac{az + b}{cz + d} = f(z)$.
28. At $z = -d/c$: $g_1(z) = 0$, $J(0) = \infty$ and $g_2(\infty) = \infty = f(-d/c)$. At $z = \infty$: $g_1(\infty) = \infty$, $J(\infty) = 0$ and $g_2(0) = a/c = f(\infty)$.
29. By steps 27 and 28, $f = g_2 \circ J \circ g_1$ on all of $\widehat{\C}$.
30. Let $C$ be a generalized circle. By steps 16 and 23, applied in turn, $g_1(C)$, $J(g_1(C))$ and $g_2(J(g_1(C))) = f(C)$ are generalized circles. With step 25 this covers both cases, so $f(C)$ is a generalized circle.

## Idea

Every circle and every line is the zero set of one equation $A \abs{z}^2 + Bz + \bar B \bar z + D = 0$. Substituting $z = 1/w$ and clearing denominators gives an equation of the same shape with $A$ and $D$ swapped, so the inversion keeps the family. Affine maps multiply all distances by $\abs{\alpha}$, so they keep circles and lines, and every Möbius map is built from these pieces.

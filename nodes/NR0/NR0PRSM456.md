---
tag: NR0PRSM456
kind: proof
name: Proof of Ptolemy's theorem by complex numbers
msc: [51M04]
proves: 058YS05YP5
uses: [049DCJZ448, 0RCP929Y1M, 0NPPGHQNXQ, 060W5CBZP6, 09FTAET5Z4, 0FTH2E9TAS, 0KW2X0TFBX, 0BRXFNQ5JV, 04R3CY41VJ, 0WM7DJCM6G, 0MP9BCF6DP, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Ptolemy%27s_theorem
    locator: Proof using complex numbers
---

## Proof

We identify the plane with the [[complex numbers|09FTAET5Z4]] and use an algebraic identity.

1. Let $S$ be the common point of the diagonals, with $S = (1 - s)A + sC = (1 - t)B + tD$ and $0 < s, t < 1$. So $A \neq C$, $B \neq D$, and $S$ is none of the four points.
   The points are [[concyclic|049DCJZ448]], so they lie on a [[circle|060W5CBZP6]] with a centre $O$ and a radius $r$. Since $A \neq C$, we have $r > 0$.
   A line $\set{Y + \tau v}$ with $v \neq 0$ meets the circle where $\norm{Y - O + \tau v}^2 = r^2$. This is a quadratic equation in $\tau$ with leading coefficient $\norm{v}^2 > 0$, so there are at most two such points.
   Suppose that $B$ or $D$ is equal to $A$ or to $C$. Then the lines $AC$ and $BD$ share $S$ and a vertex, so they are equal. This line contains $A$, $B$, $C$, $D$, so $\set{B, D} = \set{A, C}$.
   If $B = A$ and $D = C$, or if $B = C$ and $D = A$, then both sides of the claim equal $d(A, C)^2$. From now on, the four points are distinct.
2. Put $a = A - O$, $b = B - O$, $c = C - O$, $e = D - O$. Then $d(X, Y) = \abs{x - y}$ for the [[Euclidean distance|0NPPGHQNXQ]], with the [[modulus|0KW2X0TFBX]].
3. For all complex numbers, $(a - c)(b - e) = (a - b)(c - e) + (a - e)(b - c)$. Indeed, both sides expand to $ab - ae - bc + ce$.
4. For real $x$, $y$, Euler's formula gives $e^{ix} - e^{iy} = 2i\sin\frac{x - y}{2}\, e^{i(x + y)/2}$. This follows from $e^{ih} - e^{-ih} = 2i\sin h$ by [[Euler's formula|04R3CY41VJ]].
5. By the [[polar form|0BRXFNQ5JV]], write $a = re^{i\alpha}$ and $c = re^{i\gamma}$. Since $C \neq A$, we may choose $\gamma$ with $\alpha < \gamma < \alpha + 2\pi$.
6. Let $X$ be a point of the circle other than $A$. Write $X - O = re^{i\theta}$ with $\alpha < \theta < \alpha + 2\pi$. Put $g(X) = \det(C - A, X - A)$, with the [[determinant|00KDZRW4C0]].
7. For $u = u_1 + iu_2$ and $w = w_1 + iw_2$, the imaginary part of $\bar u\, w$ is $u_1 w_2 - u_2 w_1 = \det(u, w)$. So $g(X)$ is the imaginary part of $\overline{(c - a)}\,(x - a)$, with the [[complex conjugate|0FTH2E9TAS]] and $x = X - O$.
8. By steps 4 and 6 and the [[product of exponentials|0WM7DJCM6G]], $\overline{(c - a)}\,(x - a) = 4r^2 \sin\frac{\gamma - \alpha}{2}\sin\frac{\theta - \alpha}{2}\, e^{i(\theta - \gamma)/2}$.
9. So $g(X) = 4r^2 \sin\frac{\gamma - \alpha}{2}\sin\frac{\theta - \alpha}{2}\sin\frac{\theta - \gamma}{2}$. The first two sines are positive, since their arguments lie in $(0, \pi)$.
10. The third sine is negative for $\theta < \gamma$ and positive for $\theta > \gamma$, since its argument lies in $(-\pi, \pi)$. So $g(X) < 0$ for $\theta \in (\alpha, \gamma)$ and $g(X) > 0$ for $\theta \in (\gamma, \alpha + 2\pi)$.
11. By step 1, $S = (1 - t)B + tD$ with $0 < t < 1$, and $S$ is on the [[line|0MP9BCF6DP]] $AC$. So $g(S) = 0$. The determinant is linear in its second column, so $(1 - t)g(B) + t g(D) = 0$.
12. By step 10, $g(B) \neq 0$ and $g(D) \neq 0$, since $B$ and $D$ differ from $A$ and $C$. By step 11, $g(B)$ and $g(D)$ have opposite signs.
13. The claimed equation does not change if we swap the names $B$ and $D$. So by step 10 we may assume $b = re^{i\beta}$ and $e = re^{i\delta}$ with $\alpha < \beta < \gamma < \delta < \alpha + 2\pi$.
14. Put $\sigma = \frac{\alpha + \beta + \gamma + \delta}{2}$. By step 4, $(a - b)(c - e) = -4r^2 e^{i\sigma} s_1$, with $s_1 = \sin\frac{\alpha - \beta}{2}\sin\frac{\gamma - \delta}{2}$.
15. In the same way, $(a - e)(b - c) = -4r^2 e^{i\sigma} s_2$ with $s_2 = \sin\frac{\alpha - \delta}{2}\sin\frac{\beta - \gamma}{2}$.
16. By step 13, the numbers $\frac{\alpha - \beta}{2}$, $\frac{\gamma - \delta}{2}$, $\frac{\alpha - \delta}{2}$ and $\frac{\beta - \gamma}{2}$ all lie in $(-\pi, 0)$. So each of these sines is negative, and $s_1 > 0$, $s_2 > 0$.
17. By steps 3, 14 and 15, $(a - c)(b - e) = -4r^2 e^{i\sigma}(s_1 + s_2)$. Taking moduli and using $\abs{e^{i\sigma}} = 1$, we get $\abs{a - c}\abs{b - e} = 4r^2(s_1 + s_2)$.
18. Also by steps 14 and 15, $\abs{a - b}\abs{c - e} = 4r^2 s_1$ and $\abs{a - e}\abs{b - c} = 4r^2 s_2$.
19. By steps 2, 17 and 18, $d(A, C)\, d(B, D) = d(A, B)\, d(C, D) + d(B, C)\, d(A, D)$.

## Idea

The identity of step 3 holds for any four complex numbers, so the triangle inequality gives Ptolemy's inequality. For points in convex order on a circle, the two products on the right point in the same direction. Then the moduli add exactly, and the inequality becomes an equation.

---
tag: 3DHVEJ7TKJ
kind: proof
name: Proof of Ceva's theorem by barycentric coordinates
msc: [51M04]
proves: 0KN93VDSXA
uses: [0CTNFGYMM2, 0MP9BCF6DP, 0AFNNTRTJE, 0KJH6SRFZK, 0CRMGPAH83, 096V7H13H9]
sources:
  - url: https://en.wikipedia.org/wiki/Ceva%27s_theorem
    locator: Using barycentric coordinates
---

## Proof

We use barycentric coordinates with respect to $A$, $B$, $C$.

1. The points $A$, $B$, $C$ of the [[triangle|0CTNFGYMM2]] are not [[collinear|0AFNNTRTJE]]. So the vectors $B - A$ and $C - A$ are [[linearly independent|0CRMGPAH83]].
2. Two linearly independent vectors of $\mathbb{R}^2$ form a [[basis|096V7H13H9]]. So each point $X$ has a unique form $X = A + u(B - A) + v(C - A)$.
3. Equivalently, each point $X$ is a unique [[affine combination|0KJH6SRFZK]] $X = \alpha A + \beta B + \gamma C$ with $\alpha + \beta + \gamma = 1$. We call $(\alpha, \beta, \gamma)$ the coordinates of $X$.
4. The [[line|0MP9BCF6DP]] $BC$ is the set of the points $(1 - s)B + sC$ with $s \in \mathbb{R}$. By the uniqueness in step 3, a point lies on $BC$ if and only if $\alpha = 0$. In the same way, $CA$ is $\beta = 0$ and $AB$ is $\gamma = 0$.
5. Let $X = \alpha A + \beta B + \gamma C$ be a point of $AB$, so $\gamma = 0$ and $\alpha + \beta = 1$, and let $X \neq B$, so $\alpha \neq 0$. Then $X - A = \beta(B - A)$ and $B - X = \alpha(B - A)$. Hence the signed ratio is $\frac{AX}{XB} = \frac{\beta}{\alpha}$.

**The direct statement.**

6. Let $O = \alpha A + \beta B + \gamma C$ with $\alpha + \beta + \gamma = 1$. Since $O$ is not on $BC$, $CA$, $AB$, step 4 gives $\alpha \neq 0$, $\beta \neq 0$ and $\gamma \neq 0$.
7. A point of the line $AO$ has the form $(1 - t)A + tO = (1 - t + t\alpha)A + t\beta B + t\gamma C$. Its first coordinate is $1 - t(\beta + \gamma)$.
8. If $\beta + \gamma = 0$, then this coordinate is $1$ for all $t$. Then by step 4 the line $AO$ does not meet $BC$, against the hypothesis. So $\beta + \gamma \neq 0$.
9. By step 4, the point $D$ is the point of step 7 with $t = \frac{1}{\beta + \gamma}$. Thus $D = \frac{\beta}{\beta + \gamma} B + \frac{\gamma}{\beta + \gamma} C$, and $D \neq C$ since $\beta \neq 0$.
10. By step 5 applied to the side $BC$, we get $\frac{BD}{DC} = \frac{\gamma}{\beta}$.
11. In the same way, $\alpha + \beta \neq 0$ and $\gamma + \alpha \neq 0$. Also $F = \frac{\alpha A + \beta B}{\alpha + \beta}$ and $E = \frac{\gamma C + \alpha A}{\gamma + \alpha}$. So $\frac{AF}{FB} = \frac{\beta}{\alpha}$ and $\frac{CE}{EA} = \frac{\alpha}{\gamma}$.
12. Multiplying, $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = \frac{\beta}{\alpha} \cdot \frac{\gamma}{\beta} \cdot \frac{\alpha}{\gamma} = 1$.

**The converse.**

13. Let $D$, $E$, $F$ be as in the converse. Put $x = \frac{BD}{DC}$, $y = \frac{CE}{EA}$ and $z = \frac{AF}{FB}$, so $xyz = 1$.
14. From $D - B = x(C - D)$ we get $(1 + x)D = B + xC$. If $x = -1$, this gives $B = C$, which is false. So $1 + x \neq 0$. Also $x \neq 0$, because $D \neq B$.
15. In the same way, $(1 + y)E = C + yA$ and $(1 + z)F = A + zB$, with $y, z \notin \set{0, -1}$.
16. Put $S = 1 + z + zx$ and $w = A + zB + zxC$. Using step 14, $z(1 + x)D = zB + zxC$. Hence $w = A + z(1 + x)D$.
17. Using $zxy = 1$ and step 15, $zx(1 + y)E = zxC + A$. Hence $w = zB + zx(1 + y)E$. Note $zx(1 + y) = zx + 1$.
18. Using step 15, $w = zxC + (1 + z)F$.
19. Case $S \neq 0$. Put $Q = w / S$. By step 16, $Q = \frac{1}{S}A + \frac{z(1 + x)}{S}D$, an affine combination of $A$ and $D$ since the weights add up to $1$. So $Q$ lies on the line $AD$.
20. By steps 17 and 18 in the same way, $Q$ lies on the lines $BE$ and $CF$. So the three lines meet in the point $Q$.
21. Case $S = 0$. Then $w = (A + zB + zxC) - S A = z(B - A) + zx(C - A)$. This is a nonzero vector by step 1, since $z \neq 0$ by step 15.
22. Since $S = 0$, step 16 gives $z(1 + x)(D - A) = w - SA = w$. So $w$ is a direction vector of the line $AD$, as $z(1 + x) \neq 0$.
23. In the same way, steps 17 and 18 give $(1 + zx)(E - B) = w$ and $(1 + z)(F - C) = w$. Here $1 + zx = zx(1 + y) \neq 0$ and $1 + z \neq 0$.
24. So the lines $AD$, $BE$ and $CF$ all have the direction $w$, and they are parallel.

## Idea

Barycentric coordinates turn each ratio on a side into a quotient of two coordinates of the point $O$. The product of the three quotients telescopes to $1$. For the converse, the weights $1$, $z$, $zx$ build the common point directly. When these weights add up to $0$, the same computation gives a common direction.

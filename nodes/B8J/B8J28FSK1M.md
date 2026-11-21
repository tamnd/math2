---
tag: B8J28FSK1M
kind: proof
name: Proof of the geometric formula for the dot product
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
proves: 070TXS9AXM
methods: [0WCP0PVET6, 0NTF6DMVAP]
uses: [060ZVZBV3E, 0ZEHZY85E6, 0XKBKGTCPC, 0S52TNNTH9, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Equivalence of the definitions
  - url: https://en.wikipedia.org/wiki/Law_of_cosines
    locator: lead section
---

## Proof

We write the third side of the triangle $OUV$ in two ways, once with coordinates and once with the law of cosines, and compare; parallel vectors give no triangle, so we treat them apart.

1. Let $u, v \in \mathbb{R}^n$ be nonzero, with $n = 2$ or $3$, and let $U$ and $V$ be the points with position vectors $u$ and $v$. By the [[definition of the length|0XKBKGTCPC]], $OU = \|u\|$ and $OV = \|v\|$.
2. The vector from $U$ to $V$ is $v - u$, so by the [[Euclidean distance|0NPPGHQNXQ]] the third side is $UV = \|v - u\|$.
3. We expand the square of the third side in coordinates:
   $$\|v - u\|^2 = \sum_i (v_i - u_i)^2 = \sum_i v_i^2 - 2 \sum_i u_i v_i + \sum_i u_i^2.$$
4. By the definitions of the length and of the [[dot product|0S52TNNTH9]], step 3 reads
   $$\|v - u\|^2 = \|u\|^2 + \|v\|^2 - 2\, u \cdot v.$$
5. Case 1: $u$ and $v$ are not parallel. Then $O$, $U$ and $V$ are not on one line, so they form a triangle whose [[angle|0ZEHZY85E6]] at $O$ is $\theta$ and whose side opposite to $O$ is $UV$.
6. The [[law of cosines|060ZVZBV3E]] in this triangle, with steps 1 and 2, gives
   $$\|v - u\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\| \, \|v\| \cos \theta.$$
7. The left sides of steps 4 and 6 are equal, so the right sides are equal. We cancel $\|u\|^2 + \|v\|^2$ and divide by $-2$, which gives $u \cdot v = \|u\| \, \|v\| \cos \theta$.
8. Case 2: $v = cu$ with $c > 0$. The arrows point the same way, so $\theta = 0$ and $\cos \theta = 1$. By the definition of the dot product $u \cdot v = c \, (u \cdot u) = c\|u\|^2$, and by homogeneity of the length $\|u\| \, \|v\| = c\|u\|^2$. The two sides agree.
9. Case 3: $v = cu$ with $c < 0$. The arrows point opposite ways, so $\theta = \pi$ and $\cos \theta = -1$. Again $u \cdot v = c\|u\|^2$, and now $\|u\| \, \|v\| \cos \theta = -|c| \, \|u\|^2 = c\|u\|^2$. The two sides agree.
10. Two nonzero parallel vectors satisfy $v = cu$ with $c \neq 0$, so the three cases cover all pairs, and the formula holds for all nonzero $u$ and $v$.

## Idea

The law of cosines gives the third side of a triangle from two sides and the angle between them.
The same third side, written in coordinates, contains the dot product as its cross term $-2\, u \cdot v$.
Put the two expressions side by side, and everything except the dot product and the cosine term cancels.
Parallel vectors give a flat triangle, so we check them directly with $v = cu$.

## Variants

The law of cosines in step 6 must be the one of elementary geometry, proved by dropping a perpendicular and using the Pythagorean theorem twice.
The [[vector proof of the law of cosines|T5X9ZN2E4M]] defines the angle through the dot product, so using it here would make the argument circular.

In the plane there is a second proof with polar coordinates.
Write $u = \|u\| (\cos \alpha, \sin \alpha)$ and $v = \|v\| (\cos \beta, \sin \beta)$.
Then the addition formula for the cosine gives
$$u \cdot v = \|u\| \, \|v\| (\cos \alpha \cos \beta + \sin \alpha \sin \beta) = \|u\| \, \|v\| \cos(\alpha - \beta).$$
The angle between the vectors is $|\alpha - \beta|$ or $2\pi - |\alpha - \beta|$, and both have this cosine.

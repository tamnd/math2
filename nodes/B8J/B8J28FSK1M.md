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

We use the law of cosines in the triangle with the vertices $O$, $U$ and $V$, and we split off the case of parallel vectors.

1. Let $u, v \in \mathbb{R}^n$ be nonzero, with $n = 2$ or $3$. Let $U$ and $V$ be the points with position vectors $u$ and $v$.
2. By the [[definition of the length|0XKBKGTCPC]], $OU = \|u\|$ and $OV = \|v\|$.
3. The vector from $U$ to $V$ is $v - u$. By the [[Euclidean distance|0NPPGHQNXQ]], $UV = \|v - u\|$.
4. We expand in coordinates: $\|v - u\|^2 = \sum_i (v_i - u_i)^2 = \sum_i v_i^2 - 2 \sum_i u_i v_i + \sum_i u_i^2$.
5. By the definitions of the length and of the [[dot product|0S52TNNTH9]], step 4 reads $\|v - u\|^2 = \|v\|^2 - 2\, u \cdot v + \|u\|^2$.
6. Case 1: $u$ and $v$ are not parallel. Then $O$, $U$ and $V$ are not on one line, so they form a triangle.
7. In this triangle, the [[angle|0ZEHZY85E6]] at $O$ is $\theta$, and the side opposite to $O$ is $UV$.
8. The [[law of cosines|060ZVZBV3E]] gives $UV^2 = OU^2 + OV^2 - 2 \cdot OU \cdot OV \cos \theta$.
9. With steps 2 and 3, this reads $\|v - u\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\| \, \|v\| \cos \theta$.
10. We compare steps 5 and 9 and cancel $\|u\|^2 + \|v\|^2$. This gives $-2\, u \cdot v = -2\|u\| \, \|v\| \cos \theta$.
11. We divide by $-2$ and get $u \cdot v = \|u\| \, \|v\| \cos \theta$.
12. Case 2: $v = cu$ with $c > 0$. Then the arrows point the same way, so $\theta = 0$ and $\cos \theta = 1$.
13. In case 2, $u \cdot v = c\, (u \cdot u) = c\|u\|^2$, by the definition of the dot product.
14. In case 2, $\|v\| = |c| \, \|u\| = c\|u\|$, by homogeneity of the length. So $\|u\| \, \|v\| \cos \theta = c\|u\|^2$.
15. Case 3: $v = cu$ with $c < 0$. Then the arrows point opposite ways, so $\theta = \pi$ and $\cos \theta = -1$.
16. In case 3, $u \cdot v = c\|u\|^2$ as in step 13. Also $\|u\| \, \|v\| \cos \theta = -|c| \, \|u\|^2 = c\|u\|^2$.
17. Parallel nonzero vectors satisfy $v = cu$ with $c \neq 0$, so the three cases cover all pairs. This proves the formula.

## Idea

The law of cosines expresses the third side of a triangle through two sides and the angle between them.
The same third side, written in coordinates, contains the dot product as its cross term.
Comparing the two expressions isolates $u \cdot v$.
Parallel vectors give no triangle, so we check them directly.

## Variants

- The law of cosines in step 8 must be the one of elementary geometry. Its school proof drops a perpendicular and uses the Pythagorean theorem twice. The [[vector proof of the law of cosines|T5X9ZN2E4M]] defines the angle by the dot product, so it cannot be used here without a circle.
- In the plane, write $u = \|u\| (\cos \alpha, \sin \alpha)$ and $v = \|v\| (\cos \beta, \sin \beta)$ in polar form. Then $u \cdot v = \|u\| \, \|v\| (\cos \alpha \cos \beta + \sin \alpha \sin \beta) = \|u\| \, \|v\| \cos(\alpha - \beta)$ by the addition formula. The angle between the vectors is $|\alpha - \beta|$ or $2\pi - |\alpha - \beta|$, and both have this cosine.

---
tag: X90TK61BYB
kind: proof
name: Proof of the Euler line theorem by vectors
msc: [51M04]
proves: 0VX0CPRQTZ
uses: [0CTNFGYMM2, 0F98FZK14A, 0X7EEWES5G, 0WB619CA0V, 0C9MZY2RNA, 0AFNNTRTJE, 0YMB1676R1, 0KJH6SRFZK, 0S52TNNTH9, 0NPPGHQNXQ, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_line
    locator: A vector proof
---

## Proof

We argue with vectors in $\mathbb{R}^n$.

1. Let $ABC$ be a [[triangle|0CTNFGYMM2]] in $\mathbb{R}^n$, and let $P$ be its plane, the [[affine span|0YMB1676R1]] of $A$, $B$, $C$. Let $W$ be the span of $B - A$ and $C - A$. Then $P = A + W$.
2. The points $A$, $B$, $C$ are not collinear, so $B - A$ and $C - A$ are linearly independent, and $W$ has dimension $2$.
3. Let $O$ be the [[circumcentre|0F98FZK14A]]. It lies in $P$ and satisfies $\norm{A - O} = \norm{B - O} = \norm{C - O} = R$ for some $R \geq 0$.
4. Define the point $K = A + B + C - 2O$. It is the [[affine combination|0KJH6SRFZK]] of $A$, $B$, $C$, $O$ with the weights $1, 1, 1, -2$. These four points lie in $P$, so $K \in P$.
5. With the [[dot product|0S52TNNTH9]], we compute $(K - A) \cdot (C - B) = ((B - O) + (C - O)) \cdot ((C - O) - (B - O))$.
6. This equals $\norm{C - O}^2 - \norm{B - O}^2 = R^2 - R^2 = 0$ by step 3.
7. In the same way, $(K - B) \cdot (A - C) = \norm{A - O}^2 - \norm{C - O}^2 = 0$ and $(K - C) \cdot (B - A) = \norm{B - O}^2 - \norm{A - O}^2 = 0$.
8. Let $H_A$ be the foot of the [[altitude|0C9MZY2RNA]] from $A$, so $H_A = B + k\,(C - B)$ with $k = \frac{(A - B) \cdot (C - B)}{(C - B) \cdot (C - B)}$.
9. Then $(H_A - A) \cdot (C - B) = (B - A) \cdot (C - B) + (A - B) \cdot (C - B) = 0$. Also $H_A \neq A$, since $H_A$ is on the line $BC$ and $A$ is not.
10. The map $\phi \colon W \to \mathbb{R}$, $\phi(w) = w \cdot (C - B)$, is linear. It is not zero, because $C - B \in W$ and $\phi(C - B) = \norm{C - B}^2 > 0$.
11. By the [[rank–nullity theorem|0W4FSW1TVB]], the kernel of $\phi$ has dimension $2 - 1 = 1$. By step 9, it contains the nonzero vector $H_A - A$, so it is the span of $H_A - A$.
12. By steps 4 and 6, $K - A \in W$ and $\phi(K - A) = 0$. So $K - A$ is a multiple of $H_A - A$, and $K$ lies on the line through $A$ and $H_A$.
13. That line contains the altitude from $A$. In the same way, steps 7 to 12 show that $K$ lies on the lines of the altitudes from $B$ and from $C$.
14. The altitude lines from $A$ and $B$ are distinct. Otherwise this line is $AB$, so $B - A$ is orthogonal to $C - B$ and to $C - A$.
   Then $B - A$ is orthogonal to $(C - A) - (C - B) = B - A$, so $A = B$, which is false. Two distinct lines meet in at most one point.
   By the definition of the [[orthocentre|0WB619CA0V]], $H$ is the common point of the three altitude lines. Since $K$ is also a common point, $K = H$, that is, $H - O = (A - O) + (B - O) + (C - O)$.
15. The [[centroid|0X7EEWES5G]] is $G = \frac{1}{3}(A + B + C)$, so $3\,(G - O) = A + B + C - 3O = H - O$. This gives $H = O + 3\,(G - O)$.
16. Each difference of two points of $\set{O, G, H}$ is a multiple of $G - O$, because $H - O = 3(G - O)$ and $H - G = 2(G - O)$. So the span of these differences has dimension at most $1$, and $O$, $G$, $H$ are [[collinear|0AFNNTRTJE]].
17. Now suppose that $O = G$. Put $a = A - G$, $b = B - G$ and $c = C - G$. Then $\norm{a} = \norm{b} = \norm{c} = R$ and $a + b + c = 0$.
18. From $c = -(a + b)$ we get $R^2 = \norm{a + b}^2 = 2R^2 + 2\, a \cdot b$. Hence $a \cdot b = -R^2/2$.
19. Then the [[distance|0NPPGHQNXQ]] satisfies $d(A, B)^2 = \norm{a - b}^2 = 2R^2 - 2\, a \cdot b = 3R^2$.
20. The same computation for the pairs $(b, c)$ and $(c, a)$ gives $d(B, C)^2 = d(C, A)^2 = 3R^2$. So the triangle is equilateral.
21. By contraposition, if $ABC$ is not equilateral, then $O \neq G$. Then there is exactly one line through $O$ and $G$, and by step 16 it contains $H$. This line is the Euler line.

## Idea

The point $A + B + C - 2O$ is easy to test against each altitude. The dot product with a side becomes a difference of two squared radii, which is zero. So this point is the orthocentre, and comparing it with $3(G - O)$ gives the collinearity at once.

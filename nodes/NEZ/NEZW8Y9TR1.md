---
tag: NEZW8Y9TR1
kind: proof
name: Proof of the length formula for the cross product
msc: ["15A72", "51N20"]
topics: [VKVAJ94SKZ]
audience: school
proves: SAZ353S8W0
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [W8V1S8TFWF, 070TXS9AXM, 0ZEHZY85E6, 0XKBKGTCPC, 0RFWW56Y22]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Proof

We combine Lagrange's identity with the formula $a \cdot b = \|a\| \, \|b\| \cos \theta$, then read the result as base times height.

1. Let $a, b \in \mathbb{R}^3$ be nonzero, with [[angle|0ZEHZY85E6]] $\theta \in [0, \pi]$.
2. By [[Lagrange's identity|W8V1S8TFWF]], $\|a \times b\|^2 = \|a\|^2 \|b\|^2 - (a \cdot b)^2$.
3. By the [[geometric formula for the dot product|070TXS9AXM]], $a \cdot b = \|a\| \, \|b\| \cos \theta$.
4. Substituting step 3 into step 2 gives
   $$\|a \times b\|^2 = \|a\|^2 \|b\|^2 (1 - \cos^2 \theta) = \|a\|^2 \|b\|^2 \sin^2 \theta.$$
5. On $[0, \pi]$ the sine is $\geq 0$, and [[lengths|0XKBKGTCPC]] are $\geq 0$. So both sides of $\|a \times b\| = \|a\| \, \|b\| \sin \theta$ are $\geq 0$.
6. Two nonnegative numbers with equal squares are equal, so step 4 gives $\|a \times b\| = \|a\| \, \|b\| \sin \theta$.
7. Area. Draw $a = \overrightarrow{OA}$ and $b = \overrightarrow{OB}$, and take the side $OA$, of length $\|a\|$, as the base.
8. The height is the distance from $B$ to the line $OA$. In the right triangle with hypotenuse $OB$, it is $\|b\| \sin \theta$.
9. The area of a parallelogram is base times height, so it is $\|a\| \, \|b\| \sin \theta = \|a \times b\|$.
10. Zero test, case 1: $a = 0$ or $b = 0$. Then $a \times b = 0$ by the formula, and $a = 0 \cdot b$ or $b = 0 \cdot a$, so the vectors are parallel.
11. Case 2: $a, b \neq 0$. Since $\|a\|, \|b\| > 0$, step 6 shows that $a \times b = 0$ if and only if $\sin \theta = 0$.
12. On $[0, \pi]$, $\sin \theta = 0$ if and only if $\theta = 0$ or $\theta = \pi$.
13. By step 3, $\theta \in \{0, \pi\}$ means $|a \cdot b| = \|a\| \, \|b\|$. By the equality case of the [[Cauchy-Schwarz inequality|0RFWW56Y22]], this means $b = ca$ for some $c$.
14. So in both cases, $a \times b = 0$ if and only if $a$ and $b$ are parallel.

## Idea

Lagrange's identity gives the square of the length as $\|a\|^2 \|b\|^2 - (a \cdot b)^2$.
Writing $a \cdot b$ with the cosine turns this into $\|a\|^2 \|b\|^2 \sin^2 \theta$, and taking square roots is safe because both sides are nonnegative.
The area then comes from base times height, where the height is $\|b\| \sin \theta$.

## Variants

Step 13 can be done without the Cauchy-Schwarz inequality.
Suppose $a \times b = 0$ and $a_1 \neq 0$.
The third and second components of $a \times b$ give $a_1 b_2 = a_2 b_1$ and $a_1 b_3 = a_3 b_1$, so
$$b_2 = \frac{b_1}{a_1}\, a_2, \qquad b_3 = \frac{b_1}{a_1}\, a_3,$$
and therefore $b = \frac{b_1}{a_1}\, a$.
The cases $a_2 \neq 0$ and $a_3 \neq 0$ work the same way.

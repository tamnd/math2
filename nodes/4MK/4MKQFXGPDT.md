---
tag: 4MKQFXGPDT
kind: proof
name: Proof that the scalar triple product is a determinant
msc: [15A72]
proves: 059Q2XWJDC
uses: [0N5N15HWZ7, 0S52TNNTH9, 00KDZRW4C0, 0C08BQ3M05, 0XPKR18APA, 0ZN2J42SK7]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
---

## Proof

We expand both sides and compare them.

1. Let $a = (a_1, a_2, a_3)$, $b = (b_1, b_2, b_3)$ and $c = (c_1, c_2, c_3)$. Let $M$ be the $3 \times 3$ matrix with the rows $a$, $b$ and $c$.
2. By the definition of the [[cross product|0N5N15HWZ7]], $b \times c = (b_2 c_3 - b_3 c_2, \; b_3 c_1 - b_1 c_3, \; b_1 c_2 - b_2 c_1)$.
3. By the definition of the [[dot product|0S52TNNTH9]],
$$a \cdot (b \times c) = a_1 (b_2 c_3 - b_3 c_2) + a_2 (b_3 c_1 - b_1 c_3) + a_3 (b_1 c_2 - b_2 c_1).$$
4. By the [[Laplace expansion along the first row|0C08BQ3M05]], $\det M = a_1 M_{11} - a_2 M_{12} + a_3 M_{13}$. Here $M_{1j}$ is the [[minor|0XPKR18APA]]: the [[determinant|00KDZRW4C0]] of $M$ without row $1$ and column $j$.
5. By the [[formula for a $2 \times 2$ determinant|0ZN2J42SK7]], the minors are
$$M_{11} = b_2 c_3 - b_3 c_2, \quad M_{12} = b_1 c_3 - b_3 c_1, \quad M_{13} = b_1 c_2 - b_2 c_1.$$
6. Thus $\det M = a_1 (b_2 c_3 - b_3 c_2) - a_2 (b_1 c_3 - b_3 c_1) + a_3 (b_1 c_2 - b_2 c_1)$.
7. The middle term is $-a_2 (b_1 c_3 - b_3 c_1) = a_2 (b_3 c_1 - b_1 c_3)$. So the expression in step 6 is the expression in step 3.
8. Hence $a \cdot (b \times c) = \det M$, which is the statement.

## Idea

The coordinates of $b \times c$ are exactly the signed $2 \times 2$ minors that the Laplace expansion along the first row multiplies by $a_1$, $a_2$ and $a_3$. So the dot product with $a$ is this expansion term by term.

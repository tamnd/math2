---
tag: B8J28FSK1M
kind: proof
name: Proof of the geometric formula for the dot product
msc: [51N20]
proves: 070TXS9AXM
uses: [0ZEHZY85E6, 0XKBKGTCPC, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Equivalence of the definitions
---

## Proof

We argue directly from the definition of the angle.

1. Let $u$ and $v$ be nonzero vectors in $\R^n$, and let $\theta$ be the [[angle between them|0ZEHZY85E6]].
2. Since $u \neq 0$, some coordinate $u_i$ is nonzero. So the [[length|0XKBKGTCPC]] $\norm{u} = \sqrt{u_1^2 + \dots + u_n^2}$ is positive. In the same way $\norm{v} > 0$.
3. By the definition of the angle, $\theta$ is the number in $[0, \pi]$ with $\cos \theta = \dfrac{u \cdot v}{\norm{u} \, \norm{v}}$. Here $u \cdot v$ is the [[dot product|0S52TNNTH9]].
4. The denominator $\norm{u} \, \norm{v}$ is positive by step 2. We multiply both sides of the equation in step 3 by it.
5. This gives $u \cdot v = \norm{u} \, \norm{v} \cos \theta$, which is the statement.

## Idea

In $\R^n$ the angle between two vectors is defined through its cosine: the dot product divided by the product of the lengths. The formula is this definition with the denominator cleared. The geometric content is that this angle agrees with the angle of school geometry, which the law of cosines confirms.

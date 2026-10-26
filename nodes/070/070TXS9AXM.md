---
tag: 070TXS9AXM
kind: statement
role: proposition
name: Geometric formula for the dot product
msc: [51N20]
uses: [0ZEHZY85E6, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Equivalence of the definitions
---

## Statement

Let $n$ be a positive integer, and let $u$ and $v$ be nonzero vectors in $\mathbb{R}^n$.
Let $u \cdot v = u_1 v_1 + \dots + u_n v_n$ be their dot product, let $\|u\|$ and $\|v\|$ be their [[lengths|0XKBKGTCPC]], and let $\theta$ be the [[angle between them|0ZEHZY85E6]].
Then
$$u \cdot v = \|u\| \, \|v\| \cos \theta.$$

## Remarks

When the angle is defined by its cosine, the formula follows from the definition. The content is that this angle is the angle of elementary geometry. In the plane, write $u = \|u\| (\cos \alpha, \sin \alpha)$ and $v = \|v\| (\cos \beta, \sin \beta)$. Then $u \cdot v = \|u\| \, \|v\| \cos(\alpha - \beta)$ by the addition formula for the cosine.
The formula also follows from the law of cosines in the triangle with the vertices $0$, $u$ and $v$.
If $u = 0$ or $v = 0$, then both sides are $0$ for each value of $\theta$.

## Explanations

### L1 human

The dot product is large and positive when two vectors point in nearly the same direction. It is zero when they are perpendicular, and negative when they point in nearly opposite directions. For unit vectors $u$ and $v$, the dot product is just the cosine of the angle between them.

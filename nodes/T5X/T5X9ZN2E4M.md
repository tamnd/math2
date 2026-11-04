---
tag: T5X9ZN2E4M
kind: proof
name: Proof of the law of cosines with the dot product
msc: [51M04]
proves: 060ZVZBV3E
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_cosines
    locator: Using vectors
---

## Proof

We expand the square of the length of a difference of two vectors.

1. Let $u = A - C$ and $v = B - C$. With the [[Euclidean distance|0NPPGHQNXQ]] and the [[length|0XKBKGTCPC]], $\norm{u} = b$ and $\norm{v} = a$.
2. We have $u - v = A - B$, so $c^2 = \norm{u - v}^2 = (u - v) \cdot (u - v)$, with the [[dot product|0S52TNNTH9]].
3. The dot product is bilinear and symmetric. So $(u - v) \cdot (u - v) = u \cdot u - 2 \, u \cdot v + v \cdot v = b^2 + a^2 - 2 \, u \cdot v$.
4. The vertices of the [[triangle|0CTNFGYMM2]] are not collinear, so they are distinct. Thus $u \neq 0$ and $v \neq 0$, and the [[angle|0GJAJC6TNZ]] $\gamma$ at $C$ is defined.
5. By the definition of the angle at $C$, $\cos \gamma = \dfrac{u \cdot v}{\norm{u} \, \norm{v}} = \dfrac{u \cdot v}{ab}$. So $u \cdot v = ab \cos \gamma$.
6. Steps 2, 3 and 5 give $c^2 = a^2 + b^2 - 2ab \cos \gamma$.

## Idea

Put the vertex $C$ at the origin. The side $AB$ is the difference of the two vectors from $C$. Squaring its length produces the two squared sides and a cross term, and the cross term is the dot product, which is $ab \cos \gamma$.

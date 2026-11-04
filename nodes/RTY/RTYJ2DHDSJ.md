---
tag: RTYJ2DHDSJ
kind: proof
name: Proof of Thales's theorem by the dot product
msc: [51M04]
proves: 0GSDHYMA1T
uses: [060W5CBZP6, 0S706JBZBG, 0GJAJC6TNZ, 0S52TNNTH9, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Thales%27s_theorem
    locator: Fourth proof
---

## Proof

We compute one dot product in two ways.

1. Let $A$, $B$, $C$ be distinct points, and let $O$ be the [[midpoint|0S706JBZBG]] of $A$ and $C$, so $O = \frac{1}{2}(A + C)$. Put $u = A - O$ and $z = O - B$.
2. Then $C - O = -u$, so $A - B = u + z$ and $C - B = -u + z$.
3. Hence the [[dot product|0S52TNNTH9]] is $(A - B) \cdot (C - B) = (z + u) \cdot (z - u) = \norm{z}^2 - \norm{u}^2 = \norm{B - O}^2 - \norm{A - O}^2$.
4. The vectors $A - B$ and $C - B$ are nonzero, since $B \neq A$ and $B \neq C$. By the definition of the [[angle|0GJAJC6TNZ]] and [[the criterion for perpendicular vectors|03NK6RSRQ1]], $\angle ABC = \pi/2$ if and only if $(A - B) \cdot (C - B) = 0$.
5. By steps 3 and 4, $\angle ABC = \pi/2$ if and only if $\norm{B - O} = \norm{A - O}$.
6. Direct statement: $A$, $B$, $C$ lie on a [[circle|060W5CBZP6]] whose centre is $O$. So $\norm{B - O}$ and $\norm{A - O}$ are both the radius, and step 5 gives $\angle ABC = \pi/2$.
7. Converse: if $\angle ABC = \pi/2$, then step 5 gives $\norm{B - O} = \norm{A - O} = \frac{1}{2}\norm{A - C}$. This radius is positive since $A \neq C$.
8. The circle with the diameter $AC$ is the circle with the centre $O$ and the radius $\frac{1}{2}\norm{A - C}$. By step 7, $B$ lies on it.

## Idea

Measured from the centre $O$, the two sides of the angle at $B$ are $z + u$ and $z - u$. Their dot product is the difference of the squares of $\norm{z}$ and $\norm{u}$. It vanishes exactly when $B$ is as far from $O$ as $A$ is.

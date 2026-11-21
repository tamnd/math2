---
tag: HX1NMQ2B2P
kind: proof
name: Proof that vectors are perpendicular if and only if their dot product is zero
msc: ["51N20", "15A63"]
topics: [VKVAJ94SKZ]
audience: school
proves: 03NK6RSRQ1
methods: [0WCP0PVET6, 0NTF6DMVAP]
uses: [070TXS9AXM, 0PRAS55318, 0ZEHZY85E6, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Scalar projection and first properties
---

## Proof

We treat the zero vector first, and for nonzero vectors we use the formula $u \cdot v = \|u\| \, \|v\| \cos \theta$.

1. Case 1: $u = 0$ or $v = 0$. Say $u = 0$; then $u \cdot v = 0 \cdot v_1 + \dots + 0 \cdot v_n = 0$ by the definition of the [[dot product|0S52TNNTH9]]. Also $u \perp v$ by the convention for the zero vector, so both sides of the equivalence are true. The case $v = 0$ is the same.
2. Case 2: $u \neq 0$ and $v \neq 0$. Let $\theta \in [0, \pi]$ be the [[angle between $u$ and $v$|0ZEHZY85E6]].
3. We have $u \cdot v = \|u\| \, \|v\| \cos \theta$. For $n = 2$ or $3$ this is the [[geometric formula for the dot product|070TXS9AXM]]; for any $n$ it is the [[definition of the angle|0PRAS55318]], multiplied by $\|u\| \, \|v\|$.
4. A nonzero vector has a nonzero component, so its [[length|0XKBKGTCPC]] is positive, and $\|u\| \, \|v\| > 0$.
5. By steps 3 and 4 we may divide by $\|u\| \, \|v\|$, so $u \cdot v = 0$ if and only if $\cos \theta = 0$.
6. The cosine decreases strictly on $[0, \pi]$, and $\cos \tfrac{\pi}{2} = 0$, so $\cos \theta = 0$ if and only if $\theta = \tfrac{\pi}{2}$.
7. By steps 5 and 6, $u \cdot v = 0$ if and only if $\theta = \tfrac{\pi}{2}$, that is, if and only if $u \perp v$.
8. For the last claim, suppose that $w \perp v$ for every $v$. Take $v = w$; the equivalence just proved gives $w \cdot w = \|w\|^2 = 0$, so $w = 0$.
9. The two cases cover all pairs $u, v$, so the theorem holds.

## Idea

The dot product is the product of the two lengths and the cosine of the angle.
For nonzero vectors the lengths are positive, so the dot product is zero exactly when the cosine is zero, and on $[0, \pi]$ the cosine is zero only at the right angle.
The zero vector has no angle, so it needs its own case, and the convention makes that case agree with the dot product.

## Variants

For $n = 2$ or $3$ there is a proof by the Pythagorean theorem that avoids the cosine.
Expand $\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\, u \cdot v$ in coordinates.
If $u$ and $v$ are not parallel, the angle at $O$ in the triangle $O$, $U$, $V$ is right exactly when $\|u - v\|^2 = \|u\|^2 + \|v\|^2$, by the [[Pythagorean theorem|0VP3A1290K]] and its converse, and that holds exactly when $u \cdot v = 0$.
If $u$ and $v$ are parallel and nonzero, the triangle is flat; then $v = cu$ with $c \neq 0$, so $u \cdot v = c\|u\|^2 \neq 0$, and the angle is $0$ or $\pi$, not a right angle.

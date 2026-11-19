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

We treat the zero vector first, and then we use the formula $u \cdot v = \|u\| \, \|v\| \cos \theta$.

1. Case 1: $u = 0$. Then $u \cdot v = 0 \cdot v_1 + \dots + 0 \cdot v_n = 0$, by the definition of the [[dot product|0S52TNNTH9]].
2. In case 1, $u \perp v$ holds by the convention for the zero vector. So both sides of the equivalence are true.
3. Case 2: $v = 0$. The same argument as in steps 1 and 2 shows that both sides are true.
4. Case 3: $u \neq 0$ and $v \neq 0$. Let $\theta \in [0, \pi]$ be the [[angle between $u$ and $v$|0ZEHZY85E6]].
5. For $n = 2$ or $3$, the [[geometric formula for the dot product|070TXS9AXM]] gives $u \cdot v = \|u\| \, \|v\| \cos \theta$.
6. For any $n$, the [[definition of the angle|0PRAS55318]] gives the same equation, after multiplication by $\|u\| \, \|v\|$.
7. A nonzero vector has a nonzero component, so its [[length|0XKBKGTCPC]] is positive. Thus $\|u\| \, \|v\| > 0$.
8. By steps 5 to 7, $u \cdot v = 0$ if and only if $\cos \theta = 0$.
9. The cosine decreases strictly on $[0, \pi]$, and $\cos \tfrac{\pi}{2} = 0$. So $\cos \theta = 0$ if and only if $\theta = \tfrac{\pi}{2}$.
10. By steps 8 and 9, $u \cdot v = 0$ if and only if $\theta = \tfrac{\pi}{2}$, that is, if and only if $u \perp v$.
11. For the last claim: if $w \perp v$ for every $v$, take $v = w$. Then $w \cdot w = \|w\|^2 = 0$, so $w = 0$.
12. The three cases cover all pairs $u, v$. This proves the theorem.

## Idea

The dot product is the product of the two lengths and the cosine of the angle.
For nonzero vectors the lengths are positive, so the dot product is zero exactly when the cosine is zero.
The cosine vanishes on $[0, \pi]$ only at the right angle.
The zero vector needs a separate case, because it has no angle.

## Variants

- Proof by the Pythagorean theorem, for $n = 2$ or $3$ and nonzero $u$ and $v$. Expand $\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\, u \cdot v$ in coordinates. The angle at $O$ in the triangle $O$, $U$, $V$ is right if and only if $\|u - v\|^2 = \|u\|^2 + \|v\|^2$, by the [[Pythagorean theorem|0VP3A1290K]] and its converse; this holds if and only if $u \cdot v = 0$.
- If $u$ and $v$ are parallel, the triangle in the first variant is flat. Then $v = cu$ with $c \neq 0$, so $u \cdot v = c\|u\|^2 \neq 0$, and the angle is $0$ or $\pi$, not a right angle.

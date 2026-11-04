---
tag: N5HWCPJZ5N
kind: proof
name: Proof of the isosceles triangle theorem with the dot product
msc: [51M04]
proves: 056VS31A0J
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 0CWDVN132S]
sources:
  - url: https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Geometry/Euclidean/Triangle.lean
    locator: angle_eq_angle_of_dist_eq
---

## Proof

We show that the two base angles have the same cosine.

1. Let $b = d(A, C)$, $c = d(A, B)$ and $a = d(B, C)$, with the [[Euclidean distance|0NPPGHQNXQ]] $d$. By hypothesis $b = c$.
2. The vertices of the [[triangle|0CTNFGYMM2]] are not collinear, so they are pairwise distinct. Thus $a, b, c > 0$, and the [[angles|0GJAJC6TNZ]] at $B$ and $C$ are defined.
3. For vectors $x, y \in \R^n$, the [[dot product|0S52TNNTH9]] is bilinear and symmetric. So $\norm{x - y}^2 = \norm{x}^2 - 2 \, x \cdot y + \norm{y}^2$, with the [[length|0XKBKGTCPC]] $\norm{\cdot}$.
4. With $x = A - B$ and $y = C - B$, we have $x - y = A - C$. Step 3 gives $b^2 = c^2 - 2 \, x \cdot y + a^2$. Since $b = c$, this is $(A - B) \cdot (C - B) = a^2 / 2$.
5. With $x = A - C$ and $y = B - C$, we have $x - y = A - B$. Step 3 gives $c^2 = b^2 - 2 \, x \cdot y + a^2$. Since $b = c$, this is $(A - C) \cdot (B - C) = a^2 / 2$.
6. By the definition of the angle and step 4, $\cos \angle ABC = \dfrac{a^2 / 2}{c \, a} = \dfrac{a}{2c}$.
7. By the definition of the angle and step 5, $\cos \angle ACB = \dfrac{a^2 / 2}{b \, a} = \dfrac{a}{2b} = \dfrac{a}{2c}$.
8. Both angles lie in $[0, \pi]$, and they have the same cosine. The cosine is injective on $[0, \pi]$, by the uniqueness in the definition of the [[arccosine|0CWDVN132S]].
9. Hence $\angle ABC = \angle ACB$.

## Idea

The cosine of an angle of a triangle depends only on the three sides. At $B$ and at $C$ the formula uses the same numbers once $d(A, B) = d(A, C)$. Equal cosines in $[0, \pi]$ mean equal angles.

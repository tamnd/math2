---
tag: JD65S6DHQA
kind: proof
name: Proof of the law of sines from the law of cosines
msc: [51M04]
proves: 0PASQ34GHG
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0AFNNTRTJE, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 060ZVZBV3E, 0CRMGPAH83, 0RFWW56Y22, 08WFZP6P89, 03H7WZ4T3K]
sources:
  - url: https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Geometry/Euclidean/Triangle.lean
    locator: sin_angle_mul_norm_eq_sin_angle_mul_norm
---

## Proof

We compute each sine from the three sides and find that the three quotients are given by one symmetric formula.

1. The vertices of the [[triangle|0CTNFGYMM2]] are not [[collinear|0AFNNTRTJE]], so they are distinct. Thus $a, b, c > 0$, and the three [[angles|0GJAJC6TNZ]] are defined.
2. We apply the [[law of cosines|060ZVZBV3E]] with the vertices renamed, so that $A$ plays the role of $C$. It gives $a^2 = b^2 + c^2 - 2bc \cos \alpha$. So $\cos \alpha = \dfrac{b^2 + c^2 - a^2}{2bc}$.
3. In the same way, $\cos \beta = \dfrac{c^2 + a^2 - b^2}{2ca}$ and $\cos \gamma = \dfrac{a^2 + b^2 - c^2}{2ab}$.
4. Let $Q = 4b^2c^2 - (b^2 + c^2 - a^2)^2$. Two differences of squares give $Q = \left( a^2 - (b - c)^2 \right) \left( (b + c)^2 - a^2 \right) = (a - b + c)(a + b - c)(b + c - a)(a + b + c)$.
5. A permutation of $a$, $b$, $c$ only permutes the four factors in step 4. So step 4 with the letters renamed gives $Q = 4c^2a^2 - (c^2 + a^2 - b^2)^2 = 4a^2b^2 - (a^2 + b^2 - c^2)^2$.
6. Let $x = B - A$ and $y = C - A$. With the [[length|0XKBKGTCPC]] and the [[dot product|0S52TNNTH9]], $\norm{x} = c$, $\norm{y} = b$ and $x \cdot y = bc \cos \alpha = \frac{1}{2}(b^2 + c^2 - a^2)$. So $Q = 4 \left( \norm{x}^2 \norm{y}^2 - (x \cdot y)^2 \right)$.
7. Every difference of two vertices lies in the span of $x$ and $y$. Since the vertices are not collinear, this span has dimension $2$. So $x$ and $y$ are [[linearly independent|0CRMGPAH83]].
8. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]] and its case of equality, $(x \cdot y)^2 < \norm{x}^2 \norm{y}^2$. So $Q > 0$. Let $R = \sqrt{Q} > 0$.
9. The [[sine|08WFZP6P89]] is nonnegative on $[0, \pi]$, and $\alpha \in [0, \pi]$. By the [[identity $\sin^2 + \cos^2 = 1$|03H7WZ4T3K]] and step 2, $\sin^2 \alpha = 1 - \cos^2 \alpha = \dfrac{Q}{4b^2c^2}$. So $\sin \alpha = \dfrac{R}{2bc} > 0$.
10. In the same way, steps 3 and 5 give $\sin \beta = \dfrac{R}{2ca} > 0$ and $\sin \gamma = \dfrac{R}{2ab} > 0$. So the three quotients are defined.
11. By steps 9 and 10, $\dfrac{a}{\sin \alpha} = \dfrac{2abc}{R}$, $\dfrac{b}{\sin \beta} = \dfrac{2abc}{R}$ and $\dfrac{c}{\sin \gamma} = \dfrac{2abc}{R}$.
12. Hence $\dfrac{a}{\sin \alpha} = \dfrac{b}{\sin \beta} = \dfrac{c}{\sin \gamma}$.

## Idea

The law of cosines gives each cosine from the sides, and then each sine. All three sines have the same numerator $\sqrt{Q}$, a symmetric expression in the sides, which is four times the area. Dividing a side by the sine of the opposite angle then gives $2abc / \sqrt{Q}$ every time.

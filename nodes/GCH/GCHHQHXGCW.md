---
tag: GCHHQHXGCW
kind: proof
name: Proof of the angle sum of a triangle with sines and cosines
msc: [51M04]
proves: 05MDKQBEAF
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0AFNNTRTJE, 0NPPGHQNXQ, 0XKBKGTCPC, 0S52TNNTH9, 0CRMGPAH83, 0RFWW56Y22, 08WFZP6P89, 03H7WZ4T3K, 028XEQCE88, 01A8JGR4JM, 0CWDVN132S]
sources:
  - url: https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Geometry/Euclidean/Triangle.lean
    locator: angle_add_angle_add_angle_eq_pi
---

## Proof

We compute the cosine and the sine of $\alpha + \beta$ from the side lengths, and then compare with $\pi - \gamma$.

1. Let $\alpha = \angle BAC$, $\beta = \angle CBA$ and $\gamma = \angle ACB$. Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$, with the [[Euclidean distance|0NPPGHQNXQ]] $d$.
2. The vertices of a [[triangle|0CTNFGYMM2]] are not [[collinear|0AFNNTRTJE]]. So they are pairwise distinct, and $a, b, c > 0$. Thus the three [[angles|0GJAJC6TNZ]] are defined.
3. For vectors $x, y \in \R^n$, the [[dot product|0S52TNNTH9]] is bilinear and symmetric. So $\norm{x - y}^2 = \norm{x}^2 - 2 \, x \cdot y + \norm{y}^2$, with the [[length|0XKBKGTCPC]] $\norm{\cdot}$.
4. Let $x = B - A$ and $y = C - A$. Then $x - y = B - C$, and step 3 gives $a^2 = c^2 - 2 \, x \cdot y + b^2$. So $x \cdot y = \frac{1}{2}(b^2 + c^2 - a^2)$.
5. By the definition of the angle at $A$, $\cos \alpha = \dfrac{x \cdot y}{bc} = \dfrac{b^2 + c^2 - a^2}{2bc}$. The same computation at $B$ and at $C$ gives $\cos \beta = \dfrac{c^2 + a^2 - b^2}{2ca}$ and $\cos \gamma = \dfrac{a^2 + b^2 - c^2}{2ab}$.
6. Let $Q = 4b^2c^2 - (b^2 + c^2 - a^2)^2$. By step 4, $Q = 4 \left( \norm{x}^2 \norm{y}^2 - (x \cdot y)^2 \right)$.
7. Every difference of two vertices lies in the span of $x$ and $y$; for example $C - B = y - x$. Since the vertices are not collinear, this span has dimension $2$. So $x$ and $y$ are [[linearly independent|0CRMGPAH83]].
8. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]] and its case of equality, $(x \cdot y)^2 < \norm{x}^2 \norm{y}^2$. So $Q > 0$. Let $R = \sqrt{Q} > 0$.
9. Two differences of squares give $Q = \left( a^2 - (b - c)^2 \right) \left( (b + c)^2 - a^2 \right) = (a - b + c)(a + b - c)(b + c - a)(a + b + c)$.
10. A permutation of $a$, $b$, $c$ only permutes the four factors in step 9. So the computation of step 9 with the letters renamed also gives $Q = 4c^2a^2 - (c^2 + a^2 - b^2)^2 = 4a^2b^2 - (a^2 + b^2 - c^2)^2$.
11. The [[sine|08WFZP6P89]] is nonnegative on $[0, \pi]$, and $\alpha \in [0, \pi]$. By the [[identity $\sin^2 + \cos^2 = 1$|03H7WZ4T3K]] and step 5, $\sin^2 \alpha = 1 - \cos^2 \alpha = \dfrac{Q}{4b^2c^2}$. So $\sin \alpha = \dfrac{R}{2bc}$.
12. In the same way, steps 5 and 10 give $\sin \beta = \dfrac{R}{2ca}$ and $\sin \gamma = \dfrac{R}{2ab}$. All three sines are positive.
13. By the [[addition formula|028XEQCE88]], $\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta = \dfrac{(b^2 + c^2 - a^2)(c^2 + a^2 - b^2) - Q}{4abc^2}$.
14. We insert $Q = 4b^2c^2 - (b^2 + c^2 - a^2)^2$ in the numerator of step 13. The numerator becomes $(b^2 + c^2 - a^2) \cdot 2c^2 - 4b^2c^2 = 2c^2 (c^2 - a^2 - b^2)$.
15. So $\cos(\alpha + \beta) = \dfrac{c^2 - a^2 - b^2}{2ab} = -\cos \gamma$, by step 5.
16. By the addition formula, $\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta = \dfrac{R \left( (c^2 + a^2 - b^2) + (b^2 + c^2 - a^2) \right)}{4abc^2}$.
17. The sum in the numerator of step 16 is $2c^2$. So $\sin(\alpha + \beta) = \dfrac{R}{2ab} = \sin \gamma > 0$.
18. By [[$\sin \pi = 0$|01A8JGR4JM]] and $\sin 0 = 0$, step 12 shows that no angle is $0$ or $\pi$. So $\alpha, \beta \in (0, \pi)$, and $0 < \alpha + \beta < 2\pi$.
19. Suppose that $\alpha + \beta > \pi$, and let $z = \alpha + \beta - \pi$. Then $z \in (0, \pi)$, so $\sin z \geq 0$.
20. By the addition formula and [[$\cos \pi = -1$, $\sin \pi = 0$|01A8JGR4JM]], $\sin(\alpha + \beta) = \sin(z + \pi) = -\sin z \leq 0$. This contradicts step 17. So $\alpha + \beta \leq \pi$.
21. By the addition formula, $\cos(\pi - \gamma) = \cos \pi \cos(-\gamma) - \sin \pi \sin(-\gamma) = -\cos \gamma$. Here we use that the cosine is even.
22. Both $\alpha + \beta$ and $\pi - \gamma$ lie in $[0, \pi]$, and by steps 15 and 21 they have the same cosine.
23. The cosine is injective on $[0, \pi]$, by the uniqueness in the definition of the [[arccosine|0CWDVN132S]]. So $\alpha + \beta = \pi - \gamma$.
24. Hence $\angle BAC + \angle CBA + \angle ACB = \pi$.

## Idea

The law of cosines gives the cosine of each angle from the three sides, and then the sine as well. With the addition formulas, $\alpha + \beta$ has the same cosine and sine as $\pi - \gamma$. The sine condition rules out $\alpha + \beta > \pi$, and on $[0, \pi]$ the cosine determines the angle.

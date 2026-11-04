---
tag: PM8PCNPR23
kind: proof
name: Proof of Heron's formula from the law of cosines
msc: [51M25]
proves: 0FRBZ2X4HJ
uses: [065JWMZW86, 0CTNFGYMM2, 0NPPGHQNXQ, 0GJAJC6TNZ, 060ZVZBV3E, 08WFZP6P89, 03H7WZ4T3K]
sources:
  - url: https://en.wikipedia.org/wiki/Heron%27s_formula
    locator: Trigonometric proof using the law of cosines
---

## Proof

We compute $\sin \gamma$ from the sides and insert it in the formula $T = \frac{1}{2} ab \sin \gamma$.

1. Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$, with the [[Euclidean distance|0NPPGHQNXQ]] $d$. Let $\gamma = \angle ACB$ be the [[angle|0GJAJC6TNZ]] at $C$, the angle between the sides of lengths $a$ and $b$. The vertices are distinct, so $a, b > 0$.
2. The [[area of the triangle|065JWMZW86]] is $T = \frac{1}{2} ab \sin \gamma$.
3. By the [[law of cosines|060ZVZBV3E]], $c^2 = a^2 + b^2 - 2ab \cos \gamma$. So $\cos \gamma = \dfrac{a^2 + b^2 - c^2}{2ab}$.
4. The [[sine|08WFZP6P89]] is nonnegative on $[0, \pi]$, and $\gamma \in [0, \pi]$. By the [[identity $\sin^2 + \cos^2 = 1$|03H7WZ4T3K]], $\sin \gamma = \sqrt{1 - \cos^2 \gamma}$.
5. By step 3, $1 - \cos^2 \gamma = \dfrac{4a^2b^2 - (a^2 + b^2 - c^2)^2}{4a^2b^2}$. Let $Q = 4a^2b^2 - (a^2 + b^2 - c^2)^2$. Step 4 shows $Q \geq 0$, and $\sin \gamma = \dfrac{\sqrt{Q}}{2ab}$.
6. By steps 2 and 5, $T = \frac{1}{2} ab \cdot \dfrac{\sqrt{Q}}{2ab} = \dfrac{\sqrt{Q}}{4}$.
7. As a difference of squares, $Q = (2ab - a^2 - b^2 + c^2)(2ab + a^2 + b^2 - c^2) = \left( c^2 - (a - b)^2 \right) \left( (a + b)^2 - c^2 \right)$.
8. Two more differences of squares give $Q = (c - a + b)(c + a - b)(a + b - c)(a + b + c)$.
9. Since $a + b + c = 2s$, the four factors are $-a + b + c = 2(s - a)$, $a - b + c = 2(s - b)$, $a + b - c = 2(s - c)$ and $a + b + c = 2s$.
10. So $Q = 16 \, s (s - a)(s - b)(s - c)$.
11. By steps 6 and 10, $T = \dfrac{\sqrt{16 \, s(s - a)(s - b)(s - c)}}{4} = \sqrt{s (s - a)(s - b)(s - c)}$.

## Idea

Two sides and the angle between them give the area, and the law of cosines gives that angle from the three sides. The expression under the square root factors completely by differences of squares. Each factor is twice $s$ or twice $s$ minus a side.

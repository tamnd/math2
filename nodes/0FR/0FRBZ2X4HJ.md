---
tag: 0FRBZ2X4HJ
kind: statement
role: theorem
name: Heron's formula
aliases: [heros-formula]
msc: [51M25]
uses: [065JWMZW86, 0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Heron%27s_formula
    locator: lead section
same_as:
  wikidata: Q182714
  wikipedia: Heron's formula
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane, with the side lengths $a$, $b$ and $c$. Let $s = \frac{1}{2}(a + b + c)$ be its semiperimeter.
Then the [[area|065JWMZW86]] $T$ of the triangle is
$$T = \sqrt{s (s - a)(s - b)(s - c)}.$$

## Remarks

An equivalent form without $s$ is $16 T^2 = (a + b + c)(-a + b + c)(a - b + c)(a + b - c)$.
For example, the triangle with the sides $4$, $13$ and $15$ has $s = 16$ and $T = \sqrt{16 \cdot 12 \cdot 3 \cdot 1} = 24$.
One proof uses the [[law of cosines|060ZVZBV3E]] to get $\cos \gamma$ from the sides, and then $T = \frac{1}{2} a b \sin \gamma$.

## History

The formula carries the name of Heron of Alexandria, who gave a proof in his Metrica in the 1st century. It was possibly known earlier. Qin Jiushao published an equivalent formula in 1247.

## Explanations

### L1 human

Heron's formula gives the area of a triangle when you know only its three sides. You do not need a height or an angle. For the right triangle with the sides $3$, $4$, $5$: $s = 6$, and $\sqrt{6 \cdot 3 \cdot 2 \cdot 1} = 6$, which is also $\frac{1}{2} \cdot 3 \cdot 4$.

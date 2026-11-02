---
tag: FQ505YSHNA
kind: definition
name: Semiprime ring
msc: [16N60]
defines: 5F0YMCV50R
uses: [0894J980RK, 0DDA6CY7GJ, C2H26BYWHE]
sources:
  - url: https://en.wikipedia.org/wiki/Semiprime_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
$R$ is *semiprime* if, for every $a \in R$, the condition $aRa = 0$ implies $a = 0$.

## Remarks

Equivalent forms: $R$ has no nonzero [[nilpotent ideal|C2H26BYWHE]]; for every [[two-sided ideal|0DDA6CY7GJ]] $I$, $I^2 = 0$ implies $I = 0$; the [[prime radical|WF117EJ2HF]] of $R$ is $0$.
Example: $\Q \times \Q$ is semiprime: if $a = (a_1, a_2)$ and $aRa = 0$, then taking $r = 1$ gives $a_1^2 = a_2^2 = 0$, so $a = 0$.
Non-example: in the ring $R$ of upper triangular $2 \times 2$ matrices over $\Q$, the matrix unit $a = e_{12}$ is nonzero and $e_{12} R e_{12} = 0$.
Every [[prime ring|Z9TJSZZYG1]] is semiprime.
A commutative ring is semiprime if and only if it is [[reduced|SZHY975FFX]].

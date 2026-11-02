---
tag: WKG2DZDEBT
kind: definition
name: Nil ideal
msc: [16N40]
defines: NZ1G9WRWFB
uses: [0894J980RK, 0N9R5NN6TW, 5N2CJZ47D4, 0DDA6CY7GJ]
sources:
  - url: https://en.wikipedia.org/wiki/Nil_ideal
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
Let $I$ be a [[left ideal|5N2CJZ47D4]], right ideal or [[two-sided ideal|0DDA6CY7GJ]] of $R$.
The ideal $I$ is *nil* if every element of $I$ is [[nilpotent|0N9R5NN6TW]].
This means that for each $a \in I$ there is an integer $n \ge 1$ with $a^n = 0$.

## Remarks

Example: in $\Z/8\Z$, the ideal $I = 2\Z/8\Z$ is nil.
The check: every element of $I$ is $2b$ for some residue $b$, and $(2b)^3 = 8b^3 = 0$.
Non-example: in $\Z$, the ideal $2\Z$ is not nil, since $2^n \ne 0$ for all $n \ge 1$.
In a commutative ring the nil ideals are the ideals contained in the [[nilradical|2K5GKVZR78]].
The exponent $n$ may depend on the element, and there need not be a common bound.

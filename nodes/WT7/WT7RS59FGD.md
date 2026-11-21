---
tag: WT7RS59FGD
kind: example
name: An equation that is consistent over the rationals and inconsistent over the field with two elements
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0X6V9B1V10]
uses: [0X6V9B1V10, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/GF(2)
    locator: lead section
---

## Example

Consider the single equation $2x = 1$ in one unknown, and read it over two fields.

1. Over $\mathbb{Q}$, the coefficient $2$ is nonzero, so we divide by it and get $x = \tfrac12$. Check: $2 \cdot \tfrac12 = 1$. So the equation is [[consistent|0X6V9B1V10]] over $\mathbb{Q}$.
2. Over the [[finite field|0ZXZ82FTX2]] $\mathbb{F}_2 = \set{0, 1}$, we have $2 = 1 + 1 = 0$. So the equation reads $0 \cdot x = 1$.
3. Both elements of $\mathbb{F}_2$ fail: $x = 0$ and $x = 1$ both give $0 \ne 1$. So the equation is inconsistent over $\mathbb{F}_2$.

## Remarks

The same integer coefficients can give different answers over different fields, so "consistent" always refers to a fixed field.
Over $\mathbb{F}_3$ the equation is consistent again, with the solution $x = 2$, because $2 \cdot 2 = 4 = 1$ there.
In general $2x = 1$ is consistent over $\mathbb{F}_p$ for every odd prime $p$, because then $2 \ne 0$ in $\mathbb{F}_p$.

## Explanations

### L1 human

In $\mathbb{F}_2$ we compute with even and odd: $0$ stands for even and $1$ for odd.
Two times any whole number is even.
So $2x$ is never odd, and $2x = 1$ has no solution there.

### L2 human

To test consistency over $\mathbb{F}_p$, first reduce all coefficients modulo $p$.
Here $2 \bmod 2 = 0$ and $1 \bmod 2 = 1$, so the reduced row is $(0 \mid 1)$, and that row shows inconsistency.
Watch out: a pivot over $\mathbb{Q}$ can vanish modulo $p$.
So the rank of a matrix with integer entries can be smaller over $\mathbb{F}_p$ than over $\mathbb{Q}$, and a consistent system can become inconsistent.

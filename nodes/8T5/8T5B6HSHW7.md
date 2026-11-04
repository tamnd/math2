---
tag: 8T5B6HSHW7
kind: proof
name: Proof that a matrix with a zero row has determinant zero
msc: [15A15]
proves: 0FS6B46E5T
uses: [009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

1. Let row $i$ of $A$ be zero.
2. Multiplying row $i$ of $A$ by $0$ gives a matrix whose row $i$ is $0$ and whose other rows are those of $A$. This matrix is $A$ itself.
3. By the rule for [[scaling a row|009CY8JXFX]] with $c = 0$, we get $\det A = 0 \cdot \det A$.
4. So $\det A = 0$.

## Idea

A zero row is unchanged when it is multiplied by $0$. Since the determinant is linear in that row, it must be multiplied by $0$ too.

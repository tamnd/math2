---
tag: 8T5B6HSHW7
kind: proof
name: Proof that a matrix with a zero row has determinant zero
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0FS6B46E5T
methods: [0NTF6DMVAP]
uses: [009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

We scale the zero row by $0$, which changes nothing in the matrix but multiplies the determinant by $0$.

1. Let row $i$ of $A$ be zero.
2. Multiply row $i$ of $A$ by $0$.
   The new row $i$ is $0 \cdot 0 = 0$ and the other rows are those of $A$, so the new matrix is $A$ itself.
3. By the rule for [[scaling a row|009CY8JXFX]] with the factor $c = 0$, the determinant of the new matrix is $0 \cdot \det A$.
4. By step 2 the new matrix is $A$, so $\det A = 0 \cdot \det A = 0$.

This proves that $\det A = 0$.

## Idea

A zero row does not change when we multiply it by $0$.
The determinant is linear in that row, so it must get multiplied by $0$ at the same time.
A number that equals $0$ times itself is $0$.

## Variants

With the Leibniz sum, each term $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ contains exactly one entry of row $i$, and that entry is $0$.
So every term is $0$, and so is the sum.
The theorem on [[equal rows or a zero row|0K4VQB7HWR]] gives a third route: a zero row is the combination of the other rows with all coefficients $0$.

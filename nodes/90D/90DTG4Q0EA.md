---
tag: 90DTG4Q0EA
kind: proof
name: Proof that scaling a row scales the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 009CY8JXFX
methods: [0NTF6DMVAP]
uses: [0PPG793642]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

We apply linearity in one row, with the second coefficient equal to $0$.

1. Let $i$ be the row of $A$ that is multiplied by $c$, and let $a$ be row $i$ of $A$.
   Then row $i$ of $B$ is $ca$, and the other rows of $B$ are those of $A$.
2. Use the matrices $A$, $A$ and $B$ in the theorem on [[multilinearity in the rows|0PPG793642]].
   They agree outside row $i$, and their rows $i$ are $a$, $a$ and $ca = c \cdot a + 0 \cdot a$.
3. That theorem with $s = c$ and $t = 0$ gives
$$\det B = c \det A + 0 \cdot \det A.$$
4. Since $0 \cdot \det A = 0$, we get $\det B = c \det A$.

## Idea

Linearity in a row contains homogeneity in that row: a scalar factor of the row comes out of the determinant.
To get it from the rule for sums, we write $ca$ as $c$ times $a$ plus $0$ times anything, and the second term drops out.

## Variants

With the Leibniz sum, each term $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ contains exactly one entry of row $i$.
Scaling row $i$ by $c$ multiplies each term by $c$, so it multiplies the sum by $c$.

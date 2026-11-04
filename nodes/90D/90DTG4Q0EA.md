---
tag: 90DTG4Q0EA
kind: proof
name: Proof that scaling a row scales the determinant
msc: [15A15]
proves: 009CY8JXFX
uses: [0PPG793642]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

1. Let $i$ be the row of $A$ that is multiplied by $c$, and let $a$ be row $i$ of $A$. Then row $i$ of $B$ is $ca$.
2. The matrices $A$, $A$ and $B$ agree outside row $i$. Their rows $i$ are $a$, $a$ and $ca = c \cdot a + 0 \cdot a$.
3. By [[multilinearity in the rows|0PPG793642]] with $s = c$ and $t = 0$, we get $\det B = c \det A + 0 \cdot \det A$.
4. So $\det B = c \det A$.

## Idea

Linearity in one row includes homogeneity: a scalar factor in that row comes out of the determinant. We get it from the linearity rule by taking the second coefficient to be zero.

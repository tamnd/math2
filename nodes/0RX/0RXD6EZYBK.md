---
tag: 0RXD6EZYBK
kind: statement
role: proposition
name: Distributivity of matrix multiplication
msc: [15A99]
uses: [076JGP6R3T, 0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: General properties
---

## Statement

Let $R$ be a ring.
Let $A$ be an $m \times n$ matrix over $R$, and let $B$ and $C$ be $n \times p$ matrices over $R$.
Then $A(B + C) = AB + AC$.
Let $D$ and $E$ be $m \times n$ matrices over $R$, and let $G$ be an $n \times p$ matrix over $R$.
Then $(D + E)G = DG + EG$.

## Remarks

Both identities follow entry by entry from the distributive law in $R$.
We need both identities, because [[matrix multiplication|032Q9FB8MT]] is not commutative.
Together with [[associativity|073E4XC016]], they make the square matrices a [[ring|0FHVPRAE60]].

## Explanations

### L1 human

Multiplication of matrices spreads over addition, as for numbers.
For example, $A(B + C)$ is the same as $AB + AC$.
We must keep the order: $A$ stays on the left in both terms.

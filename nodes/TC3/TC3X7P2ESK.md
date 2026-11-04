---
tag: TC3X7P2ESK
kind: statement
role: proposition
name: Inverse of the inverse of a matrix
msc: [15A09]
uses: [0EB9N0S33C]
about: [0EB9N0S33C]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-1.xml#L597
    locator: src/section3-1.xml:597
---

## Statement

Let $A$ be an $n \times n$ [[invertible matrix|0EB9N0S33C]] with inverse $B$.
Then $B$ is also invertible, and its inverse is $A$.
In symbols, $(A^{-1})^{-1} = A$.

## Remarks

The proof is one line.
Since $B$ is the inverse of $A$, we have $AB = BA = I$.
These two equations say exactly that $A$ is an inverse of $B$.
By uniqueness of inverses, $A$ is the inverse of $B$.

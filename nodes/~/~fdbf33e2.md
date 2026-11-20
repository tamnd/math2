---
tag: ~fdbf33e2
kind: proof
name: Proof of the uniqueness of the inverse matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: ~139b320d
methods: [0NTF6DMVAP, GQHHNV79PA]
uses: [0TWTS88TWN, 073E4XC016, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

**Part 1.** Assume $CA = I_n$ and $AB = I_n$.

1. $C = C I_n$, because $I_n$ is the [[identity matrix|06DW9BAWB1]] for matrix multiplication.
2. $C I_n = C(AB)$, by the hypothesis $AB = I_n$.
3. $C(AB) = (CA)B$, by the [[associativity of matrix multiplication|073E4XC016]].
4. $(CA)B = I_n B$, by the hypothesis $CA = I_n$.
5. $I_n B = B$, because $I_n$ is the identity.
6. Steps 1 to 5 give $C = B$.

**Part 2.** Assume that $B$ and $C$ are both inverses of $A$.

7. By the definition of an [[inverse|0TWTS88TWN]], $CA = I_n$ and $AB = I_n$.
8. Part 1 gives $B = C$. So $A$ has at most one inverse.

## Idea

We insert the identity $I_n = AB$ next to $C$ and move the brackets.
The left inverse $C$ then meets $A$, and the product $CA$ disappears.

## Variants

The same steps prove that a left inverse and a right inverse of an element of a monoid are equal.
For matrices of sizes $n \times m$ (for $C$) and $m \times n$ (for $B$), the steps still hold.
In step 2 and step 4, replace $I_m$ by the identities of the right sizes.

---
tag: PB3ANNX7FR
kind: proof
name: Proof of the uniqueness of the inverse matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: FMCX4D7RD4
methods: [0NTF6DMVAP, GQHHNV79PA]
uses: [0TWTS88TWN, 073E4XC016, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

We write $C$ as $C$ times the identity, replace the identity by $AB$, and move the brackets.

**Part 1.** Assume $CA = I_n$ and $AB = I_n$.

1. We have $C = C I_n$, because $I_n$ is the [[identity matrix|06DW9BAWB1]] for matrix multiplication.
2. We have $C I_n = C(AB)$, by the hypothesis $AB = I_n$.
3. We have $C(AB) = (CA)B$, by the [[associativity of matrix multiplication|073E4XC016]].
4. We have $(CA)B = I_n B$, by the hypothesis $CA = I_n$.
5. We have $I_n B = B$, because $I_n$ is the identity.
6. Steps 1 to 5 form one chain of equalities from $C$ to $B$, so $C = B$.

**Part 2.** Assume that $B$ and $C$ are both inverses of $A$.

7. By the definition of an [[inverse|0TWTS88TWN]], $CA = I_n$ and $AB = I_n$.
8. Part 1 gives $B = C$, so $A$ has at most one inverse.

## Idea

The left inverse $C$ and the right inverse $B$ sit on opposite sides of $A$.
Put all three side by side in the product $CAB$ and read it in two ways.
Grouped as $(CA)B$ it is $B$, and grouped as $C(AB)$ it is $C$, so the two must agree.

## Variants

The same chain proves that a left inverse and a right inverse of an element of a monoid are equal.
For an $m \times n$ matrix $A$ with $n \times m$ matrices $C$ and $B$ such that $CA = I_n$ and $AB = I_m$, the chain is $C = C I_m = C(AB) = (CA)B = I_n B = B$.
Only the sizes of the identity matrices change.

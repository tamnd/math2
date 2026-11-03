---
tag: H9PVHBV2Y8
kind: proof
name: Proof of the formula for the inverse of a product
msc: [15A09]
proves: 0S4WTRE9GG
uses: [0TWTS88TWN, 076JGP6R3T, 073E4XC016, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

1. Since $A$ and $B$ are [[invertible|0TWTS88TWN]], they have inverses $A^{-1}$ and $B^{-1}$. These satisfy $AA^{-1} = A^{-1}A = I_n$ and $BB^{-1} = B^{-1}B = I_n$, where $I_n$ is the [[identity matrix|06DW9BAWB1]].
2. Let $C = B^{-1} A^{-1}$. It is an $n \times n$ matrix by the definition of the [[product|076JGP6R3T]].
3. By [[associativity|073E4XC016]], $(AB)C = A(BB^{-1})A^{-1} = A I_n A^{-1}$.
4. Since $A I_n = A$, step 3 gives $(AB)C = AA^{-1} = I_n$.
5. By associativity, $C(AB) = B^{-1}(A^{-1}A)B = B^{-1} I_n B = B^{-1} B = I_n$.
6. By steps 4 and 5, $(AB)C = C(AB) = I_n$. So $AB$ is invertible by definition.
7. The inverse of an invertible matrix is unique, by the definition. So $(AB)^{-1} = C = B^{-1} A^{-1}$.

## Idea

To undo "first $B$, then $A$", undo $A$ first and then undo $B$. Associativity lets the middle factors $B B^{-1}$ or $A^{-1} A$ cancel to the identity.

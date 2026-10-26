---
tag: 0S4WTRE9GG
kind: statement
role: proposition
name: Inverse of a product
msc: [15A09]
uses: [0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Statement

Let $R$ be a commutative ring and let $A$ and $B$ be [[invertible|0EB9N0S33C]] $n \times n$ matrices over $R$.
Then $AB$ is invertible, and
$$(AB)^{-1} = B^{-1} A^{-1}.$$

## Remarks

The proof is the computation $(AB)(B^{-1} A^{-1}) = A (B B^{-1}) A^{-1} = A A^{-1} = I_n$, and the same in the other order.
By induction, $(A_1 \cdots A_k)^{-1} = A_k^{-1} \cdots A_1^{-1}$.
Thus the invertible $n \times n$ matrices form a group, the [[general linear group|0FCHE902D7]].

## Explanations

### L1 human

To undo two steps, we undo the last step first.
If we first apply $B$ and then $A$, then we must first undo $A$ and then undo $B$.
So the inverse of $AB$ is $B^{-1} A^{-1}$, with the order reversed.

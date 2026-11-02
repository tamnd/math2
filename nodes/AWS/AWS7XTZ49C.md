---
tag: AWS7XTZ49C
kind: statement
role: proposition
name: Hua's identity
msc: [16K40]
uses: [0WZXK05ME7]
about: [0EA5BTA0CX]
sources:
  - url: https://en.wikipedia.org/wiki/Hua%27s_identity
same_as:
  wikidata: Q15709387
  wikipedia: Hua's identity
---

## Statement

Let $D$ be a [[division ring|0WZXK05ME7]], and let $a, b \in D$ with $a \ne 0$, $b \ne 0$ and $ab \ne 1$.
Then $a^{-1} + (b^{-1} - a)^{-1}$ is invertible, and
$$a - \left(a^{-1} + (b^{-1} - a)^{-1}\right)^{-1} = aba.$$

## Remarks

The element $b^{-1} - a$ is nonzero because $ab \ne 1$.
The proof is a direct factorization: $a^{-1} + (b^{-1} - a)^{-1} = a^{-1}\left((b^{-1} - a) + a\right)(b^{-1} - a)^{-1} = a^{-1} b^{-1} (b^{-1} - a)^{-1}$.
Its inverse is $(b^{-1} - a) b a = a - aba$, and subtracting it from $a$ gives $aba$.
For example, in $\Q$ with $a = 2$ and $b = 3$: $1/2 + (1/3 - 2)^{-1} = 1/2 - 3/5 = -1/10$, and $2 - (-10) = 12 = 2 \cdot 3 \cdot 2$.
The hypothesis $ab \ne 1$ is needed, since for $b = a^{-1}$ the term $(b^{-1} - a)^{-1}$ is not defined.

## Explanations

### L1 human

The identity writes the product $aba$ using only addition, subtraction and inverses.
So a map that respects sums, inverses and $1$ automatically respects these "sandwich" products.

### L2 human

Hua used the identity to show that a map $\sigma$ between division rings that is additive, sends $1$ to $1$ and satisfies $\sigma(x^{-1}) = \sigma(x)^{-1}$ preserves $aba$.
From this one deduces Hua's theorem: such a map is a ring homomorphism or an antihomomorphism.
The identity also underlies the use of the product $aba$ in Jordan algebras, where $aba$ plays the role of the quadratic operator.

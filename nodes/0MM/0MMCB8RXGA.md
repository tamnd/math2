---
tag: 0MMCB8RXGA
kind: statement
role: proposition
name: A ring homomorphism is injective iff its kernel is zero
msc: [16B99]
uses: [0GGE0Z0JQ1, 0AAHE7GEW6]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_homomorphism
    locator: Properties
---

## Statement

Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]].
Then $f$ is injective if and only if its [[kernel|0AAHE7GEW6]] is $\{0\}$.

## Remarks

The proof uses only the addition: $f(a) = f(b)$ holds if and only if $f(a - b) = 0$, that is, $a - b \in \ker f$.
The same criterion holds for group homomorphisms and for linear maps.

## Explanations

### L1 human

If two elements have the same image, then their difference goes to $0$.
So when only $0$ goes to $0$, no two different elements have the same image.

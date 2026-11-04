---
tag: R7EVNDA9S9
kind: proof
name: Proof of the formula for the modulus
msc: [30A99]
proves: 034FGCEYX4
uses: [0KW2X0TFBX, 02ZE6JHJ7G]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: Complex numbers
---

## Proof

1. Let $x$ and $y$ be real numbers, and let $z = x + y i$.
2. Since $x$ and $y$ are real, the definition of the [[real and imaginary parts|02ZE6JHJ7G]] gives $\operatorname{Re} z = x$ and $\operatorname{Im} z = y$.
3. By the definition of the [[modulus|0KW2X0TFBX]], $|z| = \sqrt{(\operatorname{Re} z)^2 + (\operatorname{Im} z)^2}$.
4. Substituting step 2 into step 3 gives $|x + y i| = \sqrt{x^2 + y^2}$.

## Idea

The modulus is defined through the real and imaginary parts.
When $x$ and $y$ are real, these parts of $x + y i$ are simply $x$ and $y$.

---
tag: 0TYQNHVB4C
kind: statement
role: proposition
name: Surjective iff it has a right inverse
msc: ["03E20"]
uses: [0XKH881BZ7, 0DDPZAG5ER, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Right inverses
---

## Statement

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
Assume the [[axiom of choice|0HTGB13FE2]].
Then $f$ is [[surjective|0XKH881BZ7]] if and only if $f$ has a [[right inverse|0DDPZAG5ER]].

## Remarks

If $f \circ h = \mathrm{id}_B$, then each $b$ equals $f(h(b))$, so $f$ is surjective. This direction does not use choice.
For the other direction, choose for each $b \in B$ an element $h(b)$ of the nonempty set $f^{-1}(\{b\})$.
The statement "each surjection has a right inverse" is equivalent to the axiom of choice.

## Explanations

### L1 human

For a surjection, each $b$ has at least one input that maps to it.
A right inverse picks one such input for each $b$.
For infinitely many $b$ with no rule to pick, you need the axiom of choice.

---
tag: 04CYN5G6RY
kind: statement
role: proposition
name: Variance under translation
aliases: [variance-is-shift-invariant]
msc: [60A05]
uses: [007QED3E0Y, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance
    locator: Addition and multiplication by a constant
---

## Statement

Let $X$ be an integrable real random variable and let $b \in \mathbb{R}$. Then
$$\operatorname{Var}(X + b) = \operatorname{Var}(X).$$

## Remarks

Proof: $E[X + b] = E[X] + b$ by [[linearity of expectation|0P7PTC8DDE]], so $(X + b) - E[X + b] = X - E[X]$.
Together with the [[scaling rule|0KVQ9D86BM]], this gives $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$ for all real $a$ and $b$.

## Explanations

### L1 human

If you add the same constant to every value, the whole distribution moves, but its spread does not change.

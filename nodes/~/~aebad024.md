---
tag: ~aebad024
kind: definition
name: Higher derivative
msc: [26A24]
defines: ~6651df1f
uses: [~20ed3f26]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative
    locator: Higher-order derivatives
---

## Definition

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$.
Let $f^{(0)} = f$.
If $f^{(n)}$ is defined and differentiable on $I$, let $f^{(n+1)} = (f^{(n)})'$, its [[derivative function|~20ed3f26]].
The function $f^{(n)}$ is the $n$-th derivative of $f$, and $f$ is $n$ times differentiable when it exists.

## Remarks

The [[second derivative|~4d14a831]] is $f'' = f^{(2)}$.
For example, the $n$-th derivative of $x^n$ is the constant $n!$.
Mathlib defines `iteratedDeriv n f`.

## Explanations

### L1 human

Higher derivatives come from differentiating again and again.
They describe finer features of a function, like the bending of its graph.

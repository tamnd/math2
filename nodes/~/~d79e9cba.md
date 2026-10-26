---
tag: ~d79e9cba
kind: definition
name: Right inverse
msc: ["03E20"]
defines: ~dfe40888
uses: [~f5ac250d, ~b726e813]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Right inverses
---

## Definition

Let $f \colon A \to B$ be a [[function|~d103e2ff]].
A right inverse of $f$ is a function $h \colon B \to A$ such that $f \circ h = \mathrm{id}_B$, that is, $f(h(b)) = b$ for each $b \in B$.

## Remarks

A function has a right inverse exactly when it is [[surjective|~beb187ef]]. The proof uses the [[axiom of choice|~9fdddcbe]]. See [[surjective iff it has a right inverse|~61257cd9]].
A right inverse is in general not unique.
A right inverse is [[injective|~3e705960]].

## Explanations

### L1 human

For $f(x) = x^2$ from $\mathbb{R}$ to $[0, \infty)$, the square root $h(y) = \sqrt{y}$ is a right inverse: $(\sqrt{y})^2 = y$.
The function $y \mapsto -\sqrt{y}$ is another right inverse.

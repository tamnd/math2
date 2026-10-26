---
tag: 0DDPZAG5ER
kind: definition
name: Right inverse
msc: ["03E20"]
defines: 0WWRD82HD2
uses: [07HF9YCWPP, 0FSNQ0GNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Right inverses
---

## Definition

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
A right inverse of $f$ is a function $h \colon B \to A$ such that $f \circ h = \mathrm{id}_B$, that is, $f(h(b)) = b$ for each $b \in B$.

## Remarks

A function has a right inverse exactly when it is [[surjective|0XKH881BZ7]]. The proof uses the [[axiom of choice|0HTGB13FE2]]. See [[surjective iff it has a right inverse|0TYQNHVB4C]].
A right inverse is in general not unique.
A right inverse is [[injective|0PVG1CRAJN]].

## Explanations

### L1 human

For $f(x) = x^2$ from $\mathbb{R}$ to $[0, \infty)$, the square root $h(y) = \sqrt{y}$ is a right inverse: $(\sqrt{y})^2 = y$.
The function $y \mapsto -\sqrt{y}$ is another right inverse.

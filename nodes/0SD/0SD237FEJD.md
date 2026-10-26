---
tag: 0SD237FEJD
kind: statement
role: theorem
name: Gradient theorem
aliases: [fundamental-theorem-of-line-integrals, fundamental-theorem-of-calculus-for-line-integrals]
msc: [26B20]
uses: [0YS8RX87F4, 0NS2QYVC4Y, 0W3W1VYWBP, 0A8TJ0VHC7]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient_theorem
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Gradient_theorem
    locator: lead section
same_as:
  wikidata: Q287347
  wikipedia: Gradient theorem
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $\phi \colon U \to \mathbb{R}$ be of class $C^1$, and let $\gamma \colon [a, b] \to U$ be a piecewise $C^1$ curve.
Then
$$\int_\gamma \nabla \phi \cdot d\mathbf{r} = \phi(\gamma(b)) - \phi(\gamma(a)).$$

## Remarks

Proof for a $C^1$ curve: by the [[chain rule along a curve|0A8TJ0VHC7]], $(\phi \circ \gamma)'(t) = \nabla \phi(\gamma(t)) \cdot \gamma'(t)$. Then the [[parametric formula|0W3W1VYWBP]] and the fundamental theorem of calculus give the result. For a piecewise $C^1$ curve, add the pieces.
So the line integral of a gradient field depends only on the end points. Around a closed curve it is $0$.
Example: for $\phi(x, y) = x^2 y$ and any path from $(0, 0)$ to $(1, 2)$, $\int_\gamma (2 x y, x^2) \cdot d\mathbf{r} = 2$.
This is the case of curves in the [[generalised Stokes theorem|0HPHKCGEQ0]]: the boundary of a curve consists of its two end points.

## Explanations

### L1 human

This is the fundamental theorem of calculus for curves.
To integrate the gradient of $\phi$ along a path, you only need the values of $\phi$ at the end and at the start.

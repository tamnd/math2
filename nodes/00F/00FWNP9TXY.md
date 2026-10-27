---
tag: 00FWNP9TXY
kind: definition
name: Contour integral
aliases: [curve-integral]
msc: ["30E20"]
defines: 06ZGPYTWK8
uses: [09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Contour_integration
    locator: Contour integrals
  - url: https://en.wikipedia.org/wiki/Contour_integration
    locator: Directed smooth curves
inventory: [JFQTEF3FY6]
---

## Definition

Let $a < b$ be real numbers and let $\gamma : [a, b] \to \mathbb{C}$ be a path that is continuous and piecewise continuously differentiable.
Let $f$ be a complex function that is continuous on the image $\gamma([a, b])$.
The contour integral of $f$ along $\gamma$ is
$$\int_\gamma f(z) \, dz = \int_a^b f(\gamma(t)) \, \gamma'(t) \, dt.$$
The integral on the right of a complex function $g$ of $t \in [a, b]$ is $\int_a^b \operatorname{Re} g(t) \, dt + i \int_a^b \operatorname{Im} g(t) \, dt$.

## Remarks

The length of $\gamma$ is $L(\gamma) = \int_a^b |\gamma'(t)| \, dt$.
The integral does not change under a reparametrization of $\gamma$ that keeps the direction. It changes sign if we reverse the direction.
The path $\gamma$ is closed if $\gamma(a) = \gamma(b)$. For a closed path, many authors write $\oint_\gamma f(z) \, dz$.
For example, along $\gamma(t) = t + i t$ with $t \in [0, 1]$, $\int_\gamma z \, dz = \int_0^1 (1 + i) t (1 + i) \, dt = i$.

## Explanations

### L1 human

A contour integral adds up the values of $f$ along a path, each one multiplied by a small step $dz$ of the path.
Because $dz$ is a complex number, the direction of each step matters, and not only its length.

---
tag: 0BXE0S1XER
kind: definition
name: Having a gradient
msc: [26B12]
defines: 0ABK9V9Y64
uses: [0135XZZQ8M, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Relationship with derivative
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}$, let $a \in U$, and let $g \in \mathbb{R}^n$.
The function $f$ has the gradient $g$ at $a$ when
$$\lim_{h \to 0} \frac{f(a + h) - f(a) - g \cdot h}{\|h\|} = 0,$$
where the limit is over $h \ne 0$ with $a + h \in U$.
Equivalently, $f$ is [[differentiable|0135XZZQ8M]] at $a$ and $Df(a)(h) = g \cdot h$ for each $h \in \mathbb{R}^n$.

## Remarks

This definition states a property of $f$, $a$ and $g$. When it holds, the vector $g$ is unique, and it is the [[gradient|0NS2QYVC4Y]] $\nabla f(a)$.
The same definition works in each real inner product space, with the inner product in place of the dot product.

## Explanations

### L1 human

The function has the gradient $g$ at $a$ when the plane through $(a, f(a))$ with slopes given by $g$ hugs the graph of $f$ near $a$.
The error of this approximation must be small compared with the distance from $a$.

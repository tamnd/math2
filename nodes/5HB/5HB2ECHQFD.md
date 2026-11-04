---
tag: 5HB2ECHQFD
kind: proof
name: Proof of the Laplacian as a sum of second partial derivatives
msc: ["35J05"]
proves: 05RCT1522R
uses: [0XQ2ZVN1PZ, 02NSMQVQWK, 0NS2QYVC4Y, 0135XZZQ8M, 05AXG3QRKR, 02RSXVM1ZN]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_operator
    locator: Definition
---

## Proof

We unfold the definitions.

1. Let $f \colon U \to \R$ be twice differentiable on the open set $U \subseteq \R^n$. Then $f$ is [[differentiable|0135XZZQ8M]] at each point of $U$.
2. By the coordinate form of the [[gradient|0NS2QYVC4Y]], $\nabla f = (g_1, \dots, g_n)$ on $U$, where $g_i = \partial f / \partial x_i$ is a [[partial derivative|05AXG3QRKR]].
3. The map $x \mapsto Df(x)$ is differentiable on $U$, since $f$ is twice differentiable. Its entries in the standard basis are $g_1, \dots, g_n$, so each $g_i$ is differentiable on $U$.
4. Hence each partial derivative $\partial g_i / \partial x_i$ exists on $U$. By the definition of [[higher partial derivatives|02RSXVM1ZN]], $\partial g_i / \partial x_i = \partial^2 f / \partial x_i^2$.
5. By the definition of the [[divergence|02NSMQVQWK]], $\operatorname{div}(\nabla f) = \sum_{i=1}^n \partial g_i / \partial x_i$.
6. By the definition of the [[Laplacian|0XQ2ZVN1PZ]] and steps 4 and 5, $\Delta f = \operatorname{div}(\nabla f) = \frac{\partial^2 f}{\partial x_1^2} + \dots + \frac{\partial^2 f}{\partial x_n^2}$.

## Idea

The gradient collects the first partial derivatives of $f$. The divergence then differentiates the $i$-th of them in the direction $x_i$ and adds the results. So only the unmixed second derivatives appear.

---
tag: 0CYYAF8AD2
kind: statement
role: proposition
name: Derivative of a continuous linear map
msc: [26B05]
uses: [08EVNYZF42]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Definition
---

## Statement

Let $V$ and $W$ be normed vector spaces over $\mathbb{R}$ and let $A \colon V \to W$ be a bounded linear map.
Then $A$ is Fréchet differentiable at each point $x \in V$, and its [[Fréchet derivative|08EVNYZF42]] at $x$ is $A$ itself: $DA(x) = A$.

## Remarks

The proof is one line: $A(x + h) - A(x) - A h = 0$ for each $h$, so the remainder is $0$.
For $V = \mathbb{R}^n$ and $W = \mathbb{R}^m$, each linear map is bounded. So the derivative of $x \mapsto M x$, for an $m \times n$ matrix $M$, is the linear map with matrix $M$ at each point.
An affine map $x \mapsto A x + b$ has the same derivative $A$ at each point, because the derivative of a constant map is $0$.

## Explanations

### L1 human

The best linear approximation of a linear map is the map itself.
This is the analogue of the rule that the derivative of $x \mapsto c x$ is the constant $c$.

---
tag: 0EAAS2EHDR
kind: statement
role: theorem
name: Chain rule in several variables
aliases: [multivariable-chain-rule]
msc: [26B05]
uses: [0135XZZQ8M, 08EVNYZF42, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule
    locator: 'General rule: Vector-valued multivariate functions'
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Properties
---

## Statement

Let $U \subseteq \mathbb{R}^n$ and $W \subseteq \mathbb{R}^m$ be open sets, let $g \colon U \to \mathbb{R}^m$ with $g(U) \subseteq W$, let $f \colon W \to \mathbb{R}^k$, and let $a \in U$.
Suppose that $g$ is [[differentiable|0135XZZQ8M]] at $a$ and $f$ is differentiable at $g(a)$.
Then the [[composition|0THBK9V825]] $f \circ g \colon U \to \mathbb{R}^k$ is differentiable at $a$, and
$$D(f \circ g)(a) = Df(g(a)) \circ Dg(a).$$

## Remarks

In matrix form, the [[Jacobian matrix|047NDTEPCV]] of $f \circ g$ at $a$ is the product $J_f(g(a)) \, J_g(a)$. In terms of partial derivatives, $\dfrac{\partial (f \circ g)_i}{\partial x_j}(a) = \sum_{l=1}^m \dfrac{\partial f_i}{\partial y_l}(g(a)) \, \dfrac{\partial g_l}{\partial x_j}(a)$.
The same rule, with the same proof, holds for [[Fréchet derivatives|08EVNYZF42]] of maps between normed spaces.
A special case is the [[chain rule for a composition with a curve|0A8TJ0VHC7]].

## Explanations

### L1 human

The derivative of a composition is the composition of the derivatives: first the linear approximation of $g$, then the linear approximation of $f$.
In one variable this is $(f \circ g)'(a) = f'(g(a)) \, g'(a)$, a product of two numbers. In several variables the numbers become matrices.

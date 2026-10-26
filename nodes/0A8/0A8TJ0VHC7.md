---
tag: 0A8TJ0VHC7
kind: statement
role: corollary
name: Chain rule for a composition with a curve
msc: [26B05]
uses: [0EAAS2EHDR, 0ABK9V9Y64, 0G7WM8DX4P]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule
    locator: Case of scalar-valued multivariate functions
---

## Statement

Let $I \subseteq \mathbb{R}$ be an open interval, let $U \subseteq \mathbb{R}^n$ be open, let $\gamma \colon I \to U$, let $f \colon U \to \mathbb{R}^m$, and let $t_0 \in I$.
Suppose that $\gamma$ is differentiable at $t_0$ and $f$ is differentiable at $\gamma(t_0)$.
Then $f \circ \gamma$ is differentiable at $t_0$, and
$$(f \circ \gamma)'(t_0) = Df(\gamma(t_0))\big(\gamma'(t_0)\big).$$

## Remarks

For $m = 1$, this reads $(f \circ \gamma)'(t_0) = \nabla f(\gamma(t_0)) \cdot \gamma'(t_0) = \sum_{i=1}^n \dfrac{\partial f}{\partial x_i}(\gamma(t_0)) \, \gamma_i'(t_0)$, with the [[gradient|0ABK9V9Y64]] $\nabla f$.
It is the case $n = 1$ of the [[chain rule in several variables|0EAAS2EHDR]], since a linear map $\mathbb{R} \to \mathbb{R}^n$ is $s \mapsto s \gamma'(t_0)$.
For $\gamma(t) = a + t v$ it gives the [[directional derivative|06KWGHDN2J]] $D_v f(a) = Df(a)(v)$.

## Explanations

### L1 human

Walk along a [[curve|0G7WM8DX4P]] $\gamma(t)$ through a landscape with height $f$.
The rate at which your height changes is the slope of the landscape in the direction you walk, times your speed.
For $f(x, y) = x y$ and $\gamma(t) = (t, t^2)$, the rule gives $\nabla f \cdot \gamma' = t^2 \cdot 1 + t \cdot 2t = 3 t^2$, the derivative of $t^3$.

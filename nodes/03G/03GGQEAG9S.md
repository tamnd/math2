---
tag: 03GGQEAG9S
kind: statement
role: corollary
name: Chain rule for Jacobian matrices
msc: [26B10]
uses: [0EAAS2EHDR, 0YF0VXKXGB]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule
    locator: 'General rule: Vector-valued multivariate functions'
---

## Statement

Let $U \subseteq \mathbb{R}^n$ and $W \subseteq \mathbb{R}^m$ be open, let $g \colon U \to W$, let $f \colon W \to \mathbb{R}^k$, and let $a \in U$.
Suppose that $g$ is differentiable at $a$ and $f$ is differentiable at $g(a)$.
Then the [[Jacobian matrices|0YF0VXKXGB]] satisfy
$$J_{f \circ g}(a) = J_f(g(a)) \, J_g(a),$$
a product of a $k \times m$ matrix and an $m \times n$ matrix.

## Remarks

This is the [[chain rule in several variables|0EAAS2EHDR]], written with matrices: the matrix of a composition of linear maps is the product of their matrices.
For $k = m = n$, taking determinants gives $\det J_{f \circ g}(a) = \det J_f(g(a)) \cdot \det J_g(a)$.
For example, let $g(r, \theta) = (r \cos \theta, r \sin \theta)$ and $f(x, y) = x^2 + y^2$. Then $J_f(g(r, \theta)) J_g(r, \theta) = (2r \cos \theta, \, 2r \sin \theta) J_g(r, \theta) = (2r, \, 0)$, which is the Jacobian matrix of $(f \circ g)(r, \theta) = r^2$.

## Explanations

### L1 human

Each Jacobian matrix turns small input steps into small output steps.
Doing two maps one after the other means multiplying their matrices, in the same order as the maps act, from right to left.

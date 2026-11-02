---
tag: C1KY6MAW0J
kind: definition
name: Covariant derivative
msc: [53B05, 53C05]
defines: 5FZDQQHQKM
uses: [5ZYRRVE8BW, WWX7H5W1RP, WX302T93TW]
sources:
  - url: https://en.wikipedia.org/wiki/Covariant_derivative
---

## Definition

Let $M$ be a smooth manifold, let $E \to M$ be a smooth vector bundle, and let $\nabla$ be a [[connection|5ZYRRVE8BW]] on $E$.

1. Let $p \in M$, $v \in T_pM$, and let $s$ be a smooth [[section|WWX7H5W1RP]] of $E$. The *covariant derivative* of $s$ in the direction $v$ is $\nabla_v s = (\nabla_X s)(p)$, where $X$ is any smooth vector field with $X_p = v$.
2. Let $\gamma : I \to M$ be a smooth curve on an interval $I$. The *covariant derivative along $\gamma$* is the unique map $D_t$ from smooth sections of $E$ along $\gamma$ to themselves with three properties. It is $\R$-linear. It satisfies $D_t (f V) = f' V + f D_t V$ for every smooth $f : I \to \R$. And $D_t V(t) = \nabla_{\gamma'(t)} s$ whenever $V = s \circ \gamma$ for a section $s$ of $E$.

## Remarks

Clause 1 is well defined because $\nabla_X s$ is $C^\infty(M)$-linear in $X$, so its value at $p$ depends only on $X_p$.
The existence and uniqueness in clause 2 follow by writing $V(t) = \sum_i V^i(t) e_i(\gamma(t))$ in a local frame: then $D_t V = \sum_i \big(\dot V^i + \sum_j \omega^i_j(\gamma'(t)) V^j\big) e_i$, where $\nabla e_j = \sum_i \omega^i_j \otimes e_i$.
Example: for the flat connection on $\R^n$ and $E = T\R^n$, $D_t V = \dot V$ is the ordinary derivative of the components; so $D_t \gamma' = \ddot \gamma$ is the acceleration.
Non-example: on the round sphere $S^2 \subset \R^3$ with its Levi-Civita connection, $D_t \gamma'$ is the tangential part of $\ddot \gamma$, not $\ddot\gamma$ itself.
Along a great circle $\ddot \gamma$ is normal to the sphere, so $D_t \gamma' = 0$ although $\ddot \gamma \ne 0$.
A connection on $TM$ extends uniquely to covariant derivatives of all [[tensor fields|WX302T93TW]] that obey the product rule for $\otimes$, commute with contractions and act on functions by $\nabla_X f = X f$.
In index notation $\nabla_i Y^k = \partial_i Y^k + \Gamma^k_{ij} Y^j$, often written $Y^k{}_{;i}$.

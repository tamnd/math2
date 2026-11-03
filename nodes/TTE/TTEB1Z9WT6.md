---
tag: TTEB1Z9WT6
kind: definition
name: Proximal gradient method
msc: [90C25, 65K05]
defines: 3JS2VJ5AYS
uses: [07GR3TNW4H, 0ABK9V9Y64, 0AW1E6YTJY, E239APE78P, 12317R8RTJ]
sources:
  - url: https://en.wikipedia.org/wiki/Proximal_gradient_method
---

## Definition

Let $f \colon \R^n \to \R$ be a differentiable [[convex function|07GR3TNW4H]] whose [[gradient|0ABK9V9Y64]] is [[Lipschitz|0AW1E6YTJY]] with constant $L > 0$.
Let $g \colon \R^n \to \R \cup \set{+\infty}$ be a proper, lower semicontinuous, convex function.
For $t > 0$ let
$$\operatorname{prox}_{t g}(v) = \operatorname*{arg\,min}_{u \in \R^n} \Big( g(u) + \frac{1}{2t} \norm{u - v}^2 \Big)$$
be the [[proximal operator|E239APE78P]] of $t g$.
Let $x_0 \in \R^n$ and $t \in (0, 1/L]$.
The *proximal gradient method* for minimising $f + g$ produces the sequence
$$x_{k+1} = \operatorname{prox}_{t g}\big(x_k - t \nabla f(x_k)\big) \qquad (k \ge 0).$$

## Remarks

If $g = 0$, then $\operatorname{prox}_{t g}$ is the identity and the method is [[gradient descent|12317R8RTJ]] with step $t$.
Let $g$ be the indicator function of a nonempty closed convex set $C$, equal to $0$ on $C$ and $+\infty$ outside.
Then $\operatorname{prox}_{t g}$ is the Euclidean projection onto $C$, and the method is projected gradient descent.
If $f + g$ has a minimiser $x^*$, then $f(x_k) + g(x_k) - f(x^*) - g(x^*) \le \norm{x_0 - x^*}^2 / (2 t k)$ for $k \ge 1$.

Example: the lasso, $f(x) = \tfrac12 \norm{A x - b}^2$ and $g(x) = \lambda \norm{x}_1$ with $\lambda > 0$.
Here $\nabla f(x) = A^T (A x - b)$ is Lipschitz with $L = \lambda_{\max}(A^T A)$, the largest eigenvalue of $A^T A$, and $\operatorname{prox}_{t g}$ acts on each coordinate by soft thresholding $v_i \mapsto \operatorname{sign}(v_i) \max(\abs{v_i} - t \lambda, 0)$.
The method is then called ISTA.

Non-example: let $s_k$ be a subgradient of $g$ at $x_k$.
The step $x_{k+1} = x_k - t \big(\nabla f(x_k) + s_k\big)$ is a subgradient step, not a proximal gradient step, since it does not use the proximal operator of $g$.

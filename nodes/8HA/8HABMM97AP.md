---
tag: 8HABMM97AP
kind: proof
name: Proof that the gradient is orthogonal to level sets
msc: [26B12]
proves: 0VXYV3NQQ1
uses: [0A8TJ0VHC7, 0NS2QYVC4Y, 0Y5Q8Q9WJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Level sets
---

## Proof

We differentiate the constant function $f \circ \gamma$ in two ways.

1. Let $U$, $f$, $c$, $I$, $\gamma$ and $t_0$ be as in the statement. Put $\varphi = f \circ \gamma \colon I \to \mathbb{R}$.
2. Since $\gamma$ lies in the [[level set|0Y5Q8Q9WJ7]] $L_c(f)$, $\varphi(t) = c$ for each $t \in I$.
3. So for $s \ne 0$ with $t_0 + s \in I$, the difference quotient $(\varphi(t_0 + s) - \varphi(t_0)) / s$ is $0$. Hence $\varphi'(t_0) = 0$.
4. By the [[chain rule for a composition with a curve|0A8TJ0VHC7]] with $m = 1$, $\varphi'(t_0) = Df(\gamma(t_0))\big(\gamma'(t_0)\big)$.
5. Since $f$ is differentiable at $\gamma(t_0)$, the [[gradient|0NS2QYVC4Y]] $\nabla f(\gamma(t_0))$ is defined, and $Df(\gamma(t_0))(v) = \nabla f(\gamma(t_0)) \cdot v$ for each $v \in \mathbb{R}^n$.
6. By steps 3, 4 and 5, $\nabla f(\gamma(t_0)) \cdot \gamma'(t_0) = \varphi'(t_0) = 0$.

## Idea

Along a curve inside a level set, the value of $f$ does not change, so its rate of change is $0$. The chain rule computes that rate as the dot product of the gradient with the velocity of the curve. So this dot product is $0$.

---
tag: F2YZDX33CC
kind: proof
name: Proof of the angle addition formulas by differentiation
msc: [33B10]
proves: 028XEQCE88
uses: [0WB57D9488, 00R4MWW532, 0V2DV29EGT, 0RXX2PT1MQ, 0V9A43H7WV, 0M0TKFRX2A, 003QDZ4T16]
sources:
  - url: https://proofwiki.org/wiki/Sine_of_Sum
    locator: Proof 2
---

## Proof

We fix $y$ and show that the differences of the two sides vanish, using derivatives.

1. Fix a real number $y$. For real $x$ let $g(x) = \sin(x + y) - \sin x \cos y - \cos x \sin y$.
2. For real $x$ let $h(x) = \cos(x + y) - \cos x \cos y + \sin x \sin y$.
3. The map $x \mapsto x + y$ has derivative $1$. By the [[chain rule|0RXX2PT1MQ]] with the [[derivative of sine|00R4MWW532]], $\frac{d}{dx} \sin(x + y) = \cos(x + y)$.
4. In the same way, the [[derivative of cosine|0V2DV29EGT]] gives $\frac{d}{dx} \cos(x + y) = -\sin(x + y)$.
5. By [[linearity of the derivative|0M0TKFRX2A]], with $\cos y$ and $\sin y$ constants, $g'(x) = \cos(x + y) - \cos x \cos y + \sin x \sin y = h(x)$.
6. In the same way, $h'(x) = -\sin(x + y) + \sin x \cos y + \cos x \sin y = -g(x)$.
7. Let $q(x) = g(x)^2 + h(x)^2$. By the [[product rule|0V9A43H7WV]], $q'(x) = 2 g(x) h(x) + 2 h(x) (-g(x)) = 0$ for every real $x$.
8. Since $\mathbb{R}$ is an open interval, $q$ is [[constant|003QDZ4T16]].
9. From the [[defining series|0WB57D9488]], $\sin 0 = 0$ and $\cos 0 = 1$. So $g(0) = \sin y - 0 - \sin y = 0$ and $h(0) = \cos y - \cos y + 0 = 0$.
10. So $q(x) = q(0) = 0$ for every $x$. A sum of two squares of reals is $0$ only if both are $0$. So $g(x) = 0$ and $h(x) = 0$.
11. Since $y$ was arbitrary, $\sin(x + y) = \sin x \cos y + \cos x \sin y$ and $\cos(x + y) = \cos x \cos y - \sin x \sin y$ for all real $x$ and $y$.

## Idea

The two error terms $g$ and $h$ satisfy $g' = h$ and $h' = -g$, like a rotation. So the quantity $g^2 + h^2$ cannot change. It starts at $0$ when $x = 0$, so both errors stay $0$ forever.

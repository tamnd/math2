---
tag: 5BFC3R00AF
kind: proof
name: Proof that the gradient points in the direction of steepest ascent
msc: [26B12]
proves: 0ZC78099PA
uses: [0A6PMR20N4, 0Y7PVW4Q44, 0NS2QYVC4Y, 0RFWW56Y22, 0XPR1E85W0]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Section 8.3.3
  - url: https://en.wikipedia.org/wiki/Gradient
    locator: Gradient is direction of steepest ascent
---

## Proof

We write the directional derivative as a dot product with the gradient and compare it with its largest possible value.

1. Let $U$, $f$ and $a$ be as in the statement. Put $g = \nabla f(a)$, so $g \ne 0$. Let $u \in \mathbb{R}^n$ with $\|u\| = 1$, and put $w = g / \|g\|$, a unit vector.
2. Since [[the derivative gives the directional derivatives|0A6PMR20N4]], the [[directional derivative|0Y7PVW4Q44]] $D_u f(a)$ exists and equals $Df(a)(u)$.
3. By the definition of the [[gradient|0NS2QYVC4Y]], $Df(a)(u) = g \cdot u$. So $D_u f(a) = g \cdot u$.
4. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]] in [[Euclidean space|0XPR1E85W0]], $|g \cdot u| \le \|g\| \, \|u\| = \|g\|$. So $-\|g\| \le D_u f(a) \le \|g\|$.
5. Expanding the dot product, $\|u - w\|^2 = \|u\|^2 - 2 \, u \cdot w + \|w\|^2 = 2 - 2 \, \dfrac{g \cdot u}{\|g\|}$.
6. In the same way, $\|u + w\|^2 = 2 + 2 \, \dfrac{g \cdot u}{\|g\|}$.
7. By steps 3 and 5, $D_u f(a) = \|g\|$ holds if and only if $\|u - w\| = 0$, that is, if and only if $u = g / \|g\|$.
8. By steps 3 and 6, $D_u f(a) = -\|g\|$ holds if and only if $\|u + w\| = 0$, that is, if and only if $u = -g / \|g\|$.
9. So the upper bound is attained exactly at $u = \nabla f(a) / \|\nabla f(a)\|$, and the lower bound exactly at $u = -\nabla f(a) / \|\nabla f(a)\|$.

## Idea

The slope of $f$ in a unit direction $u$ is the dot product $\nabla f(a) \cdot u$. A dot product with a fixed vector is largest when $u$ points the same way as that vector, and smallest when it points the opposite way. The identity $\|u - w\|^2 = 2 - 2 u \cdot w$ for unit vectors makes the cases of equality exact.

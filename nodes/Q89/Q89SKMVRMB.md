---
tag: Q89SKMVRMB
kind: proof
name: Proof of the volume of a ball in R^3 from the n-dimensional formula
msc: ["26B15"]
proves: 0WMDV48VSN
uses: [00YH28R457, 0V3FZMVB4K, 0FDCW77H44, 0DFT1GP1JP, 0D37QFPEZE]
sources:
  - url: https://en.wikipedia.org/wiki/Volume_of_an_n-ball
    locator: Closed form
---

## Proof

We take the case $n = 3$ of the general formula.

1. Let $R > 0$ and $B = \set{(x, y, z) \in \R^3 : x^2 + y^2 + z^2 \le R^2}$. This is the closed ball $B_3(R)$ of radius $R$ about $0$.
2. By the [[volume of a ball in R^n|00YH28R457]] with $n = 3$, $\operatorname{vol}(B) = \pi^{3/2} R^3 / \Gamma(5/2)$, where $\Gamma$ is the [[gamma function|0V3FZMVB4K]].
3. We compute $\Gamma(1/2)$. For $0 < \varepsilon < M$, the [[substitution|0D37QFPEZE]] $t = u^2$ gives $\int_\varepsilon^M t^{-1/2} e^{-t} \, dt = 2 \int_{\sqrt{\varepsilon}}^{\sqrt{M}} e^{-u^2} \, du$.
4. Let $\varepsilon \to 0$ and $M \to \infty$. The integrand $e^{-u^2}$ is even, so the [[Gaussian integral|0DFT1GP1JP]] gives $\Gamma(1/2) = \int_{-\infty}^{\infty} e^{-u^2} \, du = \sqrt{\pi}$.
5. By the [[functional equation|0FDCW77H44]] $\Gamma(s + 1) = s \, \Gamma(s)$, applied twice, $\Gamma(5/2) = \tfrac{3}{2} \cdot \tfrac{1}{2} \cdot \Gamma(1/2) = \tfrac{3}{4} \sqrt{\pi}$.
6. Hence $\operatorname{vol}(B) = \pi^{3/2} R^3 \cdot \frac{4}{3 \sqrt{\pi}} = \frac{4}{3} \pi R^3$.

## Idea

The volume of a ball in every dimension is given by one formula with the gamma function. In dimension $3$ the gamma value $\Gamma(5/2)$ reduces to $\Gamma(1/2) = \sqrt{\pi}$, and the powers of $\pi$ combine to give $\tfrac{4}{3} \pi R^3$.

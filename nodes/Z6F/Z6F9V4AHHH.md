---
tag: Z6F9V4AHHH
kind: definition
name: Complete elliptic integral of the first kind
msc: ["33E05"]
defines: RM54CPPE12
uses: [NXMCYGCB59, 05KQ3F99BQ]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
    locator: Complete elliptic integral of the first kind
---

## Definition

Let $k$ be a real number with $0 \le k < 1$.
The *complete elliptic integral of the first kind* is
$$K(k) = \int_0^{\pi/2} \frac{d\theta}{\sqrt{1 - k^2 \sin^2\theta}} = \int_0^1 \frac{dt}{\sqrt{(1 - t^2)(1 - k^2 t^2)}}.$$
It is the value at $\varphi = \pi/2$ of the incomplete [[elliptic integral|NXMCYGCB59]] $F(\varphi, k)$ of the first kind.
The *complementary modulus* is $k' = \sqrt{1 - k^2}$, and one writes $K'(k) = K(k')$.

## Remarks

The second integral comes from the first by $t = \sin\theta$; it is an [[improper integral|05KQ3F99BQ]] at $t = 1$ that converges.
Example: $K(0) = \int_0^{\pi/2} d\theta = \pi/2$.
Expanding $(1 - k^2\sin^2\theta)^{-1/2}$ by the binomial series and integrating term by term gives
$$K(k) = \frac{\pi}{2} \sum_{n=0}^{\infty} \left( \frac{(2n)!}{2^{2n} (n!)^2} \right)^2 k^{2n}.$$
Non-example: the formula does not define a finite number at $k = 1$, since $\int_0^{\pi/2} d\theta / \cos\theta$ diverges; indeed $K(k) \to \infty$ as $k \to 1^-$.
Some authors use the parameter $m = k^2$ and write $K(m)$; the value is the same function written in another variable.
The [[arithmetic–geometric mean|E0V3N93DX8]] gives $K(k) = \pi / (2 M(1, k'))$.

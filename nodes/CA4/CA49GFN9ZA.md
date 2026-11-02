---
tag: CA49GFN9ZA
kind: definition
name: Complete elliptic integral of the second kind
msc: ["33E05"]
defines: VS2PSX14C8
uses: [NXMCYGCB59, 0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
    locator: Complete elliptic integral of the second kind
---

## Definition

Let $k$ be a real number with $0 \le k \le 1$.
The *complete elliptic integral of the second kind* is
$$E(k) = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2\theta} \, d\theta = \int_0^1 \frac{\sqrt{1 - k^2 t^2}}{\sqrt{1 - t^2}} \, dt.$$
It is the value at $\varphi = \pi/2$ of the incomplete [[elliptic integral|NXMCYGCB59]] $E(\varphi, k)$ of the second kind.
With $k' = \sqrt{1 - k^2}$ one writes $E'(k) = E(k')$.

## Remarks

Example: $E(0) = \pi/2$, and $E(1) = \int_0^{\pi/2} \cos\theta \, d\theta = 1$.
The ellipse $x = a\sin\theta$, $y = b\cos\theta$ with $0 < b \le a$ has perimeter $4aE(e)$, where $e = \sqrt{1 - b^2/a^2}$ is its eccentricity, because its arc length element is $a\sqrt{1 - e^2\sin^2\theta}\,d\theta$.
Non-example: for real $k > 1$ the integrand $\sqrt{1 - k^2\sin^2\theta}$ is not real for $\theta$ near $\pi/2$, so the formula does not define a real number there.
Series: $E(k) = \frac{\pi}{2}\left(1 - \sum_{n=1}^{\infty} \left(\frac{(2n)!}{2^{2n}(n!)^2}\right)^2 \frac{k^{2n}}{2n - 1}\right)$.
Some authors write $E(m)$ with the parameter $m = k^2$.

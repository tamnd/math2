---
tag: RM54CPPE12
kind: concept
name: Complete elliptic integral of the first kind
msc: ["33E05"]
specializes: [NXMCYGCB59]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
    locator: Complete elliptic integral of the first kind
---

## Summary

The complete elliptic integral of the first kind is the function $K(k) = \int_0^{\pi/2} d\theta / \sqrt{1 - k^2\sin^2\theta}$ of the modulus $k$.
It is a quarter of the real period of the [[Jacobi elliptic functions|P071B692JF]] $\operatorname{sn}$ and $\operatorname{cn}$.
It gives the exact period of a pendulum and can be computed very fast with the arithmetic–geometric mean.

## Explanations

### L1 human

For a pendulum with small swings, the period does not depend on the amplitude.
For large swings it does, and the correction is given by $K(k)$, where $k$ is the sine of half the largest angle.
At $k = 0$ the integrand is $1$ and $K(0) = \pi/2$.
As $k$ grows toward $1$ the integral grows without bound, because the pendulum takes longer and longer to swing near the top.

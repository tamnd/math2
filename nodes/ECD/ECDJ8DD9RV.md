---
tag: ECDJ8DD9RV
kind: definition
name: Radon–Nikodym derivative
msc: [28A15]
defines: 1NTKG64F7N
uses: [1ZSZS5G1Q4, Y98C5T956Q, WEBBT18D4X, P0P21KDV6E, RARTMA0ZEC]
sources:
  - url: https://en.wikipedia.org/wiki/Radon–Nikodym_theorem
---

## Definition

Let $(X, \Sigma)$ be a measurable space and let $\mu$ and $\nu$ be [[σ-finite measures|WEBBT18D4X]] on $\Sigma$ with $\nu$ [[absolutely continuous|P0P21KDV6E]] with respect to $\mu$.
By the [[Radon–Nikodym theorem|1ZSZS5G1Q4]] there is a measurable $f \colon X \to [0, \infty)$ with $\nu(A) = \int_A f \, d\mu$ for all $A \in \Sigma$, and $f$ is unique [[$\mu$-almost everywhere|RARTMA0ZEC]].
The *Radon–Nikodym derivative* of $\nu$ with respect to $\mu$ is this function $f$, determined up to $\mu$-null sets.
It is written $\dfrac{d\nu}{d\mu}$.

## Remarks

Example: let $\mu$ be Lebesgue measure on $\R$ and $\nu(A) = \int_A 2x \, \mathbf{1}_{[0,1]}(x) \, dx$.
Then $\nu$ is a [[measure with density|Y98C5T956Q]], and $\frac{d\nu}{d\mu}(x) = 2x$ for $x \in [0,1]$ and $0$ elsewhere, up to a null set.

Non-example: the Dirac measure $\delta_0$ has no Radon–Nikodym derivative with respect to Lebesgue measure $\lambda$.
Indeed $\lambda(\{0\}) = 0$ but $\delta_0(\{0\}) = 1$, so $\delta_0$ is not absolutely continuous with respect to $\lambda$.

For every measurable $g \colon X \to [0, \infty]$,
$$\int_X g \, d\nu = \int_X g \, \frac{d\nu}{d\mu} \, d\mu.$$
If $\nu \ll \mu \ll \rho$ with all three σ-finite, then the chain rule $\frac{d\nu}{d\rho} = \frac{d\nu}{d\mu} \cdot \frac{d\mu}{d\rho}$ holds $\rho$-almost everywhere.

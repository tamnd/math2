---
tag: H84QH4K3TG
kind: definition
name: Principal stresses
msc: [74A10]
defines: M6ZWV4Y29A
uses: [KG2XWEMJ30, 0BQAA2BK3Q, 0N6960W0BV, 06J4PXRG22, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
    locator: Principal stresses and stress invariants
---

## Definition

Let $\sigma$ be a symmetric [[Cauchy stress tensor|KG2XWEMJ30]] at a point, viewed as a real symmetric $3 \times 3$ matrix.
The *principal stresses* are the three [[eigenvalues|0BQAA2BK3Q]] $\sigma_1 \ge \sigma_2 \ge \sigma_3$ of $\sigma$, counted with multiplicity.
A *principal direction* is a unit [[eigenvector|0N6960W0BV]] $n$ of $\sigma$, that is, a unit vector with $\sigma n = \sigma_k n$ for some $k$.

## Remarks

By the [[spectral theorem|06J4PXRG22]], the principal stresses are real and there is an orthonormal basis of principal directions; in that basis $\sigma = \operatorname{diag}(\sigma_1, \sigma_2, \sigma_3)$.
They are the roots of the [[characteristic polynomial|0VSSPAFM2C]] $\lambda^3 - I_1 \lambda^2 + I_2 \lambda - I_3$, with the stress invariants $I_1 = \operatorname{tr} \sigma$, $I_2 = \tfrac12 \left( (\operatorname{tr} \sigma)^2 - \operatorname{tr}(\sigma^2) \right)$ and $I_3 = \det \sigma$.
For the pure shear $\sigma$ with $\sigma_{12} = \sigma_{21} = \tau > 0$ and all other entries $0$, the principal stresses are $\tau$, $0$, $-\tau$, with directions $(e_1 + e_2)/\sqrt2$, $e_3$, $(e_1 - e_2)/\sqrt2$.
For this $\sigma$, $e_1$ is not a principal direction: $\sigma e_1 = \tau e_2$ is not a multiple of $e_1$, so the plane with normal $e_1$ carries the shear stress $\tau$.
For every unit vector $n$, the normal stress $n \cdot \sigma n$ lies between $\sigma_3$ and $\sigma_1$.

## Explanations

### L1 human

The principal stresses are the stresses in the special directions where there is no shear.
They are found as the eigenvalues of the stress matrix.
